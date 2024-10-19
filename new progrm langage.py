word = (
    "print('arthur是傻子')//一个打印'arthur是傻子'的语句",
    "print('小僵也是傻子')//一个打印'小僵也是傻子'的语句"
)
comment = {"print('arthur是傻子')":"一个打印'arthur是傻子'的语句","print('小僵也是傻子')":"一个打印'小僵也是傻子'的语句"}
set1 = "//"  
set2 = "/#/"  
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
