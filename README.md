## Upskilling in Advanced Python
This markdown file serves to summarise and finalise the understanding of
the concepts I've gained in this course. Next steps after finishing this, will be completing challenges utilising
these concepts.

### Current Progress
- [x] 1 - Language
- [ ] 2 - Builtin Functions
- [ ] 3 - Functions
- [ ] 4 - Collections
- [ ] 5 - Classes
- [ ] 6 - Logging
- [ ] 7 - Comprehensions
___
##Contents 
1. [Theory](#theory)
2. [Python Concepts and When To Use Them](#python-concepts-and-when-to-use-them)

___

### Theory
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
### Python Concepts and When To Use Them


<table>
<tr>
<td> Name </td> <td> Description </td> <td> When to Use It </td> <td> Code Example </td>
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

[comment]: <> (<tr>)

[comment]: <> (<td> Next </td>)

[comment]: <> (<td>)

[comment]: <> (Next)

[comment]: <> (</td>)

[comment]: <> (</tr>)

[comment]: <> (</table>)


