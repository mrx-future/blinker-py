from Blinker import *

Blinker.mode(BLINKER_WIFI)
Blinker.begin()
Blinker.attachAhrs()

if __name__ == '__main__':
    while True:
        Blinker.run()
        
        if Blinker.available() is True:
            BLINKER_LOG('Blinker.readString(): ', Blinker.readString())
            Blinker.print(Blinker.times())
            Blinker.vibrate()
            Blinker.print('millis', millis())

        BLINKER_LOG('AHRS Yaw: ', Blinker.ahrs(Yaw))
        BLINKER_LOG('AHRS Roll: ', Blinker.ahrs(Roll))
        BLINKER_LOG('AHRS Pitch: ', Blinker.ahrs(Pitch))

        Blinker.delay(2000)
