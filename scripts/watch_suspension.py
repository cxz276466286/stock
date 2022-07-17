import tushare as ts
import time
import winsound
from datetime import date, timedelta

codes = ['000957', '002090']
index_codes = ['399106']
# stock_index_base = 2155.56
# stock_base = 20.38


def watch():
    earlyday = date.today() - timedelta(30)
    stock_base_list = []
    for code in codes:
        hist_stock_data = ts.get_hists([code], start=str(earlyday))
        stock_base_list.append(float(hist_stock_data['close'][2]))
    hist_index_data = ts.get_hists(index_codes, start=str(earlyday))
    szzz_base = float(hist_index_data['close'][2])

    print('stock', stock_base_list)
    print('index', szzz_base)

    while(True):
        data = ts.get_realtime_quotes(codes + index_codes)
        szzz = float(data['price'][len(codes)])
        for i, code in enumerate(codes):
            stock_price = float(data['price'][i])
            name = data['name'][i]

            rate = round((stock_price - stock_base_list[i]) / stock_base_list[i] -
                        (szzz - szzz_base) / szzz_base, 5)
            target_price = round((0.2 + (szzz - szzz_base) /
                                szzz_base) * stock_base_list[i] + stock_base_list[i], 2)
            if abs(rate) >= 0.19:
                print('{} {}  {}  {}  \033[1;43m{}\033[0m'.format(
                    name, stock_price, target_price, szzz, rate))
            elif abs(rate) >= 0.2:
                print('{} {}  {}  {}  \033[1;41m{}\033[0m'.format(
                    name, stock_price, target_price, szzz, rate))
                winsound.Beep(500, 800)
            else:
                print('{} {}  {}  {}  \033[0;42m{}\033[0m'.format(
                    name, stock_price, target_price, szzz, rate))
            

        time.sleep(2)


if __name__ == "__main__":
    watch()
