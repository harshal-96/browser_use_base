import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from browser_use import Agent
import asyncio

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

async def main():
    try:
        agent = Agent(
            # task="Compare the price of gpt-4o and DeepSeek-V3",
            # task="Open this http://127.0.0.1:5000/loan.html and fill the form with anything and upload a pdf and if asked for credential username ='admin' and password ='test@123'",
            task="Compare the price of Tata Nexon on olx.com and cardekho.com",
            llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25"),
        )
        await agent.run()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())