def enumerate_bizz_buzz():
    input_numbers = input("please input a list of integers divided by blank: ").split()
    # to change the string input to int
    int_numbers = [int(num) for num in input_numbers]
    for i, num in enumerate(int_numbers):
        if num % 3 == 0 and num % 5 == 0:
            int_numbers[i] = "BizzBuzz"
        else:
            if num % 3 == 0:
                input_numbers[i] = 'Bizz'
            else: 
                if num % 5 == 0:
                    input_numbers[i] = 'Buzz'
    print (int_numbers)

enumerate_bizz_buzz()

def range_bizz_buzz():
    input_numbers = input("please input a list of integers divided by blank: ").split()
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
    print (input_numbers)
#range_bizz_buzz()
