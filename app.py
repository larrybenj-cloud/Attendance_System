from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# This list acts as our temporary database
attendance_logs = []

@app.route('/')
def index():
    return render_template('index.html', logs=attendance_logs)

@app.route('/clockin', methods=['POST'])
def clock_in():
    name = request.form.get('name')
    emp_id = request.form.get('emp_id')
    
    if name and emp_id:
        # Capture current time in West Africa Time (WAT)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"name": name, "id": emp_id, "time": now}
        attendance_logs.insert(0, entry) # Add new entries to the top
        
    return redirect('/')

if __name__ == '__main__':
    app.run()
