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

    print(my_classes.index("BC Calc"))
    # if the item is not present, it breaks our code 
    # print(my_classes.index("Journalism"))

    # item in list --- returns a boolean 
    print("Bc Calc" in my_classes)
    print("journalism" in my_classes)

    # adding a list element on to the end of our list, use append()
    my_classes.append("Journalism")
    print(my_classes)

    # add items to a list in a specific spot with .insert(index, item)
    my_classes.insert(1, "biology")
    print(my_classes)
    print(my_classes.pop())
    print(my_classes)

    #we can sort our lists to rearrange them 
    print(my_classes.sort())
    print(my_classes)

    numList = [6, -4, 3, 9]
    numList.sort()
    print(numList)

    my_classes.sort(reverse=True)
    my_classes.sort(reverse=True)
    print(my_classes)
    print(numList)

    # make a copy of your list that is sorted with sorted()
    print(sorted(my_classes, reverse=True))
    sorted_classes = sorted(my_classes)
    print(sorted_classes)

    # reverse the list in place using .reverse()
    sorted_classes.reverse()
    print(sorted_classes)

    colors_a = ["blue", "green", "baby blue", "red"]
    colors_b = ["burgundy", "orange", "blue", "brown"]

    #colors_a = colors_a + colors_b
    colors_a.extend(colors_b)
    print(colors_a)

    print("orange" in colors_a)
    print("pink" in colors_a)

    print(colors_a.index("orange"))
    #print(colors_a.index("prink"))

    # get the frequency or count of an item in a list using listName.count(item)
    count = colors_a.count("blue")
    print(f"there are {count} blues!")

    #task - updating a list item from turqoise to green 
    colors_a[colors_a.index("green")] = "turqoise"
    print(colors_a)



if __name__ == "__main__":
    main()
