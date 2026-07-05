# Get imports
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from tools import search_tool, save_to_txt, wiki_tool
import streamlit as st

load_dotenv()

# Create general structure in the AI response
class Answer(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Save Claude as a variable
llm = ChatAnthropic(model="claude-sonnet-4-6")

# Write out the system prompt
prompt = """
You are a video game research assistant.
Based off the given video game, research everything you can about it, ratings, reviews, estimated time to beat, difficulty, genre, and more.
Summarize the 3 best reviews you can find.
Give a brief overview of the video game itself, and list everything in a clear and concise format.
Save to a text file only when told to do so
"""

# Give the AI it's tools
tools = [search_tool, save_to_txt, wiki_tool]

# Using Claude, the system prompt, and the tools, create the agent
agent = create_agent(
    model=llm,
    system_prompt=prompt,
    tools=tools,
    response_format=Answer
)

# Create a greeting for the user
st.header("Hello! I'm a Video Game research assistant, I'll research everything I can about a video game and tell you what I find.")

# Create a user input for them to type in
content = st.text_input("What video game would you like for me to research for you? ")

# Invoke the agent with the user prompt, then print out the structured response
if content:
     raw_response = agent.invoke({"messages": [{"role": "user", "content": content}]})
     formatted_text = raw_response["structured_response"].summary.replace("\n", "  \n")
     st.markdown(formatted_text)