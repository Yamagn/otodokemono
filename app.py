from flask import Flask, render_template, request, url_for, jsonify, make_response
import json
from db.models import Noise
from db.database import db_session
from datetime import datetime

app = Flask(__name__)

latitude = 35.692467
longitude = 139.7581


@app.route('/')
def index():
    row = db_session.query(Noise).order_by(Noise.date.desc()).first()
    # row = Noise.query.first()
    noise = row.noise
    print(noise)
    color = ""
    if noise >= 80:
        color = "#F00"
    elif 50 < noise < 80:
        color = "#FF0"
    else:
        color = "#0FF"
    return render_template('GoogleMap.html', latitude=latitude, longitude=longitude, color=color, noise=noise)
if __name__ == '__main__':
    app.run()


@app.route('/api/status/', methods=['POST'])
def status():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    content = Noise(name=data["name"],
                    noise=data["noise"],
                    latitude=latitude,
                    longitude=longitude,
                    date=datetime.now())
    db_session.add(content)
    db_session.commit()
    return jsonify(res="ok")
