# 🤖 Day 4 - Tool Calling Agent (RAG Bootcamp)

This project demonstrates how to build a manual tool-calling AI agent using LangChain.
It is part of the RAG Bootcamp conducted by Nunnari Academy.

## 🚀 Features

- Define custom tools using @tool
- Web search using Tavily API
- Text summarization using Ollama (LLaMA 3.2)
- Manual agent loop with JSON-based tool calling
- ReAct agent using LangGraph (bonus)

## 🧠 Key Concept

Tools are just Python functions.
The LLM decides which tool to call, and your code executes it.

## 🛠️ Tools Used

- LangChain
- Tavily Search API
- Ollama (llama3.2:3b)
- LangGraph

## 📂 Project Structure

day4_tool_calling.py   # Main file with tools + agent loop
README.md              # Project documentation

## ⚙️ Setup Instructions

### 1. Install Dependencies

pip install langchain langchain-community langgraph tavily-python ollama

### 2. Start Ollama

ollama run llama3.2:3b

### 3. Set Tavily API Key (Windows PowerShell)

$env:TAVILY_API_KEY="your_api_key"

### 4. Run the Project

python day4_tool_calling.py

## 🧪 Example Queries

- What is the latest news on OpenAI?
- Summarize this paragraph: AI is transforming industries...
- Find the latest news on AI agents and summarize it

## 🎯 Learning Outcome

- Understand tool calling in AI agents
- Build manual agent loops
- Implement multi-step reasoning
- Compare manual vs ReAct agents

## 👨‍💻 Author

Bharath S  
RAG Bootcamp - Nunnari Academy
