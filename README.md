## Upskilling in Advanced Python
This markdown file serves to summarise and finalise the understanding of
the concepts I've gained in this course. Next steps after finishing this, will be completing challenges utilising
these concepts.

### Current Progress
- [x] 1 - Language
- [x] 2 - Builtin Functions
- [x] 3 - Functions
- [ ] 4 - Collections
- [ ] 5 - Classes
- [ ] 6 - Logging
- [ ] 7 - Comprehensions
___
## Contents 
1. [Theory](#theory-)
2. [Best Practice](#best-practice-)
3. [Python Concepts and When To Use Them](#python-concepts-and-when-to-use-them)

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





