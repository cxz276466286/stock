from calendar import month
import tushare as ts
import time
import winsound
from datetime import date, timedelta

codes = ['000957']
warning_v = 10000

def watch():
    while True:
        data = ts.get_realtime_quotes(codes)
        # print(data)
        b1_v = float(data['b1_v'][0]) if bool(data['b1_v'][0]) else 0
        a1_v = float(data['a1_v'][0]) if bool(data['a1_v'][0]) else 0
        name = data['name'][0]
        print(name, b1_v, a1_v, warning_v)

        if b1_v < warning_v and a1_v < warning_v:
            print('WARNING:', name)
            winsound.Beep(500, 800)

        time.sleep(2.5)


if __name__ == "__main__":
    watch()
