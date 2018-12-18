#!/usr/bin/env python3

import argparse
import zmq


def main():
    # Create argument parser...
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="Your name in the chat.", default="Anonymous User")
    parser.add_argument("-s", "--server", type=str, help="Server IP", default="localhost")
    parser.add_argument("-p", "--port", type=str, help="Server Port", default="30001")

    # Parse arguments...
    arguments = parser.parse_args()

    # Every ZeroMQ application needs a context...
    context = zmq.Context()

    # Create push socket
    push_socket = context.socket(zmq.PUSH)

    # Connect to server
    push_socket.connect("tcp://" + arguments.server + ":" + arguments.port)

    # Send messages as they come in...
    while True:
        push_socket.send_string(arguments.name + ": " + input("Enter Message: "))


if __name__ == "__main__":
    main()
