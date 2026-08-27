# AI Agent Demo

A small AI agent built to explore LLM-based agents, tool calling, REST APIs and automation.

## Overview

The project uses an LLM to interpret user requests and autonomously decide which available tools should be executed.

Current tools:

- System status monitoring
- Mathematical calculations

## Architecture

```text
User
  ↓
Python Agent
  ↓
OpenAI LLM
  ↓
Tool Calling
  ↓
Python Tools
  ↓
Tool Result
  ↓
LLM
  ↓
Final Response
```

The project also exposes the agent through a REST API using FastAPI.

## Technologies

- Python 3.13
- OpenAI API
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- uv
- Git

## Running locally

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Install dependencies:

```bash
uv sync
```

Run the CLI agent:

```bash
uv run main.py
```

Run the REST API:

```bash
uv run uvicorn api:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## API

### Health check

`GET /health`

### AI Agent

`POST /agent`

Example:

```json
{
  "message": "Check the system status and calculate 250 + 375."
}
```

The agent can decide to use multiple tools for a single request.

## Project purpose

This project was created as a practical study of AI agents, LLM tool calling, API integration and automation.
