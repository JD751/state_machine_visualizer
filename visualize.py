#  script to visualize the 
# state machine structure using Graphviz

from graphviz import Digraph
from state_machine import build_state_machine

def visualize_state_machine(state_machine):
    dot = Digraph()
    for state, transitions in state_machine.items():
        for action, next_state in transitions.items():
            dot.edge(state, next_state, label=action)
    dot.render('state_machine.gv', view=True)

if __name__ == "__main__":
    state_machine = build_state_machine()
    visualize_state_machine(state_machine)
