from src.utils import parse_update_conditions, row_condition_match, parse_fetch_conditions, parse_del_conditions,RED,RESET,YELLOW
import shutil
from tempfile import NamedTemporaryFile
import os
import csv


def new_db(filename):
    """
    Logic for the `new` command. Creates a new CSV file if it already does not exist.
    """
    if not os.path.isdir('./data/'):
        os.makedirs('./data/')
    if os.path.exists(f'./data/{filename}'):
        print(YELLOW+"[LOG] This file already exists!"+RESET)
    else:
        try:
            with open(f"./data/{filename}", 'w') as f:
                f.write("Name,Semester,Roll,DoB,CGPA,Contact\n")
        except:
            print(RED+"[ERR] Something went wrong while creating this file"+RESET)

def insert(cmd: str):
    """
    Logic for the `insert` command.
    Adds a new record at the end of a CSV file. Check DOCS for the syntax.
    """
    d = cmd.split(" ")[2]
    filename = './data/'+cmd.split(" ")[1]
    if os.path.exists(filename):
        try:
            with open(filename, 'a') as f:
                f.write(d+"\n")
        except:
            raise Exception(RED+f"[ERR] File {filename} is not writable"+RESET)
    else:
        print(RED+"[ERR] This file does not exist"+RESET)

def update(cmd: str):
    """
    Logic for the `update` command.
    Updates a specific attribute in the database for record when a condition is matched.
    Check DOCS for the update syntax.
    """
    _, filename, condition = cmd.split(" ")
    filepath = "./data/"+filename
    if os.path.exists(filepath):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        nv_dict, con_dict = parse_update_conditions(condition)
        fieldnames = ['Name', 'Semester', 'Roll', 'DoB', 'CGPA', 'Contact']
        with open(filepath, 'r', newline='') as dbfile, tempfile:
            reader = csv.DictReader(dbfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if row_condition_match(row, con_dict) == True:
                    for k in nv_dict.keys():
                        row[k] = nv_dict[k]
                writer.writerow(row)
        shutil.move(tempfile.name, filepath)
    else:
        print(RED+"[ERR] This file does not exist"+RESET)

def fetch(cmd: str):
    """
    Logic for the `fetch` command.
    Returns the attributes when matching a specific condition
    """
    _, filename, condition = cmd.split(" ")
    filepath = "./data/"+filename
    if os.path.exists(filepath):
        attr_list, cond_dict = parse_fetch_conditions(condition)
        with open(filepath, 'r', newline='') as dbfile:
            reader = csv.DictReader(dbfile)
            print("-"*20)
            for row in reader:
                if row_condition_match(row, cond_dict):
                    for a in attr_list:
                        print(f"{a}: {row[a]}")
                    print("-"*20)    
    else:
        print(RED+"[ERR] This file does not exist"+RESET)

def delete(cmd: str):
    """
    Logic for the `delete` command
    Deletes a row when a certain condition is met.
    """
    _, filename, condition = cmd.split(" ")
    filepath = "./data/"+filename
    if os.path.exists(filepath):
        tempfile = NamedTemporaryFile(mode="w", delete=False)
        cond_dict = parse_del_conditions(condition)
        fieldnames = ['Name', 'Semester', 'Roll', 'DoB', 'CGPA', 'Contact']
        with open(filepath, 'r', newline='') as dbfile, tempfile:
            reader = csv.DictReader(dbfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if row_condition_match(row, cond_dict) == False:
                    writer.writerow(row)
        shutil.move(tempfile.name, filepath)
    else:
        print(RED+"[ERR] This file does not exist"+RESET)




