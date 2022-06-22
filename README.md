## Upskilling in Advanced Python
This markdown file serves to summarise and finalise the understanding of
the concepts I've gained in this course. Next steps after finishing this, will be completing challenges utilising
these concepts.

### Outstanding Question
> What actually is the benefit of using a lambda function over a comprehension?
___
## Contents 
1. [Theory](#theory-)
2. [Best Practice](#best-practice-)
3. [Python Concepts and When To Use Them](#python-concepts-and-when-to-use-them-)
___

### Theory 📖
#### Truth Values
Python objects majorly evaluate to True.

But this is where they evaluate to False:
- If any collection is empty, e.g.: strings, lists, tuples, dictionaries and sets
  - e.g. `if not word` can evaluate to False where `word` is a string variable.
  - > N.B This logic differs to other languages such as JS where empty collections evaluate to True
- Any number literal that equals 0
  - 0
  - 0.0
  - 0j (Complex/Imaginary Number)
  - 0/5
___
#### Predicate Functions
A function is a predicate function if it returns a Boolean value. This means a predicate function can be used to filter 
and act as a conditional function.
___
#### Anonymous Functions
A function is an anonymous function if it was declared without an identifier. Therefore an anonymous function is not usable after it is created/used.
___
#### Arguments
```python
# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions) 

# define a function that takes in a variable number of arguments
def addition(*args):
    return sum(args)
```
___
#### Python list comprehension vs lambda
Let us see the difference between Python list comprehension and lambda.

- List comprehension is used to create a list.
- Lambda function process is the same as other functions and returns the value of the list.
- List comprehension is more human-readable than the lambda function.
- User can easily understand where the list comprehension is used .
- List comprehension performance is better than lambda because filter() in lambda is slower than list comprehension.
___

### Best Practice 💯
#### Docstrings
- Docstrings always in triple quotes 
- First line should be summary sentence of functionality 
- For modules, list important classes, functions, exceptions 
- For classes, list important methods 
- For functions, list parameters and explains each, one per line 
- If there's a return value, then list it; otherwise omit 
- If the function raises exceptions, mention those


```python
"""
myFunction(arg1, arg2=None) --> Doesn't really do anything special.

Parameters:
arg1: the first argument. Whatever you feel like passing.
arg2: the second argument. Defaults to None. Whatever makes you happy.
"""
```



___
### Python Concepts and When To Use Them 📋


<table>
<tr>
<td> Name </td> <td> Description </td> 
<td> When to Use It </td> 
<td> Code Example </td>
</tr>

<tr>
<td> string.Template </td>
<td>Make your strings follow a template</td>
<td><b>When you don't have control over the input.</b><br>The Format method is not totally secure, this is better if security is a priority.</td>
<td>

```python
    from string import Template
    # create a template with placeholders
    templ = Template("You're watching ${title} by ${author}")
    
    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # use the substitute method with a dictionary
    data = { 
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)    
    print(str3)
```
</td>

<tr>
<td> Iterators </td>
<td> Make lists iterable</td>
<td>To be able to use iterator methods e.g. enumerate, next</td>
<td>

```python
     # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")
```
</td>

</tr>
<tr>
<td> Itertools </td>
<td> Do more things with iterables</td>
<td>More complex methods such as cycle, count, accumulate, and chain. <b>Chain is better performance for concatenating lists.</b></td>
<td>

```python
    import itertools

    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))
        
    # use chain to connect sequences together
    # Useful as concatenating a series of lists (e.g. a.extends(b)) has quadratic performance, this does not.
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
```
</td>

</tr>
<tr>
<td> map </td>
<td> Maps every value in an iterable to another using a function </td>
<td>Whenever you need to apply a function to each value.</td>
<td>

```python
  def squareFunc(x):
        return x**2
  
  nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
  # use map to create a new sequence of values
  squares = list(map(squareFunc, nums))
  print(squares)

  def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"
  
  grades = (81, 89, 94, 78, 61, 66, 99, 74)
  grades = sorted(grades)
  letters = list(map(toGrade, grades))
  print(letters)

```
</td>
</tr>
<tr>
<td>filter</td>
<td>Filtering out values based on a predicate function</td>
<td>When you only want to extract values from an iterable that fit conditions </td>
<td>

```python
 def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"

    # use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

```
</td>
</tr> 
<tr>
<td>any(), all() </td>
<td>any will return true if any of the sequence values are true, all will return true only if all values are true</td>
<td>In scenarios where these methods would be useful</td>
<td>

```python
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values are true
    print(any(list1))
    
    # all will return true only if all values are true
    print(all(list1))
```
</td>

</tr>
<tr>
<td>lambda functions </td>
<td>In-line anonymous function definitions</td>
<td> 
<ul>
<li>When the function is only used once </li>
<li>Function not extraordinarily complex </li>
<li>To reduce complexity and increase readbility </li>
</ul>
</td>
<td>

```python
def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsius(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

```
</td>
</tr>
<tr>
<td>Counter class </td>
<td>Subclass of dictionary that allows counting of hashable objects</td>
<td> 
If you need a class to help keep track of a number of different items along with a set of operations for working on the data or multiple sets of data, the counter class is ideal. Most common seems like a usef
</td>
<td>

```python
from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # How many students in class 1 named James?
    print(c1["James"])

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)
    # Performing a boolean AND operation. Aka outputting any values and their counts that are in both datasets.

```
</td>
</tr>
<tr>
<td> DefaultDict </td>
<td>Subclass of dictionary that creates keys aka no value can be without a key</td>
<td> 
If you don't care about what keys are, <b>Do not use if you need to know if you're missing a key.</b>
</td>
<td>

```python
from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    # Inside the bracket (int) you put in a factory method
    # This is how the default keys are chosen. This time using an integer
    # You can also define your own factory methods e.g. a lambda function
```
</td>
</tr>
<tr>
<td> Deque </td>
<td>Double ended queues designed to be memory efficient when accessing it from either end</td>
<td> 
If you need to be able to operate and work with data from both sides of a list. e.g.: restaurant waiting list/reservations
</td>
<td>

```python
def main():
    # initialise a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: {}".format(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()  # removes last element of the queue
    d.popleft()  # removes first element of the queue
    d.append(2)  # adds X to the back of the queue
    d.appendleft(1)  # adds X to the front of the queue
    print(d)

    # rotate the deque
    print(d)
    d.rotate()  # positive numbers rotate X numbers to right, negative X numbers to left -> default = 1
    print(d)
```
</td>
</tr>
<tr>
<td> namedtuple </td>
<td>Tuples that are defined with parameters, allowing more readable access (instead of accessing by index)</td>
<td> 
When it is a simple data structure and defining a class would be too much work.
<b>Do not use if you do not have default values, so if the data has large number of optional properties, better to use a class</b>
</td>
<td>

```python

def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y z")

    p1 = Point(10, 20, 5)
    p2 = Point(30, 40, 0)

    print(p1, p2)
    print(p1.x, p1.y)

    # use _replace to create a new instance => replace always needs to be assigned to a new instance
    p1 = p1._replace(x=100)
    print(p1)
```
</td>
</tr>
<tr>
<td> ordereddict </td>
<td>The order of insertion into the dictionary is recorded</td>
<td> 
<ul>
<li>Functionality relies on the order of the dictionary</li>
<li>If you need to rearrange items in a dictionary then you can use .move_to_end() and also the enhanced variation of .popitem().</li>
<li>If your code compares equality, and the order of items is important, then OrderedDict is the right choice.</li>
</ul>
</td>
<td>

```python
  from collections import OrderedDict
  
  
  def main():
      # list of sport teams with wins and losses
      sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                  ("Jets", (16, 14)), ("Warriors", (25, 5))]
  
      # sort the teams by number of wins
      sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
  
      # create an ordered dictionary of the teams
      teams = OrderedDict(sortedTeams)
      print(teams)
  
      # Use popitem to remove the top item
      tm, wl = teams.popitem(False)
      print("Top team: ", tm, wl)
```
</td>
</tr>
<tr>
<td> Object Comparison Operators </td>
<td>Use special methods to compare objects to each other</td>
<td>
<ul>
<li> If your class object needs comparison operations you can override the inbuilt operations to be compatible </li>
<li> By doing this we establish an order in our object instances</li>
<li> This means when we use sort methods, it utilises the overridden comparators.</li>
</ul>


</td>
<td>

```python
      def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level
```
</td>
</tr>
<tr>
<td>  __getattr__ </td>
<td> Customise string representations of objects</td>
<td> 
Extend the features that your class supports and provide a way to reuse existing attributes in new ways
</td>
<td>

```python
  def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)
```
</td>
</tr>
<tr>
<td>  enum </td>
<td> Data type consisting of a set of named values. The enumerator names are identifiers that behave as constants.</td>
<td> 
Easy to understand and maintain. Constant values, not mutable like with namedtuples.
</td>
<td>

```python
from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    # NAME = VALUE
    # can access this using Class.NAME.name -> to get 'NAME'
    # and Class.Name.value -> to get 'VALUE'
    # Duplicate names are not okay, duplicate values are
    # You can prevent duplicate values by importing the 'unique' decorator and adding it to the class
    # If you don't care about the values you can import the auto package from enum which will automatically create one
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))  # gets a string representation of the object

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)  # Value is 5 which increments from the other values
       
```
</td>
</tr>
<tr>
<td> Numerical Operators </td>
<td>Use special methods to give objects number-like behaviour</td>
<td> 
If your class object needs numeric operations you can override mathematical operations to be compatible
</td>
<td>

```python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # Add two points
    p3 = p1 + p2
    print(p3)

    # subtract two points
    p4 = p2 - p1
    print(p4)
```
</td>
</tr>
<tr>
<td> Logging </td>
<td>Log problems or statements</td>
<td> 
...If you need logging
</td>
<td>

```python
# use the built-in logging module
import logging


def main():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    logging.basicConfig(level=logging.DEBUG,
                        filemode="w",
                        filename="output.log")

    # Try out each of the log levels
    logging.debug("This is a debug-level log message")  # Diagnostic information useful for debugging
    logging.info("This is an info-level log message")  # General info about execution results
    logging.warning("This is a warning-level message")  # Something unexpected, or an approaching problem
    logging.error("This is an error-level message")  # Unable to perform a specific operation due to a problem
    logging.critical("This is a critical-level message")  # Program may not be able to continue, serious error

#### CUSTOMISED LOGGING
import logging

extData = {'user': 'joem@example.com'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    # asctime - Human readable date format when the log record was created
    # filename/functioname - file/function where the log message originated
    # levelname/levelno - String/Numeric representation of the message level (DEBUG, INFO etc.)
    # lineno - Source line number where the logging call was issued (if applicable)
    # message - The logged message string itself
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    # extData string passed in through below method to access data through the keys
    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()
```
</td>
</tr>
<tr>
<td> Comprehensions </td>
<td> A way to concisely apply a predicate function to an iterable</td>
<td> 
N/A
</td>
<td>

```python
## List comprehension
oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]

## Dictionary comprehension
# below 't: t*9/5' is creating a key value pair
tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}

## Set comprehension
sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp if not c.isspace()}
```
</td>
</tr>
</table>





