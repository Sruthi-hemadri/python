stud_mark={"john":86.5,"jack":91.2,"jill":84.5,"harry":72.1,"joe":80.5}
print(stud_mark)
asc=(sorted(stud_mark.values()))
print(asc)
l=len(asc)
d=[]
while l!=0:
    d.append(asc[l-1])
    l=l-1
print("desc order",d)
print(sum(stud_mark.values())/float(len(stud_mark)))