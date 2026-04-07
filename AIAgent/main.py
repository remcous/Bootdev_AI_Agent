import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable not found")

parser = argparse.ArgumentParser(description="AIAgent")
parser.add_argument("user_prompt", type=str, help="User Prompt")

args = parser.parse_args()

client = genai.Client(api_key=api_key)

print(f"User Prompt: {args.user_prompt}")

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=args.user_prompt
)

if response.usage_metadata == None:
    raise RuntimeError("API request failed, recieved response with no usage metadata")

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response:\n{response.text}")