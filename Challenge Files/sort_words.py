def sort_words(string):
    original = string.split()
    words = string.lower().split()
    words.sort()
    result = ""
    for word in words:
        for format in original:
            if format.lower() == word:
                word = format
                result += word + " "
    return result


print(sort_words("giraffe xylophone ELEPHANT Apple ant"))


## EXAMPLE SOLUTION
def sort_words(string):
    return ' '.join(sorted(string.split(), key=str.casefold))

## Syntax
# sorted(iterable, key=key, reverse=reverse)

## Parameter Values
# Parameter	Description
# iterable	Required. The sequence to sort, list, dictionary, tuple etc.
# key - Optional. A Function to execute to decide the order. Default is None
