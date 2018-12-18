#!/usr/bin/env python3

import argparse
import zmq


def main():
    # Create argument parser...
    parser = argparse.ArgumentParser()
    parser.add_argument("--message_port", type=str, help="Port that a client connects to.", default="30001")
    parser.add_argument("--monitor_port", type=str, help="Port that a monitor connects to.", default="30002")

    # Parse arguments...
    arguments = parser.parse_args()

    # Every ZeroMQ app needs a context...
    context = zmq.Context()

    # Create sockets...
    pull_socket = context.socket(zmq.PULL)
    publisher_socket = context.socket(zmq.PUB)

    # Bind sockets to ports...
    pull_socket.bind("tcp://*:" + arguments.message_port)
    publisher_socket.bind("tcp://*:" + arguments.monitor_port)

    # Actual server...
    while True:
        message = pull_socket.recv_string()
        publisher_socket.send_string(message)

    # That's it :)


if __name__ == "__main__":
    main()
