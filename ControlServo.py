import RPi.GPIO as GPIO
import time

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_servo_angle(angle):
    pulse_ms = 1.5 - (angle/180)
    duty_cycle = (pulse_ms/20)*100
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

try:
    while True:
        set_servo_angle(-90)
        time.sleep(3)
        set_servo_angle(0)
        time.sleep(3)
        set_servo_angle(90)
        time.sleep(3)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

finally:
    GPIO.cleanup()