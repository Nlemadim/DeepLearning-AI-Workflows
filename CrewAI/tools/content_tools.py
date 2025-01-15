"""
Content Tools Module
===================

This module manages the creation and organization of tools for CrewAI agents.

Tool Assignment Hierarchy:
-------------------------

Tools in CrewAI can be assigned at two levels:

1. Agent Level:
   - Tools assigned directly to an agent are available for all tasks
   - The agent has discretionary use of these tools
   
2. Task Level:
   - Tools assigned to specific tasks override agent-level tools
   - When a task has assigned tools, the agent will ONLY use those tools
   - This provides precise control over tool usage for specific tasks

Visual Representation:
---------------------

                     Assigning Tools
                     
                    ┌──────────────┐
                    │    Tools     │
                    └──────┬───────┘
                           │
                 ┌────────┴────────┐
                 │                  │
        ┌────────┴───────┐    ┌────┴────┐
        │     Agent      │    │  Task   │
        │   (Default)    │    │(Override)│
        └────────────────┘    └─────────┘

Notes:
- Tools assigned to Agent: Available for all tasks (discretionary use)
- Tools assigned to Task: Exclusively used for that specific task
"""

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool, CSVSearchTool, DOCXSearchTool, YoutubeChannelSearchTool, GithubSearchTool, PDFSearchTool

def create_research_tools():
    """
    Create and return tools for content research
    """
    search_tool = SerperDevTool()     # Integrates with SerpAPI. Its an external tool that allows you to search Google
    scrape_tool = ScrapeWebsiteTool()  # Accesses a given url and scrapes the contents
    web_tool = WebsiteSearchTool()     # General web search tool that can work with different search engines
    
    return [search_tool, scrape_tool, web_tool]

def create_test_research_tools():
    """
    Create and return a tool that will scrape a page (only 1 URL) of the CrewAI documentation 
    """
    docs_scrape_tool = ScrapeWebsiteTool(
        website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
    )
    
    return [docs_scrape_tool]

def get_all_content_tools():
    """
    Get all tools needed for content creation
    """
    research_tools = create_research_tools()
    test_tools = create_test_research_tools()
    
    return research_tools + test_tools 