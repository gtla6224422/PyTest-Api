from flask import Flask, jsonify, request, render_template

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

#渲染html
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('user.html', name=name)
#渲染表单
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f'Received data: {data}'

#渲染boostrap
@app.route('/Bootstrap/index')
def index():
    return render_template('/Bootstrap/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)