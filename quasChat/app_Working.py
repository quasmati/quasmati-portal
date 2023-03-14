from flask import Flask, request, jsonify
import requests
import json 
import sys
import time

app = Flask(__name__)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1) # adjust this value to change the speed

@app.route("/")
def index():
    # create a string with John and Amanda repeated 95 times
    output = "John and Amanda\n" * 95
    # return the output as plain text
    return output, 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run()
