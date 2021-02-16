from flask import Flask
from fitfarmer.diagnose import diagnose
app = Flask(__name__)

@app.route('/diagnose/', methods=['POST'])
def diagnose_api():
    patient = flask.request.get_json()
    diagnosis = diagnose(patient)
    return flask.jsonify(diagnosis)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
