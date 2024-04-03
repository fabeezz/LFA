# 🚀 Lambda-NFA Implementation

This repository contains a Python implementation of a Lambda-NFA (Non-deterministic Finite Automaton with Lambda transitions) recognizer. A Lambda-NFA is an extension of the traditional NFA, where transitions can occur without consuming any input symbols, denoted as lambda (λ) or epsilon (ε) transitions. These transitions allow the automaton to change states without reading the input string, providing a powerful mechanism for modeling various computational problems.

## 📚 Understanding Lambda-NFA

A Lambda-NFA is defined by a 5-tuple, (Q, Σ, δ, q0, F), where:

- Q is a finite set of states,
- Σ is a finite set of input symbols,
- δ is the transition function: Q × (Σ ∪ {λ}) → P(Q),
- q0 is the initial state, and
- F is the set of accept states.

The key feature distinguishing a Lambda-NFA from a traditional NFA is the presence of λ-transitions, which allow the automaton to "jump" between states without consuming any input.

## 🔍 Implementation Overview

The implementation provided in this repository (`lnfa/lnfa.py`) focuses on recognizing whether a given input string is accepted by the defined Lambda-NFA. The core components of the implementation include:

### 🔄 State Transition Functions

Two primary functions handle state transitions:

- `starePrinLitera(stare_, litera_)`: Determines the possible states that can be reached from a given state `stare_` by consuming an input symbol `litera_`.
- `starePrinLambda(stari_)`: Identifies all states that can be reached from a set of states `stari_` through λ-transitions alone.

### 🎯 Lambda-NFA Recognizer

The `lnfa(cuvant)` function orchestrates the recognition process. It iteratively processes each symbol of the input string, updating the current set of active states based on both the input symbol and λ-transitions. The process is as follows:

1. Start with the initial state and expand it through λ-transitions to get the initial set of active states.
2. For each symbol in the input string:
   - Determine the next set of possible states based on the current states and the input symbol.
   - Expand this set through λ-transitions.
3. After processing the entire string, if any of the current states are accept states, the string is accepted; otherwise, it is rejected.

### 📁 Input and Output

The program reads the Lambda-NFA definition and a list of input strings from a file (`input_lnfa_greu.txt`), processes each string to determine if it is accepted by the Lambda-NFA, and writes the results to an output file (`output_lnfa_greu_fabi.txt`).

## ▶️ Running the Implementation

To run the implementation, ensure you have Python installed on your system. Place your input file in the same directory as the script, and execute the script:

```bash
python lnfa/lnfa.py
```

The output will be written to the specified output file, indicating for each input string whether it is accepted (`DA`) or rejected (`NU`) by the Lambda-NFA.

## 🎉 Conclusion

This implementation provides a straightforward approach to recognizing strings using a Lambda-NFA, demonstrating the power and flexibility of non-deterministic automata with λ-transitions in computational theory and applications.