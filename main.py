def main():
    # variables
    done = False
    print("Welcome to Your Grading Assistant!")

    # Initial statement
    while not done:
        left = False
        studentID = int(input("Please enter the students ID: "))
        studentFirstName = str(input("Please enter the students First Name: "))
        studentLastName = str(input("Please enter the students Last Name: "))
        assignmentGrade = float(input("Please enter the students grade for Assignments: "))
        quizGrade = float(input("Please enter the students grade for Quizzes: "))
        midtermGrade = float(input("Please enter the students grade for Midterms: "))
        finalGrade = float(input("Please enter the students grade for the Final: "))
        print("")

        totalScore = (assignmentGrade * 0.5) + (quizGrade * 0.2) + (midtermGrade * 0.1) + (finalGrade * 0.2)
        if totalScore >= 90:
            letterGrade = "A"
        elif totalScore >= 80:
            letterGrade = "B"
        elif totalScore >= 70:
            letterGrade = "C"
        elif totalScore >= 60:
            letterGrade = "D"
        else:
            letterGrade = "E"

        print(studentLastName, ", ", studentFirstName)
        print("Student ID:", studentID)
        print("Homework:", assignmentGrade)
        print("Quizzes:", quizGrade)
        print("Midterm:", midtermGrade)
        print("Final:", finalGrade)
        print("Total Score:", totalScore, "       Grade: ", letterGrade)
        print("")

        while not left:
            print("Would you like to enter another student?")
            print("Y: Yes")
            print("N: No")
            print("")
            userQuitChoice = input("Yes or No? ")

            if userQuitChoice.upper() == "N":
                print("")
                print("GoodBye")
                done = True
                left = True
            elif userQuitChoice.upper() == "Y":
                left = True
            else:
                print("")
                print("I do not understand that command, please try again.")
                print("")


# calling the main function
main()
