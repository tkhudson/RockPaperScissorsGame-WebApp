from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/play', methods=['POST'])
def play():
    moves = ['rock', 'paper', 'scissors']
    user_move = request.json.get('move')
    if user_move not in moves:
        return jsonify({'error': 'Invalid move'}), 400

    computer_move = random.choice(moves)
    
    # Determine the winner
    if user_move == computer_move:
        result = 'draw'
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        result = 'win'
    else:
        result = 'lose'

    return jsonify({'user_move': user_move, 'computer_move': computer_move, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)