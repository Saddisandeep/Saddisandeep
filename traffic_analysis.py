from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Coordinates of the intersection (Example: Wipro Circle, Hyderabad)
intersection_location = "Wipro+Circle,+Hyderabad"

# Open Google Maps
url = f"https://www.google.com/maps/place/{intersection_location}"
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
driver.get(url)

# Wait for Google Maps to load
time.sleep(5)

# Extract traffic details (Modify XPath based on Google Maps structure)
traffic_data = driver.page_source  # Extracts the full page HTML (can be parsed)

# Save data locally (optional for debugging)
with open("traffic_data.html", "w", encoding="utf-8") as file:
    file.write(traffic_data)

print("Traffic data fetched successfully!")

# Close the browser
driver.quit()