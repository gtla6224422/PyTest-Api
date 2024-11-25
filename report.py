from flask import Flask, send_from_directory

app = Flask(__name__)

# 设置静态文件夹路径
REPORT_DIR = '../reports'

@app.route('/')
def index():
    return "Welcome to the Test Report Service!"

@app.route('/report')
def report():
    return send_from_directory(REPORT_DIR, 'report.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)