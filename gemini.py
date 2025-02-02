import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))#enter your api key as an env variable

def gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")#or the model you would like to use
        response = model.generate_content(prompt)
        # Extract the actual text from the API response
        return response.text
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return None


prompt = ""
while prompt != "q":
    prompt = input("\x1b[35m Enter the prompt or q to terminate: \x1b[0m")
    if prompt != "q":
        result = gemini(prompt)
        if result:
            print(f"\x1b[36m  Response: {result}\x1b[0m")
