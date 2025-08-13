#for inputting a list of integers
int_list = [int(n) for n in input("input some numbers separated by a spaces").split()]
print(int_list)

#for inputting a list of strings
str_list = input("give some characters separated by spaces").split()
print(str_list)

#for finding the length of a list
length = ["1", "2", "3", "4", "5", "6", "7"]
print(len(length))

#for finding the range of a list. first number is where to start (inclusive), if left blank it will go to start of list, 2nd number is where to stop (non-inclusive), if left blank it will go to end of list, and 3rd number is how much to count by (default is 1)
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "new car", "feet", "peach"]
print(smells[0::2])

#for finding the biggest number in the list
largest = max(4, 20, 40, -12409378, -100000000000, 15)
print(largest)

#for finding the smallest number in the list
smallest = min(1203471982572475, 999999999999999999999999999999999, 2358, -1000, 4, 20)
print(smallest)

#appends an item to a list
list_needing_more = ["this", "is", "a"]
list_needing_more.append("list.")
print(list_needing_more)

#combines 2 lists together, basically appending but for multiple items at once. If you only input 1 string, it splits the string up into individual characters and puts them in the list. ex: list.extend("cool") would become in the list ["whatever that was", "already in", "c", "o", "o", "l"]
list_needing_more_mor = ["this", "is"]
list_needing_more_mor.extend(["pretty", "cool", "list", "you", "got"])
print(list_needing_more_mor)

#inserts an item into a list at a specific point. first number is where it goes, the next thing is a string
insert = ["I", "Can", "Anything!"]
insert.insert(2, "Do")
print(insert)

#removes an item from the list. if multiple occurances of the string, it will take only the 1st one out
remove = ["important", "important", "useless", "important"]
remove.remove("useless")
print(remove)

#moves an item from a list
trashcan = ["trash", "plate", "social security card", "paper towels"]
wallet = trashcan.pop(2)
print(wallet)

#replaces an item in a list
replaces = ["whasgood", "asdklfj", "useless"]
replaces[2] = "bbg"
print(replaces)

#sorts a list by alphabetical order. can also be done with numbers. you can reverse sort by typing whatshappening.sort(reverse=True)
whatshappening = ["red 40", 'adrian', 'enrique', 'eeffoc', 'instagrammer', 'eepy', 'qwsqzkg']
whatshappening.sort()
print(whatshappening)
