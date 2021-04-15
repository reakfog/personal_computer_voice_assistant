from .actions import *


def search_command(command_name: str, *args: list):
    """
    Searching user-specified command and arguments
    :param - command_name: command_name
    :param - *args: command_options
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass


def execute_command(text):
    """
    Executing a user-defined command
    :param - text: the text we received after listening to the voice
    """
    input_text = text.split(' ')
    command_name = input_text[0]
    command_options = [str(part) for part in input_text[1:len(input_text)]]
    search_command(command_name, command_options)


commands = {
    ('hello', 'hi', 'morning', 'привет'): play_greetings,
    ('bye', 'goodbye', 'quit', 'exit', 'stop', 'пока'): play_goodbye_and_quit,
    ('search', 'find', 'google', 'найди'): search_for_term_on_google,
    ('Error:'): play_error,
}
