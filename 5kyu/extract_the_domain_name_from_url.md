# Extract the domain name from a URL

## Problem:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

[codewars](https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python)

### Examples:
```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```

### Given code
```python
def domain_name(url):
    pass
```

## Solution
```python
import re

def domain_name(url):
    pat = re.compile(r'(https?://)?(www.)?(.+?)\.')
    return pat.search(url).group(3)
```

## Test
```python
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
```