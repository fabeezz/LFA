with open("input.txt") as f:
    init_state = f.readline().strip()
    final_states = f.readline().strip().split()
    words = f.readline().strip().split()
    transitions = []
    for line in f:
        transitions.append([x for x in line.strip().split() if x != "->"])
# q0
# q3
# aaabbc aaabbcc aaabbbc aabbc abcc d
# q0 a $ -> q1 X
# q1 a X -> q1 X
# q1 b X -> q2 pop
# q2 b X -> q2 pop
# q2 c $ -> q3 pop
# print(init_state)
# print(final_states)
# print(transitions)
# q1
# q3
# aaabbb
# q1 a $ -> q1 A
# q1 a A -> q1 A
# q1 b A -> q2 pop
# q2 b A -> q2 pop
# q2 . $ -> q3 pop

# q1
# q2
# aaabb aaabbb aaabbbb
# q1 a $ -> q1 A
# q1 a A -> q1 A
# q1 b A -> q2 pop
# q2 b A -> q2 pop
# q2 b $ -> q2 pop
# q2 a $ -> q2 pop

def dpda(word, init_state_ = init_state, final_states_ = final_states, transitions_ = transitions):
    curr_state = init_state_
    stack_ = ['$']

    for letter in word:
        for transition in transitions_:
            if curr_state == transition[0] and transition[1] == letter and stack_[-1] == transition[2]:
                if transition[4] == 'pop':
                    stack_.pop()
                else:
                    stack_.append(transition[4])
                curr_state = transition[3]
                break
        else:
            return False

    if curr_state in final_states_ or (len(stack_) == 0 or stack_ == ['$']):
        return True
    return False

with open("output.txt", "w") as g:
    for word in words:
        if dpda(word):
            g.write("YES\n")
        else:
            g.write("NO\n")