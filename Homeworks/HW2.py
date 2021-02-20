gradeList = list() # ["midterm", "final", "homework"]
studentList = list() #["Name","Surname"]
studentInfo = {
    "studentName": studentList,
    "studentGrade" : gradeList
}

average = list()

for i in range(5):
  x = input("%d. Öğrencinin ismini giriniz: " % (i+1))
  y = input("%d. Öğrencinin soy ismini giriniz: " % (i+1))

  while True:
    try:
      z = int(input("%d. Öğrencinin vize notu giriniz: " % (i+1)))
      if z <= 0 or 100 <= z:
        print("1 ile 100 arasında bir değer girmelisiniz")
      elif isinstance(z,int):
        break
    except ValueError:
      print("1 ile 100 arasında bir int değer girmelisiniz")

  while True:
    try:
      t = int(input("%d. Öğrencinin final notu giriniz: " % (i+1)))
      if t <= 0 or 100 <= t:
        print("1 ile 100 arasında bir değer girmelisiniz")
      elif isinstance(t,int):
        break
    except ValueError:
      print("1 ile 100 arasında bir int değer girmelisiniz")

  while True:
    try:
      w = int(input("%d. Öğrencinin ödev notu giriniz: " % (i+1)))
      if w <= 0 or 100 <= w:
        print("1 ile 100 arasında bir değer girmelisiniz")
      elif isinstance(w,int):
        break
    except ValueError:
      print("1 ile 100 arasında bir int değer girmelisiniz")

  tempStudent=[]
  tempStudentGrade=[]

  tempStudent.append(x)
  tempStudent.append(y)
  tempStudentGrade.append(z)
  tempStudentGrade.append(t)
  tempStudentGrade.append(w)

  gradeList.append(tempStudentGrade)
  studentList.append(tempStudent)
  average.append(int(sum(studentInfo["studentGrade"][i])/3))
  
print(studentInfo)
print("Tebrikler %s" % studentList[average.index(max(average))][0])