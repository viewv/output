import re

from groq import Groq
from config import Config

client = Groq(
    # This is the default and can be omitted
    # api_key=os.environ.get("GROQ_API_KEY"),
    api_key=Config.GROQ_API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Generate the Python code to execute the command: 'dscl . list /Users'",
        }
    ],
    model="llama3-8b-8192",
)

# print(chat_completion.choices[0].message.content)

original_string = chat_completion.choices[0].message.content

# Extract the code using regular expressions
code_match = re.search(r'```(?:python)?\n(.*?)```',
                       original_string, re.DOTALL | re.IGNORECASE)

if code_match:
    extracted_code = code_match.group(1)
    print("Extracted code:")
    print(extracted_code)

    print("\nExecuting the extracted code:\n")
    exec(extracted_code)
else:
    print("No Python code found in the string.")
