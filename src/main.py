import re
import execnet

from groq import Groq
from config import Config

client = Groq(
    # This is the default and can be omitted
    # api_key=os.environ.get("GROQ_API_KEY"),
    api_key=Config.GROQ_API_KEY
)

prompt = input("Enter your prompt: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            # "content": "Generate the Python code to execute the command: 'dscl . list /Users'",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
)

original_string = chat_completion.choices[0].message.content
# print("\nOriginal string:\n", original_string)

# Extract the code using regular expressions
code_match = re.search(r'```(?:python)?\n(.*?)```',
                       original_string, re.DOTALL | re.IGNORECASE)

if code_match:
    extracted_code = code_match.group(1)
    print("Executing the extracted code:")
    print(extracted_code)

    # exec(extracted_code)

    print("\nExecuting the extracted code without exec:")
    gateway = execnet.makegateway()
    channel = gateway.remote_exec(
        extracted_code + "\n\nchannel.send(message)\n")
    result = channel.receive()
    print(f"Result from remote execution: {result}")

else:
    print("No Python code found in the string.")
