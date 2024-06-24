import os
from pymongo import MongoClient
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch

def parse_test_results(test_names):
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://testauto135:testauto@cluster0.zatvjbz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["TestLogs"]
    collection = db["TestColl"]

    test_results = []

    application_name = "Mens Apparel"
    total_test_cases = 0
    passed_test_cases = 0
    fail_count=0
    failed_test_cases = []

    # Query MongoDB for test results
    test_result = collection.find({"TestName": test_names}).sort('time', -1)
    print(test_names)
    print(test_result)

    # Check if any document was found for the current test case
    if collection.count_documents({"TestName": test_names}) == 0:
        print('') # Skip if no test result found for this test case
    else:
        total_test_cases=collection.aggregate([
    {"$match": {"TestName": test_names}},
    {"$group" :  {
        "_id": "$TestName",
        "sumval": {"$sum": 1}
        }}
])
        for result in test_result:
            # Format date and time
            formatted_date = result['time'].strftime('%d-%m-%Y')
            formatted_time = result['time'].strftime('%I:%M:%S %p')

            # Check test summary (Pass/Fail)
            if result['status'] == 'Pass':
                passed_test_cases += 1
            else:
                fail_count+=1
                failed_test_cases.append(test_names)

            result['formatted_date'] = formatted_date
            result['formatted_time'] = formatted_time
            test_results.append(result)

    # Calculate test summary
    test_summary = "Pass" if passed_test_cases == total_test_cases else "Fail"
    for res in total_test_cases:
        totalcount=int(res['sumval'])
    print(passed_test_cases, fail_count)

    return {
        "application_name": application_name,
        "total_test_cases": totalcount,
        "pass_cases": passed_test_cases,
        "fail_cases": fail_count,
        "test_summary": test_summary,
        "failed_test_cases": failed_test_cases,
        "test_results": test_results
    }

def capture_user_information():
    # Collect user-related information (name and email) through user input
    with open("..\\form_backend\\admindetails.txt", "r") as file:
        filedata=file.read()
    filedata=filedata.split(" ")
    user_name = filedata[0]
    user_email = filedata[1]
    application_name=filedata[2];
    return {"name": user_name, "email": user_email}

def generate_pdf_report(application_name, passcount, failcount, run_by, no_of_test_cases, test_summary, failed_tests, user_info, test_results,):
    # Create a PDF file
    directory_path = "C:/xampp/htdocs/Selenium-Website-Testing/TestCase_Reports"  # Change this to your desired directory
    # Ensure the directory exists, if not, create it
    os.makedirs(directory_path, exist_ok=True)
    # Create the full file path
    pdf_file = os.path.join(directory_path, f"{application_name}_test_report.pdf")
    #pdf_file = f"{application_name}_test_report.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading1']
    normal_style = styles['Normal']
    bold_style = ParagraphStyle('BoldStyle', parent=normal_style, fontName='Helvetica-Bold')
    
    # Content for PDF
    content = []

    # Add title
    title_text = f"Test Report for {application_name}"
    title = Paragraph(title_text, title_style)
    content.append(title)
    content.append(Spacer(1, 0.5 * inch))  # Add space after title

    # Add test summary
    test_summary_text = f"Test Summary: {test_summary}"
    test_summary_para = Paragraph(test_summary_text, heading_style)
    content.append(test_summary_para)
    content.append(Spacer(1, 0.2 * inch))  # Add space after test summary
    
    # Add date and time
    current_datetime = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
    datetime_text = f"Report generated on: {current_datetime}"
    datetime_para = Paragraph(datetime_text, normal_style)
    content.append(datetime_para)
    content.append(Spacer(1, 0.2 * inch))  # Add space after date and time

    # Add test results
    test_results_text = "Test Results:"
    test_results_para = Paragraph(test_results_text, heading_style)
    content.append(test_results_para)
    content.append(Spacer(1, 0.2 * inch))  # Add space after test results

    
    datetime_text = f"Total No. of test Runs: {no_of_test_cases}"
    datetime_para = Paragraph(datetime_text, normal_style)
    content.append(datetime_para)
    content.append(Spacer(1, 0.2 * inch))
    
    datetime_text = f"Number of Passed Test Cases : {passcount}"
    datetime_para = Paragraph(datetime_text, normal_style)
    content.append(datetime_para)
    content.append(Spacer(1, 0.2 * inch)) 
    
    datetime_text = f"Number of Failed Test Cases : {failcount}"
    datetime_para = Paragraph(datetime_text, normal_style)
    content.append(datetime_para)
    content.append(Spacer(1, 0.2 * inch)) 
    
    # Define table data for test results
    data = [['Test Name', 'Test Date', 'Status']]
    for result in test_results:
        data.append([result['TestName'], result['time'].strftime('%d-%m-%Y %I:%M:%S %p'), result['status']])

    # Define table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Create table object
    table = Table(data)
    table.setStyle(table_style)
    content.append(table)
    content.append(Spacer(1, 0.5 * inch))  # Add space after table

    # Add user information
    user_info_text_1 = "<b>User Information:</b><br/>"
    user_info_text_2 = f"- Name: {user_info['name']}<br/>"
    user_info_text_3 = f"- Email: {user_info['email']}"
    user_info_text = user_info_text_1 + user_info_text_2 + user_info_text_3
    user_info_para = Paragraph(user_info_text, bold_style)
    #user_info_para = Paragraph(user_info_text_1,user_info_text_2,user_info_text_3, bold_style)
    content.append(user_info_para)
    content.append(Spacer(1, 0.5 * inch))  # Add space after user information
       # user_info_text = f"User Information:<br/>- <b>{user_info['name']}</b><br/>- {user_info['email']}"

    # Build PDF
    doc.build(content)
    
    return pdf_file

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server details
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the PDF file
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
    message.attach(part)

    # Attach body text
    message.attach(MIMEText(body, 'plain'))

    smtp_server.send_message(message)
    smtp_server.quit()

# Main script
# 1. Capture test results from MongoDB
# List of test case names
with open("testcasename.txt", "r") as file:
        test_names=file.read()

# Call parse_test_results with test_names argument
test_results = parse_test_results(test_names)
print(test_results)
# 2. Capture user information before testing
user_info = capture_user_information()

# 3. Generate report with test results and user information
application_name = test_names
run_by = 'Tester'
no_of_test_cases = test_results['total_test_cases']  # Update this line
test_summary = test_results['test_summary']  # Update this line
failed_tests = test_results['failed_test_cases']  # Update this line
passcount=test_results['pass_cases']
failcount=test_results['fail_cases']

pdf_file = generate_pdf_report(application_name,passcount, failcount, run_by, no_of_test_cases, test_summary, failed_tests, user_info, test_results['test_results'])

# 4. Send email with report attachment
sender_email = 'testauto135@gmail.com'
sender_password = 'oqlmteruznmpwldi'
recipient_email = user_info['email']
subject = 'Automated Test Results'
body = 'Please find attached the test report in PDF format.'
send_email(sender_email, sender_password, recipient_email, subject, body, pdf_file)