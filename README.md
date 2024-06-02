# CrewAI Health Assistant

> **Note:** This is the description of the assignment, refer to CONFIG.md for installing dependencies and LLMs for the assignment, refer to ACKNOWLEDGMENT.md for my acknowledgments 😊

## Description

This project sets up a crew of agents using the CrewAI framework to create a health assistant. The health assistant takes a sample blood test report, analyzes it, searches the internet for articles tailored to the person's health needs based on the blood test results, and finally provides health recommendations along with relevant article links.

## Approach

1. **Framework Selection**: Utilize the CrewAI framework for building the health assistant.
2. **Data Input**: Develop a module to take input in the form of a sample blood test report.
3. **Data Analysis**: Analyze the blood test report to extract relevant health information.
4. **Web Scraping**: Implement web scraping functionality to search the internet for articles related to the person's health needs.
5. **Recommendations**: Generate health recommendations based on the analyzed data and the retrieved articles.

## Code Description

This project contains 3 agents, one as the captain and two others as workers. The captain is <span style="color:blue">Expert Blood Analyser</span>, and the two workers are <span style="color:blue">Text Summarisation Expert</span> and <span style="color:blue">Expert Health Recommender</span>.

Their duties are as follows:-

### Expert Blood Analyser

- **Role**: Expert Blood Analyser
- **Backstory**: Expert in blood report analysis. I have decades of experience making reports on people's blood reports. I tell people whether they are okay or have abnormalities in their blood, and then provide health recommendations.
- **Goal**: Create a health recommendation report, must include links to articles for each abnormality found in blood test report and ways to treat those abnormalities.

### Text Summarisation Expert

- **Role**: Text Summarisation Expert
- **Backstory**: Expert at Summarising Text and extracting important details from the text.
- **Goal**: Select relevant information from text related to blood analysis and then summarise it and show it to the user in a brief format.

### Expert Health Detector

- **Role**: Expert Health Detector
- **Backstory**: Knowledgeable health recommender with extensive information about blood, its normal ranges, its abnormal ranges, health recommendations to treat blood abnormalities, links on articles present on the internet regarding such abnormalities and reasons behind blood abnormalities.
- **Goal**: Provide a summarised report that provides health recommendations and links to articles on the internet for abnormalities detected in the blood report.