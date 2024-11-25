from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 设置静态文件夹路径
REPORT_DIR = os.path.abspath('.')
STATIC_DIR = os.path.join(REPORT_DIR, 'assets')

@app.route('/')
def index():
    return "Welcome to the Test Report Service!"

@app.route('/report')
def report():
    return send_from_directory(REPORT_DIR, 'report.html')


@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)