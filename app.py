from flask import Flask ,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    result={
        "name":"harsh"
    }
    return jsonify(result)



app.run(debug=True)
