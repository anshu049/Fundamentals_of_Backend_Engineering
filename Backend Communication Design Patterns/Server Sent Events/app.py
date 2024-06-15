from flask import Flask, jsonify, request, Response, render_template
import threading
import time
import queue

app = Flask(__name__)
jobs = {}
clients = {}

def update_job(job_id):
    for i in range(0, 101, 10):
        jobs[job_id] = i
        print(f"Updated {job_id} to {i}%")
        if job_id in clients:
            clients[job_id].put(i)
        time.sleep(3)
    jobs[job_id] = 100
    if job_id in clients:
        clients[job_id].put(100)
    print(f"Job {job_id} completed.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_job():
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0
    clients[job_id] = queue.Queue()
    threading.Thread(target=update_job, args=(job_id,)).start()
    return jsonify({"job_id": job_id}), 200

@app.route('/status/<job_id>')
def status(job_id):
    def generate(job_id):
        while True:
            if job_id not in clients:
                break
            status = clients[job_id].get()
            yield f"data: {status}\n\n"
            if status == 100:
                break
    return Response(generate(job_id), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

