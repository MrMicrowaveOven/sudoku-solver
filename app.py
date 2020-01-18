from flask import Flask, request, jsonify
app = Flask(__name__)

import sys
sys.path.append("lib")

from board import Board
from script import parse_board

@app.route('/', methods=["POST"])

def main_interface():
    response = request.get_json()
    board = response['board']
    Board(board).attempt_to_solve()
    return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(debug=True)
