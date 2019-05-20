# List

## List is an array of data, using '[]' to denote. 

```
l = []
l.append('jack')
l.insert(1, 3.14)
print (l)

['jack', 3.14]

## The list can use the 'last' index to refer. '-1' means the last one element. 
l.pop(-1)
print(l)

['jack']
```

# Tuple
### Tuple can be treated as a 'non-changable' list. It is useful when a function needs to return a serie of data and dont want them to be changed. 

```
t = ('jack', 'rose', 3.14)
print (t)

('jack', 'rose', 3.14)

t[0] = 'hong'

TypeError: 'tuple' object does not support item assignment
```

### There is no 'append', 'pop',  or 'insert' on tuple, as tuple cannot be changed. But the value can be modified in this way: 

```
    t = ('jack', 'rose', 3.14, ['shanghai', 'beijing'])
    print (t)
    t[3][0] = 'guangzhou'
    print (t)

('jack', 'rose', 3.14, ['shanghai', 'beijing'])
('jack', 'rose', 3.14, ['guangzhou', 'beijing'])
```
### Indeed, the place where tuple point to cannot be changed. But if the tuple contains a list, the position of the list cannot be changed. But the value contains in the list can be changed. 

# Dict
### Dictionary is the most intereting data type in python and very powerful, as it provides a very unique 'key'->'value' way to store the data. 

### Dictionay can only be accessed by 'key', but cannot by 'index'. 

```
    d = {'beijing': 23, 'shanghai': 24, 'guangzhou': 25}
    print (d)
    print (d.get('beijing'))

    {'beijing': 23, 'shanghai': 24, 'guangzhou': 25}
    23

    print (d[0])
    KeyError: 0
```

### The key of a dictinary cannot be changed but the corresponding value can be changed. 

```
    d['beijing'] = 26
    print (d.get('beijing'))

26
```
### 
### List VS dictionary: Dictionary has no sequence but list has. Dict is quick for seaching and it uses key as the index but consums more memory. List is slow for seaching but occupies less memory. 

## Combine two dicts--> dict()
```
    d1 = {'jack': 32, 'john': 40}
    d2 = {'jack': 20, 'rose': 30}

    d_merge1 = {**d1, **d2}
    print (d_merge1)

{'jack': 20, 'john': 40, 'rose': 30}

The duplicated values will be combined. 
```
## Set

### set is like a dictionary without 'key', an unordered list of data but with no duplicates. Set is used to verify whether a value contains in the list or not as the value in the set are unique. 

```
s = {1, 2, 3, 3, 4, 5, }

Only unique numbers will be kept in s
{1, 2, 3, 4, 5}

s1 = {x for x in s if x <4 }
//the s1 is derived from s
{1, 2, 3}

```

### set VS list
- Set is unordered. List is ordered. 
- Set only has unique data. 
- Set is quicker in seaching compared with list. 



