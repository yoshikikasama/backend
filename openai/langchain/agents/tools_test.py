from langchain.agents import load_tools

tool_names = ["python_repl"]
tools = load_tools(tool_names)
print(tools)