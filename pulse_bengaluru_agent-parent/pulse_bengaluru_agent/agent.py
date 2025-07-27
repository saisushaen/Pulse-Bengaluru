from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from pulse_bengaluru_agent.sub_agents.network_quality_analyst.agent import network_quality_analyst
from pulse_bengaluru_agent.sub_agents.social_media_analyst.agent import social_media_analyst
from pulse_bengaluru_agent.sub_agents.radio_charter_analyst.agent import radio_charter_analyst

# Define the root agent
root_agent = Agent(
    name="pulse_bengaluru_agent",
    model="gemini-2.5-pro",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    We have 3 kinds of data: social media data, network quality data, and radio charter converted to text. 

    Always coordinate the task to the appropriate agent as mentioned. You need to use every agent as data
    contains all the 3 different information. If any data is missing only then don't use that agent.

    You also have access to the following agents/tools:
    - social_media_analyst
    - network_quality_analyst
    - radio_charter_analyst

    You are responsible for coordinating tasks from the following agents:
    Social Media Data - social_media_analyst
    Network Analysis Data - network_quality_analyst
    Radio Charter Data - radio_charter_analyst

    Use the output from multiple agents and decide/suggest if there is any impact on the public in any way.
    If in the data there are list of interested_activities, give the output in such a way about how it will 
    impact that particular activity. If the list is not there, give the output in a generic way.

    The final output should be a JSON with a list of alerts. Each alert should have:
    - alert_summary
    - time
    - alert_reason
    - possible_impact
    - tags_for_prediction (e.g., ["fire", "Koramangala", "civilian_impact", "pedestrian_zone", "Bangalore_south"])

    There shouldn't be any alert for network congestion. Network congestion data should only be used as validation 
    for the generated alerts from other sources. Don't mention the reason or impact of network congestion in 
    alert_summary or possible_impact (only include it in alert_reason).
    """,
    tools=[
        AgentTool(social_media_analyst),
        AgentTool(network_quality_analyst),
        AgentTool(radio_charter_analyst),
    ],
)
