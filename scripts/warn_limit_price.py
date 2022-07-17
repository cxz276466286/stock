from calendar import month
import tushare as ts
import time
import winsound
from datetime import date, timedelta

codes = ['601369']
warning_v = 10000

def watch():
    while True:
        data = ts.get_realtime_quotes(codes)
        # print(data)
        b1_v = float(data['b1_v'][0]) if bool(data['b1_v'][0]) else 0
        a1_v = float(data['a1_v'][0]) if bool(data['a1_v'][0]) else 0
        print(b1_v, a1_v, warning_v)

        if b1_v < warning_v and a1_v < warning_v:
            winsound.Beep(800, 1000)

        time.sleep(2.5)


if __name__ == "__main__":
    watch()
