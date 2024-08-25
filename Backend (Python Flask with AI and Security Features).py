from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import hashlib
import bcrypt
import hmac
import os

app = Flask(__name__)
CORS(app)

# Advanced AI Model
model = Sequential([
    Dense(256, activation='relu', input_shape=(1,)),
    Dense(512, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Dummy data for training
X_train = np.array([i for i in range(1000)])
y_train = np.array([i % 2 for i in range(1000)])

# Train the model
model.fit(X_train, y_train, epochs=10)

# Traditional Hashing
def generate_traditional_hash(input_data, algorithm):
    if algorithm == 'md5':
        return hashlib.md5(input_data.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(input_data.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(input_data.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        return bcrypt.hashpw(input_data.encode(), bcrypt.gensalt()).decode()
    elif algorithm == 'hmac':
        key = os.urandom(32)
        return hmac.new(key, input_data.encode(), hashlib.sha256).hexdigest()
    else:
        return None

# AI-based Hashing
@app.route('/generate-ai-hash', methods=['POST'])
def generate_ai_hash():
    input_data = request.json['input']
    input_data_len = len(input_data)
    input_data_np = np.array([input_data_len])
    prediction = model.predict(input_data_np)
    ai_hash = hashlib.sha256(f"{input_data_len}-{prediction[0][0]}".encode()).hexdigest()
    return jsonify({"ai_hash": ai_hash})

# Traditional Hashing Endpoint
@app.route('/generate-traditional-hash', methods=['POST'])
def generate_traditional_hash_endpoint():
    input_data = request.json['input']
    algorithm = request.json['algorithm']
    hash_value = generate_traditional_hash(input_data, algorithm)
    if hash_value:
        return jsonify({"hash": hash_value})
    else:
        return jsonify({"error": "Unsupported algorithm"}), 400

# Security Analysis (Simplified)
def analyze_hash_strength(hash_value):
    entropy = -sum((hash_value.count(char)/len(hash_value)) * np.log2(hash_value.count(char)/len(hash_value)) for char in set(hash_value))
    return {"length": len(hash_value), "entropy": entropy}

@app.route('/analyze-hash', methods=['POST'])
def analyze_hash():
    hash_value = request.json['hash']
    analysis = analyze_hash_strength(hash_value)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
