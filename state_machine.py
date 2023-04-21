#  script that builds the state machine structure
#  by connecting to the server and sending actions

from meq_client import SERVER_IP, PORT, BUFFER_SIZE
import socket

def build_state_machine():
    state_machine = {'A': {}}
    visited_states = set()

    def dfs(state):
        if state in visited_states:
            return
        visited_states.add(state)

        for action in ['1', '2', '3']:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_IP, PORT))
                s.recv(BUFFER_SIZE)  # Ignore initial state 'A'
                s.sendall(f"{action}\n".encode())
                data = s.recv(BUFFER_SIZE)
                new_state = data.decode().strip()
                if new_state not in state_machine:
                    state_machine[new_state] = {}
                state_machine[state][action] = new_state
                dfs(new_state)

    dfs('A')
    return state_machine

if __name__ == "__main__":
    state_machine = build_state_machine()
    print(state_machine)

