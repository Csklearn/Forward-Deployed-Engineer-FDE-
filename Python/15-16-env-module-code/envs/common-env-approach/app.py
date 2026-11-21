
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Who is Forward Deployed Engineer and what is their role? Please explain the future scope",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
