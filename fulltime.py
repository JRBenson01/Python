import time
tell = time.asctime(time.localtime(time.time()))
class time(object):
    def __init__(self, tell):
        self.tell = tell
    def hour(self):
        first = self.tell[11]
        second = self.tell[12]
        return first + second
    def minute(self):
        first = self.tell[14]
        second = self.tell[15]
        return first + second
    def second(self):
        first = self.tell[17]
        second = self.tell[18]
        return first + second
now = time(tell)
print now.hour()
print now.minute()
print now.second()
print str(now.hour)
