#pass or fail.
Sno = int(input("Enter student no:"))
Sname = input("Enter student name:")
Sgroup = input("enter student group:")
s1=int(input("maths marks:"))
s2=int(input("phyton marks:"))
s3=int(input("java marks:"))
s4=int(input("telugu marks:"))
s5=int(input("english marks:"))
s6=int(input("computer marks:"))
if (s1>35) and (s2>35) and (s3>35) and (s4>35) and (s5>35) and (s6>35):
    print("pass")
else:
    print("fail")
