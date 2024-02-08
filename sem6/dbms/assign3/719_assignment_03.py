def find_closure(attributes, functional_dependencies):
    closure = set(attributes)
    added = True
    
    while added:
        added = False
        for X, Y in functional_dependencies:
            if X.issubset(closure) and not Y.issubset(closure):
                closure |= Y
                added = True
    return closure



def bcnf_decomposition(relation, functional_dependencies):
    bcnf_relations = []
    remaining_fds = functional_dependencies.copy()
    
    while remaining_fds:
        for X, Y in remaining_fds:
            if X.issubset(relation):
                closure = find_closure(X, remaining_fds)
                if not closure.issuperset(relation):
                    new_relation = X | (closure - X)
                    # print(new_relation)
                    bcnf_relations.append(new_relation)
                   
                    remaining_fds = [(X, Y) for X, Y in remaining_fds if not X.issubset(new_relation)]
                    relation = relation - Y
                    break
        else:
            break
    
    if relation:
       
        bcnf_relations.append(relation)
        
    return bcnf_relations


relation = set('CSJDPQV')
functional_dependencies = [
    (set('C'), set('CSJDPQV')),
    (set('SD'), set('P')),
    (set('JP'), set('C')),
    (set('J'), set('S'))
]

bcnf_relations = bcnf_decomposition(relation, functional_dependencies)

for i, rel in enumerate(bcnf_relations, 1):
    print(f"R{i}:", ''.join(sorted(rel)))