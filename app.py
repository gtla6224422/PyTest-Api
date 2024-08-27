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

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)