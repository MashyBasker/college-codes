from src.utils import get_command, RED, RESET
from src.commands import new_db, insert, update, fetch, delete
import sys

def handle_command(cmd: str):
    """
    This function parses the command provided and
    handles it accordingly
    """
    match cmd.split(" ")[0]:
        case 'new':
            new_db(cmd.split(" ")[1])
        case 'insert':
            insert(cmd)
        case 'update':
            update(cmd)
        case 'fetch':
            fetch(cmd)
        case 'delete':
            delete(cmd)
        case 'exit':
            sys.exit(0)
        case _:
            print(RED+'[ERR] Command not recognized'+RESET)

def main():
    """
    The main program loop that is responsible for running the 
    database application
    """
    while True:
        x = get_command()
        handle_command(x)
