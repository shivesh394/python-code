import time
def gen1(num):
    time.sleep(2)
    yield num
for x in range(10):
    print(next(gen1(x)))