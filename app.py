from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

# Global variable to store the start time
start_time = None

def get_start_time():
    global start_time
    if start_time is None:
        # Check if the start time is stored in a file or a database
        # If the file doesn't exist or database is empty, set the start time to the current time
        # For simplicity, I'll just set the start time to the current time
        start_time = datetime.datetime.now()
    return start_time

@app.route('/api/welcome', methods=['POST'])
def welcome_python_app():
    data = request.json
    user_input = data.get('user_input', '').lower()

    if user_input == 'hello':
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reply = f'Welcome to the Python app! The app is active from last {calculate_time_since_start()}'
        return jsonify({'reply': reply})
    else:
        return jsonify({'reply': 'Unknown input'})

def calculate_time_since_start():
    current_time = datetime.datetime.now()
    duration = current_time - get_start_time()
    total_seconds = int(duration.total_seconds())

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours > 0 and minutes > 0:
        return f'{hours} hours and {minutes} minutes.'
    elif hours > 0:
        return f'{hours} hours.'
    elif minutes > 0:
        return f'{minutes} minutes.'
    else:
        return 'less than a minute.'

@app.route('/', methods=['POST'])
def welcome_react_app():
    data = request.json
    user_input = data.get('user_input', '').lower()

    if user_input == 'hello':
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reply = f'Welcome to the React app! The app is active from last {calculate_time_since_start()}'
        return jsonify({'reply': reply})
    else:
        return jsonify({'reply': 'Unknown input'})

if __name__ == '__main__':
    # On application start, get the start time
    start_time = get_start_time()
    app.run()
