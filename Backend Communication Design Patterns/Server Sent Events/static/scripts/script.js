function startJob() {
    fetch('/submit', {method: 'POST'})
        .then(response => response.json())
        .then(data => {
            const jobId = data.job_id;
            const eventSource = new EventSource(`/status/${jobId}`);
            
            eventSource.onmessage = function(event) {
                document.getElementById('status').innerText = `Job ${jobId} Status: ${event.data}%`;
                if (event.data == "100") {
                    eventSource.close();
                }
            };
        });
}

