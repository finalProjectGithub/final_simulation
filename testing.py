import time


def currentTime():
    global timeString

    hours = 17
    minutes = 59
    seconds = 58

    while True:
        seconds = seconds + 1
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
            if minutes == 60:
                minutes = 0
                hours = hours + 1
                if hours == 24:
                    hours = 0
        timeString = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        time.sleep(1)
        print(timeString)


currentTime()