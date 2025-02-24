import random

# Fixed order for traffic signal cycle
signal_order = ["East", "West", "North", "South"]
total_cycle_time = 240  # 4 minutes = 240 sec
min_time = 10  # Minimum signal time per direction

# Function to simulate real-time traffic data
def get_traffic_data():
    return {
        "East": random.randint(5, 100),
        "West": random.randint(5, 100),
        "North": random.randint(5, 100),
        "South": random.randint(5, 100),
    }

# Function to calculate signal timing dynamically
def calculate_signal_timings():
    traffic_density = get_traffic_data()
    
    # Step 1: Assign minimum time to each direction
    signal_timings = {direction: min_time for direction in signal_order}
    
    # Step 2: Distribute remaining time proportionally
    remaining_time = total_cycle_time - (min_time * len(signal_order))
    total_traffic = sum(traffic_density.values())

    for direction in signal_order:
        proportion = traffic_density[direction] / total_traffic if total_traffic > 0 else 0
        allocated_time = int(proportion * remaining_time)
        signal_timings[direction] += allocated_time

    # Step 3: Ensure total cycle time remains 240 sec
    total_allocated_time = sum(signal_timings.values())

    if total_allocated_time > total_cycle_time:
        excess_time = total_allocated_time - total_cycle_time
        most_traffic_side = max(traffic_density, key=traffic_density.get)
        signal_timings[most_traffic_side] -= excess_time

    return traffic_density, signal_timings

# Run the function and display results
traffic_density, signal_timings = calculate_signal_timings()
print("Traffic Density:", traffic_density)
print("Signal Timings:", signal_timings)
print("🚦 Cycle Order: East → West → North → South")
