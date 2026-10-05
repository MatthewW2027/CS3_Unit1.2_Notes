# Lists - a data collection option that is ORDERED and MUTABLE 
    # we declare lists using []
def main():
    my_list = []
    my_other_list = list()

    #declare a list with items already in it 
    my_classes = ["BC Calc", "Post AP CS", "Physics C"]

    #using len() to find the length of the list
    print(len(my_classes))
    # we can index using the name of the list followed by [x]
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    #using a negative index always accesses from the right to left
    print(my_classes[-1])
    print(my_classes[-2])
    #using a 0 index always gives us our first element 
    print(my_classes[0])

    # we can update and replace items of our list with indeces 
    my_classes[1] = "AP CS"
    print(my_classes)

    # we can concatenate on to our list elements with +=
    my_classes[1] += " A"
    print(my_classes)

    print(len(my_classes) >= 4)

if __name__ == "__main__":
    main()
