import multiprocessing
import easypdb
import numpy as np
def test():
    print('12111')
    print('12111')
    print('12111')
    ttt = np.array((10,10))
    ttt.sum()
    print('12111')
    print('12111')

def func():
    easypdb.set_trace()

    # 这里是你的函数实现
    print("Hello from process with ID:", multiprocessing.current_process().name)
    print("test code line 1")
    print("test 2")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    test()
    test()
    test()
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 3")
    print("test line 4")
    print("test line 4")
    print("test line 4")
    print("test line 4")
    print("test line 4")
    print("test line 4")
    print("test line 4")



if __name__ == '__main__':
    num_processes = 1
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(target=func)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
