def main():
    originalString = input("Input: ")
    twttr(originalString)


def twttr(x):
    list=[]
    for letter in x:
        list.pop(letter, None)
        list[letter] = 1
    print("Output: ", list)
    
    
    
if __name__ == "__main__":
    main()