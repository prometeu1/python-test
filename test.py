def line(a):
    b = len(a) + 4
    c = "-" * b
    d = "|" 
    

    print(c)
    print(d,a,d) 
    print(c)

line("oteria")

def column(*args):
  for arg in args:
    b = len(arg) + 4
    c = "-" * b
    d = "|"

    print(c)
    print(d, arg, d)
    print(c)


column("hello", "world")
