import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.topics import get_topic, get_all_topics
from config.settings import validate_settings
from main import create_content_crew

try:
    from IPython.display import Markdown
    IN_NOTEBOOK = True
except ImportError:
    IN_NOTEBOOK = False

def display_result(result):
    """Display result in markdown if in notebook, otherwise print"""
    if IN_NOTEBOOK:
        return Markdown(result)
    else:
        print(result)

def test_configuration():
    """
    Test configuration and environment setup
    """
    print("\n=== Testing Configuration ===")
    try:
        validate_settings()
        print("✓ Configuration validated successfully")
    except Exception as e:
        print(f"✗ Configuration error: {str(e)}")
        sys.exit(1)  # Exit if configuration is invalid

def test_content_creation():
    """
    Test content creation with a specific topic
    """
    topic = "Artificial Intelligence"
    print(f"\n=== Testing Content Creation for {topic} ===")
    try:
        result = create_content_crew(topic)
        display_result(result)
    except Exception as e:
        print(f"Error: {str(e)}\n")

def test_topics():
    """
    Test topic retrieval functionality
    """
    print("\n=== Testing Topic Retrieval ===")
    print(f"Technology topic: {get_topic('technology')}")
    print(f"Business topic: {get_topic('business')}")
    print(f"Science topic: {get_topic('science')}")
    print("\nAll topics:", get_all_topics())

if __name__ == "__main__":
    # Test configuration first
    test_configuration()
    
    # Test topics
    test_topics()
    
    # Test content creation
    test_content_creation() 