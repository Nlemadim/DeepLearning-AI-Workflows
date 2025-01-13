import warnings
from crewai import Crew
from agents.content_agents import create_content_agents
from tasks.content_tasks import create_content_tasks
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
    
    # Create agents
    planner, writer, editor = create_content_agents()
    
    # Create tasks
    tasks = create_content_tasks(planner, writer, editor)
    
    # Create crew
    crew = Crew(
        agents=[planner, writer, editor],
        tasks=tasks,
        verbose=VERBOSE_OUTPUT
    )
    
    # Run the crew
    result = crew.kickoff(inputs={"topic": topic})
    return result

if __name__ == "__main__":
    # Example usage
    topic = get_topic("technology")  # Gets "Artificial Intelligence"
    result = create_content_crew(topic)
    print(result)
