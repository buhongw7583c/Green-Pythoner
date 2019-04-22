# BizzBuzz Qustion
### Among an integer list, use the bizz to replce numbers that could be divided by 3 and use buzz to replace the ones that could be divided by 5, and bizzbuzz to replce the ones that could be divided by both. 

### Using 'range' is a common way. While 'enumerate' will provide a more elegent way as it returns both the index and the real value. 

#### use range to get the value

```
for i, num in enumerate(input_numbers):
        temp_num = int(num)
        if temp_num % 3 == 0 and temp_num % 5 == 0:
            input_numbers[i] = "BizzBuzz"
        else:
            if temp_num % 3 == 0:
                input_numbers[i] = 'Bizz'
            else: 
                if temp_num % 5 == 0:
                    input_numbers[i] = 'Buzz'
```

#### use enumerate to get both the index and the value
```
for i in range(len(input_numbers)):
        temp_num = int (input_numbers[i])
        
        if temp_num % 3 == 0 and temp_num % 5 == 0:
            input_numbers[i] = "BizzBuzz"
        else:
            if temp_num % 3 == 0:
                input_numbers[i] = 'Bizz'
            else: 
                if temp_num % 5 == 0:
                    input_numbers[i] = 'Buzz'
```
