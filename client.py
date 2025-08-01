import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid model
model = genai.GenerativeModel('gemini-2.5-pro')

# Generate content
prompt = f"You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please.\nUser: {input("Enter question")}"
response = model.generate_content(prompt)

# Print the result
print(response.text)