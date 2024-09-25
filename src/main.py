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
            "content": "Generate the Python code to output Hello World, Only output the code",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

code = chat_completion.choices[0].message.content
exec(code)
