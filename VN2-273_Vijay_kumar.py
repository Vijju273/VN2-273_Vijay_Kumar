# Instructions:
# ---------------
# 	1. Use proper namaing conventions
# 	2. Use pep8 standards
# 	3. Write readable and clean code 
# 	4. Where ever required use functions,oops,exception hanlding etc.,
# 	5. Give detailed comments if required 
# 	6. Write all programs in one .py file 


import codecs


print("--------------Program 1-------------------")
print("----1. Implement palindrome using iterator(for loop) and generator mechanism----")
print(" ------- 1.a. Normal For Loop -------")

num = input("enter number :")
i = 0
for i in range(len(num)):
	if num[i]!=num[-1-i]:
		print("It is not a Palindrome")
		break
	else:
		print("It is a palindrome")
		break

print(" ------- 1.b. Generator mechanism ----")




print("--------------Program 2-------------------")
print("----2. Sum of 2 digits into output----")

n1 = input("Enter first number:")
n2 = input("Enter second number:")

n1 = list(n1)
n2 = list(n2)

Out = []
n = 0
for i in n1:
    res = int(i) + int(n2[n])
    Out.append(res)
    n += 1
    continue

print(f"Sum of two digit is: {sum(Out)}")

# Output: 9+1 2+9 3+9 4+9 
#  10 + 11 + 12 + 13
#  46

print("--------------Program 3-------------------")
print("----3.Reverse string considering only alphabets. Symobls should not be reversed-----")

st = "ab@#cd!ef"
print("Input string :",st)
list1=list(st)
 
i=0
j=len(list1)-1
 
while i<j:
    if not list1[i].isalpha():
        i+=1
    elif not list1[j].isalpha():
        j-=1
    else:
        list1[i], list1[j]=list1[j], list1[i]
        i+=1
        j-=1

strOut=''.join(list1)
print("Output string :",strOut)

# Output: fe@#dc!ba

print("--------------Program 4-------------------")
print("------findout elements duplicate count output in  dict format-----")

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

sum = {}
for i in some_list:
    sum[i] = sum.get(i, 0) + 1
print(sum)

print("--------------Program 5-------------------")

t1 = (1, 2, 3, "a", "c") 
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break
print(lis1)
# Output: (10,10,10,"ab","cd")

print("--------------Program 6-------------------")
print("-----Write a Python program to remove leading zeros from an IP address-----")

inp = "216.08.094.196"
print("Given Input :",inp)
inp = list(inp)

for i in inp:
    if i == "0":
        inp.remove(i)

print("Expected Output :",''.join(inp))

# o/p =  216.8.94.196
   
print("--------------Program 6-------------------")

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

print(list(map(lambda x:int(x),str(l).replace('[','').replace(']','').split(', '))))

   #output= [1,2,3,4,5,6,7,8,9,10]

'''
8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total '''

# with codecs.open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as rd:
#     lines = len(rd.readlines())
#     print('Total Number of lines:', lines)

with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
    data = data.readlines()
    print(f"Number of lines :{len(data)}")


# 2. No of words in each line

with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
    data = data.readlines()

c = 1
for line in data:
    line = line.split(' ')
    print(f"Word in Line no {c}: {len(line)}")
    c += 1


# 3. No of chars in each line

with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
    data = data.readlines()
c = 0
l = 1
for i in range(1, len(data)+1):
    with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
        data = data.readline()
        for char in data:
            if char.isalpha:
                c += 1
        print(f"Char in line no.{l}: {c}")
        l += 1


# 4. No of vowels and consonants

with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
    data = data.read()

v = 'aeiou'
sc = '\.n'
vc = 0
cc = 0
for char in data:
    if char in v:
        vc += 1
    elif char in sc:
        continue
    else:
        cc += 1

print(f"Total Vowels: {vc}")
print(f"Total Consonants: {cc}")


# 5. No of special chars linewise and total 


with open(r"C:\Users\DELL\Desktop\Vijay123\Introduction_Interview_vijay.txt",'r', encoding="utf-8") as data:
    data = data.read()

c = 0
for char in data:
    if not char.isalpha() and char.isalnum():
        c += 1

print(f"Total special characters: {c}")
