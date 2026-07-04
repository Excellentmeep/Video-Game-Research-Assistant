from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from tools import search_tool, save_to_txt

load_dotenv()

class Answer(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-sonnet-4-6")

prompt = """
You are a video game research assistant.
Based off the given video game, research everything you can about it, ratings, reviews, estimated time to beat, difficulty, genre, and more.
Summarize the 3 best reviews you can find.
Give a brief overview of the video game itself, and list everything in a clear and concise format.
Save the output to a text file when told to do so.
"""

tools = [search_tool, save_to_txt]

agent = create_agent(
    model=llm,
    system_prompt=prompt,
    tools=tools,
    response_format=Answer
)

content = input("What would you like for me to research? ")

raw_response = agent.invoke({"messages": [{"role": "user", "content": content}]})
print(raw_response["structured_response"])
