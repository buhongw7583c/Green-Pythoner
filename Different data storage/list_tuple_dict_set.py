def different_data_type():
    l = []
    l.append('jack')
    l.insert(1, 3.14)
    print (l)
    l.pop(-1)
    print(l)

    t = ('jack', 'rose', 3.14, ['shanghai', 'beijing'])
    print (t)
    t[3][0] = 'guangzhou'
    print (t)

    d = {'beijing': 23, 'shanghai': 24, 'guangzhou': 25}
    print (d)
    print (d.get('beijing'))
    
    d['beijing'] = 26
    print (d.get('beijing'))

    dict_list = [{'frameid': 1, 'index': 2 }, \
        {'frmaeid': 2, 'index': 3}]
    print (dict_list[0].get('frameid'))

    d1 = {'jack': 32, 'john': 40}
    d2 = {'jack': 20, 'rose': 30}

    d_merge1 = {**d1, **d2}
    print (d_merge1)

    d_merge1['jack'] = 40
    print (d_merge1)
    print (d1)

    s = {1, 2, 3, 3, 4, 5, }
    s1 = {x for x in s if x <4 }

    s2 = set (s)
    print (s1)
    print (s2)
    print (s)
    print (s1 | s2, s1 & s2, s1 ^ s2)

different_data_type()
