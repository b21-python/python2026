### Conditions

For your program to make decisions you can use logical conditions.  

```python
a = 42
b = 64
if a < b:
  print ("a is smaller than b")
else:
  print ("a is greater than or equal to b")
```

We have introduced two concepts here, logical conditions and the if/else statement.  Modify the code so  the text in the else condition is printed.

> NOTE: Python requires that you get indentation correct.  Try removing the spaces before either print and see what happens when you run the code.


### Loops

Loops allow you to repeat something multiple times without writing it out multiple times.  It also lets you repeat something any number of times based on a variable.

Write the code to print the word `banana` 3 times, once on each line like this:

```
banana
banana
banana
```

This could be done by calling print three times:

```python
print("banana")
print("banana")
print("banana")
```

Or it could be done with a loop:

```python
i = 0
while i < 3:
  print("banana")
  i = i + 1
```

Modify the loop to print out banana 11 times.


### Functions

You have already used a function without knowing it, `print`!  A function is a named block of code that is only run when it is called.  Like `print` it can take input (parameters) and return output.  You can use functions that someone else wrote, like `print` or you can write your own.  For now we will just stick to using existing functions.

Functions are often grouped together into libraries that you can use.  Pygame is a library, another common library is `math`.  To use a library you must import it.

```python
import math
x = math.pi
print(x)
```

We just printed Pi on a Raspberry Pi!

### Lists

Lists, also known as arrays store a number of values.  You can add and remove values from the list.

```python
numbers = [1,5,3,89,1000, "banana"]
print(numbers)

number.append(42)
print(numbers)

number.pop(0)
print(numbers)
```

#### Looping over lists

```python
for number in numbers:
  print(number)
```

Create a list and a loop that says something funny.

### Dictionaries

Dictionaries, also know as maps store key/value pairs.  You can quickly find any value using it's key.

```python
# Create dictionary representing a person
person = {"Name":"Joe", "Age":42, "Address":{"Street":"801 Market", "City":"Philly", "Zip":19102, "State": "PA"}}
print(person)

# Print out just the persons name
print(person["Name"])

# Change the persons name
person["Name"] = "Jane"
print(person)

# Add a last name
person["LastName"]= "Doe"
print(person)
```