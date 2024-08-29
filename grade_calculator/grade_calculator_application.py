import grade_calculator_utility as u

def main():

    print("Welcome to the grade calculator!")
    
    assignment_grades = u.create_assignment_grades_dictionary()
    
    menu = "\nmenu"

    choice = ''

    while choice != "exit":

        print("\n[add] This adds an assignment to the assignment dictionary")
        print("[delete] This removes an assignment from the assignment dictionary.")
        print("[display] This shows all of the assignments in the assignment dictionary.")
        print("[average] This returns the average grade for all the assignments in the assignment dictionary.")
        print("[final] This returns the grade you need on your final to get a desired final grade.")
        print("[repcard] This prints a report card of all your grades.")
        print("[gpa] This returns your GPA based on how many classes you have taken and each class’s grade.")
        print("[exit] This quits the program.")

        choice = input("\nPlease input your selection: ")

        if choice == "add":
            if u.add_assignment(assignment_grades) == True:
                print("\nAssignment added.")
            else:
                print("\nAssignment already exists.")

        elif choice == "delete":
            if u.delete_assignment(assignment_grades) == True:
                print("\nAssignment deleted.")
            else:
                print("\nUnable to delete assignment.")
            
        elif choice == "display":     
            u.display_assignments(assignment_grades)

        elif choice == "average":
            u.average_grade(assignment_grades)

        elif choice == "gpa":
            u.gpa()

        elif choice == "final":
            u.final_needed(assignment_grades)

        elif choice == "repcard":
            if u.report_card(assignment_grades) == True:
                print("\nReport card printed successfully.")

        elif choice == "exit":
            print("\nExiting application")
            quit

        else:
            print("\nYou entered an invalid option. Returning to main menu.")

main()

































