import time
from adb import ADB
import requests

# Initialize ADB object
adb = ADB()

# Connect to the first device found
device = adb.devices()[0]

while True:
    # Get the phone temperature
    result = device.shell("cat /sys/class/thermal/thermal_zone0/temp")

    # Extract the temperature from the result
    temp = int(result.strip()) / 1000

    # Check if the temperature is more than 45 degrees
    if temp > 45:
        # Prepare the message
        message = f"ALERT: Temperature of the device is {temp} degrees Celsius, which is higher than the threshold of 45 degrees"

        # Use the Chatbot API to send the message
        response = requests.post(
            "https://chatbot_api_url",
            json={
                "message": message
            }
        )

        # Print the response status
        print(response.status_code)

    # Wait for 30 seconds before checking the temperature again
    time.sleep(30)
