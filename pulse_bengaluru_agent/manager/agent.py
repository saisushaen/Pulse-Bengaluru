from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.network_quality_analyst.agent import network_quality_analyst
from .sub_agents.social_media_analyst.agent import social_media_analyst
from .sub_agents.radio_charter_analyst.agent import radio_charter_analyst
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    we have 3 kinds of data. one is the social media data, one is network quality data and one is
    radio charter converted to text. 

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
    if in the data there are list of interested_activities, give the output in sush a way about how it will 
    impact that particular activity, if the list is not there, give the output in a generic way.

    The final output should be a json with a list of alerts. alerts should have the following fields:
    alert summary, date and time, comprehensive reason for the alert, possible impact that can be created and Add generic, semantically useful tags like ["fire", "Koramangala", "civilian_impact", "pedestrian_zone", "Bangalore_south"] — useful for time-series forecasting.
    The alert fields shoule be named like this: alert_summary, time, alert_reason, possible_impact. ⁠tags_for_prediction.
    There shouldn't be any alert for network congestion. network congestion data should just be used like a validation
    mechanism for the generated alerts from the other sources.
    Don't mention the reason and about network congestion in alert_sumary and possible_impact(only mention it in reason.)


    """,
    # sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(social_media_analyst),
        AgentTool(network_quality_analyst),
        AgentTool(radio_charter_analyst)
        # get_current_time,
    ],
)
