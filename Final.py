import RPi.GPIO as GPIO
import time
import dht11

# GPIO pin configuration
GSM_RX_PIN = 4
GSM_TX_PIN = 5

# Initialize the DHT11 sensor
sensor = dht11.DHT11(pin=2)

# Function to make a call
def make_call(phone_number):
    print("Making a call to {}...".format(phone_number))
    GPIO.output(GSM_TX_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GSM_TX_PIN, GPIO.LOW)

# Function to send an SMS
def send_sms(phone_number, message):
    print("Sending an SMS to {}...".format(phone_number))
    GPIO.output(GSM_TX_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GSM_TX_PIN, GPIO.LOW)

# Main loop
while True:
    # Read the temperature and humidity from the sensor
    temperature, humidity = sensor.read()

    # Print the temperature and humidity
    print("Temperature: {} degrees Celsius".format(temperature))
    print("Humidity: {}%".format(humidity))

    # Make a call if the temperature is above a certain threshold
    if temperature > 30:
        make_call("+1234567890")

    # Send an SMS if the humidity is above a certain threshold
    if humidity > 80:
        send_sms("+1234567890", "The humidity is too high!")

    # Wait for one hour
    time.sleep(3600)
