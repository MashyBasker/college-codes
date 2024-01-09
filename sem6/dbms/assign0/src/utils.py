from typing import Dict, Tuple, List

# ANSI escape codes for text color
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'  # Reset to default color

def get_command() -> str:
    """
    This function gets the command from the 
    user with a prompt at the beginning
    """
    i = input(GREEN+"α> "+RESET)
    return i

def parse_update_conditions(conditions: str) -> Tuple[Dict, Dict]:
    """
    Function for parsing and converting the conditions in the `update`
    command into dictionaries.
    """
    new_vals, where = conditions.split("|")
    # dictionary for storing the new attribute values
    new_val_dict = {}
    if len(new_vals) == 1:
        attr, val = new_vals[0].split(":")
        new_val_dict[attr] = val
    else:
        for x in new_vals.split(','):
            attr, val = x.split(":")
            new_val_dict[attr] = val
    # dictionary for storing the where clause
    condition_dict = {}
    if len(where) == 1:
        attr, val = where[0].split(":")
        condition_dict[attr] = val
    else:
        for x in where.split(","):
            attr, val = x.split(":")
            condition_dict[attr] = val

    return new_val_dict, condition_dict

def row_condition_match(row: Dict, cond: Dict) -> bool:
    """
    To check if a row matches a specific dictionary condition
    """
    v = True
    for k in cond.keys():
        if row[k] != cond[k]:
            v = False
    return v

def parse_fetch_conditions(cond: str) -> Tuple[List, Dict]:
    """
    Parse the query of the fetch command into attributes and conditions
    """
    attr, condition = cond.split("|")
    attr_list = []
    if len(attr) == 1:
        attr_list = list(attr[0])
    else:
        attr_list = attr.split(",")
    cond_dict = {}
    if len(condition) == 1:
        a, val = condition[0].split(":")
        cond_dict[a] = val
    else:
        for x in condition.split(","):
            a, val = x.split(":")
            cond_dict[a] = val
    return attr_list, cond_dict

def parse_del_conditions(cond: str) -> Dict:
    """
    Parse the query of the delete command into conditions dictionary
    """
    cond_dict = {}
    if len(cond) == 1:
        a, v = cond[0].split(":")
        cond_dict[a] = v
    else:
        for x in cond.split(","):
            a, v = x.split(":")
            cond_dict[a] = v
    return cond_dict

