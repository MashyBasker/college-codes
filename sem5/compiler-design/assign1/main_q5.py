class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def __str__(self):
        return f'NFA::\nStates: {self.states}\nAlphabets: {self.alphabet}\nStart State: {self.start_state}\nAccepted States: {self.accept_states}\nTransitions: {self.transitions}'
    
    def epsilon_closure(self, states):
        closure = set(states)
        queue = list(states)
        
        while queue:
            state = queue.pop(0)
            
            if (state, ' ') in self.transitions:
                epsilon_states = self.transitions[(state, ' ')]
                
                for epsilon_state in epsilon_states:
                    if epsilon_state not in closure:
                        closure.add(epsilon_state)
                        queue.append(epsilon_state)
        
        return closure
    
    def move(self, states, symbol):
        result = set()
        
        for state in states:
            if (state, symbol) in self.transitions:
                result |= self.transitions[(state, symbol)]
        
        return result
    
    def convert_to_dfa(self):
        dfa_states = [frozenset(self.epsilon_closure({self.start_state}))]
        dfa_alphabet = self.alphabet
        dfa_transitions = {}
        dfa_start_state = dfa_states[0]
        dfa_accept_states = []
        
        unmarked_states = [dfa_start_state]
        
        while unmarked_states:
            current_state = unmarked_states.pop(0)
            
            for symbol in dfa_alphabet:
                # print('sym:', symbol)
                move_result = self.move(current_state, symbol)
                # print('move_result:', move_result)
                epsilon_closure_result = self.epsilon_closure(move_result)
                # print('epsilon_closure:', epsilon_closure_result)
                
                if epsilon_closure_result not in dfa_states and epsilon_closure_result:
                    dfa_states.append(frozenset(epsilon_closure_result))
                    unmarked_states.append(frozenset(epsilon_closure_result))
                
                if epsilon_closure_result:
                    # print((current_state, symbol), epsilon_closure_result)
                    dfa_transitions[(current_state, symbol)] = epsilon_closure_result

                # print(dfa_states)
        
        for state in dfa_states:
            if state.intersection(self.accept_states):
                dfa_accept_states.append(state)
        
        # print(dfa_states, dfa_alphabet, dfa_start_state, dfa_accept_states)
        return DFA(dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)


class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def is_accepted(self, string):
        current_state = self.start_state
        
        for symbol in string:
            # print((current_state, symbol))
            if (current_state, symbol) not in self.transitions:
                return False
            
            current_state = frozenset(self.transitions[(current_state, symbol)])
        
        return current_state in self.accept_states
    
    def __str__(self):
        return f'DFA::\nStates: {self.states}\nAlphabets: {self.alphabet}\nStart State: {self.start_state}\nAccepted States: {self.accept_states}\nTransitions: {self.transitions}'


def read_nfa_from_file(file):
    lines = file.readlines()
    
    states = set(lines[0].strip().split(','))
    alphabet = set(lines[1].strip().split(','))
    transitions = {}
    
    for line in lines[2:-3]:
        parts = line.strip().split(',')
        current_state = parts[0]
        symbol = parts[1]
        next_state = parts[2:]
        if (current_state, symbol) in transitions:
            transitions[(current_state, symbol)].add(next_state[0])
        else:
            transitions[(current_state, symbol)] = set(next_state)
    
    start_state = lines[-2].strip()
    accept_states = {lines[-1].strip()}

    #print(states, alphabet, transitions, start_state, accept_states)
    return NFA(states, alphabet, transitions, start_state, accept_states)


def read_dfa_from_file(file):
    lines = file.readlines()
    
    states = set(lines[0].strip().split(','))
    states = [frozenset({s}) for s in states]
    alphabet = set(lines[1].strip().split(','))
    transitions = {}
    
    for line in lines[2:-3]:
        parts = line.strip().split(',')
        current_state = parts[0]
        symbol = parts[1]
        next_state = parts[2:]
        if (current_state, symbol) in transitions:
            transitions[(frozenset({current_state}), symbol)].add(next_state[0])
        else:
            transitions[(frozenset({current_state}), symbol)] = set(next_state)
    
    start_state = {lines[-2].strip()}
    start_state = frozenset(start_state)
    accept_states = {lines[-1].strip()}
    accept_states = [frozenset(accept_states)]

    #print(states, alphabet, transitions, start_state, accept_states)
    return DFA(states, alphabet, transitions, start_state, accept_states)


def process_input_file(file_path, string):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line == 'NFA':
            # print("\nProcessing NFA...")
            nfa = read_nfa_from_file(file)
            dfa = nfa.convert_to_dfa()
            if dfa.is_accepted(string):
                return 1
            else:
                return 0
            # print(dfa)
        elif first_line == 'DFA':
            # print("\nProcessing DFA...")
            dfa = read_dfa_from_file(file)
            if dfa.is_accepted(string):
                return 1
            else:
                return 0
            # print(dfa)
        else:
            print("\nInvalid input file format.")


if __name__ == '__main__':
    ch = int(input('\nEnter 1 for loading default example NFA and string\nEnter 2 for user inputs: '))
    if ch == 1:
        input_file = 'input_nfa.txt'
        input_string = 'abb'
    else:
        try:
            input_file = input('Enter input file name: ')
            input_string = input('Enter input string: ')
        except Exception as err:
            print(err)

    if process_input_file(input_file, input_string):
        print(f"\nThe string '{input_string}' is accepted by the FA.\n")
    else:
        print(f"\nThe string '{input_string}' is not accepted by the FA.\n")
