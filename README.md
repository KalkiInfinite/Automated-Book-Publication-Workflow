# Automated Book Publication Workflow

## Objective
Create a system to fetch content from a web URL, apply an AI-driven "spin" to chapters, and allow multiple human-in-the-loop iterations with reinforcement learning (RL) based reward mechanisms.

## Key Capabilities

1. **Scraping & Screenshots**
   - Fetch content from web sources (e.g., [The Gates of Morning - Chapter 1](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)).
   - Save screenshots of the fetched content.
   - Integrate RL-based reward system for scraping quality and relevance.

2. **AI Writing & Review**
   - Use Large Language Models (LLMs) such as Gemini or others for AI-driven chapter "spinning" (rewriting).
   - Refine content using an AI Reviewer agent.

3. **Human-in-the-Loop**
   - Enable multiple iterations with human input for writers, reviewers, and editors before finalization.
   - Ensure RL-based inference techniques are used to optimize human feedback and content quality.

4. **Agentic API**
   - Seamless content flow between AI agents.
   - Voice support for agent interactions.
   - Version support and semantic search for content management.
   - RL-based reward model for agent actions and decisions.

## Core Tools & Technologies

- **Python**: Main programming language.
- **Playwright**: For web scraping and screenshots.
- **LLM**: For AI writing, reviewing, and editing.
- **ChromaDB**: For content versioning and semantic search.
- **RL Search Algorithm**: For consistent and optimized data retrieval.

## Project Structure

```
agent/
    api_agent.py
    voice.py
feedback/
    human_interface.py
    rl_reward.py
llm/
    reviewer.py
    writer.py
scraping/
    scrapper.py
storage/
    chroma_store.py
utils/
    config.py
main.py
requirements.txt
.env
```

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Configure environment:**
   - Set up your `.env` file with necessary environment variables.

3. **Run the workflow:**
   ```bash
   python main.py
   ```

## How It Works

- The system scrapes a chapter from a given URL, saves a screenshot, and processes the text.
- The AI Writer spins the chapter, and the AI Reviewer refines it.
- Human users can iteratively review and edit the content, with RL-based feedback guiding improvements.
- All content versions are stored and searchable via ChromaDB.
- Agents communicate via an API, with optional voice support and RL-based reward modeling.

## Assignment Context
This project was developed as an assignment to demonstrate a full-stack, agentic, AI-driven workflow for automated book publication, integrating scraping, LLMs, RL, and human-in-the-loop processes.

---
