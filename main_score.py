from flask import Flask, render_template
from utils import scores_file_name, bad_return_code
import os

app = (Flask(__name__))
@app.route('/')
def score_server():
    if os.name == "nt":
        file_path = (f"c:\\temp\\{scores_file_name}")
    else:
        file_path = (f"/tmp//{scores_file_name}")

    error_code = bad_return_code
    score_file = open(file_path, 'r')
    score = score_file.read()
    score_file.close()
    if score != "":
        return render_template('score.html', score=score)
    else:
        return render_template('error.html', error=error_code)


app.run(host='127.0.0.1', debug=True, port=5000)
