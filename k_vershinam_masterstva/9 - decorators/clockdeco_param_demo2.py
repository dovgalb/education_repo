import time
from clockdeco_param import clock


@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(sec):
    time.sleep(sec)


for i in range(3):
    snooze(.4)