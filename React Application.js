// src/App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [input, setInput] = useState('');
    const [algorithm, setAlgorithm] = useState('sha256');
    const [hash, setHash] = useState('');
    const [aiHash, setAiHash] = useState('');
    const [analysis, setAnalysis] = useState(null);

    const generateHash = async () => {
        const response = await axios.post('http://localhost:5000/generate-traditional-hash', { input, algorithm });
        setHash(response.data.hash);
        const analysisResponse = await axios.post('http://localhost:5000/analyze-hash', { hash: response.data.hash });
        setAnalysis(analysisResponse.data);
    };

    const generateAiHash = async () => {
        const response = await axios.post('http://localhost:5000/generate-ai-hash', { input });
        setAiHash(response.data.ai_hash);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Advanced AI-based Hash Generator</h1>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Enter input"
                />
                <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
                    <option value="md5">MD5</option>
                    <option value="sha256">SHA-256</option>
                    <option value="sha512">SHA-512</option>
                    <option value="bcrypt">Bcrypt</option>
                    <option value="hmac">HMAC</option>
                </select>
                <button onClick={generateHash}>Generate Traditional Hash</button>
                <button onClick={generateAiHash}>Generate AI Hash</button>

                {hash && (
                    <div>
                        <h3>Generated Hash:</h3>
                        <p>{hash}</p>
                        {analysis && (
                            <div>
                                <h4>Security Analysis:</h4>
                                <p>Length: {analysis.length}</p>
                                <p>Entropy: {analysis.entropy.toFixed(4)}</p>
                            </div>
                        )}
                    </div>
                )}

                {aiHash && (
                    <div>
                        <h3>Generated AI Hash:</h3>
                        <p>{aiHash}</p>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
