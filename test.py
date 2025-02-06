def longest_word(*args):
    return max(*args, key=len)

def column(*args):
    e = longest_word(*args)
    e = len(e) + 2
    for arg in args:
        
        c = "-" * e
        d = "|" 
        
        
        print(c)
        print(d + arg + d)
    print(c)




column("a          ", "small      ", "schrumberry")
