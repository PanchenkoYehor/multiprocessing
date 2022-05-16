from multiprocessing import Process
import time


def delaysec():
    time.sleep(1)
    #print(5)


if __name__ == "__main__":

    start = time.time()

    processes_list = []
    for i in range(100):
        processes_list.append(Process(target=delaysec))

    for process in processes_list:
        process.start()

    for process in processes_list:
        process.join()

    print(time.time() - start)
