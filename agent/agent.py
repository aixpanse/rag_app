
from langgraph.graph import StateGraph, END
from utils.nodes import handle_user_request
from utils.state import State
from utils.tools import get_orders, retrieve, make_order, get_current_date, send_message
from langgraph.prebuilt import ToolNode, tools_condition

tools = ToolNode([retrieve, make_order, get_current_date, send_message, get_orders])

builder = StateGraph(State)

builder.add_node(handle_user_request)
builder.add_node(tools);

builder.set_entry_point('handle_user_request')
builder.add_conditional_edges(
    "handle_user_request",
    tools_condition,
    { END: END, "tools": "tools" },
)
builder.add_edge("tools", "handle_user_request")

graph = builder.compile()
