

#importing -importing is important
import sys #system functions and parameters
from datetime import datetime as dt     #using an alias


#Strings
print("Hello, World!")
print('Hello, World!')
print("""this is a
      Tripple Quote""") #comments anywhere this is multiple lines
print("this is a "+" conncatennation") #conncatennate, remember to have space and quotes
print('\n') #creates a space, new line
print("test new line")
print('\n')

#math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #division float
print(50 // 50) #division without remainder
print(50 - 50 + 50 /50 * 50)
print(50 ** 2) #to the power
print('\n')

#variables and methods

age = 29 #integer
name = "Balal" #string
gpa = 2.3 #float

print(age)
print(name)
print(gpa)
print(int(age))
print(int(gpa)) #adding the int gets rid of float .3
print(int(29.6)) #rid of float again

quote = "All is fair in love and war"
print(quote)
print("My name is "+name+" and I am "+str(age)+" years old")
age += 1
print(age)
birthday = 1
age += birthday
print(age)

print('\n')

#user input

#x= float(input("Give me a number: "))
#y = float(input("Give me another number: "))
#print(x + y)

print('\n')

#functions - Reusable block of code like a program make it do something

def whoami():
    age = 29
    name = "Balal"
    print(f"My name is {name} and I am {age} years old.")
whoami()

def who_am_i(age,name):
    print(f"my name is {name} and I am {age} years old.")
who_am_i(30,"Bill")

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(200)
def add(x,y):
    print(x + y)

add(1,2)

def subtract(x,y):
    print(x - y)
subtract(7,7)

def multiply(x,y):
    print(x * y)
multiply(7,6)

def divide(x,y):
    print(x / y)
divide(64,8)

def multi(x,y):
    return x * y
print(multi(7,8))
result = multi(8,8)
print(result)

def square_root(x):
    print(x ** .5)
square_root(99)

def nl():    #new line 
    print('\n')
nl()

bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)

print(type(bool1))
print(type(bool3))

bool5 = "True"
print(bool5)
print(type(bool5))



nl()

less_than = 5 < 7
greater_than = 7 > 5
less_than_equal_to = 7 <= 7
greater_than_equal_to = 7 > 7
equals = 7==7
not_equals = 7 != 8
nl()

test_and = (7 > 5) and (5 < 7) #True AND
test_and1 = (7 > 5) and (5 > 7) #False AND
test_or = (7 > 5) or (5 < 7) #True
test_or1 = (7 > 5) or (5 > 7) #True only 1 has to be true for OR
test_not = not True #False

def drink(money):
    if (money >= 5):
        return "Have a drink"
    else:
        return "No drink for you"
print(drink(4))
print(drink(5))

def alcohol(money,age):
    if (money >= 5) and (age >= 21):
        return "Heres your drink mate"
    elif (money >= 5) and (age < 21):
        return "You are too young. No drink for you."
    elif (money < 5) and (age >= 21):
        return "You dont have enough money bro"
    else:
        return "You are not old enough and you dont have enough money either"

print(alcohol(5,21))
print(alcohol(4,21))
print(alcohol(3,19))
     
nl()
# for loops -start to finish of an iterate

vegetables = ["cucumber" , "spinach", "cabbage"]
for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)
   
meat = ["beef" , "chicken"]
for carnivore in meat:
    print(carnivore)

saiyan = "goku"
for saiyan in "goku":
    print(saiyan)

nl()

# while loops - execute as long as true

l = 1
while l < 10:
    print(l)
    l += 1

#password = ""
#while password != "spaghetti":
 #   password = input("Enter the password: ")

#print("Access Granted")

nl()
#building a calculator

#x = float(input("Give me a number: "))
#o = input("Give me an operator: ")
#y = float(input("Give me another number: "))

#if o == "+":
#    print(x + y)
#elif o == "-":
#    print(x - y)
#elif o == ("*"):
#    print(x * y)
#elif o == "/":
#    print(x / y)
#elif o == ("**"):
#    print(x ** y)
#else:
#    print("Unknown Operator")

#lists
movies = ["Avengers", "Terminator", "Friday", "Batman"]
print(movies)
print(len(movies))
print(movies[1]) #return second item in list
print(movies[-1]) #return last item
print(movies[0:])
print(movies[:2])
print(movies[0:2]) #will rlist all from first up until 2(before friday)
movies.append('Snow White') #adds to end of list
movies.insert(1, "James Bond")
print(movies)
movies.pop()
print(movies)
movies.pop(1)
print(movies)

Hina_movies = ["romance", "doo", "jane", "dog"]
our_movies = (movies + Hina_movies)
print(our_movies)

nl()
Grades = [["Bob", 80], ["Alice", 90], ["John", 60]]
Alice_Grade = Grades[1][1]
print(Alice_Grade)

#Dictionaries -key/value pairs {}
drinks = {"pepper": 5, "sprite": 3, "coke": 2}
print(drinks)
print(len(drinks))
employees = {"Finances": ["Bob", "lisa", "Josh"], "IT": ["Bil", "HB", "Wade"], "HR": ["Shelley"], "Managers": ["Martin"]}
print(employees)
employees["Legal"] = ["Shizam"] #adds new key val pair
print(employees)
employees.update({"Sales": ["Oliver", "Alice"]})
print(employees)
drinks["pepper"] = 6
print(drinks)
print(drinks.get("coke"))
nl()

#Advanced Strings

my_name ="Balal"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence)
print(sentence[2:])
print(sentence[0:])

nl()

print(sentence.split()) #delimeter -default is space
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'Give me all your money'"
quote = "He said,\"Give me all your money\""
print(quote)

too_much_spaces = "                      hi        "
print(too_much_spaces.strip())      #removes spaces
print("A" in "Apple")
print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

#user_input = input("Enter yes or no: ")
#if user_input.lower().strip() == "yes": #.lower() allows lower and upper .strip() allows space in your answer
 #   print("you agree!")
#else:
#    print("you disagree")

nl()

movie = "Mario"
print(f"My favorite movie is {movie}")


    
print(sys.version)
print(dt.now())