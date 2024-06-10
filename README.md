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

This project contains 2 agents specialized in different tasks:

### Expert Blood Analyser

- **Role**: Expert Blood Analyser
- **Backstory**: Expert in blood report analysis. Decades of experience in providing comprehensive reports on blood tests. Determines whether blood values are within normal ranges and provides tailored health recommendations.
- **Goal**: Summarize the blood report, identifying normal and abnormal values. Provide health recommendations and links to articles for each abnormality found.

### Text Summarisation Expert

- **Role**: Text Summarisation Expert
- **Backstory**: Skilled in summarizing text and extracting essential details. Proficient at condensing information into concise formats.
- **Goal**: Extract relevant information from the text related to blood analysis and summarize it in a brief format for the user.

## IMPORTANT POINTS

1. **CrewAI Usage and Cost**: CrewAI is well suited for OpenAI, specifically ChatGPT-3.5-Turbo and ChatGPT-4. However, it requires payment for each request made, potentially leading to high costs.

2. **Issues with Local LLMs**: Local LLMs like Llama2 from Ollama face consistent issues such as "Invalid Format: Missing 'Action Input:' after 'Action:'" and "Invalid Format: Missing 'Action Input:' after 'Thought:'", causing looping for users.

3. **Performance of LLMs**: LLMs like Mistral 8x7B, Dolphin, and Mistral 7B Blend show better performance compared to other local LLMs. However, OpenAI models exceed in performance and provide better conclusions.

4. **LLMs Used in the Project**: The project utilized two LLMs for testing, namely Llama2 and Mistral7B. Mistral7B outperformed Llama2. Setup information for both LLMs is included in CONFIG.md.

5. **Compatibility with Text and PDFs**: The assignment works well with text and PDFs containing tables as blood reports, particularly on the first page. The code is designed to check only the first page, but it can be easily modified to check all pages using loops.
