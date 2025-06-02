#!/usr/bin/env python3
import os
import sys

def load_awarded():
    awarded = 0
    if os.path.exists("awarded.txt"):
        try:
            awarded = int(open("awarded.txt", "r").read().strip())
        except ValueError:
            pass
    return awarded

def load_request():
    argc = len(sys.argv)
    request: int | None = None
    if argc > 1:
        try:
            request = int(sys.argv[1])
        except ValueError:
            pass
    if request is None:
        request = int(input())
    return request

def main():
    awarded = load_awarded()
    request = load_request()

    if request <= awarded:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
    sys.exit(0)
