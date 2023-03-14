from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def chat():

    # Get the message from the frontend
    message = request.json['message']

    # Send a request to the ChatGPT API
    chatgpt_response = requests.post(
        'https://chatgpt-api.com',
        headers={'Authorization': 'Bearer <ACCESS_TOKEN>'},
        json={'message': message}
    )

    # Get the response from the ChatGPT API
    response = json.loads(chatgpt_response.content)['response']

    # Return the response to the frontend
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
