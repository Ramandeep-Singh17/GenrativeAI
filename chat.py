from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
  model="openai/gpt-oss-120b",
    temperature=0.7
)

response = model.invoke("What is cricket?")

print(response.content)