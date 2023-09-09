from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def status():
    return {"message": "OK", "code": 200 }

@app.route("/api", methods=['GET'])
def HNG_status():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    data = {
        'slack_name': slack_name,
        'current_day': datetime.strftime(datetime.now(), '%A'),
        'utc_time': utc_time,
        'track': track,
        'github_file_url': "https://github.com/CaptainAril/HNG-backend/blob/main/stage_one/app.py",
        "github_repo_url": "https://github.com/CaptainAril/HNG-backend",
        'status_code': 200
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()
