import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_support_crew
from agents.content_agents import create_support_agents

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

def test_customer_support():
    """
    Test the customer support multi-agent system
    """
    print("\n=== Testing Customer Support Multi-Agent System ===")
    try:
        support_agent, qa_agent = create_support_agents(customer="Gister App")
        
        result = create_support_crew(
            support_agent=support_agent,
            qa_agent=qa_agent,
            inquiry=(
                "I need help with setting up a Crew "
                "and kicking it off, specifically "
                "how can I add memory to my crew? "
                "Can you provide guidance?"
            ),
            person="Ike"
        )
        display_result(result)
        print("✓ Customer support test completed successfully")
    except Exception as e:
        print(f"✗ Customer support test error: {str(e)}")

if __name__ == "__main__":
    test_customer_support()
