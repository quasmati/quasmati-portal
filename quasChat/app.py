from flask import Flask, request, jsonify
import requests
import json 
import sys
import time

app = Flask(__name__)

def print_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) # adjust this value to change the speed

@app.route("/")
def index():
    # create a string with John and Amanda repeated 95 times
    output = "John and Amanda\n" * 95
    # call print_slow to output the string slowly
    print_slow(output)
    # return an empty response since the output has already been sent to stdout
    return "", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run()
