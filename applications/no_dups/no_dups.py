def no_dups(s):
    cache = {}

    s_list = s.split()
    for word in s_list:
        cache.update({word: None})

    string = ""
    for word in cache:
        string += word + " "

    string = string.strip(" ")
    return string
    
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))