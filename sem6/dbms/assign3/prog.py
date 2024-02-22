def parse_input():
    a = open('./input.txt').read().split('\n')
    fd = []
    attrs = set(''.join(str(i) for i in a[0].split(",")))
    for i in range(1, len(a)):
        lhs, rhs = a[i].split(" -> ")
        lhs_string, rhs_string = "", ""
        if ',' in lhs:
            lhs_string = set(''.join(str(w) for w in lhs.split(",")))
        else:
            lhs_string = lhs
        if ',' in rhs:
            rhs_string = set(''.join(str(w) for w in rhs.split(",")))
        else:
            rhs_string = rhs

        fd.append((set(lhs_string), set(rhs_string)))
    return attrs, fd


def get_closure(attributes, functional_dependencies):
    closure = set(attributes)
    added = True
    
    while added:
        added = False
        for X, Y in functional_dependencies:
            if X.issubset(closure) and not Y.issubset(closure):
                closure |= Y
                added = True
    return closure



def bcnf(relation, functional_dependencies):
    bcnf_relations = []
    remaining_fds = functional_dependencies.copy()
    
    while remaining_fds:
        for X, Y in remaining_fds:
            if X.issubset(relation):
                closure = get_closure(X, remaining_fds)
                if not closure.issuperset(relation):
                    new_relation = X | (closure-X)
                    bcnf_relations.append(new_relation)
                   
                    remaining_fds = [(X, Y) for X, Y in remaining_fds if not X.issubset(new_relation)]
                    relation = relation - Y
                    break
        else:
            break
    
    if relation: 
        bcnf_relations.append(relation)
        
    return bcnf_relations

if __name__ == '__main__':
    attrs, fd = parse_input()
    bcnf_rel = bcnf(attrs, fd)
    for i, x in enumerate(bcnf_rel):
        print(f"R{i}  =>  {''.join(sorted(x))}")


