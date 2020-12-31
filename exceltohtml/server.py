from flask import Flask, render_template
app = Flask(__name__)


@app.route('/form')
def index():
    return render_template('form.html')


@app.route('/confirm', methods=['POST'])
def confirm():
    return render_template('confirm.html')