# Overview of the Demo
The demo involves a Flask web application that allows users to submit jobs and receive real-time status updates on those jobs using Server-Sent Events (SSE).


## Server-Side (Flask Application):
- Handles job submission.
- Updates job status in the background.
- Streams real-time updates to the client using SSE.


## Client-Side (HTML and JavaScript):
- Provides a user interface to start a job.
- Listens for real-time updates from the server and displays the job status.
