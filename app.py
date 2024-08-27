from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    if 'name' in data:
        response = {'message': f'Hello, {data["name"]}!'}
    else:
        response = {'error': 'Missing name in the request.'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='1.14.155.39', port=5002)