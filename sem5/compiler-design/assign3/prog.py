import os
import re
import numpy as np

precedence_table = {
    '+': {'+': '>', '-': '>', '*': '<', '/': '<', '^': '<', '(': '<', ')': '>', '#': '<', '$': '>'},
    '-': {'+': '>', '-': '>', '*': '<', '/': '<', '^': '<', '(': '<', ')': '>', '#': '<', '$': '>'},
    '*': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '<', '(': '<', ')': '>', '#': '<', '$': '>'},
    '/': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '<', '(': '<', ')': '>', '#': '<', '$': '>'},
    '^': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': '<', ')': '>', '#': '<', '$': '>'},
    '(': {'+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '(': '<', ')': '=', '#': '<', '$': None},
    ')': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': None, ')': '>', '#': None, '$': '>'},
    '#': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': None, ')': '>', '#': None, '$': '>'},
    '$': {'+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '(': '<', ')': None, '#': '<', '$': None}
}

# subroutine to read grammar from `grammar.txt` file
# NOTE: Absolute spaghetti code. Someone please improve it
def read_grammar(filename):
    operators = set()
    with open(filename, 'r') as file:
        for line in file:
            rhs = line.split("->")[1]
            # print(rhs)
            rhs_ns = rhs.replace(' ', '')
            rhs_ns = rhs_ns.replace('\n', '')
            if len(rhs_ns) > 2 and '(' not in rhs_ns:
                operators.add(rhs_ns.replace('E', ''))
            else:
                if '(' not in rhs_ns:
                    operators.add(rhs_ns)
                else:
                    operators.add(rhs_ns[0])
                    operators.add(rhs_ns[2])

    operators.add('$')
    # print(operators)
    return list(sorted(operators))


# subroutine print the Operator Relation Table
def create_opt(filename):
    operators = read_grammar(filename)
    print("\n################### DISPLAYING THE OPERATOR PRECEDENCE TABLE #####################################\n")
    # display table bars
    # print("|       |", end="")
    # for op in operators:
        # print(f"   {op}   |", end="")
    # print()
    # print("|--------|", end="")
    # for _ in operators:
        # print("--------|", end="")
    # print()

    table = []
    table.append(operators)
    for row_op in operators:
        row = []
        # print(f"|  {row_op}   |", end="")
        for col_op in operators:
            if precedence_dict[row_op] < precedence_dict[col_op]:
                relation = ">"
            elif precedence_dict[row_op] > precedence_dict[col_op]:
                relation = "<"
            else:
                relation = "=" if associativity_dict[row_op] == associativity_dict[col_op] else "x"
            
            row.append(relation)
            # print(f"   {relation}   |", end="")
        table.append(row)
        print()
    print("\n###################################################################################################")
    return table

def get_relation(row_op, col_op, operators, operator_relation_table):
    row_idx = operators.index(row_op)
    col_idx = operators.index(col_op)
    return operator_relation_table[row_idx][col_idx]


def display_table(opt):
    opt = np.array(opt)
    r, c = opt.shape
    for i in range(r):
        for j in range(c):
            print(opt[i][j], end=" ")
        print() 

def operator_precedence_parser(input_string, precedence_table):
    operators_stack = ['$']
    input_tokens = list(input_string) + ['$']
    
    while operators_stack:
        top = operators_stack[-1]
        relation = precedence_table[top][input_tokens[0]]
        print('Stack:', operators_stack)

        if top == '$' and top == input_tokens[0]:
            return True

        if relation == '<' or relation == '=':
            operators_stack.append(input_tokens[0])
            input_tokens = input_tokens[1:]
        elif relation == '>':
            if operators_stack.pop() == ')':
                operators_stack.pop()
        else:
            print('Invalid')
            return False

    return True

    
def runtests(table):
    tests = open("tests.txt").read().split("\n")
    for idx, val in enumerate(tests):
        output = display_stack(val, table)
        print("------------------------------------------")
        with open(f'{idx+1}.txt', 'w') as f:
            for x in output:
                f.write(str(x)+'\n')


def main():
    
    # opt = create_opt('grammar.txt')
    # opt[1][0] = 'x'
    # exp = '((((#+#+#+#)/(#+#))-(#+#))*#)^#'
    # exp = '(#+#)*(#+#)'
    exp = "((((#+#+#+#)/(#+#))-(#+#))*#)^#"
    # display_stack(exp, opt)
    # runtests(opt)
    operator_precedence_parser(exp, precedence_table)


    

if __name__ == '__main__':
    main()
    
    
