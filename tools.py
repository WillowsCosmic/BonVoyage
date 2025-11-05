from crewai.tools import tool
from crewai import Agent, LLM
from duckduckgo_search import DDGS
import os
import streamlit as st

def get_llm():
    """Returns LLM configured for Streamlit Cloud"""
    try:
        # Try to get API key from Streamlit secrets first
        api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv('GEMINI_API_KEY')
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key
            return LLM(model="gemini/gemini-2.5-flash-exp")
        else:
            st.error("⚠️ GEMINI_API_KEY not found! Add it in Streamlit Cloud Settings → Secrets")
            st.stop()
    except Exception as e:
        st.error(f"Error initializing LLM: {e}")
        st.stop()

# Initialize LLM
llm = get_llm()

@tool
def search_web_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo to find current information.
    
    Args:
        query (str): The search query string
        
    Returns:
        str: Search results containing relevant information
    """
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=3)
        
        if not results:
            return f"No search results found for '{query}'. Please use your general knowledge to provide information about this topic."
        
        # Format results concisely
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            body = result.get('body', 'No description')[:200]
            formatted_results.append(f"{i}. {title}\n{body}...\n")
        
        return "\n".join(formatted_results)
        
    except Exception as e:
        return f"Search unavailable. Please provide information about '{query}' based on your training data."

# Agent: Location Expert
location_expert = Agent(
    role="Travel Logistics Expert",
    goal="Research and provide comprehensive travel information including transportation, accommodations, costs, weather, and requirements",
    backstory="""You are an experienced travel researcher who quickly gathers essential 
    travel information. You know how to find the most relevant details about destinations, 
    transportation options, costs, and travel requirements. You provide clear, actionable 
    information without unnecessary elaboration.""",
    tools=[search_web_tool],
    verbose=True,
    max_iter=15,
    llm=llm,
    allow_delegation=False
)

# Agent: City Guide Expert
guide_expert = Agent(
    role="Local City Guide",
    goal="Discover attractions, restaurants, and experiences tailored to traveler interests",
    backstory="""You are a knowledgeable local guide who loves sharing the best spots 
    in the city. You quickly identify top attractions, authentic restaurants, and unique 
    experiences that match travelers' interests. You provide specific recommendations 
    with practical details.""",
    tools=[search_web_tool],
    verbose=True,
    max_iter=15,
    llm=llm,
    allow_delegation=False
)

# Agent: Planner Expert
planner_expert = Agent(
    role="Travel Itinerary Planner",
    goal="Create a detailed, well-organized day-by-day travel itinerary using information from other experts",
    backstory="""You are a professional travel planner who excels at organizing 
    information into clear, practical itineraries. You take research from the Location Expert 
    and City Guide Expert and craft it into a cohesive travel plan with specific times, 
    locations, and costs. You write comprehensive guides that travelers can actually use.
    
    You DO NOT search for new information. You ONLY organize and structure the information 
    provided to you by other experts into a beautiful, easy-to-follow itinerary.""",
    tools=[],
    verbose=True,
    max_iter=10,
    llm=llm,
    allow_delegation=False
)