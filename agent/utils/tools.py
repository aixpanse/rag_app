from datetime import datetime
from langchain_core.tools import tool
from utils.store import list_orders, search_websites, create_order, create_message

@tool(
    response_format="content_and_artifact",
    description="Retrieve information related to a query. The query must be in English language.",
    parse_docstring=False
)
def retrieve(query: str):
    """
    Retrieve information related to a query.
    
    Args:
        query (str): A query string in English language.
    """
    return search_websites(query)

@tool(
    description="Returns current date and time"
)
def get_current_date():
    """
    Retrieve information about current date and time.
    
    Returns:
        datetime: The current date and time.
    """
    return datetime.now()

@tool(
    description="Create users's order",
    parse_docstring=True
)
def make_order(orderDetails: str, readyDate: str, readyTime: str, contactDetails: str):
    """
    Create user's order.
    
    Args:
        orderDetails (str): What user ordered.
        readyDate (str): Date when order should be ready.
        readyTime (str): Time when order should be ready.
        contactDetails (str): Email or phone number of the user who made the order.
    
    Returns:
        str: "ok" if the order is saved successfully, otherwise an error message.
    """

    if orderDetails == "":
        return "error: orderDetails is required"
    if readyDate == "":
        return "error: readyDate is required"    
    if contactDetails == "":
        return "error: contactDetails are required"

    create_order({
        "orderDetails": orderDetails,
        "readyDate": readyDate,
        "readyTime": readyTime,
        "contactDetails": contactDetails
    })
    
    return "ok"

@tool(
    description="Sends user's message",
    parse_docstring=True
)
def send_message(messageContent: str, sender: str):
    """
    Sends user's message.
    
    Args:
        messageContent (str): User's message.
        sender (str): Email or phone number of the user who send the message.
    
    Returns:
        str: "ok" if the message is send successfully, otherwise an error message.
    """

    if messageContent == "":
        return "error: messageContent is required"
    if sender == "":
        return "error: sender is required"    

    create_message({
        "messageContent": messageContent,
        "sender": sender
    })
    
    return "ok"

@tool(
    description="Returns list of orders",
    parse_docstring=True
)
def get_orders(isRead: bool = None):
    """
    Returns list of orders.
    
    Args:
        isRead (bool): If false, returns only unread orders. If true, returns read orders. If None returns all orders. This parameter is optional and defaults to None.
    
    Returns:
        []: array of orders.
    """

    orders = list_orders()
    
    if isRead is None:
        return orders
    
    return [order for order in orders if order["isRead"] == isRead]
