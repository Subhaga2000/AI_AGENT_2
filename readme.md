# AI Agent 2 (LangGraph + OpenAI)

A simple CLI chatbot built with LangGraph and LangChain OpenAI.
It keeps conversation history during the session and saves the full chat to a `logging.txt` file when you exit.

## Features
- Command-line chat loop
- Conversation history (messages list)
- Saves chat transcript to a log file on exit

## Setup

### 1) Clone the repo
```bash
git clone <https://github.com/Subhaga2000/AI_AGENT_2.git>
cd llm-chatbot
```

### 2) Create and activate a virtual environment
```bash
#Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

#Mac/Linux
python -m venv venv
source venv/bin/activate
```
### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Add your OpenAI API key
```bash
##Create a .env file in the project root:
OPENAI_API_KEY=your_openai_key_here
```

### 5) Run
```bash
python agent2.py
```
