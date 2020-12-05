import sys
def çık():
    sys.exit()
def selection():
    course = input("You can choose a minimum of 3 and a maximum of 5 courses, Please enter the name of the courses you want to choose,  : ")
    selected_courses = course.replace(",","").split()
    if (len(selected_courses))>5:
      return ("You can choose up to 5 courses")
    elif(len(selected_courses))<3:
      return ("You failed in class")
        
    else:
        return selected_courses
name = "Yeliz İşler"
check = False
for x in range(3):
  your_name = (input("Please enter your name and surname: "))
  
  if your_name == name:
    print("Wellcome")
    check = True
    break
  else:
    print("Try again!")
if not check:
  print("Please try again later!!!")
  çık()
  

print(selection())


midtermp= int(input("enter midterm point: "))  
finalp = int(input("enter final point: "))
projectp=int(input("enter prjoect point: "))

exams= ["midterm", "final","project"]
points= [midtermp,finalp, projectp]

res={}
for key in exams:
  for value in points:
    res[key]= value
    points.remove(value)
    break
print(res)

mg = res["midterm"]
fg = res["final"] 
pg = res["project"]
grades = mg*0.30 +fg*0.50 + pg*0.20

if grades> 90:
  print("AA")
elif 70 <= grades <= 90:
  print("BB")
elif 50 <= grades < 70:
  print("CC")
elif 30 <= grades <50:
  print("DD")
elif grades<30:
  print("FF, you failed this course")

    

    





  
  



  
   

    