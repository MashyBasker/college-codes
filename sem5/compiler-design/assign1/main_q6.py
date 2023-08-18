


from main_q5 import process_input_file
from main_q1_to_q4 import tokenise, display, find_inputs, find_outputs, find_comments
import keyword


# Get all keywords
keywords = list(keyword.kwlist)


def find_identifiers(data):
    input_file = 'identifiers_nfa.txt'
    identifieres = set()
    
    filtered_data = []
    for line in data:
        if '=' in line:
            filtered_data.append(line)
    data = filtered_data
    
    in_statements = find_inputs(data)
    out_statements = find_outputs(data)
    cmt_statements = find_comments(data)

    data = '\n'.join(data)
    for statement in in_statements:
        data = data.replace(statement, '')
    for statement in out_statements:
        data = data.replace(statement, '')
    for statement in cmt_statements:
        data = data.replace(statement, '')

    for word in data.split():
        if process_input_file(input_file, word) and word not in keywords:
            identifieres.add(word)

    return list(identifieres)


input_file_name = 'input_src_program.py'
with open(input_file_name, 'r') as f:
    tokenised_data = tokenise(f)
    identifieres = find_identifiers(tokenised_data)

print(f'\n\nIdentifiers found using finite automation in the program are:\n')
display(identifieres)

