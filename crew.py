from crewai import Crew, Process, Task
from textwrap import dedent
from agents import BlogWritingAgents

# Take input from the user
topic = input("Enter the topic for the blog: ")

# Initialize inputs
inputs = {"topic": topic}

# Initialize agents
agents = BlogWritingAgents()
researcher = agents.research_specialist()
strategist = agents.content_strategist()
writer = agents.copywriter()

# Define tasks
research_task = Task(
    description=dedent(f"""
        Find the latest news and trends on the topic provided: {inputs['topic']}.
        Summarize findings into bullet points with references.
    """),
    expected_output="A concise summary of recent events or trends with references.",
    agent=researcher,
)

content_task = Task(
    description=dedent(f"""
        Organize research findings into a structured blog outline.
        Include an introduction, 3-5 main points, and a conclusion.
    """),
    expected_output="A detailed blog outline in markdown format.",
    agent=strategist,
)

writing_task = Task(
    description=dedent(f"""
        Write a LinkedIn-ready blog post based on the provided outline.
        Ensure professional tone, engaging style, and LinkedIn audience appeal.
    """),
    expected_output="A polished blog post ready for LinkedIn.",
    agent=writer,
)

# Create the crew
blogging_crew = Crew(
    agents=[researcher, strategist, writer],
    tasks=[research_task, content_task, writing_task],
    process=Process.sequential  # Execute tasks in order.
)

# Kickoff with input
result = blogging_crew.kickoff(inputs=inputs)
print(result)
