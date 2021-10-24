from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    """Passing parameters below."""
    who=request.args.get('who','CA')
    return f'Hello {who}!\n'