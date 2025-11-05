import streamlit as st
from crewai import Agent, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_web_tool
from tasks import location_task, guide_task, planner_task
import os

# Page config
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# Title
st.title("✈️BonVoyage - AI Travel Planning Assistant")
st.markdown("Plan your perfect trip with AI-powered recommendations!")

# Input form
col1, col2 = st.columns(2)

with col1:
    from_city = st.text_input("🏠 From City", placeholder="e.g., New York")
    destination_city = st.text_input("🎯 Destination City", placeholder="e.g., Paris")
    
with col2:
    date_from = st.date_input("📅 Departure Date")
    date_to = st.date_input("📅 Return Date")

interests = st.text_area(
    "🎨 Your Interests", 
    placeholder="e.g., Art, History, Food, Nature, Adventure, Shopping...",
    help="Tell us what you enjoy! This helps us customize your itinerary."
)

# Plan trip button
if st.button("🚀 Plan My Trip", type="primary", use_container_width=True):
    
    # Validation
    if not all([from_city, destination_city, interests]):
        st.error("⚠️ Please fill in all fields!")
        st.stop()
    
    if date_to <= date_from:
        st.error("⚠️ Return date must be after departure date!")
        st.stop()
    
    # Initialize LLM
    with st.spinner("🔧 Initializing AI..."):
        try:
            api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv('GEMINI_API_KEY')
            if not api_key:
                st.error("⚠️ GEMINI_API_KEY not found! Add it in Streamlit Cloud Settings → Secrets")
                st.stop()
            
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                google_api_key=api_key,
                temperature=0.7
            )
        except Exception as e:
            st.error(f"Error initializing LLM: {e}")
            st.stop()
    
    # Create agents
    with st.spinner("🤖 Creating AI agents..."):
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
    
    # Create tasks
    task1 = location_task(location_expert, from_city, destination_city, str(date_from), str(date_to))
    task2 = guide_task(guide_expert, destination_city, interests, str(date_from), str(date_to))
    task3 = planner_task([task1, task2], planner_expert, destination_city, interests, str(date_from), str(date_to))
    
    # Create crew
    crew = Crew(
        agents=[location_expert, guide_expert, planner_expert],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=True
    )
    
    # Run the crew
    with st.spinner("🌍 Planning your perfect trip... This may take 2-3 minutes..."):
        try:
            result = crew.kickoff()
            
            # Display results
            st.success("✅ Your travel itinerary is ready!")
            st.markdown("---")
            st.markdown(result)
            
            # Download button
            st.download_button(
                label="📥 Download Itinerary",
                data=str(result),
                file_name=f"itinerary_{destination_city}_{date_from}.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"❌ Error creating itinerary: {str(e)}")
            st.info("💡 Try simplifying your request or check your API key.")