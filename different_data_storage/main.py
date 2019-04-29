import timeit
def list_search():
    test_list = [i*i for i in range (100000)]
    count = 0
    for i in range (100000):
        if i in test_list:
            count +=1
        else:
            continue

def set_search():
    test_set = {i*i for i in range (100000)}
    count = 0
    for i in range (100000):
        if i in test_set:
            count +=1
        else:
            continue
def main():
    print ("I am main.")

if __name__ == '__main__':
    main()
    t1 = timeit.timeit("list_search", setup="from __main__ import list_search", number=10)
    print (t1)
    t2 = timeit.timeit("set_search", setup="from __main__ import set_search", number=10)
    print (t2)
    
