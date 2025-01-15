from crewai import Agent

def create_content_agents():
    """
    Create and return the content creation agents
    """
    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="You're working on planning a blog article "
                  "about the topic: {topic}."
                  "You collect information that helps the "
                  "audience learn something "
                  "and make informed decisions. "
                  "Your work is the basis for "
                  "the Content Writer to write an article on this topic.",
        allow_delegation=False,
        verbose=True
    )

    writer = Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate "
             "opinion piece about the topic: {topic}",
        backstory="You're working on a writing "
                  "a new opinion piece about the topic: {topic}. "
                  "You base your writing on the work of "
                  "the Content Planner, who provides an outline "
                  "and relevant context about the topic. "
                  "You follow the main objectives and "
                  "direction of the outline, "
                  "as provide by the Content Planner. "
                  "You also provide objective and impartial insights "
                  "and back them up with information "
                  "provide by the Content Planner. "
                  "You acknowledge in your opinion piece "
                  "when your statements are opinions "
                  "as opposed to objective statements.",
        allow_delegation=False,
        verbose=True
    )

    editor = Agent(
        role="Editor",
        goal="Edit a given blog post to align with "
             "the writing style of the organization. ",
        backstory="You are an editor who receives a blog post "
                  "from the Content Writer. "
                  "Your goal is to review the blog post "
                  "to ensure that it follows journalistic best practices,"
                  "provides balanced viewpoints "
                  "when providing opinions or assertions, "
                  "and also avoids major controversial topics "
                  "or opinions when possible.",
        allow_delegation=False,
        verbose=True
    )

    return planner, writer, editor

def create_support_agents(customer):
    """
    Create and return the support agents
    
    Args:
        customer (str): The customer name for support agents
    """
    customer_support_agent = Agent(
        role="Senior Support Representative",
        goal="Be the most friendly and helpful support representative in your team",
        backstory=(
            f"You work at crewAI (https://crewai.com) and are now working on providing "
            f"support to {customer}, a super important customer for your company. "
            "You need to make sure that you provide the best support! "
            "Make sure to provide full complete answers, and make no assumptions."
        ),
        allow_delegation=False,
        verbose=True
    )

    support_quality_assurance_agent = Agent(
        role="Support Quality Assurance Specialist",
        goal="Get recognition for providing the best support quality assurance in your team",
        backstory=(
            f"You work at crewAI (https://crewai.com) and are now working with your team "
            f"on a request from {customer} ensuring that the support representative is "
            "providing the best support possible.\n"
            "You need to make sure that the support representative is providing full "
            "complete answers, and make no assumptions."
        ),
        verbose=True  
    )

    return customer_support_agent, support_quality_assurance_agent 