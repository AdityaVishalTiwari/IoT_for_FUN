from machine import Pin, PWM, RTC, ADC
import time
import urequests
import network
import ujson

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Daims_Atomix', 'Piyush4c1v@')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

def send_status_to_thingspeak(api_key, field1_value, field2_value):
    url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(api_key, field1_value, field2_value)
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print("Status updated successfully to ThingSpeak: Field1={}, Field2={}".format(field1_value, field2_value))
        else:
            print("Failed to update status to ThingSpeak. Status code:", response.status_code)
    except Exception as e:
        print("Error:", str(e))



PIR_PIN1 = 14  # PIR sensor 1 pin
LIGHTS_PIN1 = 27  # Light 1 pin
ALERT_PIN1 = 4  # Alert 1 pin

PIR_PIN2 = 25  # PIR sensor 2 pin
LIGHTS_PIN2 = 26  # Light 2 pin
ALERT_PIN2 = 2  # Alert 2 pin

pir1 = Pin(PIR_PIN1, Pin.IN)
pir2 = Pin(PIR_PIN2, Pin.IN)

# Use PWM to control light intensity for both lights
lights_pwm1 = PWM(Pin(LIGHTS_PIN1), freq=1000, duty=0)  # Light 1 PWM
lights_pwm2 = PWM(Pin(LIGHTS_PIN2), freq=1000, duty=0)  # Light 2 PWM

alert1 = Pin(ALERT_PIN1, Pin.OUT)
alert2 = Pin(ALERT_PIN2, Pin.OUT)

alert1.value(0)  # Initialize alert pins to low
alert2.value(0)

rtc = RTC()
rtc.init((2023, 9, 22, 5, 23, 44, 0, 0))  # Set the initial date and time to 2023-01-01 17:30:00


    # Rest of your code for controlling lights and motion detection
fall_threshold = 10  # Adjusted to 100 seconds
sleep_pattern_timeout = 6000  # Time in milliseconds without motion to turn off lights

def turn_off_lights():
    lights_pwm1.duty(0)  # Turn off lights
    lights_pwm2.duty(0)
    print("Lights turned off.")

while True:
    current_time = rtc.datetime()
    hour = current_time[4]

    motion_detected1 = pir1.value() == 1
    motion_detected2 = pir2.value() == 1
    

    if 17 <= hour < 21:  # Lights automatically on from 5:30 PM to 9 PM
        lights_pwm1.duty(500)
        lights_pwm2.duty(500)
        time_since_last_motion1 = rtc.datetime()[5]
        if motion_detected1 and time_since_last_motion1 > fall_threshold:
            print("Fall detected by PIR 1! Call for help.")
            alert1.value(1)
            time.sleep(5)
            alert1.value(0)
            

        # Fall detection logic for PIR 2
        time_since_last_motion2 = rtc.datetime()[5]
        if motion_detected2 and time_since_last_motion2 > fall_threshold:
            print("Fall detected by PIR 2! Call for help.")
            alert2.value(1)
            time.sleep(5)
            alert2.value(0)
    elif 6 <= hour < 17:  # Lights automatically off from 6 AM to 5:00 PM
        lights_pwm1.duty(0)
        lights_pwm2.duty(0)
        
        # Fall detection logic for PIR 1
        time_since_last_motion1 = rtc.datetime()[5]
        if motion_detected1 and time_since_last_motion1 > fall_threshold:
            print("Fall detected by PIR 1! Call for help.")
            alert1.value(1)
            time.sleep(5)
            alert1.value(0)
        
        # Fall detection logic for PIR 2
        time_since_last_motion2 = rtc.datetime()[5]
        if motion_detected2 and time_since_last_motion2 > fall_threshold:
            print("Fall detected by PIR 2! Call for help.")
            alert2.value(1)
            time.sleep(5)
            alert2.value(0)

            
    else:
        # Outside of the specified time range, rely on motion detection
        lights_pwm1.duty(0)
        lights_pwm2.duty(0)
        if motion_detected1:
            print("Motion detected by PIR 1!")
            # Light 1 on with low intensity
            lights_pwm1.duty(50)
        else:
            print("No motion detected by PIR 1.")

        if motion_detected2:
            print("Motion detected by PIR 2!")
            # Light 2 on with low intensity
            lights_pwm2.duty(50)
        else:
            print("No motion detected by PIR 2.")

        # Fall detection logic for PIR 1
        time_since_last_motion1 = rtc.datetime()[5]
        if motion_detected1 and time_since_last_motion1 > fall_threshold:
            print("Fall detected by PIR 1! Call for help.")
            alert1.value(1)
            time.sleep(5)
            alert1.value(0)
            lights_pwm1.duty(500)
            time.sleep(15)
            send_status_to_thingspeak("L0FCLSMTPYA1NYST", 1, 0)

        # Fall detection logic for PIR 2
        time_since_last_motion2 = rtc.datetime()[5]
        if motion_detected2 and time_since_last_motion2 > fall_threshold:
            print("Fall detected by PIR 2! Call for help.")
            alert2.value(1)
            time.sleep(5)
            alert2.value(0)
            lights_pwm2.duty(500)
            time.sleep(15)
            send_status_to_thingspeak("L0FCLSMTPYA1NYST", 0, 1)

        # Sleep pattern tracking for PIR 1
        if not motion_detected1:
            if time_since_last_motion1 > sleep_pattern_timeout:
                print("Patient might be asleep (PIR 1).")
                lights_pwm1.duty(0)

        # Sleep pattern tracking for PIR 2
        if not motion_detected2:
            if time_since_last_motion2 > sleep_pattern_timeout:
                print("Patient might be asleep (PIR 2).")
                
     

        

        time.sleep(1)  # Adjust the sleep interval as needed