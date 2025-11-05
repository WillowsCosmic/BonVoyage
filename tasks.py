from crewai import Task

def location_task(agent, from_city, destination_city, date_from, date_to):
    return Task(
        description=f"""Research comprehensive travel information for a trip from {from_city} 
        to {destination_city} from {date_from} to {date_to}.
        
        Find:
        - Transportation options (flights, trains, etc.) with approximate costs
        - Accommodation recommendations with price ranges
        - Weather conditions during travel dates
        - Visa/passport requirements
        - Local transportation options
        - Currency and exchange rates
        - Safety tips and travel advisories
        
        Provide practical, actionable information.""",
        
        expected_output="""A detailed report containing:
        - Transportation options with costs
        - 3-5 accommodation recommendations with prices
        - Weather forecast
        - Visa requirements
        - Local transport info
        - Budget estimates""",
        
        agent=agent
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""Research and recommend attractions and experiences in {destination_city} 
        for travelers interested in: {interests}.
        Travel dates: {date_from} to {date_to}.
        
        Find:
        - Top 5-10 attractions matching interests
        - 5-8 recommended restaurants (local cuisine)
        - Unique local experiences
        - Cultural events during travel dates
        - Shopping areas
        - Nightlife options (if relevant to interests)
        
        Include specific names, locations, and approximate costs.""",
        
        expected_output="""A detailed guide containing:
        - List of attractions with descriptions and costs
        - Restaurant recommendations with cuisine types and prices
        - Local experiences and activities
        - Cultural events
        - Practical tips for each location""",
        
        agent=agent
    )

def planner_task(context, agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""Create a comprehensive day-by-day travel itinerary for {destination_city} 
        from {date_from} to {date_to}.
        
        **IMPORTANT**: Use ONLY the information provided by the Location Expert and City Guide Expert.
        DO NOT search for new information. Your job is to ORGANIZE the existing research.
        
        Create a detailed itinerary that includes:
        - Day-by-day schedule with specific times
        - Morning, afternoon, and evening activities
        - Restaurant recommendations for each meal
        - Transportation between locations
        - Estimated costs for each activity
        - Daily budget summary
        - Practical tips and notes
        
        Format the itinerary clearly with:
        ## Day 1: [Date]
        ### Morning (9:00 AM - 12:00 PM)
        ### Afternoon (12:00 PM - 6:00 PM)
        ### Evening (6:00 PM - 10:00 PM)
        
        Make it practical and easy to follow.""",
        
        expected_output=f"""A complete travel itinerary document with:
        
        # Travel Itinerary: {destination_city}
        
        ## Trip Overview
        - Dates: {date_from} to {date_to}
        - Duration: X days
        - Total Estimated Budget: $X,XXX
        
        ## Pre-Trip Information
        [Visa, weather, what to pack, etc.]
        
        ## Day-by-Day Itinerary
        [Detailed daily plans with times, activities, costs]
        
        ## Budget Summary
        [Breakdown of estimated costs]
        
        ## Important Tips
        [Key information for travelers]
        
        Write in clear, organized markdown format.""",
        
        agent=agent,
        context=context
    )