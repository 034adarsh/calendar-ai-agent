import os
import dotenv
from datetime import datetime
from crewai import Agent, Task, Crew
from composio_crewai import ComposioToolSet, App
from langchain_google_genai import ChatGoogleGenerativeAI
from composio import ActionType

dotenv.load_dotenv()
llm = ChatGoogleGenerativeAI(google_api_key=os.environ["GEMINI_API_KEY"], model="gemini-1.5-flash")

composiotoolset = ComposioToolSet()
tools = composiotoolset.get_tools(actions=["GOOGLECALENDAR_CREATE_EVENT"])


date = datetime.today().strftime('%Y-%m-%d')
timezone = datetime.now().astimezone().tzinfo

todo = '''
    1PM - 3PM -> Code,
    5PM - 7PM -> Meeting,
    9AM - 12AM -> Learn soemthing
    8PM - 10PM -> Game

'''
def run_crew():
    gcal_agent = Agent(role='Google Calendar Agent',
    goal="""You take action on Google Calendar using Google Calendar APIs""",
    backstory="""You are an AI agent that is responsible for taking actions on
    Google Calendar on users' behalf. You need to take action on
    Calendar using Google Calendar APIs. Use the Correct tools to run
    APIs from the given tool-set""",
    verbose=True,
    tools=tools,
    llm=llm)
    task = Task(
    description=f"Create new events in Google Calendar for the following time slots... {todo}. Label them with the work provided to be done in that time period. Schedule it for today. Today's date is {date} (it's in YYYY-MM-DD format) and make the timezone be {timezone}.",
    agent=gcal_agent,
    expected_output="if a free slot is found"
    )
    crew = Crew(agents=[gcal_agent], tasks=[task])
    crew.kickoff()
    return "Crew run initiated", 200

run_crew()