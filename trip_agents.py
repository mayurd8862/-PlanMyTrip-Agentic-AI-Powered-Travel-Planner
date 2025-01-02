from crewai import Agent, LLM
from tools.calculator_tools import CalculatorTools
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool
import streamlit as st
import re

from dotenv import load_dotenv

load_dotenv()

# Initialize the tool for internet searching capabilities
search_tool = SerperDevTool()
web_scrap_tool = ScrapeWebsiteTool()

llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.7
)

# llm = LLM(
#     model="ollama/mistral",
#     base_url="http://localhost:11434"
# )


def tripagents():
    city_selection_agent = Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory=
            'An expert in analyzing travel data to pick ideal destinations',
            llm = llm,
            tools=[
                search_tool,
                web_scrap_tool,
            ],
            verbose=True)

    local_expert_agent = Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
            about the city, it's attractions and customs""",
            llm = llm,
            tools=[
                search_tool,
                web_scrap_tool,
            ],
            verbose=True)

    travel_budget_agent = Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
            packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
            decades of experience""",
            llm = llm,
            tools=[
                search_tool,
                web_scrap_tool,
                CalculatorTools.calculate,
            ],
            verbose=True)
    
    return city_selection_agent, local_expert_agent, travel_budget_agent


