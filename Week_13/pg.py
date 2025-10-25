import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set it (e.g., export GOOGLE_API_KEY='your_api_key') before running.")
    print("You can get an API key from https://aistudio.google.com/app/apikey")
    exit()

genai.configure(api_key=api_key)

print("Attempting to list available models...")
try:
    found_any_model = False
    for m in genai.list_models():
        print(f"Model Name: {m.name}")
        print(f"  Description: {m.description}")
        print(f"  Supported Generation Methods: {m.supported_generation_methods}")
        print("-" * 30)
        found_any_model = True

    if not found_any_model:
        print("No models found. This could indicate an issue with your API key or network.")
except Exception as e:
    print(f"An error occurred while listing models: {e}")