# Get imports
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from tools import search_tool, save_to_txt, wiki_tool

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
Always save the output to a text file.
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

# Create a user input for them to type in
content = input("What would you like for me to research? ")

# Invoke the agent with the user prompt, then print out the structured response
raw_response = agent.invoke({"messages": [{"role": "user", "content": content}]})
print(raw_response["structured_response"])