#  The "__main__" function

### __ main __ function 
### A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is importd. 

```
main.py

NUMBER = 100
def main():
    print ("I am main.")
```

### there is no problem with this. But when some other modules would like to import the data from the main.py, the main() will be executed as well. 

```
from different_data_storage.main import NUMBER

def main():
    print (NUMBER)

main()

##Result: 
I am main.
10000000
```
### the problem is, python is script language, when import the main module, the whole file has been excecuted as well. But sometimes we only want the main to be called when it is the executed. 

```
def main():
    print ("I am main.")
    t1 = timeit.timeit("list_search", setup="from __main__ import list_search", number=10)
    print (t1)
    t2 = timeit.timeit("set_search", setup="from __main__ import set_search", number=10)
    print (t2)


if __name__ == '__main__':
    main()   

```

### if main function was written like this, when run below code, only the number will be printed out as we expected. Because the "if __name__ == '__main__':" usage is, when the file is called as program, the main function will be called. But if the file is called when importing, the main function will not be called. 
```
from different_data_storage.main import NUMBER

def main():
    print (NUMBER)

main()

##Result: 

10000000
```

- 加上 -m 参数时会把当前工作目录添加到 sys.path 中，而不加时则会把脚本所在目录添加到 sys.path 中。
- 加上 -m 参数时 Python 会先将模块或者包导入，然后再执行
- 所以， _ _main_ _.py 文件是一个包或者目录的入口程序。不管是用 python package 还是用 python -m package 运行时， _ _main_ _.py 文件总是被执行。