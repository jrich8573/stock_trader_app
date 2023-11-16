from flask import Flask, jsonify
from backend.sp500_data import get_sp500_data

app = Flask(__name__)


@app.route('/api/sp500')
def sp500():
    data = get_sp500_data()
    return jsonify(data)

  
if __name__ == "__main__":
     app.run(debug=True)  