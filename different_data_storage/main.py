import timeit
NUMBER = 10000000
def list_search():
    test_list = [i*i for i in range (NUMBER)]
    count = 0
    for i in range (100000):
        if i in test_list:
            count +=1
        else:
            continue

def set_search():
    test_set = {i*i for i in range (NUMBER)}
    count = 0
    for i in range (100000):
        if i in test_set:
            count +=1
        else:
            continue
def main():
    print ("I am main.")
    t1 = timeit.timeit("list_search", setup="from __main__ import list_search", number=10)
    print (t1)
    t2 = timeit.timeit("set_search", setup="from __main__ import set_search", number=10)
    print (t2)


if __name__ == '__main__':
    main()   
