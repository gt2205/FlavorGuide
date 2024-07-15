# Dineout Planner Project

## Overview
The **Dineout Planner Project** is an AI-driven system designed to suggest optimal dining options based on user preferences, budget, and location. By utilizing advanced AI tools and multi-agent collaboration, the system analyzes various dineout choices and generates tailored recommendations.

## Key Features
- **Personalized Recommendations:** Generates dining suggestions based on individual user preferences, including budget, location, and type of cuisine.
- **Multi-Agent Collaboration:** Employs specialized AI agents to ensure comprehensive and accurate dining options.
- **Integration with External Tools:** Utilizes tools like ScrapeWebsiteTool and TavilySearchAPIWrapper to gather relevant dining data.
- **Detailed Role Definition:** Each agent has a specific role, including a Senior Dineout Advisor and a Senior Content Writer, ensuring a structured approach to recommendations.

## Problem Statement
Finding suitable dining options can be overwhelming due to the abundance of choices and varying user preferences. Traditional methods often require extensive searching and can be time-consuming, leading to frustration and missed opportunities for enjoyable dining experiences.

## Solution Provided by Dineout Planner Project
The project addresses these challenges by providing an automated, user-friendly solution for dining suggestions:

- **Accessibility:** Combines various expert roles into a single AI system, making personalized dining recommendations accessible to all users.
- **Efficiency:** Reduces the time spent searching for dining options by delivering tailored suggestions quickly.
- **Accuracy:** Leverages AI tools to ensure recommendations meet user preferences and budget constraints.

## Agents and Their Roles
- **Advisor Agent**
  - **Role:** Analyze user preferences to suggest dining options.
  - **Goal:** Provide a list of suitable dineout choices based on budget, location, and type of cuisine.
  - **Backstory:** Specializes in identifying the best dining options for users.
  - **Tools:** [ScrapeWebsiteTool, TavilySearchAPIWrapper]
  - **LLM:** ChatGoogleGenerativeAI

- **Writer Agent**
  - **Role:** Create enticing descriptions of recommended dining options.
  - **Goal:** Write engaging content that highlights the best choices for users.
  - **Backstory:** Focuses on crafting appealing summaries for dineout suggestions.
  - **Tools:** [ScrapeWebsiteTool, TavilySearchAPIWrapper]
  - **LLM:** ChatGoogleGenerativeAI

## Process Flow
1. **Information Gathering:** The Advisor Agent collects data on available dining options based on user input.
2. **Recommendation Generation:** The Advisor Agent processes the data to generate a list of suitable options.
3. **Content Creation:** The Writer Agent creates compelling descriptions for the suggested dining choices.

## How It Works
- **Initialization:** The system initializes multiple agents with specific roles and goals.
- **Task Assignment:** Agents are assigned tasks based on their specialization.
- **Collaboration:** Agents work together to analyze preferences and generate recommendations.
- **Output:** The final output includes a curated list of dining options with engaging descriptions.

## Benefits
- **Tailored Dining Experience:** Provides users with personalized recommendations that enhance their dining experience.
- **Time-Saving:** Automates the search for dining options, saving users valuable time.
- **User Satisfaction:** Ensures that recommendations align with user preferences and budget, leading to greater satisfaction.
