from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run()


# from datetime import datetime 
# @app.route('/health')
# def health():
#     return jsonify(
#         {
#             "status": "ok",
#             "service":"ecs-demo",
#             "time
#         }
        
#     )