from collections import OrderedDict
import pandas as pd
import re


class Terminal:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol
    

class NonTerminal:
    def __init__(self, symbol):
        self.symbol = symbol
        self.first = set()
        self.follow = set()

    def __str__(self):
        return self.symbol

    def add_first(self, symbols):
        self.first |= set(symbols)

    def add_follow(self, symbols):
        self.follow |= set(symbols)


class State:
    _id=0
    def __init__(self, closure):
        self.closure = closure
        self.no = State._id
        State._id += 1


class Item(str):
    def __new__(cls, item, lookahead=list()):
        self = str.__new__(cls, item)
        self.lookahead = lookahead
        return self

    def __str__(self):
        return super(Item, self).__str__()+", "+'|'.join(self.lookahead)
        

def closure(items):
    def exists(newitem, items):
        for i in items:
            if i == newitem and sorted(set(i.lookahead)) == sorted(set(newitem.lookahead)):
                return True
        return False

    while True:
        flag=0
        for i in items: 
            
            if i.index('.') == len(i)-1: continue

            Y = i.split('->')[1].split('.')[1][0]

            if i.index('.')+1<len(i)-1:
                lastr = list(compute_first(i[i.index('.')+2])-set(chr(1013)))
                
            else:
                lastr = i.lookahead
            
            for prod in production_list:
                head, body = prod.split('->')
                
                if head != Y: continue
                
                newitem = Item(Y+'->.'+body, lastr)

                if not exists(newitem, items):
                    items.append(newitem)
                    flag=1

        if flag==0: break

    return items


def goto(items, symbol):
    initial = []

    for i in items:
        if i.index('.') == len(i)-1: continue

        head, body = i.split('->')
        seen, unseen = body.split('.')

        if unseen[0] == symbol and len(unseen) >= 1:
            initial.append(Item(head+'->'+seen+unseen[0]+'.'+unseen[1:], i.lookahead))

    return closure(initial)


def calc_states():
    def contains(states, t):
        for s in states:
            if len(s) != len(t): continue

            if sorted(s) == sorted(t):
                for i in range(len(s)):
                        if s[i].lookahead != t[i].lookahead: break
                else: return True

        return False

    head, body = production_list[0].split('->')

    states = [closure([Item(head+'->.'+body, ['$'])])]
    
    while True:
        flag = 0
        for s in states:
            for e in nt_list + t_list:
                t = goto(s, e)
                if t == [] or contains(states, t): continue
                states.append(t)
                flag = 1
        if not flag: break
    
    return states 


def make_table(states):
    def getstateno(t):
        for s in states:
            if len(s.closure) != len(t): continue

            if sorted(s.closure) == sorted(t):
                for i in range(len(s.closure)):
                        if s.closure[i].lookahead != t[i].lookahead: break
                else: return s.no

        return -1

    def getprodno(closure):
        closure = ''.join(closure).replace('.', '')
        return production_list.index(closure)

    SLR_Table = OrderedDict()
    
    for i in range(len(states)):
        states[i] = State(states[i])

    for s in states:
        SLR_Table[s.no] = OrderedDict()

        for item in s.closure:
            head, body = item.split('->')
            if body == '.': 
                for term in item.lookahead: 
                    if term not in SLR_Table[s.no].keys():
                        SLR_Table[s.no][term]={'r'+str(getprodno(item))}
                    else: SLR_Table[s.no][term] |= {'r'+str(getprodno(item))}
                continue

            nextsym = body.split('.')[1]
            if nextsym == '':
                if getprodno(item) == 0:
                    SLR_Table[s.no]['$'] = 'A'
                else:
                    for term in item.lookahead: 
                        if term not in SLR_Table[s.no].keys():
                            SLR_Table[s.no][term] = {'r'+str(getprodno(item))}
                        else: SLR_Table[s.no][term] |= {'r'+str(getprodno(item))}
                continue

            nextsym = nextsym[0]
            t = goto(s.closure, nextsym)
            if t != []: 
                if nextsym in t_list:
                    if nextsym not in SLR_Table[s.no].keys():
                        SLR_Table[s.no][nextsym] = {'s'+str(getstateno(t))}
                    else: SLR_Table[s.no][nextsym] |= {'s'+str(getstateno(t))}

                else: SLR_Table[s.no][nextsym] = str(getstateno(t))

    return SLR_Table


def augment_grammar():
    for i in range(ord('Z'), ord('A')-1, -1):
        if chr(i) not in nt_list:
            start_prod = production_list[0]
            production_list.insert(0, chr(i)+'->'+start_prod.split('->')[0]) 
            return


def compute_first(symbol):
    if symbol in tl:
        return set(symbol)

    for prod in production_list:
        head, body = prod.split('->')
        
        if head != symbol: continue

        if body == '':
            ntl[symbol].add_first(chr(1013))
            continue

        for i, Y in enumerate(body):
            if body[i] == symbol: continue
            t = compute_first(Y)
            ntl[symbol].add_first(t-set(chr(1013)))
            if chr(1013) not in t:
                break 
            if i == len(body)-1: 
                ntl[symbol].add_first(chr(1013))

    return ntl[symbol].first


def get_first(symbol):
    return compute_first(symbol)


def compute_follow(symbol):
    if symbol == list(ntl.keys())[0]:
        ntl[symbol].add_follow('$')

    for prod in production_list:    
        head, body = prod.split('->')

        for i, B in enumerate(body):        
            if B != symbol: continue

            if i != len(body)-1:
                ntl[symbol].add_follow(get_first(body[i+1]) - set(chr(1013)))

            if i == len(body)-1 or chr(1013) in get_first(body[i+1]) and B != head: 
                ntl[symbol].add_follow(get_follow(head))
    

def get_follow(symbol):
    if symbol in tl.keys():
        return None
    
    return ntl[symbol].follow


def read_grammar(grammar):
    start = None
    productions = {}

    for prod in grammar:
        l = re.split("(/→/\n/)*", prod)
        m = [i for i in l if i not in ['', None, '\n', ' ', '→']]
        i = 0
        while i < (len(m)-1):
            if m[i]+m[i+1] == 'id':
                m[i] = 'id'
                del m[i+1]
            i+=1

        left_prod, right_prod = m.pop(0), []
        if m[0] == "'":
            left_prod += m.pop(0)
    
        t = []
        for j in m:
            if j != '|':
                t.append(j)
            else:
                right_prod.append(t)
                t = []

        right_prod.append(t)
        productions[left_prod] = right_prod

        if start is None:
            start = left_prod

    return productions


def tableize(df):
    if not isinstance(df, pd.DataFrame):
        return
    df_columns = df.columns.tolist() 
    max_len_in_lst = lambda lst: len(sorted(lst, reverse=True, key=len)[0])
    align_center = lambda st, sz: "{0}{1}{0}".format(" "*(1+(sz-len(st))//2), st)[:sz] if len(st) < sz else st
    align_right = lambda st, sz: "{0}{1} ".format(" "*(sz-len(st)-1), st) if len(st) < sz else st
    max_col_len = max_len_in_lst(df_columns)
    max_val_len_for_col = dict([(col, max_len_in_lst(df.iloc[:,idx].astype('str'))) for idx, col in enumerate(df_columns)])
    col_sizes = dict([(col, 2 + max(max_val_len_for_col.get(col, 0), max_col_len)) for col in df_columns])
    build_hline = lambda row: '+'.join(['-' * col_sizes[col] for col in row]).join(['+', '+'])
    build_data = lambda row, align: "|".join([align(str(val), col_sizes[df_columns[idx]]) for idx, val in enumerate(row)]).join(['|', '|'])
    hline = build_hline(df_columns)
    out = [hline, build_data(df_columns, align_center), hline]
    for _, row in df.iterrows():
        out.append(build_data(row.tolist(), align_right))
    out.append(hline)
    return "\n".join(out)



def main():
    global production_list, ntl, nt_list, tl, t_list

    file_name = 'grammar.txt'

    with open(file_name, 'r', encoding='utf-8') as grammar:
        productions = read_grammar(grammar)
    if "S'" in productions.keys():
        del productions["S'"]

    print('\n*****GRAMMAR*****\n')
    for lhs, rhs in productions.items():
        print(lhs, ':', rhs)
    print()

    production_list = []
    t_list = []
    nt_list = list(productions.keys())
    for items in productions.values():
        for item in items:
            for it in item:
                if (not it.isupper()) and it != 'ε' and it not in t_list:
                    if it == 'id' and '#' not in t_list:
                        t_list.append('#')
                    else:
                        t_list.append(it)

    tl = OrderedDict()
    for i in t_list:
        tl[i] = Terminal(i)
    t_list.append('$')

    ntl = OrderedDict()
    for i in nt_list:
        ntl[i] = NonTerminal(i)
        ntl[i].first = get_first(i)
        ntl[i].follow = compute_follow(i)

    for k, v in productions.items():
        for prod in v:
            temp = ''
            for entity in prod:
                temp += entity
            if temp == 'ε':
                temp = ''
            if 'id' in temp:
                temp = temp.replace('id', '#')
            p = f'{k}->{temp}'
            production_list.append(p)

    # print(production_list)
    # print(ntl)
    # print(tl)
    # print(nt_list)
    # print(t_list)

    augment_grammar()
    j = calc_states()

    print('\n*****LR-1 Items*****\n')
    ctr = 0
    for s in j:
        print(f"Item{ctr}:")
        for i in s:
            tt = i.replace('->', '→')
            tt = ' '.join(tt)
            tt = tt.replace('#', 'id')
            print("\t", tt)
        ctr += 1

    table = make_table(j)
    print('\n\n*****LR-1 Parsing Table*****\n')
    sym_list = t_list + nt_list
    df = pd.DataFrame(columns=['']+sym_list)
    for i in table:
        df.loc[i] = [i] + [table[i][j] if j in table[i].keys() else '' for j in sym_list]
    print(tableize(df))

    print('\n\n*****Input String Parsing*****\n')
    Input = input("Enter the string to be parsed: ")
    Input = Input.replace('id', '#')
    Input += '$'
    
    try:
        stack=['0']
        a = list(table.items())
        
        print("\nUsing Productions:", productions)
        print("Nt:: Here user input 'id' will be internally treated as '#' symbol")
        print('\nStack',"\t\t\t\t\t",'Input')
        print(*stack,"\t\t\t\t\t", *Input, sep='')
        
        while(len(Input)!=0):
            
            b = list(a[int(stack[-1])][1][Input[0]])
            
            if b[0][0] == 's':
                stack.append(Input[0])
                stack.append(b[0][1:])
                Input = Input[1:]
                print(*stack, "\t\t\t\t\t", *Input, sep="")
            
            elif b[0][0] == 'r':
                s = int(b[0][1:])
                l = len(production_list[s])-3
                prod = production_list[s]
                l*=2
                l = len(stack)-l
                stack = stack[:l]
                s = a[int(stack[-1])][1][prod[0]]
                stack += list(prod[0])
                stack.append(s)
                print(*stack, "\t\t\t\t\t", *Input, sep="")
            
            elif b[0][0] == 'A':
                print("\n\tString Accepted!\n")
                break
    
    except:
        print('\n\tString Parsing failed for given Grammar!\n')
    
    return


if __name__ == '__main__':
    main()
