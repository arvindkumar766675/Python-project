lst=["Milk","Bread", "Eggs", "Butter"]
print(lst)
print(len(lst))

#Q2
movies=["Avengers","Inception","Interstellar","Dangal", "3 Idiots"]
print(movies[0])
print(movies[4])
print(movies[2])

#Q3
menu=["Chai","Samosa","Biryani","Dosa","Paneer","Naan"]
print(menu[:3])
print(menu[-2:])
print(menu[1:5])

#Q4
colors=["Red", "Gren", "Blue"]
colors[1]="Green"
print(colors)

#Q5
friends=["Aman","Priya","Rohan"]
friends.append("Neha")
print(friends)

#Q6
class_list=["Aman", "Priya", "Rohan","Neha", "Kavya"]
class_list.remove("Rohan")
print(class_list)

#Q7
shopping=["Milk", "Bread","Eggs"]
print("Bread" in shopping)
print("Butter" in shopping)

#Q8
days=["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
x=tuple(days)
print(x)
print(len(x))
print(type(x))

#Q9
a=("Hello")
b=("Hello",)
print(type(a))
print(type(b))

#Q10
weekdays=("Mon","Tue","Wed","Thu","Fri")
print(weekdays[0])
print(weekdays[-1])
print(weekdays[1:4])
print("Sat" in weekdays)

#Q11
playlist=[]
playlist.append("Tum Hi Ho")
playlist.append("Kesariya")
playlist.append("Kal Ho Na Ho")

playlist.pop(1)
playlist.insert(0,"Kesariya")
print(playlist)

#Q12
subjects=["Math","Physics","Chemistry","Biology", "English"]
subjects[1:3]="Economics","Statistics"
print(subjects)

#Q13
team_a=["Virat","Rohit","Dhoni"]
team_b=["Bumrah","Jadeja"]
team_a.extend(team_b)
team_a.insert(3,"Hardik")
print(team_a)
print(len(team_a))

#Q14
items=["Pen", "Book", "Eraser","Ruler", "Pencil"]
removed=items.pop(2)
print("Removed :",removed)
print(items)

#Q15
profile=["Aman",20,True,8.5]
print(profile)
print(type(profile[0]))
print(type(profile[1]))
print(type(profile[2]))
print(type(profile[3]))

#Q16
numbers=[1,2,3,4,5]
backwards= numbers[::-1]
print("Original :", numbers)
print("Reversed :",backwards)

#Q17

colors=("Red","Green", "Blue")
x=list(colors)
x[1]="Yellow"
tppl=tuple(x)
print(tppl)
print(type(tppl))

#Q18
fruits=("Apple","Banana")
p=list(fruits)
p.append("Mango")
print(tuple(p))
print(len(p))

#Q19
x="Math","Science","English"
a=list(x)
b=tuple(x)
print(a)
print(b)
print(type(a))
print(type(b))
a[0]="Art"
print(a)
# b[0]="Art"
# print(b)   # TypeError because tuple is unchangable, we can't add or remove directlu from tuple 

#Q20
info=("Priya",2024005,"CSE")
marks=[85,92,78,88]
print("Name :",info[0])
print("Branch :",info[-1])
print("First mark :",marks[0])

marks[-2]=82
print("Updated marks :",marks)