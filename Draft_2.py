import time
import RPi.GPIO as GPIO
import serial

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

# Initialize the serial port
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

# Read the temperature and humidity from the sensor
temperature = round(100 * GPIO.input(15) / 255)
humidity = round(100 * GPIO.input(14) / 255)

# Send an SMS with the temperature and humidity
message = "Water temperature: {} degrees Celsius\nWater humidity: {}%".format(temperature, humidity)
ser.write("AT+CMGF=1\n")
ser.write("AT+CMGS=\"+1234567890\"\n")
ser.write(message)
ser.write("\n")

# Make a call with the temperature and humidity
ser.write("ATD+1234567890;\n")

# Sleep for one hour
time.sleep(3600)
