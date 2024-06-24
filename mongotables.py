import pymongo
import webbrowser
from flask import Flask, render_template
import streamlit as st
import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader


client = pymongo.MongoClient("mongodb+srv://testauto135:testauto@cluster0.zatvjbz.mongodb.net/")
mydb = client["TestLogs"]
mycol = mydb["TestColl"]

# Initialize Jinja2 environment with the directory containing the template file
#env = Environment(loader=FileSystemLoader('.'))

# Load the template from the file
#template = env.get_template('info.html')

# Retrieve data from MongoDB
q={"id": {"$gt": 0}}

data = list(mycol.find(q,{"TSid":0}).batch_size(100).sort("TestName"))
print(data)

query= {"TSid": {"$gt": 0}}
tsdata=list(mycol.find(query))
#rendered_template = template.render(data)

# Print the rendered HTML
#print(rendered_template)
with open('output.html', 'w') as f:
    f.write('<html>\n')
    f.write('<style>\n')
    f.write('table, th, td {\n')
    f.write('border: 2px solid black;\n')
    f.write('border-collapse: collapse;\n')
    f.write('margin-left: auto; margin-right: auto;\n');
    f.write('padding: 10px;}\n');
    f.write('</style>\n')
    f.write('')
    f.write('<body>\n')
    f.write('<h1 style="text-align:center;">Test Logs</h1>')
    f.write('<table border="1">\n')
    f.write('<tr><th>ID</th><th>Test Name</th><th>Time</th><th>Description</th><th>Status</th></tr>\n')  # Add more table headers if needed
    for item in data:
        f.write(f'<tr><td>{item["id"]}</td><td>{item["TestName"]}</td><td>{item["time"]}</td><td>{item["Output"]}</td><td>{item["status"]}</td></tr>\n')  # Add more table cells if needed
    f.write('</table>\n')
    f.write('<br><br>')
    f.write('<table border="1">\n')
    f.write('<tr><th>ID</th><th>Test Suite Name</th><th>Time</th><th>Description</th><th>Number of Test Passed</th><th>Number of Test Failed</th></tr>\n')  # Add more table headers if needed
    for item in tsdata:
        f.write(f'<tr><td>{item["TSid"]}</td><td>{item["TestSuiteName"]}</td><td>{item["time"]}</td><td>{item["Output"]}</td><td>{item["pc"]}</td><td>{item["pf"]}</td></tr>\n')  # Add more table cells if needed
    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>\n')
url = 'output.html'

# Open URL in a new tab, if a browser window is already open
webbrowser.open_new_tab(url)