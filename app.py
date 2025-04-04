from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get `top` command output
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -20", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    html_response = f"""
    <h2>System Information</h2>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h3>Top Output:</h3>
    <pre>{top_output}</pre>
    """
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
