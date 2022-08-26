def order(sentence):
    words = sorted({c:word for word in sentence.split() for c in word if c.isdigit()}.items(), key=lambda item : item[0])
    print(words)
    #return ' '.join([i[1] for i in words])
    
    

print(order("is2 Thi1s T4est 3a"))