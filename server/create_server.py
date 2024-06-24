
import os
from flask import Flask, request,jsonify
from flask_cors import CORS
import webbrowser
from pymongo import MongoClient
from streamlit.web import cli as stcli
import sys
import subprocess

app = Flask(__name__)

@app.route('/run-script-testLog', methods=['GET'])
def MongoLog():
    quantum_path= '..\mongotables.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"


@app.route('/run-script1', methods=['GET'])
def run_streamlitform():
    subprocess.run(["python", "-m", "streamlit", "run",'C:\\xampp\\htdocs\\Selenium-Website-Testing\\testscript_uploads\\MensApparel\\streamlitform.py'])
    return 'Executed streamlitform.py!'


@app.route('/run-script2', methods=['GET'])
def run_streamlitLoginTC():
    subprocess.run(["python", "-m", "streamlit", "run",'C:\\xampp\\htdocs\\Selenium-Website-Testing\\testscript_uploads\\MensApparel\\streamlitLoginTC.py'])
    return 'Executed streamlitLoginTC.py!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

