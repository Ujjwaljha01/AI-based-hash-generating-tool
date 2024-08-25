from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hashes.db'
db = SQLAlchemy(app)

class HashEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.String(100))
    algorithm = db.Column(db.String(50))
    hash_value = db.Column(db.String(256))
    entropy = db.Column(db.Float)

@app.route('/save-hash', methods=['POST'])
def save_hash():
    data = request.json
    new_entry = HashEntry(input_data=data['input'], algorithm=data['algorithm'], hash_value=data['hash'], entropy=data.get('entropy', 0))
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Hash saved successfully!"})
