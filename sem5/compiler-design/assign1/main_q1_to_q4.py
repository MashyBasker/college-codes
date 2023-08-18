import keyword

# Get all keywords
keywords = list(keyword.kwlist)


def tokenise(file):
    data = file.readlines()
    tokenised_data = []
    
    for line in data:
        if line[-1] == '\n':
            tokenised_data.append(line[:-1])

    return tokenised_data


def display(data):
    for line in data:
        print('\t', line)


def find_identifiers(data):
    identifiers = set()
    for line in data:
        splited_lines = line.split()
        for cur, nextt in zip(splited_lines[:-1], splited_lines[1:]):
            if nextt == '=':
                if cur not in keywords:
                    identifiers.add(cur)
    
    return list(identifiers)


def find_inputs(data):
    inputs = []
    for line in data:
        if 'input' in line:
            input_idx = line.find('input')
            input_idx_end = line.find(')')
            inputs.append(line[input_idx+6:input_idx_end])
    
    return inputs


def find_outputs(data):
    outputs = []
    for line in data:
        if 'print' in line:
            outputs_idx = line.find('print')
            output_idx_end = line.find(')')
            outputs.append(line[outputs_idx+6:output_idx_end])
    
    return outputs


def find_keywords(data):
    keys = set()
    in_statements = find_inputs(data)
    out_statements = find_outputs(data)

    data = '\n'.join(data)
    for statement in in_statements:
        data = data.replace(statement, '')
    for statement in out_statements:
        data = data.replace(statement, '')

    for word in data.split():
        if word in keywords:
            keys.add(word)

    return list(keys)


def find_comments(data):
    data = '\n'.join(data)

    cmts = []
    cmt = ''
    flag = 0

    for item in data:
        if item == '#':
            cmt += item
            flag = 1
        if flag and item == '\n':
            cmts.append(cmt[1:])
            cmt = ''
            flag = 0
        if flag:
            cmt += item
    
    for c in cmts:
        data = data.replace(c, '')
   
    with open('input_src_program_without_cmts.py', 'w') as f:
        f.write(data)

    return cmts


if __name__ == '__main__':
    input_file_name = 'input_src_program.py'
    with open(input_file_name, 'r') as f:
        tokenised_data = tokenise(f)
        identifieres = find_identifiers(tokenised_data)
        input_statements = find_inputs(tokenised_data)
        output_statements = find_outputs(tokenised_data)
        keys = find_keywords(tokenised_data)
        comments = find_comments(tokenised_data)

    print(f'\n\nIdentifiers found in the program are:\n')
    display(identifieres)
    print(f'\nInput statements found in the program are:')
    display(input_statements)
    print(f'\nOutput statements found in the program are:\n')
    display(output_statements)
    print(f'\nKeywords found in the program are:\n')
    display(keys)
    print(f'\nComments found in the program are:\n')
    display(comments)
    print('\nProgram without comments saved as src_program_without_cmts.py')