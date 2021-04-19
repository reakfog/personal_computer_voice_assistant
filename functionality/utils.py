import sys
sys.path = ['', '..'] + sys.path[1:]

from termcolor import colored
from assistance_bot import core


def print_owner_speech(text: str) -> str:
    """Get formatted message from owner

    Args:
        text (str): text to format

    Returns:
        str: formatted message from owner
    """
    owner = core.owner.name
    message = ''.join([owner,': ',colored(text.capitalize(), 'green')])
    return message


def print_assistant_speech(text:str, error:bool=False) -> str:
    """Get formatted message from assistant

    Args:
        text (str): text to format
        status (bool, optional): To get error formatting pass 'error'.
                                                    Defaults to False.

    Returns:
        str: formatted message from assistant
    """
    assistant = core.assistant.name
    if error:
        message = ''.join([assistant, ': ', colored(text, 'red')])
    else:
        message = ''.join([assistant, ': ', colored(text, 'yellow')])
    return message
