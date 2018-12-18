#!/usr/bin/env python3

import argparse
import zmq


def main():
    # Every ZeroMQ application needs a context...
    context = zmq.Context()

    # Create socket.
    subscriber_socket = context.socket(zmq.SUB)

    # Connect to server and listen to everything it sends our way...
    subscriber_socket.connect("tcp://127.0.0.1:30002")
    subscriber_socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # Receive and print messages...
    while True:
        print(subscriber_socket.recv_string())


if __name__ == "__main__":
    main()
