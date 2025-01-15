import warnings
from crewai import Crew
from agents.content_agents import create_content_agents, create_support_agents
from tasks.content_tasks import create_content_tasks, customer_support_task
from config.topics import get_topic, get_all_topics
from config.settings import VERBOSE_OUTPUT, validate_settings

# Suppress warnings
warnings.filterwarnings('ignore')

def create_content_crew(topic):
    """
    Create and run a crew for content creation
    
    Args:
        topic (str): The topic to create content about
    """
    # Validate settings before proceeding
    validate_settings()
    
    # 1. Create agents
    planner, writer, editor = create_content_agents()
    
    # 2. Create tasks with the agents
    tasks = create_content_tasks(planner, writer, editor)
    
    # 3. Create and run crew
    content_crew = Crew(
        agents=[planner, writer, editor],
        tasks=tasks,
        verbose=VERBOSE_OUTPUT
    )
    
    # 4. Execute with topic input
    return content_crew.kickoff(inputs={"topic": topic})

def create_support_crew(inquiry, person, customer="Gister App"):
    """
    Create and run a crew for customer support
    
    Args:
        inquiry (str): The customer inquiry
        person (str): The person making the inquiry
        customer (str): The customer company name
    """
    # Validate settings before proceeding
    validate_settings()
    
    # 1. Create agents
    support_agent, qa_agent = create_support_agents(customer=customer)
    
    # 2. Create tasks with agents and tools
    tasks = customer_support_task(
        support_agent=support_agent,
        qa_agent=qa_agent
    )  # Returns list of [support_inquiry, quality_review]
    
    # 3. Create and run crew
    support_crew = Crew(
        agents=[support_agent, qa_agent],
        tasks=tasks,  # Pass the list of tasks directly
        verbose=VERBOSE_OUTPUT,
        memory=True  # Support crew needs memory for context
    )
    
    # 4. Execute with inquiry inputs
    return support_crew.kickoff(inputs={
        "inquiry": inquiry,
        "person": person,
        "customer": customer
    })

if __name__ == "__main__":
    # Example usage for content creation
    topic = get_topic("technology")
    content_result = create_content_crew(topic)
    print("Content Creation Result:", content_result)
    
    # Example usage for support
    support_result = create_support_crew(
        inquiry=(
            "I need help with setting up a Crew "
            "and kicking it off, specifically "
            "how can I add memory to my crew? "
            "Can you provide guidance?"
        ),
        person="Ike",
        customer="Gister App"
    )
    print("Support Result:", support_result)
