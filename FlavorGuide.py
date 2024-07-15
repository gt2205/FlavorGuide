# -*- coding: utf-8 -*-


!pip install -qU crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29



!pip install -qU langchain-google-genai

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

from crewai import Crew, Process, Agent, Task
from google.colab import userdata
import os


os.environ["GOOGLE_API_KEY"] = userdata.get('gemini')
os.environ["TAVILY_API_KEY"]=userdata.get('tavily')

from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)
scrape_tool = ScrapeWebsiteTool()

advisor_agent = Agent(
    role="Senior dineout advisor specialist",
    goal="Analyze different dineout options and suggets the best suitable one as per given budget,place and type",
    backstory="Specialized in analyzing different dineout options,it suggests the best choice for user",
    verbose=True,
    tools = [scrape_tool, search_tool],
    llm=llm,

)

writer_agent= Agent(
    role="Senior content writer",
    goal="Checks if given options are in customer budget and type and gives a list of top 5 possible choices",
    backstory="Specialized in writing short length but creative blogs on dineout option suggestions so that they seem tempting to go to",
    verbose=True,
    tools = [scrape_tool, search_tool],

    llm=llm

)

advisor_agent_task = Task(
    description=(
        "finds dinout {type} for customer budget of {budget} at {place} and suggests best possible ones"
    ),
    expected_output=(
        "Dineout options as per given customer preference and budget constraints"
    ),
    agent=advisor_agent,
)

writer_agent_task = Task(
    description=(
        "writes an tempting review about the places and suggests the best ones checking {budget} and {place}"
    ),
    expected_output=(
        "Dineout options  creative blog in a tempting fashion as per given customer preference and budget constraints"
    ),
    agent=writer_agent,
)

from crewai import Crew, Process
dineout_planner_crew = Crew(
    agents=[advisor_agent,
            writer_agent],

    tasks=[advisor_agent_task,
           writer_agent_task],
    manager_llm=llm,
    process=Process.hierarchical,

    verbose=True
)

inputs={
    'budget':'200-250 rupees inr per person',
    'place':'mansarovar,jaipur',
    'type':'cafe'
}

result=dineout_planner_crew.kickoff(inputs=inputs)

result
