from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder='../templates')

CYCLE_TIME = 240
MIN_TIME = 10  
ORANGE_TIME = 2
signal_order = ["East", "West", "North", "South"]
remaining_time_carryover = 0  
traffic_data = {}
signal_timings = {}

def fetch_initial_traffic_data():
    global traffic_data, signal_timings, remaining_time_carryover
    traffic_data = {direction: random.randint(5, 100) for direction in signal_order}
    signal_timings = {direction: MIN_TIME for direction in signal_order}
    available_time = CYCLE_TIME - (MIN_TIME * len(signal_order)) + remaining_time_carryover
    total_traffic = sum(traffic_data.values())
    remaining_time_carryover = 0  
    
    if total_traffic > 0:
        for direction in signal_order:
            proportion = traffic_data[direction] / total_traffic
            allocated_time = int(proportion * available_time)
            if allocated_time < MIN_TIME:
                remaining_time_carryover += (MIN_TIME - allocated_time)
            signal_timings[direction] += allocated_time

@app.route('/')
def home():
    fetch_initial_traffic_data()
    return render_template('traffic_signals.html')

@app.route('/traffic_data')
def traffic_data_api():
    fetch_initial_traffic_data()
    return jsonify({
        "traffic_density": traffic_data,
        "signal_timings": signal_timings,
        "remaining_time": remaining_time_carryover
    })

if __name__ == '__main__':
    app.run(debug=True)
