from flask import Flask, jsonify, request
import threading
import time
import queue

app = Flask(__name__)
jobs = {}
job_queues = {}

def update_job(job_id):
    for i in range(0, 101, 10):
        jobs[job_id] = i
        print(f"Updated {job_id} to {i}%")
        time.sleep(3)
    jobs[job_id] = 100
    print(f"Job {job_id} completed.")
    
    if job_id in job_queues:
        job_queues[job_id].put({"job_id": job_id, "status": 100})

@app.route('/')
def index():
    return "Welcome to Demo Long Polling!"

@app.route('/submit', methods=['POST'])
def submit_job():
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0
    job_queues[job_id] = queue.Queue()
    
    threading.Thread(target=update_job, args=(job_id,)).start()
    return jsonify({"job_id": job_id}), 200

@app.route('/checkstatus', methods=['GET'])
def check_status():
    job_id = request.args.get('job_id')
    if job_id not in jobs:
        return jsonify({"error": "Job not found"}), 404
    
    if jobs[job_id] == 100:
        return jsonify({"job_id": job_id, "status": 100}), 200
    
    job_queue = job_queues[job_id]
    try:
        result = job_queue.get(timeout=30)  # Long polling timeout set to 30 seconds
        return jsonify(result), 200
    except queue.Empty:
        return jsonify({"job_id": job_id, "status": jobs[job_id]}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)

