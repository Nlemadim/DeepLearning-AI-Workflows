import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import validate_settings
from main import create_support_crew
from tools.content_tools import create_test_research_tools

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
    """Test configuration and environment setup"""
    print("\n=== Testing Configuration ===")
    try:
        validate_settings()
        print("✓ Configuration validated successfully")
        
        # Verify tools are available
        tools = create_test_research_tools()
        if tools and len(tools) > 0:
            print("✓ Support tools loaded successfully")
        else:
            raise Exception("Failed to load support tools")
            
    except Exception as e:
        print(f"✗ Configuration error: {str(e)}")
        sys.exit(1)

def test_customer_support():
    """
    Test the customer support multi-agent system with tools
    """
    print("\n=== Testing Customer Support Multi-Agent System ===")
    
    # Test case parameters
    test_params = {
        "inquiry": (
            "I need help with setting up a Crew "
            "and kicking it off, specifically "
            "how can I add memory to my crew? "
            "Can you provide guidance?"
        ),
        "person": "Ike",
        "customer": "Gister App"
    }
    
    try:
        # Execute support crew workflow
        result = create_support_crew(**test_params)
        
        # Display results
        print("\nSupport Interaction Result:")
        display_result(result)
        
        # Verify result contains expected elements
        if not result or len(result.strip()) == 0:
            raise Exception("Support crew returned empty result")
            
        print("\n✓ Customer support test completed successfully")
        
    except Exception as e:
        print(f"✗ Customer support test error: {str(e)}")
        raise e

if __name__ == "__main__":
    # Test configuration first
    test_configuration()
    
    # Run customer support test
    test_customer_support()
