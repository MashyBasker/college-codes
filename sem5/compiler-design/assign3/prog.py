import os
import re

# dictionary for specifying operator precedence
precedence_dict = {
    '^': 0,
    '*': 1,
    '/': 1,
    '+': 2,
    '-': 2,
    '-E': 2,
    '(': 3,
    ')': 3,
    '#': 3, # id is being represented by `#`
    '$': 3
}

# dictionary for specifying associativity
associativity_dict = {
    '^': "right",
    '*': "left",
    '/': "left",
    '+': "left",
    '-': "left",
    '-E': "right",
    '(': "n/a",
    ')': "n/a",
    '#': "n/a",
    '$': "n/a"
}

# subroutine to read grammar from `grammar.txt` file
# NOTE: Absolute spaghetti code. Someone please improve it
def read_grammar(filename):
    operators = set()
    with open(filename, 'r') as file:
        for line in file:
            rhs = line.split("->")[1]
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
    return list(operators)


# subroutine print the Operator Relation Table
def create_opt(filename):
    operators = read_grammar(filename=filename)
    print("\n################### DISPLAYING THE OPERATOR PRECEDENCE TABLE #####################################\n")
    # display table bars
    print("|       |", end="")
    for op in operators:
        print(f"   {op}   |", end="")
    print()
    print("|--------|", end="")
    for _ in operators:
        print("--------|", end="")
    print()

    table = []
    table.append(operators)
    for row_op in operators:
        row = []
        print(f"|  {row_op}   |", end="")
        for col_op in operators:
            if precedence_dict[row_op] < precedence_dict[col_op]:
                relation = ">"
            elif precedence_dict[row_op] > precedence_dict[col_op]:
                relation = "<"
            else:
                relation = "=" if associativity_dict[row_op] == associativity_dict[col_op] else "x"
            
            row.append(relation)
            print(f"   {relation}   |", end="")
        table.append(row)
        print()
    print("\n###################################################################################################")
    return table

def get_relation(row_op, col_op, operators, operator_relation_table):
    row_idx = operators.index(row_op)
    col_idx = operators.index(col_op)
    return operator_relation_table[row_idx+1][col_idx+1]



def display_stack(expression_to_check, opt):
    operators = opt[0][1:]
    # print(operators)
    operators_stack = ['$']
    print("Expression:", expression_to_check)

    tokens = []
    i = 0
    while i < len(expression_to_check):
        if expression_to_check[i].isalpha() or expression_to_check[i] == '#':
            tokens.append(expression_to_check[i])
            i += 1
        elif expression_to_check[i] in "()+-*/^":
            tokens.append(expression_to_check[i])
            i += 1
        else:
            i += 1

    for token in tokens:
        if token.isalpha() or token == '#':
            operators_stack.append(token)
        elif token == '(':
            operators_stack.append(token)
        elif token == ')':
            while operators_stack[-1] != '(':
                print("Stack:", operators_stack)
                operators_stack.pop()
            operators_stack.pop()  # Pop the '('
        else:
            while operators_stack and operators_stack[-1] != '(' and get_relation(token, operators_stack[-1], operators, opt) == '>':
                print("Stack:", operators_stack)
                operators_stack.pop()
            operators_stack.append(token)
        print("Stack:", operators_stack)

# Check if operators_stack is not empty before accessing its elements
    if len(operators_stack) == 1:
        print("String is accepted. Evaluation result:", operators_stack[0])
    else:
        print("String is not accepted.")

    
def runtests(start, table):
    tests = open("tests.txt").read().split("\n")
    for idx, val in enumerate(tests):
        output = display_stack(val, start, table)
        with open(f'{idx}.txt', 'w') as f:
            for x in output:
                f.write(str(x))


def main():
    opt = create_opt('grammar.txt')
    exp = '((((#+#+#+#)/(#+#))-(#+#))*#)^#'
    exp = "(#+#)*(#+#)"
    display_stack(exp, opt)

# Check if operators_stack is not empty before accessing its elements
    # if len(operators_stack) == 1:
    #     print("String has been accepted. Result: ", operators_stack[0])
    # else:
    #     print("String is not accepted.")

    

if __name__ == '__main__':
    main()
    
    
