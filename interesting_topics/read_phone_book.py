file_name = '/Users/hong/Desktop/phonebook.txt'
csv_file_name = '/Users/hong/Desktop/test.csv'

#read normal txt file
def read_file(input_file_name):
    with open(input_file_name) as file_object:
        phone_book_list = file_object.readlines()
    return phone_book_list

#read csv file
import csv
def read_csv_file(input_csv_file_name):
    with open(input_csv_file_name) as csv_file:
        rows = csv.reader(csv_file)
        for row in rows:
            print(row)
    
'''
def read_phone_book(input_file_name):
    phone_book_lists = read_file(input_file_name)
    print (phone_book_lists)
    phone_book_dicts = {}
    phone_book_dict = {}
    for phone_book_list in phone_book_lists:
        name = []
        phone = []
'''    

#read_phone_book(file_name)
read_csv_file(csv_file_name)
