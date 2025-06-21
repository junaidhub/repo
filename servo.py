import pigpio
import time

# Set up the pigpio instance
pi = pigpio.pi()

# Set the GPIO pin used for the servo
servo_gpio_pin = 19

# Set the frequency for the servo (50 Hz is typical)
servo_frequency = 50

# Set the range for the servo (500 to 2500 is typical for most servos)
servo_range = (500, 2500)

# Function to move the servo to a specific angle
def set_servo_angle(angle):
    pulse_width = int((angle / 180.0) * (servo_range[1] - servo_range[0]) + servo_range[0])
    pi.set_servo_pulsewidth(servo_gpio_pin, pulse_width)

    try:
        # Set the servo GPIO pin to output
        pi.set_mode(servo_gpio_pin, pigpio.OUTPUT)

        # Set the servo frequency
        pi.set_PWM_frequency(servo_gpio_pin, servo_frequency)
##        while True:
##            user=input("enter angle")
##            move_servo_angle(int(user))
##
##    ##            # Move the servo to different angles
##    ##        move_servo_angle(0)  # Move to 0 degrees
##    ##        time.sleep(1)
##    ##        move_servo_angle(90)  # Move to 90 degrees
##    ##        time.sleep(1)
##    ##        move_servo_angle(180)  # Move to 180 degrees
##    ##        time.sleep(1)
##    ##        move_servo_angle(90)  # Move back to 90 degrees
##    ##        time.sleep(1)


    except KeyboardInterrupt:
        # Clean up
        pi.stop()
        # Code block to handle the KeyboardInterrupt exception
        print("Keyboard interrupt received. Exiting...")
set_servo_angle(160)
pi.stop()
