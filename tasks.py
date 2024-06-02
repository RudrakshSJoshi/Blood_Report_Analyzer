from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed blood report analysis which includes health recommendations and summaries about user's health

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Blood Report Analysis: Analyse the blood report, provide its summary and then provide health recommendations and article links from internet for abnormalities detected in blood report
    - Report Summariser: Summarises the report and shows all the IMPORTAT details in teh blood report the user in a brief format
    - Health Recommendation: Provide health recommendations along with article links from the internet regarding abnormalities detected in the blood report

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class BloodTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def blood_analysis(self, agent, text):
        return Task(
            description=dedent(
                f"""
            **Task**: Analyse a blood report and then provide health recommendations and article links for blood abnormalities
            **Description**: Expand the blood report into a detailed analysis that will first summarise the report by checking the values corresponding to each test, 
            and then check for abnormalities detected in the blood report, an abnormality is defined when the value lies outside the range of normal values,
            and then provide health recommendations and supporting articles from the internet regarding those blood abnormalities and how to tackle them.

            **Parameters**: 
            - text: {text}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def report_summariser(self, agent, text):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Summarises the blood report that includes all the IMPORTANT details about the person's blood
                    **Description**: Analyse the report and 
                    then provide a summary that includes all important details about the person's blood, it must include all the results in the blood test report.

                    **Parameters**: 
                    - text: {text}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def health_recommendation(self, agent, text):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Gather In-Depth Report Information
                    **Description**: Compile an in-depth information 
                    regarding the blood report regarding blood range abnormalities detected in the blood report
                    and then provide health recommendations and articles from the internet regarding those abnomralities detected.

                    **Parameters**: 
                    - text: {text}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )