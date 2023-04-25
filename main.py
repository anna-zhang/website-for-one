#! /usr/bin/env python
"""This Module creates and runs the HTTP server with which our website/client will interact with.
    This server will run on a default port"""
import argparse # handle command-line arguments
import sys
from app import app

def main():
    """Main function of program."""
    run_app()

def run_app():
    """Runs an instance of the Flask server on the specified port,
        which in turn runs the application"""
    try:
        app.run(host='0.0.0.0', port=8080)
    except OverflowError as err:
        print("This is an invalid port number.", file = sys.stderr)
        print(err, file = sys.stderr)
        sys.exit(1)
    except OSError as err:
        print("Connection failed. Please try another port", file = sys.stderr)
        print(err, file = sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
