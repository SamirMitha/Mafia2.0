import React, { useState } from 'react';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [roomCode, setRoomCode] = useState('');
  const [currentRoom, setCurrentRoom] = useState(null);
  const [users, setUsers] = useState([]);
  const [error, setError] = useState('');

  const API_URL = 'https://mafia2-0.onrender.com';

  const createRoom = async () => {
    try {
      const response = await fetch('${API_URL}/api/create_room', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username })
      });
      
      const data = await response.json();
      if (response.ok) {
        setCurrentRoom(data.room_code);
        setUsers([username]);
        setError('');
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to create room');
    }
  };

  const joinRoom = async () => {
    try {
      const response = await fetch('${API_URL}/api/join_room', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, room_code: roomCode })
      });
      
      const data = await response.json();
      if (response.ok) {
        setCurrentRoom(data.room_code);
        setUsers(data.users);
        setError('');
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to join room');
    }
  };

  return (
    <div className="App">
      <h1>Room Chat</h1>
      
      {!currentRoom ? (
        <div className="join-create-container">
          <input
            type="text"
            placeholder="Enter your username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          
          <div className="actions">
            <button onClick={createRoom} disabled={!username}>
              Create Room
            </button>
            
            <div className="join-room">
              <input
                type="text"
                placeholder="Enter room code"
                value={roomCode}
                onChange={(e) => setRoomCode(e.target.value.toUpperCase())}
              />
              <button onClick={joinRoom} disabled={!username || !roomCode}>
                Join Room
              </button>
            </div>
          </div>
          
          {error && <p className="error">{error}</p>}
        </div>
      ) : (
        <div className="room">
          <h2>Room: {currentRoom}</h2>
          <div className="users">
            <h3>Users:</h3>
            <ul>
              {users.map((user, index) => (
                <li key={index}>{user}</li>
              ))}
            </ul>
          </div>
          <button onClick={() => {
            setCurrentRoom(null);
            setUsers([]);
            setRoomCode('');
          }}>
            Leave Room
          </button>
        </div>
      )}
    </div>
  );
}

export default App;