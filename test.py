class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node
    
    def set_value(self):
        return self.value
    
    def set_next_ndoe(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head_node = None):
        self.head_node = head_node

    def insert_beginning(self, new_value):

        new_node = Node(new_value)

        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value):
        new_node = Node(new_value)

        # check if list is empty

        if self.head_node.get_value is None:
            self.head_node.set_next_node(new_node)

        current = self.head_node
        while current.get_next_node() is not None:
            current = current.get_next_node()

        current.set_next_node(new_node)

        if self.py() 

    def remove(self, new_value):
        new_node = Node(new_value)

        


    

    























#03/31 -----------------------------------------

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node= next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)

        new_node.set_next_node(self.head_node)

        self.head_node = new_node

    
    def insert_end(self, new_value):
        new_node = Node(new_value)

        if self.head_node is None:
            self.head_node = new_node
            return
        
        current = self.head_node
        while current.get_next_node() is not None:
            current = current.get_next_node()

        current.set_next_node(new_node)
            
        return
    
    def remove(self, value):
        if self.head_node is None:
            return
        
        if self.head_node.get_value() == value:
            self.head_node = self.head_node.get_next_node()
            return
        
        current = self.head_node
        while current.get_next_node() is not None:
            if current.get_next_node().get_value() == value:
                current.set_next_node(current.get_next_node().get_next_node())
                return
            current = current.get_next_node()



















# 03/28 --------------------------

def pattern(size):
    for i in range(1, size+1):
        for i in range(1, i+1):
            print(i, end=" ")
        print('\n')

# pattern(5)


# Time Complpexity: O(n)
def cal(num):
    s = 0
    l = []
    for i in range(1, num + 1):
        l.append(i)
    s = sum(l)
    return s
# print(cal(10))


# Time Complpexity: O(1)
def cal(num):
    print (int((num*(num+1)) // 2))

# cal(10)


def cnt(num):
    print (len(list(str(num))))

#cnt(75869)


def pattern(size):
    for i in range(size, 0, -1):
        for i in range(i, 0, -1):
            print(i, end=" ")
        print("\n")

# pattern(5)

    
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

def make_list(l1, l2):
    new_l = []
    for i, j in zip(l1, l2):
        if(i % 2 != 0):
            new_l.append(i)
            
        if(j % 2 == 0):
            new_l.append(j)
            
    return new_l
        

# print(make_list(list1, list2))


sorted_list = [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9]
target = 9

def insert(l, target):
    for i in range(len(l)):
        if l[i] >= target:
            return i




sorted_list = [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9]
target = 9

def insert(l, target):
    for i in range(len(l)):
        if l[i] > target:
            return i
        
    return len(l)

# print(insert(sorted_list, target))


from collections import deque

# Example queue initialization
my_queue = deque([0, 1, 2, 3])

# Function definition stub
def display_queue(queue):

    if not queue:
        print(True)
        
    print("Members: ")
    for i in queue:
        print(i, end=" ")

    print("Length: ", end="\n")
    print(len(my_queue))


display_queue(my_queue)


from collections import deque

# Starter FIFO queue
fifo_queue = deque()

# Function stub
def create_fifo_queue():




            



# 03/26 --------------------------

num1 = 200
num2 = 10

def product (x, y):
    if (x*y) <= 1000: 
        return (x*y)
    else:
        return (x+y)


#print (product(num1, num2))


def iterate (r):
    print("Printing current and previous number sum in a range({range})")
    for i in range(r):
        print("Current number", i + 1, "Previous number", i, "Sum: ", (i+1)+i)

#iterate(11)


def even(string):

    s = len(string)

    for i in range(0, s, 2):
        print(string[i], end=" ")  

    # for i in string:
    #     if (string.index(i) % 2) == 0:
    #         print (i)
    #     else:
    #         continue


# even("manikanta")


# m n k n a



def remove_char(s, x):

    if x > len(s):
        return 
    else:
        return (s[x:])

# remove_char("PYnative", 4)


def same(l):
    if l[0] == l[len(l) - 1]:
        print(True)
    else: 
        print(False)
    
# list = [10, 20, 30, 40, 10]
    
# same(list)


def div_five(l):
    for i in list:
        if (i % 5) == 0:
            print(i)
        else:
            continue


# list = [10, 20, 33, 27, 40, 43, 50, 35, 15.6]

# div_five(list)


def sub(s, p):

    s_l = s.lower()

    p_l = p.lower()

    index = 0
    cnt = 0 

    while index < len(s_l):
        position = s_l.find(p_l, index)

        if position != -1:
            cnt += 1
            index = position + len(p_l)
        else:
            break

    return cnt


my_string = "Kobe when to the park. Kobe went poop in the park. Kobe played with all his friends in the grass at the park. "
part = "Park"
# print(sub(my_string, part))




def patter(val):
    for i in range(val):
        for j in range(i):
            print(i, end=" ")
        print('\n')

v = 5

# patter(v)


def palindrome(x):
        y = int(str(x)[::-1])
        if x == y:
            print (True)
        else :
            print (False)

num = 121
# palindrome(num)




def merge(l1, l2):
    new_l = []


    for i in list1:
        if (i%2 != 0 ):
            new_l.append(i)
        
    for j in list2:
        if(j%2 == 0):
            new_l.append(j)

    return(new_l)



list1 = [5, 10, 15, 20, 30, 25, 40]
list2 = [30, 35, 45, 15, 50, 55, 70]

# print(merge(list1, list2))



def rev_order(n):
    new_n = int(str(n)[::-1])

    while n > 0:
        dig = n % 10
        n = n // 10
        print(dig, end=" ")

num = 1456748
# rev_order(num)




# income = int(input("Enter Income: "))

def tax(income):
    if income > 20000:
        first = 10000*0
        next = 10000*0.1
        remaining = (income - 20000) * 0.2
        tax = first + next + remaining

    return int(tax)
# print("Tax to pay: ", tax(income))




def mult_table(size):

    for i in range(1,size + 1):
        print(i, end=" ")
        for j in range(1, size + 1):
            print(i*j, end=" ")
        print("\n")
        

# mult_table(10)

    
# input = int(input("Drawing Size: "))
def star(size):

    while size > 0:
        print((size * "* "), end="\n")
        size -= 1

# star(5)



def exponent(base, expo):

    if expo > 0:
        fnl = base**expo    
    elif expo < 0:
        fnl = float((1/(base**(-expo))))
    elif expo == 0:
        fnl = 1
    elif base < 0:
        fnl 
        
    print(fnl)

# exponent(5, 0)



# 03/25 --------------------------

# s = 'banana'
# index = 0

# while index < len(s):
#     l = s[index]
#     print(index, l)
#     index += 1


# print("\nfor loop\n")


# for l in s:
#     print(l)

# print("\nhow many A n string\n")


# n = "Manikantanagasai Harshit Illuri"

# cnt = 0

# for letter in n:
#     if letter == "a":
#         cnt += 1

# print (cnt) 



