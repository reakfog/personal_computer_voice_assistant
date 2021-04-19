from .actions import *


def search_command(command_name:str, *args: list) -> None:
    """Searching user-specified command and arguments
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass


def execute_command(text:str) -> None:
    """Executing a user-defined command
    """
    input_text = text.split(' ')
    command_name = input_text[0]
    command_options = [str(part) for part in input_text[1:len(input_text)]]
    search_command(command_name, command_options)


commands = {
    ('hello', 'hi', 'morning', 'привет'): play_greetings,
    ('bye', 'goodbye', 'quit', 'exit', 'stop', 'пока'): play_goodbye_and_quit,
    ('search', 'find', 'google', 'найди'): search_for_term_on_google,
    ('video', 'youtube', 'watch', 'видео'): search_for_video_on_youtube,
    ('timer for','set a timer for', 'set the timer for', 'set timer for',
    'таймер на', 'поставь таймер на', 'установи таймер на'):timer,
    ('Error:'): play_error,
}
