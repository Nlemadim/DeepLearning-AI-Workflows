# CrewAI Content Generation System

A modular and extensible content generation system built with CrewAI that demonstrates multi-agent collaboration for content creation. This system uses a team of AI agents (planner, writer, and editor) to generate high-quality content on any given topic.

## Project Structure 

```
CrewAI/
├── main.py                 # Main application entry point
├── agents/                 # Agent definitions
│   ├── __init__.py
│   └── content_agents.py   # Content creation agents
├── tasks/                  # Task definitions
│   ├── __init__.py
│   └── content_tasks.py    # Content creation tasks
├── config/                 # Configuration files
│   ├── __init__.py
│   ├── settings.py        # Global settings
│   ├── topics.py         # Topic configurations
│   └── llm_config.py     # LLM provider configurations
├── tests/                 # Test files
│   ├── __init__.py
│   ├── manual_test.py    # Manual testing script
│   └── test_llm_config.py # LLM configuration tests
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Virtual environment (recommended)
- Jupyter Notebook (optional, for interactive testing)

### Installation

1. Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd CrewAI
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```
OPENAI_API_KEY=your-openai-key-here
HUGGINGFACE_API_TOKEN=your-huggingface-token
MISTRAL_API_KEY=your-mistral-key
COHERE_API_KEY=your-cohere-key
```

### Running the Application

You can run the application in two ways:

1. Command Line:
```bash
python main.py
```

2. Jupyter Notebook (for interactive testing):
```bash
jupyter notebook
```

#### Using Jupyter Notebook

Create a new notebook (e.g., `crewai_test.ipynb`) and use this example:

```python
# Import required modules
from main import create_content_crew, create_support_crew
from config.topics import get_topic
from IPython.display import Markdown, display

# Test content creation
def test_content():
    topic = get_topic("technology")
    result = create_content_crew(topic)
    display(Markdown(result))

# Test support system
def test_support():
    result = create_support_crew(
        inquiry="How do I add memory to my crew?",
        person="John",
        customer="Tech Corp"
    )
    display(Markdown(result))

# Run tests
print("Testing Content Creation:")
test_content()

print("\nTesting Support System:")
test_support()
```

**Note**: Jupyter Notebook provides:
- Interactive execution of code cells
- Rich markdown rendering of results
- Real-time debugging capabilities
- Ability to save and share results

## 🔧 Features

### 1. Topic Management (`config/topics.py`)

Predefined topics in categories:
- Technology
- Business
- Science

Access topics programmatically:
```python
from config.topics import get_topic, get_all_topics

# Get a specific topic
tech_topic = get_topic("technology")

# Get all topics in a category
business_topics = get_all_topics("business")
```

### 2. Multiple LLM Support (`config/llm_config.py`)

Support for various LLM providers:
- OpenAI (default)
- HuggingFace
- Mistral
- Cohere

### 3. Testing

Two testing approaches:
1. Unit Tests:
```bash
python -m unittest tests/test_llm_config.py
```

2. Manual Testing:
```bash
python tests/manual_test.py
```

### 4. Interactive Development

Jupyter Notebook support for:
- Interactive testing
- Markdown rendering
- Real-time output viewing

## 🔧 Component Overview

### 1. Agents (`agents/content_agents.py`)

The system uses three specialized agents:

- **Content Planner**: Develops content strategy and outlines
- **Content Writer**: Creates the actual content based on the plan
- **Editor**: Reviews and refines the content

Each agent has:
- A specific role
- A defined goal
- A detailed backstory
- Configurable delegation permissions
- Verbosity settings

Example of extending with a new agent:
```python
new_agent = Agent(
    role="Research Specialist",
    goal="Conduct in-depth research on specific topics",
    backstory="You are an expert researcher...",
    allow_delegation=False,
    verbose=True
)
```

### 2. Tasks (`tasks/content_tasks.py`)

Tasks define the work each agent needs to perform. Each task includes:
- A detailed description
- Expected output format
- Assigned agent

### Task Setup with Tools

Tasks can be configured with specific tools that override agent-level tools:

```python
# Create a tool instance
research_tool = create_test_research_tools()[0]

# Task with specific tool
support_task = Task(
    description="Handle customer inquiry about {topic}",
    expected_output="Detailed response addressing inquiry",
    tools=[research_tool],  # Tool assigned at task level
    agent=support_agent
)
```

#### Tool Assignment Hierarchy:

1. **Agent-Level Tools**:
   - Available for all tasks
   - Agent has discretionary use

2. **Task-Level Tools**:
   - Override agent's default tools
   - Exclusively used for specific task
   - Provide precise control

#### Best Practices:
- Assign general-purpose tools at agent level
- Use task-specific tools for specialized operations
- Document tool dependencies clearly
- Test tool availability before task execution

To add a new task:
```python
new_task = Task(
    description="Detailed task description...",
    expected_output="Expected output format...",
    agent=assigned_agent
)
```

### 3. Configuration (`config/settings.py`)

Manages global settings and environment variables:
- API keys
- Model configurations
- Environment variables

### 4. Utilities (`utils/api_keys.py`)

Helper functions for:
- API key management
- Environment variable handling
- Error handling

## 🔄 Workflow

1. **Initialization**:
   - Load configuration
   - Initialize agents
   - Set up tasks

2. **Execution**:
   - Planner creates content strategy
   - Writer develops content
   - Editor reviews and refines

3. **Output**:
   - Final content in markdown format
   - Execution logs (if verbose)

## 🛠️ Customization and Extension

### Adding New Agent Types

1. Create new agent definitions in `agents/`:
```python
def create_custom_agents():
    custom_agent = Agent(
        role="Custom Role",
        goal="Custom Goal",
        backstory="Custom Backstory"
    )
    return custom_agent
```

### Creating New Task Types

1. Add new task definitions in `tasks/`:
```python
def create_custom_tasks(agent):
    custom_task = Task(
        description="Custom task description",
        expected_output="Expected output format",
        agent=agent
    )
    return [custom_task]
```

### Modifying the Workflow

1. Update `main.py` to include new agents and tasks:
```python
def create_custom_crew(input_data):
    custom_agents = create_custom_agents()
    custom_tasks = create_custom_tasks(custom_agents)
    crew = Crew(
        agents=[custom_agents],
        tasks=custom_tasks,
        verbose=2
    )
    return crew.kickoff(inputs=input_data)
```

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment

1. Set up environment variables in your production environment
2. Ensure all dependencies are installed
3. Configure logging and monitoring as needed
4. Consider using a process manager (e.g., PM2, Supervisor)

### Docker Deployment

1. Create a Dockerfile:
```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

2. Build and run:
```bash
docker build -t crewai-content .
docker run -e OPENAI_API_KEY=your-key crewai-content
```

## 🔄 Alternative Use Cases

This system can be adapted for various purposes:

1. **Research Analysis**:
   - Modify agents for research roles
   - Add data collection tasks
   - Include analysis and reporting tasks

2. **Customer Support**:
   - Create support agent roles
   - Add ticket handling tasks
   - Include response generation tasks

3. **Code Generation**:
   - Define developer agent roles
   - Add code planning tasks
   - Include testing and review tasks

## 📝 Logging and Monitoring

Enable verbose logging in the Crew initialization:
```python
crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=2  # 0=minimal, 1=basic, 2=detailed
)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 