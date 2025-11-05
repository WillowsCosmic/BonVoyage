from crewai import Crew, Process
from tools import location_expert, guide_expert, planner_expert
from tasks import location_task, guide_task, planner_task
import streamlit as st

st.set_page_config(
    page_title="BonVoyage - AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ BonVoyage - AI Powered Trip Planner")

st.markdown("""
💡 **Plan your next trip with AI!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
- 🎡 Best places to visit
- 💰 Accommodation & budget planning
- 🍕 Local food recommendations
- 🚆 Transportation & visa details
""")

st.subheader("📝 Enter Your Travel Details")

col1, col2 = st.columns(2)

with col1:
    from_city = st.text_input("🏠 From City", placeholder="e.g., Paris, New York")
    date_from = st.date_input("📅 Departure Date")

with col2:
    destination_city = st.text_input("✈️ Destination City", placeholder="e.g., Tokyo, Rome")
    date_to = st.date_input("📅 Return Date")

interests = st.text_area(
    "🎯 Your Interests",
    placeholder="e.g., sightseeing, food, adventure, culture, nightlife",
    height=100
)

if st.button("🚀 Generate Travel Plan", type="primary", use_container_width=True):
    
    if not from_city or not destination_city or not interests:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    
    elif date_from >= date_to:
        st.error("⚠️ Return date must be after departure date!")
    
    else:
        try:
            with st.spinner("🤖 AI agents are working on your travel plan..."):
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("📋 Step 1/4: Creating tasks...")
                progress_bar.progress(25)
                
                task1 = location_task(
                    agent=location_expert,
                    from_city=from_city,
                    destination_city=destination_city,
                    date_from=date_from,
                    date_to=date_to
                )
                
                task2 = guide_task(
                    agent=guide_expert,
                    destination_city=destination_city,
                    interests=interests,
                    date_from=date_from,
                    date_to=date_to
                )
                
                task3 = planner_task(
                    context=[task1, task2],
                    agent=planner_expert,
                    destination_city=destination_city,
                    interests=interests,
                    date_from=date_from,
                    date_to=date_to
                )
                
                status_text.text("🤖 Step 2/4: Assembling AI crew...")
                progress_bar.progress(50)
                
                crew = Crew(
                    agents=[location_expert, guide_expert, planner_expert],
                    tasks=[task1, task2, task3],
                    process=Process.sequential,
                    verbose=True
                )
                
                status_text.text("🚀 Step 3/4: AI agents working...")
                progress_bar.progress(75)
                
                result = crew.kickoff()
                
                status_text.text("✅ Step 4/4: Finalizing...")
                progress_bar.progress(100)
            
            # Success message
            st.success("🎉 Your travel plan is ready!")
            
            st.markdown("---")
            st.subheader(f"✈️ Your AI-Powered Travel Plan: {destination_city}")
            
            # Try to display the actual content
            try:
                # CrewAI result might have different attributes
                if hasattr(result, 'raw'):
                    content = result.raw
                elif hasattr(result, 'output'):
                    content = result.output
                else:
                    content = str(result)
                
                # Display the content
                with st.expander("📖 View Full Travel Plan", expanded=True):
                    st.markdown(content)
                
                # Download button
                st.download_button(
                    label="📥 Download Travel Plan as Text File",
                    data=content,
                    file_name=f"Travel_Plan_{destination_city}_{date_from}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error displaying result: {e}")
                # Fallback - show raw result
                st.code(str(result))
        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")