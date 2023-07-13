import time
import RPi.GPIO as GPIO
import serial

# GPIO pin configuration
GSM_RX = 17
GSM_TX = 18
WATER_TEMP_SENSOR = 21

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GSM_RX, GPIO.IN)
GPIO.setup(GSM_TX, GPIO.OUT)
GPIO.setup(WATER_TEMP_SENSOR, GPIO.IN)

# Initialize the serial port
ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)

# Main loop
while True:
    # Read the water temperature
    water_temp = GPIO.input(WATER_TEMP_SENSOR)

    # Send an SMS if the water temperature is above a certain threshold
    if water_temp > 80:
        message = "Water temperature is too high: " + str(water_temp)
        ser.write(message.encode("utf-8"))

    # Sleep for one hour
    time.sleep(3600)
