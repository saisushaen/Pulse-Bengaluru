from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


# def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
#     """Get a nerdy joke about a specific topic."""
#     print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

#     # Example jokes - in a real implementation, you might want to use an API
#     jokes = {
#         "python": "Why don't Python programmers like to use inheritance? Because they don't like to inherit anything!",
#         "javascript": "Why did the JavaScript developer go broke? Because he used up all his cache!",
#         "java": "Why do Java developers wear glasses? Because they can't C#!",
#         "programming": "Why do programmers prefer dark mode? Because light attracts bugs!",
#         "math": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!",
#         "physics": "Why did the photon check a hotel? Because it was travelling light!",
#         "chemistry": "Why did the acid go to the gym? To become a buffer solution!",
#         "biology": "Why did the cell go to therapy? Because it had too many issues!",
#         "default": "Why did the computer go to the doctor? Because it had a virus!",
#     }

#     joke = jokes.get(topic.lower(), jokes["default"])

#     # Update state with the last joke topic
#     tool_context.state["last_joke_topic"] = topic

#     return {"status": "success", "joke": joke, "topic": topic}


# Create the funny nerd agent
network_quality_analyst = Agent(
    name="network_quality_analyst",
    model="gemini-2.5-pro",
    description="An agent that tells nerdy jokes about various topics.",
    instruction="""You are a network quality agent. Analyze this data for HSR Layout:
    Compute historical averages for Network_Quality_Score, Signal_Strength_dBm, Download_Speed_Mbps, Latency_ms.
    Compare the latest values to the averages.
    If the current quality is worse compared to the historical averages, classify the area as 'congested' and give what might be the impact due to this. There could also be multiple impacts.
    Return a structured JSON with: 'area', 'is_congested', 'latest', 'historical_avg','possible_impact' and alerts.
    """,
    # tools=[get_nerd_joke],
)
