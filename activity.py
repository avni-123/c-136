from flask import Flask, jsonify, request
from info import data

app = Flask(__name__)

@app.route('/')

def fist_flask():
    return('This is my first flask program')

@app.route('/1')
def second():
    return jsonify({
        'data':data,
        'message' : 'success'
    }), 200 # 200 indicate that the API fectching was successful

@app.route('/planet')
def planets():
    name = request.args.get('name') 
    names = next(pl_name for pl_name in data if pl_name['name'] == name) #[expression loop-statment condition]
    return jsonify({
        'data':names,
        'message' : 'success'
    }), 200

app.run()
