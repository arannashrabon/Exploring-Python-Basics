'''Task 1: Variable Manipulation'''
def Task_1_Variable_Manipulation():
    name = "Aranna Shrabon"
    age = 25
    print ("My name is" + ' ' + name + " and I am" + ' ' + str(age) + " years old.")

'''Task 2: Data Types and Type Conversion'''
def Task_2_Data_Types_and_Type_Conversion():
    num1 = 64
    num2 = 98.7
    num1_float = float(num1)
    num2_int = int(num2)
    print("num1:", num1, "Type:", type(num1))
    print("num2:", num2, "Type:", type(num2))
    print("num1_float:", num1_float, "Type:", type(num1_float))
    print("num2_int:", num2_int, "Type:", type(num2_int))

'''Task 3: String Manipulation'''
def Task_3_String_Manipulation():
    string_variable_sentence = "Python programming is fun!"
    print("Length of the string:", len(string_variable_sentence))
    print("8th character:", string_variable_sentence[7])
    substring = string_variable_sentence[0:6]
    new_sentence = substring + " I enjoy it!"
    print("The result is:", new_sentence)

'''Task 4: Lists and List Manipulation'''
def Task_4_Lists_and_List_Manipulation():
    fruits = ["apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print("Length of the list:", len(fruits))
    sliced_fruits = fruits[1:3]
    extra_fruits = ["kiwi", "lemon"]
    combined_fruits = sliced_fruits + extra_fruits
    print("Combined list of the fruits:", combined_fruits)

'''Task 5: Conditional Statements'''
def Task_5_Conditional_Statements():
    num = 2023
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

'''Task 6: Loops'''
def Task_6_Loops():
    print("Numbers from 1 to 10 are: ")
    for num in range(1, 11):
        print(num)
    sumofnumbers = 0
    for num in range(1, 101):
        sumofnumbers += num
    print("Sum of numbers from 1 to 100: ", sumofnumbers)

'''Task 7: Functions'''
def Task_7_Functions():
    def calculate_square(num):
        return num * num

    def is_prime(num):
        flag = False
        for n in range(2,num):
            if num % n == 0:
                flag = True
                break;
        return flag
    print(calculate_square(7))
    print(is_prime(29))

'''Task 8: Dictionaries'''
def Task_8_Dictionaries():
    student = {
        "name": "Sakib Al Hasan",
        "age": 34,
        "grade": "A+"
    }
    student["course"] = "Discrete Mathematics"
    print("Keys in the dictionary:", list(student.keys()))
    print("Key-value pairs:")
    for key, value in student.items():
        print(key, ":", value)