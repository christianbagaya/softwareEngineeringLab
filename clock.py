import datetime
import time
import threading
import playsound


# import winsound


class myClock():
    def __init__(self, name_of_user, time_format, snooze_time):
        self.name_of_user = name_of_user
        self.name_of_user = name_of_user
        self.time_format = name_of_user
        self.snooze_time = snooze_time
    
    def show_time_of_day(self):        
        print(datetime.datetime.now())
        
    def set_alert(self, date_string):
        # import pdb; pdb.set_trace()
        input_time = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        difference = input_time - datetime.datetime.now()
        d = datetime.timedelta(seconds = difference.total_seconds())
        # time.sleep(d.total_seconds())
        time.sleep(d.total_seconds())

        print('wake up!!')
        # self.sound()
        self.fire_alert()

    def snooze(self, min=None):
        if not min:
            self.set_alert(self, min)

    def off(self):
        pass

    def fire_alert(self):
        playsound.playsound('alarm.mp3')

    def ask_user_for_second_alarm(self):
        pass


def main():
    # import pdb; pdb.set_trace()
    t = raw_input("Enter the full date of the alarm in format YYYY-mm-dd HH:MM:SS : ")
    clock = myClock("Christian Bagaya", 24, 2)
    clock.show_time_of_day()
    clock.set_alert(t)

main()