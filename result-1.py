x1 = float(input("   \nEnter student ENGLISH score: "))
if x1 > 100:
    print("\n   INVALID SCORE")
elif x1 >= 75:
    print("\n   GRADE IS A")
elif x1 >= 60:
    print("\n   GRADE IS B")
elif x1 >= 50:
    print("\n   GRADE IS C")
elif x1 >= 45:
    print("\n   GRADE IS D")
elif x1 >= 40:
    print("\n   GRADE IS E")
elif x1 >= 0:
    print("\n   GRADE IS F")
else:
    print("\n   INVALID SCORE.") 
    
       
x2 = float(input("   \nEnter student MATH score: "))
if x2 > 100:
    print("\n   INVALID SCORE")
elif x2 >= 75:
    print("\n   GRADE IS A")
elif x2 >= 60:
    print("\n   GRADE IS B")
elif x2 >= 50:
    print("\n   GRADE IS C")
elif x2 >= 45:
    print("\n   GRADE IS D")
elif x2 >= 40:
    print("\n   GRADE IS E")
elif x2 >= 0:
    print("\n   GRADE IS F")
else:
    print("\n   INVALID SCORE.")
    
        
x3 = float(input("   \nEnter student CHEM score: "))
if x3 > 100:
    print("\n   INVALID SCORE")
elif x3 >= 75:
    print("\n   GRADE IS A")
elif x3 >= 60:
    print("\n   GRADE IS B")
elif x3 >= 50:
    print("\n   GRADE IS C")
elif x3 >= 45:
    print("\n   GRADE IS D")
elif x3 >= 40:
    print("\n   GRADE IS E")
elif x3 >= 0:
    print("\n   GRADE IS F")
else:
    print("\n   INVALID SCORE.")
    
        
x4 = float(input("   \nEnter student BIOLOGY score: "))
if x4 > 100:
    print("\n   INVALID SCORE")
elif x4 >= 75:
    print("\n   GRADE IS A")
elif x4 >= 60:
    print("\n   GRADE IS B")
elif x4 >= 50:
    print("\n   GRADE IS C")
elif x4 >= 45:
    print("\n   GRADE IS D")
elif x4 >= 40:
    print("\n   GRADE IS E")
elif x4 >= 0:
    print("\n   GRADE IS F")
else:
    print("\n   INVALID SCORE.")
     
x5 = float(input("   \nEnter student PHY score: "))
if x5 > 100:
    print("\n   INVALID SCORE")
elif x5 >= 75:
    print("\n   GRADE IS A")
elif x5 >= 60:
    print("\n   GRADE IS B")
elif x5 >= 50:
    print("\n   GRADE IS C")
elif x5 >= 45:
    print("\n   GRADE IS D")
elif x5 >= 40:
    print("\n   GRADE IS E")
elif x5 >= 0:
    print("\n   GRADE IS F")
else:
    print("\n   INVALID SCORE.") 
    
    
print("ENGLISH GRADE: ",x1 )
print("MATHEMATICS GRADE:" ,x2)
print("CHEMISTRY GRADE:" ,x3)
print("BIOLOGY GRADE:" ,x4)
print("PYHSICS GRADE:" ,x5)




# TO CALC SUM AND AVERAGE
sum = x1+x2+x3+x4+x5
print("\nSUM OF ALL SUBJECTS:",sum)
average = sum/5
print("AVERAGE:",average)


