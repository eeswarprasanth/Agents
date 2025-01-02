from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

class BlogWritingAgents:
    def __init__(self):
        # Setting up LLMs
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.search_tool = SearchTools.search_internet  # Instantiate the tool here.

    def research_specialist(self):
        return Agent(
            role="Research Specialist",
            backstory=dedent(
                f"""Expert at uncovering the most recent and relevant information
                on any topic using advanced search tools."""),
            goal=dedent(
                f"""Research the most recent happenings, news, and trends 
                about a given topic. Summarize findings with references."""),
            tools=[self.search_tool],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

#define another agent for content strategist

    def content_strategist(self):
        return Agent(
            role="Content Strategist",
            backstory=dedent(
                f"""A master at organizing information into engaging and logical structures
                for impactful storytelling."""),
            goal=dedent(
                f"""Take research summaries and organize them into a structured blog outline. 
                The outline should include an introduction, key points, and a conclusion."""),
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def copywriter(self):
        return Agent(
            role="Professional Copywriter",
            backstory=dedent(
                f"""An accomplished writer skilled at creating engaging and professional content
                tailored for a LinkedIn audience."""),
            goal=dedent(
                f"""Draft a polished and professional blog post based on the outline and research. 
                The tone should be professional, concise, and engaging, suitable for LinkedIn."""),
            verbose=True,
            llm=self.OpenAIGPT4,
        )
