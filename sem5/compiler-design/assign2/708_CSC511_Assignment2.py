
def find_follow(s, productions, first):
    follow = set()

    if len(s) != 1:
        return {}

    if s == list(productions.keys())[0]:
        follow.add('$')

    for i in productions:
        for j in range(len(productions[i])):
            if s in productions[i][j]:
                idx = productions[i][j].index(s)

                if idx == len(productions[i][j]) - 1:
                    if productions[i][j][idx] == i:
                        break
                    else:
                        f = find_follow(i, productions, first)
                        follow.update(f)
                else:
                    while idx != len(productions[i][j]) - 1:
                        idx += 1
                        if not productions[i][j][idx].isupper():
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = find_first(productions[i][j][idx], productions)

                            if 'ε' not in f:
                                follow.update(f)
                                break
                            elif 'ε' in f and idx != len(productions[i][j]) - 1:
                                f.remove('ε')
                                follow.update(f)
                            elif 'ε' in f and idx == len(productions[i][j]) - 1:
                                f.remove('ε')
                                follow.update(f)
                                f = find_follow(i, productions, first)
                                follow.update(f)

    return follow

def find_first(s, productions):
    first = set()

    for i in range(len(productions[s])):
        for j in range(len(productions[s][i])):
            c = productions[s][i][j]

            if c.isupper():
                f = find_first(c, productions)
                if 'ε' not in f:
                    first.update(f)
                    break
                else:
                    if j == len(productions[s][i]) - 1:
                        first.update(f)
                    else:
                        f.remove('ε')
                        first.update(f)
            else:
                first.add(c)
                break

    return first

def parsing_table(productions, first, follow):
    import pandas as pd
    table = {}
    for key in productions:
        for value in productions[key]:
            val = ''.join(value)
            if val != 'ε':
                for element in first[key]:
                    if(element != 'ε'):
                        if(not val[0].isupper()) :
                            if(element in val):
                                table[key, element] = val
                            else:
                                pass
                        else:
                            table[key, element] = val
            else:
                for element in follow[key]:
                    table[key, element] = val

    # for key,val in table.items():
    #     print(key,"=>",val)

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]
    print("\nDISPLAYING THE PARSE TABLE")
    print("==============================================\n")
    pd_new_table = pd.DataFrame(new_table).fillna('-')
    print(pd_new_table)
    print("\n")
    
    return table, list(pd_new_table.columns)

def does_accept(string, start, table):
    accepted = True
    input_string = string + '$'
    stack = ['$']
    stack.append(start)
    idx = 0
    total = []

    while len(stack) > 0:
        
        total.append(stack.copy())
        total.append('\n')
        top = stack[-1]
        curr_string = input_string[idx]

        if top == curr_string:
            stack.pop()
            idx += 1
        else:
            key = (top, curr_string)
            if key not in table:
                accepted = False
                break
            value = table[key]
            if value != 'ε':
                value = value[::-1]
                stack.pop()
                stack.extend(value)
            else:
                stack.pop()

    if accepted:
        print("\n[SUCCESS] String was accepted\n")
    else:
        print("\n[FAIL] String was not accepted\n")
    
    return total

def runtests(start, table):
    tests = open("tests.txt").read().split("\n")
    for idx, val in enumerate(tests):
        output = does_accept(val, start, table)
        with open(f'{idx}.txt', 'w') as f:
            for x in output:
                f.write(str(x))



def main():
    import re 

    productions = {}
    grammar = open("grammar.txt", "r")
    first = {}
    follow = {}
    table = {}
    start = ""

    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = [i for i in l if i not in ["", None, '\n', ' ', '-', '>']]

        left_prod = m.pop(0)
        right_prod = []
        t = []

        for j in m:
            if j != '|':
                t.append(j)
            else:
                right_prod.append(t)
                t = []

        right_prod.append(t)
        productions[left_prod] = right_prod

        if start == "":
            start = left_prod

    for s in productions.keys():
        first[s] = find_first(s, productions)

    print("FIRST")
    print("======================")
    for lhs, rhs in first.items():
        print(lhs, ":", rhs)
    print("")

    for lhs in productions:
        follow[lhs] = set()

    for s in productions.keys():
        follow[s] = find_follow(s, productions, first)

    print("FOLLOW")
    print("======================")
    for lhs, rhs in follow.items():
        print(lhs, ":", rhs)

    table, ter = parsing_table(productions, first, follow)

    # s = input("Provide a string to check its validity: ")
    # does_accept(s, start, table)
    y = input("Do you want to run tests? [y/n]: ")
    if y.upper() == 'Y':
        runtests(start, table)
    else:
        print("Exiting...")
    grammar.close()


if __name__ == '__main__':
    main()