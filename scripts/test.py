from multiprocessing import Pool

def f(x):
    # print(x)
    pass


print("xxx")

if __name__ == '__main__':
    pool = Pool(processes=4)
    for i in range(1000):
        # start 4 worker processes
        # evaluate "f(10)" asynchronously in a single process
        pool.apply_async(f, (i,))

    pool.close()
    pool.join()
