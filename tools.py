# Import everything and assign the user agent to avoid JSON error
import wikipedia
wikipedia.set_user_agent("Video Game Research Assistant (Jaredfrench64@Gmail.com)")
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

# Assign search
search = DuckDuckGoSearchRun()

# Create the internet search tool
@tool
def search_tool(query: str) -> str:
    """
    Search the web for information
    """
    search.run
    return query

# Create the Wikipedia search tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Create the save to a text file tool, saves the response to a separate text file and gets a snapshot of the date and time of when it was created
@tool
def save_to_txt(data: str, filename: str = "Video Game Overview.txt"):
    """
    Saves the structured video game overview to a text file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Video Game Overview ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"