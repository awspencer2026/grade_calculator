# Create Assignment Grades List
def create_assignment_grades_dictionary():
    assignment_grades = {}
    return assignment_grades


# Adds Assignment to Grade List
def add_assignment(assignment_grades):
        
    assignment_name = input("\nPlease input assignment name: ")

    if assignment_name not in assignment_grades.keys():

        assignment_grade_dict = {}

        grade = input("\nPlease input grade you recieved on that assignemnt (without the percentage sign): ")
        weight = input("\nPlease input weight of that assignment as a decimal value: ")
        assignment_grade_dict.update({grade: weight})
    
        assignment_grades.update({assignment_name: assignment_grade_dict})
        return True
    else:
        return False

# Deletes Assignment from Assignment Grades List    
def delete_assignment(assignment_grades):

    delete_assignment = input("\nPlease input the name of the assignment that you wish to delete: ")

    if delete_assignment not in assignment_grades.keys():
        return False

    else:
        assignment_grades.pop(delete_assignment)
        return True
    
# Displays Assignment Grades List
def display_assignments(assignment_grades):

    weighted_grade = 0

    for k, v in assignment_grades.items():
        print("\nAssignment Name: " + k)
        
        for key, value, in v.items():

            weighted_grade = (float(key) * float(value))  
            print("Grade: "+key+", Weight: "+value)
                  
# Weighted Grade Calculator
def average_grade(assignment_grades):

    assignment_avg = 0
    weight_total = 0

    for k, v in assignment_grades.items():

        for key, value in v.items():

            assignment_avg += ((float(key) * float(value)))
            weight_total += float(value)
            
    average = assignment_avg/weight_total
    print("\nCurrent Average Grade: "+ str(average))


# Final Grade Needed Calculator
def final_needed(assignment_grades):

    assignment_avg = 0
    weight_total = 0

    for k, v in assignment_grades.items():

        for key, value in v.items():

            assignment_avg += ((float(key) * float(value)))
            weight_total += float(value)
            
    average = assignment_avg/weight_total
    print("\nCurrent Average Grade: "+ str(average))

    final_weight = float(input("\nEnter the weight of your final exam as a decimal: "))
    desired_grade = float(input("\nEnter your desired final grade for the class: "))

    final = (desired_grade - (1 - final_weight) * average) / final_weight
    print("\nIn order to obtain a final grade of: " + str(desired_grade) +", a minimum score of: "+str(final)+" must be obtained on the final exam.") 
    

# GPA Calculator 
def gpa():

    grades = []

    print("\nConversion scale: A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0")
    
    grade_count = float(input("\nEnter the number of classes you have taken: "))
    grade_count_iteration = grade_count

    while grade_count_iteration > 0:

        grade = input("\nPlease enter letter grade, as an uppercase letter: ")
        grades.append(grade)
        grade_count_iteration -= 1

    print("\nYour grades: ")
    print(grades)

    gpa_sum = 0.0
    
    for grade in grades:
        if grade == "A":
            gpa_sum += 4.0
        elif grade == "B":
            gpa_sum += 3.0
        elif grade == "C":
            gpa_sum += 2.0
        elif grade == "D":
            gpa_sum += 1.0
        elif grade == "F":
            gpa_sum += 0.0

    final_gpa = (gpa_sum / grade_count)

    print("\nYour GPA: " + str(round(final_gpa, 2)))
        
def report_card(assignment_grades):

    rep_card = open("report_card.txt", "a") 

    for k, v in assignment_grades.items():

        rep_card.write("Assignment: "+k)
        
        
        for key in v.keys():

            if float(key) >= 95:
                rep_card.write(". Letter Grade: A\n")

            elif float(key) >= 85:
                rep_card.write(". Letter Grade: B\n")
  
            elif float(key) >= 75:
                rep_card.write(". Letter Grade: C\n")

            elif float(key) >= 65:
                rep_card.write(". Letter Grade: D\n")

            elif float(key) < 65:
                rep_card.write(". Letter Grade: F\n")

    rep_card.close()

    return True

    
        



