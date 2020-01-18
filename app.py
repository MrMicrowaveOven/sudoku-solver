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

@app.route('/one_move', methods=["POST"])
def make_single_move():
    jsonified_request = request.get_json()
    board = jsonified_request['board']
    after_one_move = Board(board).make_one_move().to_arr()
    # response = { board: after_one_move}
    return jsonify(after_one_move)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(debug=True)
