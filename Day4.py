from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.chat_models import ChatOllama
from langgraph.prebuilt import create_react_agent
import json

# -----------------------------
# LLM Setup
# -----------------------------
llm = ChatOllama(model="llama3.2:3b")

# -----------------------------
# Exercise 1 — Define Tools
# -----------------------------
@tool
def web_search(query: str) -> str:
    """Search the web for real-time information"""
    search = TavilySearchResults()
    results = search.invoke(query)
    return str(results)

@tool
def summarize(text: str) -> str:
    """Summarize given text into a short paragraph"""
    prompt = f"Summarize this in 3-4 lines:\n\n{text}"
    response = llm.invoke(prompt)
    return response.content


# -----------------------------
# Test tools standalone
# -----------------------------
if __name__ == "__main__":
    print("\n--- Testing Tools Standalone ---")

    print("\nWeb Search Test:")
    print(web_search.invoke("Latest news on OpenAI"))

    print("\nSummarize Test:")
    print(summarize.invoke(
        "AI is transforming industries by enabling automation and smarter decision-making."
    ))


# -----------------------------
# Exercise 2 — Manual Tool Loop
# -----------------------------
SYSTEM_PROMPT = """
You are an AI agent with access to tools.

Available tools:
1. web_search(query: str)
2. summarize(text: str)

Rules:
- Always respond in JSON
- If using tool:
  {"tool": "tool_name", "args": {"param": "value"}}
- If final answer:
  {"final_answer": "your answer"}
"""

def run_agent(query):
    print("\n==============================")
    print("USER QUERY:", query)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]

    while True:
        response = llm.invoke(messages)
        content = response.content.strip()

        print("\nLLM OUTPUT:", content)

        try:
            parsed = json.loads(content)
        except:
            print("❌ Invalid JSON, stopping...")
            break

        # Final answer
        if "final_answer" in parsed:
            print("\n✅ FINAL ANSWER:", parsed["final_answer"])
            break

        # Tool call
        tool_name = parsed.get("tool")
        args = parsed.get("args", {})

        print(f"\n🔧 Tool Chosen: {tool_name}")

        if tool_name == "web_search":
            result = web_search.invoke(args.get("query", ""))
        elif tool_name == "summarize":
            result = summarize.invoke(args.get("text", ""))
        else:
            result = "Unknown tool"

        print("\n📤 Tool Result:", result)

        # ✅ FIX: Feed result as USER (NOT tool role)
        messages.append({"role": "assistant", "content": content})
        messages.append({
            "role": "user",
            "content": f"Tool result: {result}"
        })


# -----------------------------
# Exercise 3 — Test Queries
# -----------------------------
if __name__ == "__main__":
    print("\n\n--- Running Manual Agent Loop ---")

    run_agent("What is the latest news on OpenAI?")

    run_agent(
        "Summarize this paragraph: AI is revolutionizing industries by improving efficiency and enabling automation."
    )

    run_agent("Find the latest news on AI agents and summarize it")


# -----------------------------
# Exercise 4 — ReAct Agent
# -----------------------------
if __name__ == "__main__":
    print("\n\n--- Running ReAct Agent ---")

    tools = [web_search, summarize]
    react_agent = create_react_agent(llm, tools)

    queries = [
        "What is the latest news on OpenAI?",
        "Summarize this paragraph: AI is revolutionizing industries.",
        "Find the latest news on AI agents and summarize it"
    ]

    for q in queries:
        print("\n==============================")
        print("QUERY:", q)
        result = react_agent.invoke({"messages": [("user", q)]})
        print("RESPONSE:", result)