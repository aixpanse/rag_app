from langgraph.graph import MessagesState
from utils.tools import get_orders, retrieve
from utils.config import llm
from utils.tools import make_order, get_current_date, send_message
from langchain_core.messages import SystemMessage

def handle_user_request(state: MessagesState):
    system_message_content = (
        "You are helpful assistant who answers user's questions and make orders."
        "If order is to general ask user for more details about order."
        "Before saving an order ask user to confirm order's data."
        "Do not allow user to make two or more the same orders."
        "Send user message if asked using send_message tool."
        "If message send successfully reply exactly with this in user's language: Your message has been sent."
    )
    llm_with_tools = llm.bind_tools([retrieve, make_order, send_message, get_current_date, get_orders])
    response = llm_with_tools.invoke([SystemMessage(system_message_content)] + state["messages"])
    return { "messages": [response] }

    """Generate answer."""
    recent_tool_messages = []
    for message in reversed(state["messages"]):
        if message.type == "tool":
            recent_tool_messages.append(message)
        else:
            break
    tool_messages = recent_tool_messages[::-1]

    docs_content = "\n\n".join(doc.content for doc in tool_messages)
    system_message_content = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        f"{docs_content}"
    )
    conversation_messages = [
        message
        for message in state["messages"]
        if message.type in ("human", "system")
        or (message.type == "ai" and not message.tool_calls)
    ]
    prompt = [SystemMessage(system_message_content)] + conversation_messages

    response = llm.invoke(prompt)
    return {"messages": [response]}
