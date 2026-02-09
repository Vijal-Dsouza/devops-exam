from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/health')
def health():
    return jsonify(
        {
            "Status": "ok",
            "service": "ecs-demo",
            "timestamp": "dummy-time"
        }

    )


if __name__ == '__main__':
    app.run()


