def longest_word(*args):
    return max(*args, key=len)

def column(*args):
    e = longest_word(*args)
    e = len(e) + 2
    i = 0
    for arg in args:
        z =" "*(len(longest_word(*args)) - len(args[i]) ) 
        i += 1
        c = "-" * e
        d = "|" 

        
        
        print(c)
        print(d + arg + z + d)
    print(c)




column("a", "small", "schrumberry")
