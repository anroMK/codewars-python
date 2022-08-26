def printer_error(s):
    #errors = len([1 for i in s if i > 'm'])
    return f"{len([1 for i in s if i > 'm'])}/{len(s)}"

print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))