import tushare as ts
import time
import winsound

codes = ['601360']
warning_v = 10000

def watch():
    while True:
        data = ts.get_realtime_quotes(codes)
        for i, code in enumerate(codes):
            # print(data)
            b1_v = int(data['b1_v'][i]) if bool(data['b1_v'][i]) else 0
            a1_v = int(data['a1_v'][i]) if bool(data['a1_v'][i]) else 0
            name = data['name'][i]
            print(name, b1_v, a1_v, warning_v)

            if b1_v < warning_v and a1_v < warning_v:
                print('WARNING:', name, code)
                winsound.Beep(500, 800)

        time.sleep(2.5)


if __name__ == "__main__":
    watch()
