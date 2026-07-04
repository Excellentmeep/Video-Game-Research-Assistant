from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from datetime import datetime

search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """
    Search the web for information
    """
    search.run
    return query

@tool
def save_to_txt(data: str, filename: str = "Video Game Overview.txt"):
    """
    Saves the structured teaching notes to a text file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Video Game Overview ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"
