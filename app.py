from flask import Flask, render_template, request, url_for, jsonify, make_response
import json
from db.models import Noise
from db.database import db_session
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    title = "おとどけもの"
    return render_template('GoogleMap.html', title=title)
if __name__ == '__main__':
    app.run()


@app.route('/api/status', methods=['POST'])
def status():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    data = json.load(request.data)
    if data["name"] & data["noise"] & data["latitude"] & data["longitude"]:
        content = Noise(name=data["name"],
                        noise=data["noise"],
                        latitude=data["latitude"],
                        longitude=data["longitude"],
                        date=datetime.now())
        db_session.add(content)
        db_session.commit()
        return jsonify(req="ok")
    else:
        return make_response(jsonify({"error": "Bad request"}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




