import os
from flask import Flask, jsonify
import importlib.util
import subprocess

def generate_flask_app(directory,x):
    app_name = "create_server"
    flask_app = f"""
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
    quantum_path= '..\\mongotables.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"

"""
    i=1
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            if filename.startswith("streamlit"):
                file_path = os.path.join(directory, filename)
                flask_app += f"""
@app.route('/run-script{i}', methods=['GET'])
def run_{filename[:-3]}():
    subprocess.run(["python", "-m", "streamlit", "run",'C:\\\\xampp\\\\htdocs\\\\Selenium-Website-Testing\\\\testscript_uploads\\\\{x}\\\\{filename}'])
    return 'Executed {filename}!'

"""
            else:
                file_path = os.path.join(directory, filename)
                #route = f"/{filename[:-3]}"
                flask_app += f"""
@app.route('/run-script{i}', methods=['GET'])
def run_{filename[:-3]}():
    subprocess.run(['python','C:\\\\xampp\\\\htdocs\\\\Selenium-Website-Testing\\\\testscript_uploads\\\\{x}\\\\{filename}'])
    return 'Executed {filename}!'

"""
        i+=1

    flask_app += """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

"""

    with open(f"../server/{app_name}.py", "w") as file:
        file.write(flask_app)

if __name__ == "__main__":
    arr=[]
    with open("C:/xampp/htdocs/Selenium-Website-Testing/form_backend/admindetails.txt", "r") as file:
        arr = file.read()
    arr=arr.split(' ')
    directory = "C:/xampp/htdocs/Selenium-Website-Testing/testscript_uploads/" + arr[2]+"/"
    generate_flask_app(directory,arr[2])
    print("Flask app file generated successfully!")

