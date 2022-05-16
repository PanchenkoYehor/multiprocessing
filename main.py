from multiprocessing import Pool
import time

def delaysec(x):
    time.sleep(x)

if __name__ == "__main__":
    start = time.time()
    with Pool(5) as p:
        #p.apply(delaysec)
        p.map(delaysec, [1, 1, 1, 1, 1])
    print(time.time() - start)
