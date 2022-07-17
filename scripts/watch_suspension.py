import tushare as ts
import time
import winsound
from datetime import date, timedelta

codes = ['000957', '399106']
# stock_index_base = 2155.56
# stock_base = 20.38


def watch():
    earlyday = date.today() - timedelta(30)
    hist_stock_data = ts.get_hists(codes[:1], start=str(earlyday))
    hist_index_data = ts.get_hists(codes[1:], start=str(earlyday))
    stock_base = float(hist_stock_data['close'][2])
    stock_index_base = float(hist_index_data['close'][2])
    print('stock', stock_base)
    print('index', stock_index_base)

    while(True):
        data = ts.get_realtime_quotes(codes)
        stock_price = float(data['price'][0])
        stock_index = float(data['price'][1])
        name = data['name'][0]

        rate = round((stock_price - stock_base) / stock_base -
                     (stock_index - stock_index_base) / stock_index_base, 5)
        target_price = round((0.2 + (stock_index - stock_index_base) /
                             stock_index_base) * stock_base + stock_base, 2)
        if abs(rate) >= 0.19:
            print('{} {}  {}  {}  \033[1;43m{}\033[0m'.format(
                name, stock_price, target_price, stock_index, rate))
        elif abs(rate) >= 0.2:
            print('{} {}  {}  {}  \033[1;41m{}\033[0m'.format(
                name, stock_price, target_price, stock_index, rate))
            winsound.Beep(500, 800)
        else:
            print('{} {}  {}  {}  \033[0;42m{}\033[0m'.format(
                name, stock_price, target_price, stock_index, rate))
            

        time.sleep(2)


if __name__ == "__main__":
    watch()
