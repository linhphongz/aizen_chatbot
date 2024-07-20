import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from a .env file
load_dotenv()

# Set the Tavily API key from environment variables
os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")

# Function to perform a search using the Tavily API
def api_search(question):
    # Initialize the Tavily search tool
    tool = TavilySearchResults()
    
    # Invoke the search tool with the given question and get the response
    response_api = tool.invoke({"query": question})
    
    # Return the first result from the search response
    return response_api[0]
