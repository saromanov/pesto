import logging

from flask import Flask, render_template

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')

@app.route('/sources', methods=['GET'])
def main_page():
    return render_template('source.html')

if __name__ == '__main__':
    app.run()
