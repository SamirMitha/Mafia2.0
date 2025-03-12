from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import time

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

rooms = {}

def generate_room_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route('/api/create_room', methods=['POST'])
def create_room():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({'error': 'Username is required'}), 400
        
    room_code = generate_room_code()
    while room_code in rooms:
        room_code = generate_room_code()
    
    rooms[room_code] = {
        'users': [username],
        'created_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify({
        'room_code': room_code,
        'username': username
    })

@app.route('/api/join_room', methods=['POST'])
def join_room():
    data = request.get_json()
    username = data.get('username')
    room_code = data.get('room_code')
    
    if not username or not room_code:
        return jsonify({'error': 'Username and room code are required'}), 400
        
    if room_code not in rooms:
        return jsonify({'error': 'Room not found'}), 404
        
    if username in rooms[room_code]['users']:
        return jsonify({'error': 'Username already in room'}), 400
        
    rooms[room_code]['users'].append(username)
    
    return jsonify({
        'room_code': room_code,
        'username': username,
        'users': rooms[room_code]['users']
    })

@app.route('/api/room/<room_code>', methods=['GET'])
def get_room(room_code):
    if room_code not in rooms:
        return jsonify({'error': 'Room not found'}), 404
        
    return jsonify({
        'room_code': room_code,
        'users': rooms[room_code]['users']
    })

if __name__ == '__main__':
    app.run()