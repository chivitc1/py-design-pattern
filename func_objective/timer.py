import datetime
import time


class TimeEvent:
    def __init__(self, endtime, callback):
        """store endtime and callback"""
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    def __init__(self):
        """stores a list of upcoming events"""
        self.events = []

    def call_after(self, delay: int, callback):
        """to add a new event
        :arg delay in second
        """
        endtime = datetime.datetime.now() + \
            datetime.timedelta(seconds=delay)
        self.events.append(TimeEvent(endtime, callback))

    def run(self):
        """to filter out any events
        whose time has come, and executes them in order"""
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)