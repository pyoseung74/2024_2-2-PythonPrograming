students=[]
with open("students.csv","r")as f:
    lines = f.readlines()
    lines = lines[1:]
    #print(lines)
    for rec in lines:
        rec = rec.strip()
        print(rec.split(","))
        student = {"name":rec[0],"age":int(rec[1]),"addr":rec[2]}
        #duplicate check
        result = check_dup(students, student)
        if result == False:
            students.append(student)
        print(student)
    for rec in students:
        print(f'{rec["name"]}{rec["age"]}{rec["addr"]}')
    #print(students)
    #print(students[1]["name"])
