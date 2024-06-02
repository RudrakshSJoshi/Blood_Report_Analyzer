from crewai import Agent
from textwrap import dedent

from tools.search_tools import SearchTools
from tools.summarise_tools import SummariseTools
from langchain_openai import ChatOpenAI

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a detailed analysis of blodd report provided by the user
        -must convert the report to text, and then summarise it, and then look up on the internet for abnormalities, should provide relevant health recommendations and links to articles

Captain/Manager/Boss:
- Expert Blood Analyser

Employees/Experts to hire:
- Text Summarisation Expert
- Expert Health Recommender


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

llm = ChatOpenAI(
    model="crewai-mistral",
    base_url="http://localhost:11434/v1"
)


class BloodAgents:
    def __init__(self):
        pass

    def expert_blood_analyser(self):
        return Agent(
            role="Expert Blood Analyser",
            backstory=dedent(
                f"""Expert in blood report analysis.
                I have decades of expereince making reports on people's blood reports.
                I tell people whether they are okay or have abnormalities in their blood, 
                and then provide health recommendations.
                """),
            goal=dedent(f"""
                        Create a health recommendation report,
                        must include links to articles for each abnormality found in blood test report and 
                        ways to treat those abnormalities
                        """),
            tools=[
                SearchTools.search_internet,
                SummariseTools.summarize_text
            ],
            verbose=True,
            max_iter=1,
            llm=llm
        )

    def text_summariser_expert(self):
        return Agent(
            role="Text Summarisation Expert",
            backstory=dedent(
                f"""Expert at Summarising Text and extracting important details from the text"""),
            goal=dedent(
                f"""
                Select relevant information from text related to blood analysis and 
                then summarise it and show it to the user in a brief format
                """),
            tools=[SummariseTools.summarize_text],
            verbose=True,
            max_iter=1,
            llm=llm
        )

    def expert_health_recommender(self):
        return Agent(
            role="Expert Health Detector",
            backstory=dedent(
                f"""
                Knowledgeable health recommender with extensive information
                about blood, its normal ranges, its abnormal ranges, 
                health recommendations to treat blood abnormalities, 
                links on articles present on the internet regarding such abnormalities and reasons behind blood abnormalities
                """),
            goal=dedent(
                f"""
                provide a summarised report that provides health recommendations and 
                links to articles on the internet for abnormalities detected in teh blood report
                """),
            tools=[
                SearchTools.search_internet,
                SummariseTools.summarize_text
                ],
            verbose=True,
            max_iter=1,
            llm=llm
        )