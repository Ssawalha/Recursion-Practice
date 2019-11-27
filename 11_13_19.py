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
    def __init__(self, num, next = None):
        self.num = num
        self.next = next

    def len(self): # using loops
        count = 0 #<-- WRONG! should be 1 because if we have a list with 1 element the code will return 0 which is wrong
        while self.next != None:
            count += 1
            self = self.next
        return count

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        elif self.num != other.num:
            return False
        else:
            return self.next == other.next

    def recursivelen(self): #using recursion, find len(self)
        if self.next == None: #<-- base case with 1 element in self
            return 1
        else: 
            return 1 + self.next.recursivelen() # <--recursive case with more than 1 element in self

    def Lmax(self): #<--recursive max function
        if self.next == None:
            return self.num
        else: 
            return max(self.num, self.next.Lmax())
    
    def Linsert(self, index, insertion): #<-- recursive insert function 
        #                       ^(what is being inserted)
        if index == 0:
            new_node = linkedlist(insertion)
            new_node.next = self
            self = new_node
            return self
        elif index == 1:
            new_node = linkedlist(insertion)
            new_node.next = self.next
            self.next = new_node
            return self
        else:
            self.next.Linsert(index - 1, insertion)

    # def lsearch(self, target): # returns index position ##WORKS BUT doesnt return -1 if not found
    #     if self.num == target and self.next == None:
    #         return 0
    #     elif self.num == target and self.next != None:
    #         return 0
    #     elif self.num != target and self.next != None:
    #         return 1 + self.next.lsearch(target)

    def isTarget(self, target, index):
        if self.num != target and self.next == None:
            return -1
        elif self.num == target:
            return index
        else:
            return self.next.isTarget(target, index + 1)
    

    def lsearch(self, target): #returns index position if found / -1 if not 
        return self.isTarget(target, 0)
        

    def lmodify(self, target, modification): # return new list 
        if self.num == target and self.next == None:
            self.num = modification
            # return 0
        elif self.num == target and self.next != None:
            self.num = modification
            # return 0
        elif self.num != target and self.next != None:
            # return 1 + self.next.lmodify(target, modification)
            self.next.lmodify(target, modification)

    def ldelete(self, target): # return self is wrong??
        if self.num == target and self.next == None:
            self = None
        elif self.num != target and self.next == None:
            pass
        elif self.next.num == target:
            self.next = self.next.next
        else:
            self.next.ldelete(target)

    def traverse(self):
        pass # return list in string format '[0, 1, 2, 5]'

    def add_to_end(self, addition):
        pass # append linkedlist to end  

# lst = linkedlist(1, linkedlist(2, linkedlist(0, None)))
# lst2 = linkedlist(1, linkedlist(2, linkedlist(3, None)))
lst3 = linkedlist(2, None)
lst2 = linkedlist(2, linkedlist(1, None))
# lst2.Linsert(1, 2)
lst2.ldelete(1)

print(lst2 == lst3)

# print(lst2.Lmax())
# print(lst2.recursivelen())
# print(lst2.lsearch(-5))