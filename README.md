# Pulse Bengaluru Agent

This repository contains the implementation of the Pulse Bengaluru Agent, a multi-agent system designed to analyze various aspects related to Bengaluru, including network quality, radio charter data, and social media sentiment. The project leverages Google's Agent Development Kit (ADK) and LangChain for building sophisticated LLM-powered agents.

## Technologies Used

The project primarily uses Python and the following key libraries:

*   **`google-generativeai`**: For interacting with Google's Generative AI models.
*   **`langchain`**: A framework for developing applications powered by language models.
*   **`langchain-google-genai`**: LangChain integration for Google Generative AI.
*   **`langchain-core`**: Core abstractions for LangChain.
*   **`langchain-community`**: Community integrations for LangChain.
*   **`python-dotenv`**: For managing environment variables.

## Project Structure

The repository is organized into two main components:

*   **`pulse_bengaluru_agent-parent/`**: This directory contains the main multi-agent application.
    *   `main.py`: The entry point for running the main agent.
    *   `agent.py`: Defines the orchestrating agent.
    *   `sub_agents/`: Contains specialized sub-agents.
        *   `network_quality_analyst/`: Agent focused on analyzing network quality data.
        *   `radio_charter_analyst/`: Agent focused on analyzing radio charter data.
        *   `social_media_analyst/`: Agent focused on analyzing social media sentiment.
    *   `tools/`: Contains custom tools used by the agents.
*   **`pulse_cloud_fn/`**: This directory contains the necessary files for deploying the agent as a Google Cloud Function.
    *   `main.py`: The entry point for the Cloud Function.
    *   `requirements.txt`: Dependencies specific to the Cloud Function environment.

## Getting Started (Local Setup)

Follow these steps to set up the project and run the agent locally:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd "Agentic AI Day Hackathon" # Or the name of your cloned directory
```

### 2. Setup Python Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# Create virtual environment in the root directory
python -m venv .venv

# Activate the virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required Python packages for both the main agent and the cloud function.

```bash
pip install -r pulse_bengaluru_agent-parent/requirements.txt
pip install -r pulse_cloud_fn/requirements.txt
```

### 4. Setting Up Google API Key

The agents require a Google API Key to interact with Generative AI models.

1.  Create an account in Google Cloud: [https://cloud.google.com/](https://cloud.google.com/)
2.  Create a new project within Google Cloud.
3.  Go to Google AI Studio API Keys: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
4.  Create a new API key and associate it with your Google Cloud project.
5.  Ensure your Google Cloud project has a billing account connected (required for some API usage).

After obtaining your API key:

1.  Navigate to the `pulse_bengaluru_agent-parent/` directory.
2.  Create a new file named `.env` in this directory.
3.  Add your API key to the `.env` file in the following format:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```
    Replace `your_api_key_here` with your actual Google API Key.

### 5. Running the Main Agent Locally

Once the environment is set up and the API key is configured, you can run the main agent:

```bash
cd pulse_bengaluru_agent-parent/
python main.py
```

This will start the main agent, and you can interact with it through the console.

## Sub-Agents Overview

*   **Network Quality Analyst**: Specializes in processing and analyzing data related to network performance and quality.
*   **Radio Charter Analyst**: Focuses on analyzing radio charter data, potentially for frequency allocation, signal strength, or regulatory compliance.
*   **Social Media Analyst**: Designed to monitor and analyze social media trends, sentiment, and discussions relevant to Bengaluru.

Each sub-agent contributes to a comprehensive understanding of the Bengaluru context by providing specialized insights.