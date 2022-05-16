from multiprocessing import Pool
import time


def delaysec(x):
    time.sleep(x)


if __name__ == "__main__":
    start = time.time()
    num_workers = 32
    with Pool(num_workers) as p:
        p.map(delaysec, [1] * num_workers)
    print(time.time() - start)
