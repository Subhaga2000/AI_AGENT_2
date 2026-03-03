import os
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AIAgent(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

llm = ChatOpenAI(model = "gpt-3.5-turbo")
    

def agent(state: AIAgent) -> AIAgent:
    """This node will solve the request you input"""
    response = llm.invoke(state["messages"])


    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    print("CURRENT STATE: ", state["messages"])

    return state

graph = StateGraph(AIAgent)
graph.add_node(agent,"agent")
graph.add_edge(START, "agent")
graph.add_edge("agent", END)

app = graph.compile()

conversation_history = []

user_input = input("You: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))

    result = app.invoke({"messages": conversation_history.copy()})
    conversation_history = result["messages"]
    
    user_input = input("Enter: ")

with open("logging.txt", "w") as file:
    file.write("Your conversation Log:\n")

    for msg in conversation_history:
        if isinstance(msg, HumanMessage):
            file.write(f"You: {msg.content}\n")
        elif isinstance(msg, AIMessage):
            file.write(f"AI: {msg.content}\n\n")
    file.write("End of conversation")

print("Conversation log saved to logging.txt")

