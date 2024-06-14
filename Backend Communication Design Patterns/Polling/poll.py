from flask import Flask, jsonify, request
import threading
import time

app = Flask(__name__)
jobs = {}

def update_job(job_id):
    for i in range(0, 101, 10):
        jobs[job_id] = i
        print(f"Updated {job_id} to {i}%")
        time.sleep(3)
    jobs[job_id] = 100
    print(f"Job {job_id} completed.")

@app.route('/')
def index():
    return "Welcome to Demo Short Polling!"

@app.route('/submit', methods=['POST'])
def submit_job():
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0
    threading.Thread(target=update_job, args=(job_id,)).start()
    return jsonify({"job_id": job_id}), 200

@app.route('/checkstatus', methods=['GET'])
def check_status():
    job_id = request.args.get('job_id')
    if job_id not in jobs:
        return jsonify({"error": "Job not found"}), 404

    job_status = jobs[job_id]
    return jsonify({"job_id": job_id, "status": job_status}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)

