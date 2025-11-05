
# 🌍 AI Travel Planning Assistant

An intelligent travel planning system powered by **CrewAI** and **LLM agents** that generates comprehensive travel itineraries, city guides, and location reports.

## ✨ Features

- 🤖 **Multi-Agent System**: Three specialized AI agents working together
  - **Location Expert**: Researches transportation, accommodation, weather, and visa requirements
  - **City Guide Expert**: Finds attractions, restaurants, and local experiences
  - **Travel Planner**: Creates detailed day-by-day itineraries

- 🎯 **Personalized Planning**: Customized based on:
  - Origin and destination cities
  - Travel dates
  - Personal interests and preferences

- 📊 **Comprehensive Reports**: 
  - Location research report
  - City guide with recommendations
  - Complete travel itinerary with schedule and costs

- 🌐 **Deployed on Streamlit Community Cloud**: Fast, reliable, and always available

## 🚀 Live Demo

**🔗 [Try the app now!](https://your-app-name.streamlit.app)**

> *Replace with your actual Streamlit Cloud URL after deployment*

## 🛠️ Technology Stack

- **Framework**: [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent orchestration
- **UI**: [Streamlit](https://streamlit.io/) - Web interface
- **Search**: DuckDuckGo Search - Real-time web search
- **LLM**: Gemini and Quen2.5
- **Hosting**: Streamlit Community Cloud

## 🎯 How to Use

1. **Visit the live app** at the link above
2. **Fill in your travel details**:
   - From City (e.g., "New York")
   - To City (e.g., "Paris")
   - From Date (e.g., "2024-06-01")
   - To Date (e.g., "2024-06-07")
   - Interests (e.g., "art, history, food")
3. **Click "Plan My Trip"**
4. **Get three comprehensive reports**:
   - 📍 Location Report (logistics and travel info)
   - 🗺️ City Guide (attractions and restaurants)
   - 📅 Travel Itinerary (detailed daily schedule)

## 🏃 Run Locally (Optional)

### Prerequisites
- Python 3.8+
- pip package manager
- (Optional) Ollama for local LLM usage

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/travel-agent-crewai.git
cd travel-agent-crewai
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
touch .env

# Add your API key:
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open in browser**
```
http://localhost:8501
```

## 📁 Project Structure

```
travel-agent-crewai/
├── app.py                 # Streamlit web interface
├── tools.py              # Agent definitions and search tools
├── tasks.py              # Task definitions for each agent
├── crew.py               # CrewAI orchestration
├── requirements.txt      # Python dependencies
├── .env                  # API keys (local only, not in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🌐 Deployment (Streamlit Community Cloud)

This app is deployed on **Streamlit Community Cloud** - a free hosting platform for Streamlit apps.




## 💡 Features Explained

### Location Expert Agent
Researches practical travel information:
- ✈️ Transportation options and costs
- 🏨 Accommodation recommendations
- 🌤️ Weather forecasts
- 📋 Visa and passport requirements
- 🚕 Local transportation
- 💱 Currency information

### City Guide Expert Agent
Discovers local experiences:
- 🎭 Top attractions matching your interests
- 🍽️ Restaurant recommendations
- 🎨 Cultural events and activities
- 🛍️ Shopping areas
- 🌃 Nightlife options

### Travel Planner Agent
Creates your perfect itinerary:
- 📅 Day-by-day schedule with specific times
- ⏰ Morning, afternoon, and evening activities
- 🍴 Meal recommendations
- 🚌 Transportation between locations
- 💰 Cost estimates for each activity
- 📝 Practical tips and notes

## 🔒 Security & Privacy

- ✅ No personal data is stored
- ✅ API keys secured via Streamlit Secrets
- ✅ All searches are anonymous
- ✅ No user tracking or analytics
- ⚠️ Never share your API keys publicly

## 🐛 Troubleshooting

### App is slow
- This is normal! The agents need time to research and plan
- Typical completion time: 2-5 minutes
- The app is working even if it seems stuck

### "Error generating plan"
- Check that all fields are filled in correctly
- Make sure dates are in the future
- Try refreshing the page and submitting again

### Want faster results?
- The deployed version uses OpenAI API for optimal speed
- Local Ollama is slower but free (see Run Locally section)


If you find this project helpful, please consider giving it a ⭐ on GitHub!

---

**Built with ❤️ using CrewAI and Streamlit**

*Happy Traveling! 🌍✈️*
