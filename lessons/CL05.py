"""comparing list and strings"""
a:str = "24"
b:str = a
a += "6"
print(b)
print(a)

a : list[int] = [2,4]
b : list[int] = a
a.append(6)
print(b)

'''list + Functions'''
def remove_first(xs:list[int]):
    xs.pop(0)

course: list[str] = ["comp","110"]
remove_first(course)
print(course)

"""list + functions"""
def dup(xs: list[int]):
    start_len: int = len(xs)
    i: int = 0
    while i <= start_len -1: