# 2 types of programming interview questions 
# Theoreritcal Questions
# Programming Questions (Typical types of questions: Data Structures | Recursion | Efficiency)
# 

# Programming Quesitions - Data Structures
# Lists | Trees | Graphs | Hashtables (dictionaires in python, key:value) 
# ^ Typical questions asked for each these data structures involve: insert | modify | search | delete

# Recursion: 
# Base Case - Recursive Case
# Base Case at n = 0 (how do you solve for 1 piece of data)
# Recursive case, how do you solve for more than 1 piece of data

# Formal definition of a list: A list is either empty ( [] ) or it is list.append(num)

# so if we had a list l = [1,2,3]

# and we know a list is defined as either [] or as list.append(num)

# so if we were to describe the list L in a recursive manner:
# we could say M = (([].append(1)).append(2)).append(3)


# Any data structure is a class. 

# definition of a linkedlist:

# class linkedlist: <-- base case (1 value in element (next num is None))
#     def __init__(self, num):
#         self.num = num
#         self.next = None

# given the definition of the linkedlist class
# myL = linkedlist(5)

# the myL will point to 5 for myL.num and None for myL.next

# given the definition of the linkedlist class

# myL = linkedlist(3, None)

# the myL will point to 5 for myL.num and None for myL.next

# so to get L using linkedlist class:

# myL = linkedlist(1, linkedlist(2, linkedlist(3, None)))

# if we change the definition to:
class linkedlist: #<-- base case always depends on definition of function (can be 0 or 1 or whatever function says (cant be broken down further))
    def __init__(self, num, next):
        self.num = num
        self.next = next

    def len(self): # using loops
        count = 0 #<-- WRONG! should be 1 because if we have a list with 1 element the code will return 0 which is wrong
        while self.next != None:
            count += 1
            self = self.next
        return count

    # def __eq__(self, other):
    #     while self != None or other != None:
    #         if self.num != other.num:
    #             return False
    #         self = self.next
    #         other = other.next
    #     return True if self == None and other == None else False

    def recursivelen(self): #using recursion, find len(self)
        if self.next == None: #<-- base case with 1 element in self
            return 1
        else: 
            return 1 + len(self.next) # <--recursive case with more than 1 element in self

    def Lmax(self): #<--recursive max function
        if self.next == None:
            return self.num
        else: 
            return max(self.num, self.next.Lmax())
    
    def Linsert(self, insertion): #<-- recursive insert function 
        #                ^(what is being inserted)
        if self.next == None:
            self.next = linkedlist(insertion, None)
            return self
        else:
            return self.next.Linsert(insertion)

    def lsearch(self, target): # returns index position
        if self.num == target and self.next == None:
            return 0
        elif self.num == target and self.next != None:
            return 0
        elif self.num != target and self.next != None:
            return 1 + self.next.lsearch(target)

    def lmodify(self, target, modification): 
        if self.num == target and self.next == None:
            self.num = modification
            # return 0
        elif self.num == target and self.next != None:
            self.num = modification
            # return 0
        elif self.num != target and self.next != None:
            # return 1 + self.next.lmodify(target, modification)
            self.next.lmodify(target, modification)

    def ldelete(self, target):
        if self.num == target and self.next == None:
            self.num = None 
            # self.next = ????
        elif self.num == target and self.next != None:
            self.num = None
            # return 0
        elif self.num != target and self.next != None:
            self.next.ldelete(target)

lst = linkedlist(1, linkedlist(9, linkedlist(2, linkedlist(10, linkedlist(5, None)))))
otherlst = linkedlist(1, linkedlist(9, linkedlist(2, linkedlist(10, linkedlist(5, None)))))

if otherlst == lst:
    print('true')
else:
    print('false')
