word = (
    "print('a')/#/一个打印'a'的语句",
    "print('b')/#/一个打印'b'的语句"
)
set2 = "///"  
set1 = "/#/"  
def f1(x, y, z):
    result = []
    for text in x:
        if y in text:
            ntext = text.split(y)[0] + z
            result.append(ntext.strip())  
    return "\n".join(result)  
#def f2(x, y, z):
#    for text in x:
#        if z in word:
#            ntext = text.replace(z, y + "一个打印'arthur是傻子'的语句")
#            return .append(ntext.strip())
result = f1(word, set1, set2)
print(result)
