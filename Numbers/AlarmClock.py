import datetime
import time

def alarm(tie):
    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(), tie)
    # Think of time.sleep() as having the operating system set an alarm for you,
    # and waking you up when the alarm fires.
    time.sleep((alarm_time - now).total_seconds())

    return "ALARM ALARM"

if __name__ == '__main__':
    # Format is Hours, Minutes, Seconds, Milliseconds...
    ctn = datetime.time(10,0,0)
    alarm(ctn)
