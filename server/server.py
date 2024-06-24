from flask import Flask, request,jsonify
from flask_cors import CORS
import webbrowser
from pymongo import MongoClient
from streamlit.web import cli as stcli
import sys
#app = Flask(__name__)
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run-script-testLog', methods=['GET'])
def MongoLog():
    quantum_path= 'mongotables.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"

@app.route('/run-script-testrunall', methods=['GET'])
def testrunall():
    subprocess.run(['python','server\\TestSuite.py'])
    print("Test successful")
    return "success"

@app.route('/run-script', methods=['GET'])
def carosel():
    quantum_path= 'server\\test_sport.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"

@app.route('/run-script-test2', methods=['GET'])
def itemfilter():
    quantum_path= 'server\\test_itemfilter.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"

@app.route('/run-script-test3', methods=['GET'])
def addtocart():
    quantum_path= 'server\\streamlitform.py'

    #subprocess.run(['f"{sys.executable}"',quantum_path])
    subprocess.run(["python", "-m", "streamlit", "run", quantum_path])
    print("Test add to cart successful")
    return "success"

@app.route('/run-script-test4', methods=['GET'])
def cartcount():
    quantum_path= 'server\\test_cartcount.py'

    subprocess.run(['python',quantum_path])
    print("Test cart count successful")
    return "success"

@app.route('/run-script-test5', methods=['GET'])
def loginTest():
    quantum_path= 'server\\streamlitLoginTC.py'

    subprocess.run(["python", "-m", "streamlit", "run", quantum_path])
    print("Test successful")
    return "success"

@app.route('/run-script-test6', methods=['GET'])
def logouttest():
    quantum_path= 'server\\LogoutTest.py'

    subprocess.run(['python',quantum_path])
    print("Test successful")
    return "success"

@app.route('/run-script-Falselogin', methods=['GET'])
def FalseLogin():
    subprocess.run(['python','server\\FalseCases\\FalseloginTest.py'])
    print("Test successful")
    return "success"

@app.route('/run-script-FalseCount', methods=['GET'])
def FalseCount():
    subprocess.run(['python','server\\FalseCases\\Falsetest_cartcount.py'])
    print("Test successful")
    return "Fail test case success"

@app.route('/run-script-FalseCarosel', methods=['GET'])
def FalseCarosel():
    subprocess.run(['python','server\\FalseCases\\Falsetest_sport.py'])
    print("Test successful")
    return "success"

@app.route('/run-script-FalseTestSuite', methods=['GET'])
def Falsetestsuite():
    subprocess.run(['python','server\\FalseCases\\FalseTestSuite.py'])
    print("Test successful")
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


