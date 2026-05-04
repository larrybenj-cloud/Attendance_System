from flask import Flask, render_template, request, redirect, Response
from datetime import datetime
import io
import csv

app = Flask(__name__)
attendance_logs = []

@app.route('/')
def index():
    return render_template('index.html', logs=attendance_logs)

@app.route('/clockin', methods=['POST'])
def clock_in():
    name = request.form.get('name')
    emp_id = request.form.get('emp_id')
    if name and emp_id:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance_logs.insert(0, {"name": name, "id": emp_id, "time": now})
    return redirect('/')

# NEW: Function to export logs to a CSV file
@app.route('/export')
def export():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Employee ID', 'Clock-In Time'])
    for log in attendance_logs:
        writer.writerow([log['name'], log['id'], log['time']])
    
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=attendance_report.csv"}
    )

if __name__ == '__main__':
    app.run()
