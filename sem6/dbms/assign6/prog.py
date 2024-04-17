def conflict_serializable(schedule):
    """
    Checks if a schedule is conflict serializable.
    """
    transactions = set()
    edges = set()

    for i in range(len(schedule)):
        for j in range(i+1, len(schedule)):
            if schedule[i][0] != schedule[j][0] and \
               schedule[i][1] == "W" and schedule[j][1] == "W" and \
               schedule[i][2] == schedule[j][2]:
                if schedule[i][0] not in transactions:
                    transactions.add(schedule[i][0])
                if schedule[j][0] not in transactions:
                    transactions.add(schedule[j][0])
                edges.add((schedule[i][0], schedule[j][0]))

    for i in transactions:
        for j in transactions:
            if i != j:
                if (i, j) in edges:
                    for k in transactions:
                        if k != i and k != j:
                            if (i, k) in edges and (k, j) in edges:
                                return False
    return True


def view_serializable(schedule):
    """
    Checks if a schedule is view serializable.
    """
    transactions = set()
    edges = set()

    for i in range(len(schedule)):
        for j in range(i+1, len(schedule)):
            if schedule[i][0] != schedule[j][0] and \
               schedule[i][1] == "R" and schedule[j][1] == "W" and \
               schedule[i][2] == schedule[j][2]:
                if schedule[i][0] not in transactions:
                    transactions.add(schedule[i][0])
                if schedule[j][0] not in transactions:
                    transactions.add(schedule[j][0])
                edges.add((schedule[i][0], schedule[j][0]))

    for i in transactions:
        for j in transactions:
            if i != j:
                if (i, j) in edges:
                    for k in transactions:
                        if k != i and k != j:
                            if (i, k) in edges and (k, j) in edges:
                                return False
    return True


def main():
    schedule = [('T1', 'R', 'X'), ('T2', 'R', 'Y'), ('T1', 'W', 'X'),
                ('T2', 'R', 'X'), ('T2', 'W', 'X'), ('T1', 'W', 'Y')]
    
    conflict_serializable_result = conflict_serializable(schedule)
    view_serializable_result = view_serializable(schedule)

    print("Conflict Serializable:", conflict_serializable_result)
    print("View Serializable:", view_serializable_result)


if __name__ == "__main__":
    main()

