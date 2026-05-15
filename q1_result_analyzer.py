def analyze_result(name,roll,marks):
    print(f"Student: {name} (Roll: {roll} )")
    total = sum(marks)
    average = total/5
    print(f"Total: {total}, Average:  {average:.1f}")
    
    if average >= 90:
        print("Grade : A")
    elif average >= 75:
        print("Grade : B")
    elif average >= 60:
        print("Grade : C")
    elif average >= 40:
        print("Grade : D")
    else:
        print("Fail")
    
    print("Subjects below 40:")
    
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i+1}")
analyze_result("Puja",32,[98.5,92.0,76.9,98.9,34.5])
    