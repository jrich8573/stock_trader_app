from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from backend.sp500_data import get_sp500_data
import os



app = Flask(__name__)

#update for your specific postgres container and secrets store
app.config['SQLAlCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class LogEntry(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    message = db.Column(db.String(256), nullable = False) 

@app.route('/api/sp500')
def sp500():
    data = get_sp500_data()
    log_entry = LogEntry(message='S&P 500 data requested')
    db.session.add(log_entry)
    db.session.commit()
    return jsonify(data)

  
if __name__ == "__main__":
    db.create_all() 
    app.run(debug=True)  