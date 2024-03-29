from flask import Flask, render_template, request
from MicroSoft import login_to_microsoft as run_selenium_bot
from health import check_cpu_usage as  chek_processes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_task', methods=['POST'])
def run_task():
    username = request.form['username']
    password = request.form['password']
    # Call the Selenium bot function
    if not chek_processes():
        result = run_selenium_bot(username, password)
    else:
        result = "Too many Chrome processes running. Please try again later."
    return render_template('error.html', result=result)

@app.route('/*', methods=['GET'])
def not_found():
    return render_template('error.html', error='Page not found')

if __name__ == '__main__':
    app.run(debug=True)
