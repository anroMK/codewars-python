import re

# def domain_name(url):
#     pat = re.compile(r'(https?)?(://)?(www.)?(.+?)\.')
#     return pat.search(url).group(4)

def domain_name(url):
    pat = re.compile(r'(https?://)?(www.)?(.+?)\.')
    return pat.search(url).group(3)



print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))