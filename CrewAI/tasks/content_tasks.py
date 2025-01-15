from crewai import Task
from tools.content_tools import create_test_research_tools

docs_scrape_tool = create_test_research_tools()[0]

def create_content_tasks(planner, writer, editor):
    """
    Create and return the content creation tasks
    """
    plan = Task(
        description=(
            "1. Prioritize the latest trends, key players, "
                "and noteworthy news on {topic}.\n"
            "2. Identify the target audience, considering "
                "their interests and pain points.\n"
            "3. Develop a detailed content outline including "
                "an introduction, key points, and a call to action.\n"
            "4. Include SEO keywords and relevant data or sources."
        ),
        expected_output="A comprehensive content plan document "
            "with an outline, audience analysis, "
            "SEO keywords, and resources.",
        agent=planner,
    )

    write = Task(
        description=(
            "1. Use the content plan to craft a compelling "
                "blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Sections/Subtitles are properly named "
                "in an engaging manner.\n"
            "4. Ensure the post is structured with an "
                "engaging introduction, insightful body, "
                "and a summarizing conclusion.\n"
            "5. Proofread for grammatical errors and "
                "alignment with the brand's voice.\n"
        ),
        expected_output="A well-written blog post "
            "in markdown format, ready for publication, "
            "each section should have 2 or 3 paragraphs.",
        agent=writer,
    )

    edit = Task(
        description=("Proofread the given blog post for "
                     "grammatical errors and "
                     "alignment with the brand's voice."),
        expected_output="A well-written blog post in markdown format, "
                        "ready for publication, "
                        "each section should have 2 or 3 paragraphs.",
        agent=editor
    )


    return [plan, write, edit]

def customer_support_task(support_agent, qa_agent):
    """
    Create tasks for customer support workflow
    
    Args:
        support_agent: The customer support agent
        qa_agent: The quality assurance agent
        
    Returns:
        list: List of tasks for the support workflow
    """
    support_inquiry = Task(
        description=(
            "{customer} just reached out with a super important ask:\n"
            "{inquiry}\n\n"
            "{person} from {customer} is the one that reached out. "
            "Make sure to use everything you know "
            "to provide the best support possible."
            "You must strive to provide a complete "
            "and accurate response to the customer's inquiry."
        ),
        expected_output=(
            "A detailed, informative response to the "
            "customer's inquiry that addresses "
            "all aspects of their question.\n"
            "The response should include references "
            "to everything you used to find the answer, "
            "including external data or solutions. "
            "Ensure the answer is complete, "
            "leaving no questions unanswered, and maintain a helpful and friendly "
            "tone throughout."
        ),
        tools=[docs_scrape_tool],
        agent=support_agent
    )

    quality_review = Task(
        description=(
            "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
            "Ensure that the answer is comprehensive, accurate, and adheres to the "
            "high-quality standards expected for customer support.\n"
            "Verify that all parts of the customer's inquiry "
            "have been addressed "
            "thoroughly, with a helpful and friendly tone.\n"
            "Check for references and sources used to "
            "find the information, "
            "ensuring the response is well-supported and "
            "leaves no questions unanswered."
        ),
        expected_output=(
            "A final, detailed, and informative response "
            "ready to be sent to the customer.\n"
            "This response should fully address the "
            "customer's inquiry, incorporating all "
            "relevant feedback and improvements.\n"
            "Don't be too formal, we are a chill and cool company "
            "but maintain a professional and friendly tone throughout."
        ),
        agent=qa_agent
    )
    
    return [support_inquiry, quality_review]




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
