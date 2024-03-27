def  meow(n: int)-> str:
    """Meow n times.
    :param n: Number of times to meow
    :type n:int
    :raise TypeError:
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n
    #for _ in range(n):
    #    print("meow")


numer: int = int(input("How many times do you want me to meow? "))
meows:str = meow(numer)
print(meows)