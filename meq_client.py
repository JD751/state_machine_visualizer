
# Python script that will connect to the MEQ server 
# and communicate with the state machine

import socket

SERVER_IP = "20.28.230.252"
PORT = 65432
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        data = s.recv(BUFFER_SIZE)
        print(f"Server: {data.decode().strip()}")

        while True:
            action = input("Enter action (1, 2, 3) or 'quit': ")
            if action == 'quit':
                break

            s.sendall(f"{action}\n".encode())
            data = s.recv(BUFFER_SIZE)
            response = data.decode().strip()
            print(f"Server: {response}")
            if response == 'Z':
                data = s.recv(BUFFER_SIZE)
                print(f"Server: {data.decode().strip()}")

if __name__ == "__main__":
    main()
