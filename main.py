import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool
seper_dev_tool = SerperDevTool()

from dotenv import load_dotenv

load_dotenv()

def crewai_setup(company=""):

  
  #----------SRATEGIC_PLANNER------------#
  strategic_planner = Agent(
    role="Social Media Analyst",
    goal="Be a dominant leader in Social Media marketing, using Twitter, Reddit and Facebook to drive digital engagement to a company's audience and beyond helping grow their brand",
    backstory="Armed with a robust analytical toolkit and a strategic mindset, I distill complex data into clear, actionable insights that drive the marketing agenda forward.",
    verbose=True,
    tools=[]
  )

  develop_marketing_plan= Task(
    description="Develop a comprehensive marketing plan detailing strategies and tactics for achieving business objectives.",
    agent=strategic_planner,
    expected_output="A detailed marketing plan document that outlines strategies, tactics, and expected outcomes."
  )

  monitor_key_performance = Task(
      description="Set and monitor key performance indicators to track the success of marketing strategies and identify improvement areas.",
      agent=strategic_planner,
      expected_output="A report on key performance indicators with analysis of current performance against targets."
  )

  task1= Task(
      description="Identify and analyze target markets to tailor marketing strategies effectively for this company {company}.",
      agent=strategic_planner,
      expected_output="A market analysis report detailing demographic, psychographic, and behavioral characteristics of target markets."
  )

  task2 = Task(
      description="Draft me a post on linkedin about {company}",
      agent=strategic_planner,
      expected_output="Linkedin post"
  )

  #----------------------------------#
  market_research_analyst= Agent(
    role="Market Research Analyst",
    goal="Deliver deep insights into market dynamics, customer preferences, and competitive landscapes to inform strategic planning.",
    backstory="As a seasoned explorer of market ecosystems, I wield expertise in unearthing critical trends and behaviors that dictate market success.",
    verbose=True,
    tools=[]
  )

  #----------------------------------#

  creative_director= Agent(
    role="Creative Director",
    goal="Steer the creative direction of marketing campaigns to ensure they are impactful, cohesive, and aligned with brand values.",
    backstory="A visionary in the realm of creativity, I orchestrate the aesthetic and narrative threads that define brand identity and consumer engagement.",
    verbose=True,
    tools=[]
  ) 


  # twitter_posts= Task(
  #   description="""
  #     write me a relevant twitter post to promote this website : https://xespn.com/. Use the searchTool for that ",
      
  #   """,
  #   agent=content_creator,
  #   excepted_output="twitter post "
  # )

  # Instantiate your crew with a sequential process
  crew = Crew(
    agents=[strategic_planner],
    tasks=[task1, task2 , develop_marketing_plan, monitor_key_performance],
    verbose=True
  )

  # Get your crew to work!
  result = crew.kickoff({"company":company})

  print("######################")
  return result