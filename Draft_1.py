import time
import RPi.GPIO as GPIO
import serial

# GPIO pin configuration
GSM_RX = 17
GSM_TX = 18
WATER_TEMP_SENSOR = 22

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GSM_RX, GPIO.IN)
GPIO.setup(GSM_TX, GPIO.OUT)
GPIO.setup(WATER_TEMP_SENSOR, GPIO.IN)

# Initialize the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Main loop
while True:
    # Read the water temperature sensor
    water_temp = GPIO.input(WATER_TEMP_SENSOR)

    # Send an SMS with the water temperature
    if water_temp > 30:
        ser.write('AT+CMGF=1\r')
        time.sleep(1)
        ser.write('AT+CMGS="+1234567890"\r')
        time.sleep(1)
        ser.write('Water temperature is: ' + str(water_temp) + '\r')
        time.sleep(1)
        ser.write('\r')

    # Sleep for 1 hour
    time.sleep(3600)
