# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my test plan report.
# Student ID: W2054017/20230255
# Date: 10/12/2023


def is_valid_credit_level(credit_value):
    return credit_value in [0, 20, 40, 60, 80, 100, 120]

def get_credits(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            #If the user input is any value other than integers, this will get displayed and will ask user to enter a valid integer
            print()
            print("Integer required!\n")
            continue
        if not is_valid_credit_level(user_input):
            #If the user input is not any of the values mentioned in function "is_valid_credit_value()", this will get printed and ask user for a in range value
            print("Out of range\n")
            continue
        return int(user_input)
##
#Start of Code for Students
##

#Variable Initialization and retrieving User Inputs
credit_pass = 0 # Volume of credits at Pass Level (Credits_Pass)
credit_defer = 0 # Volume of credits at Defer Level (Credits_Defer)
credit_fail = 0 # Volume of credits at Fail Level (Credits_Fail)

print("1. Staff \n2. Student")
staff_or_stu = input("Enter 1 for Staff Version or 2 for Student Version: ")
while staff_or_stu not in ['1' , '2' ]:
    print()
    print("Please use only the given options!")
    print()
    staff_or_stu = input("Enter 1 for Staff Version or 2 for Student Version: ")
    print()
    continue
if staff_or_stu == '2':
    print()
    print("Using Student Version-----")
    print()
    while True:
        try:
        #To check whether the credits entered credits are in the range of function "is_valid_credit_level()"

            credit_pass = get_credits("Enter Number of credits at Pass: ")
            if not is_valid_credit_level(credit_pass):
                print("Out of Range")
                
            credit_defer = get_credits("Enter Number of credits at Defer: ")
            if not is_valid_credit_level(credit_defer):
                print("Out of Range")
                
            credit_fail = get_credits("Enter Number of credits at Fail: ")
            if not is_valid_credit_level(credit_fail):
                print("Out of Range")

            credits_tot = credit_pass + credit_defer + credit_fail #Validation to keep the total as 120
            if credits_tot != 120:
                print ("Total is Incorrect \n")
                continue

            #Ranges for "Progress" Progression Outcome
            if (credit_pass == 120 and credit_defer == 0 and credit_fail == 0):
                print()
                print ("Progression Outcome: Progress")
                break

            #Ranges for "Progress (Module Trailer)" Progression Outcome
            elif (credit_pass == 100 and credit_defer + credit_fail == 20):
                print()
                print ("Progression Outcome: Progress (Module Trailer) ")
                break

            #Ranges for "Exclude" Progression Outcome
            elif (credit_pass + credit_defer) <= 40:
                print()
                print("Progression Outcome: Exclude")
                break

            #Ranges for "Do not Progress - Module Retriever" Progression Outcome
            else:
                print()
                print("Progression Outcome: Do not progress - Module Retriever")
                break
            
            
        except ValueError: #Validation to inform the user to only enter integers
            print("Integer Required")

if staff_or_stu == '1':
    print()
    print("Using Staff Version-----")
    print()
##
#Start of Code for the Staff Members
##


    def prompting_for_credits():
        credit_list = []
        
        while True:
            #Variable Initialization
            credit_list.append(get_credits("Enter Number of credits at Pass: ")) # Volume of credits at Pass Level
            credit_list.append(get_credits("Enter Number of credits at Defer: ")) # Volume of credits at Defer Level
            credit_list.append(get_credits("Enter Number of credits at Fail: ")) # Volume of credits at Fail Level

            #Checking whether the total of entered values in the list are 120
            if sum(credit_list) != 120:
                print()
                print("Total Incorrect!")
                credit_list.clear() #Clear the list of the currently saved values
                print()
                continue

            return credit_list

    def show_output(progress_level, credit_list, file):
        output_str = f"{progress_level} --- {str(credit_list)[1:-1]}"
        print(output_str)
        file.write(output_str + "\n")

    #Initializing count variables for Histogram
    count_progress = 0
    count_trailer = 0
    count_retriever = 0
    count_excluded = 0

    file = open("InfoOnMarks.txt" , "w")

    while True:
        credit_list = prompting_for_credits()
        pass_credit, defer_credit, fail_credit = credit_list

        if pass_credit == 120:
            print()
            #printing("Progress")
            show_output("Progress" , credit_list , file)
            count_progress += 1
        elif pass_credit == 100:
            print()
            #printing("Progress (Module Trailer)")
            show_output("Progress (Module Trailer)" , credit_list , file)
            count_trailer += 1
        elif (pass_credit + defer_credit) <= 40:
            print()
            #printing("Exclude")
            show_output("Exclude" , credit_list , file)
            count_excluded += 1
        else:
            print()
            #printing("Do not progress - Module Retriever")
            show_output("Do not progress - Module Retriever" , credit_list , file)
            count_retriever += 1

        
        while True:
            print()
            print("Would you like to enter another set of data? ")
            user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print()

            if user_input in ["y", "q"]:
                break

        if user_input == "q":
            break


    file.close()
    file = open("InfoOnMarks.txt" , "r")

    print()
    print(file.read())

    file.close()

    print("Showing results........")
    print("Progress Count - ", count_progress, ",","Trailer Count - ",  count_trailer ,"," , "Retriever Count - ", count_retriever ,",", "Exclude Count - ",  count_excluded)

    from graphics import *

    def histogram():
        progress_count = count_progress #Variable to save how many students progressed
        trailer_count = count_trailer #Variable to save how many students trailered
        retreiver_count = count_retriever #Variable to save how many students got retriever
        exclude_count = count_excluded #Variable to save how many students got excluded
        total_outcomes = progress_count + trailer_count + retreiver_count + exclude_count

    #Creating Histogram window with bar graphs
        #Window Title
        win = GraphWin("Histogram", 800, 568)
        win.setBackground("white")

        #Bottom Line
        bottom_line = Line(Point(50,480), Point(700,480))
        bottom_line.draw(win)

        #Topic - Histogram Results
        text = Text(Point(200,50), "Histogram Results")
        text.setFill("slate gray")
        text.setStyle("bold")
        text.setSize(25)
        text.draw(win)

        #Progress Bar
        rectangle_progress = Rectangle(Point(100,480), Point(200,(480 - (progress_count*15))))
        rectangle_progress.setFill(color_rgb(174,248,168))
        rectangle_progress.draw(win)
        progress_text = Text(Point(150,500), "Progress")
        progress_text.setStyle("bold")
        progress_text.setSize(16)
        progress_text.setTextColor("slate gray")
        progress_text.draw(win)

        #Adding Count to top of the Progress bar
        text_progressCount = Text(Point(150,((480-(progress_count*15))-15)),f"{progress_count}")
        text_progressCount.setSize(18)
        text_progressCount.setStyle("bold")
        text_progressCount.setTextColor("slate gray")
        text_progressCount.draw(win)

        #Trailer Bar
        rectangle_trailer = Rectangle(Point(250,480), Point(350,(480 - (trailer_count*15))))
        rectangle_trailer.setFill(color_rgb(160,198,138))
        rectangle_trailer.draw(win)
        trailer_text = Text(Point(300,500), "Trailer")
        trailer_text.setStyle("bold")
        trailer_text.setSize(16)
        trailer_text.setTextColor("slate gray")
        trailer_text.draw(win)

        #Adding Count to top of the Trailer bar
        text_trailerCount = Text(Point(300,((480-(trailer_count*15))-15)),f"{trailer_count}")
        text_trailerCount.setSize(18)
        text_trailerCount.setStyle("bold")
        text_trailerCount.setTextColor("slate gray")
        text_trailerCount.draw(win)

        #Retriever Bar
        rectangle_retreiver = Rectangle(Point(400,480), Point(500,(480 - (retreiver_count*15))))
        rectangle_retreiver.setFill(color_rgb(167,188,119))
        rectangle_retreiver.draw(win)
        retreiver_text = Text(Point(450,500), "Retriever")
        retreiver_text.setStyle("bold")
        retreiver_text.setSize(16)
        retreiver_text.setTextColor("slate gray")
        retreiver_text.draw(win)

        #Adding Count to top of the Retriever bar
        text_retreiverCount = Text(Point(450,((480-(retreiver_count*15))-15)),f"{retreiver_count}")
        text_retreiverCount.setSize(18)
        text_retreiverCount.setStyle("bold")
        text_retreiverCount.setTextColor("slate gray")
        text_retreiverCount.draw(win)

        #Excluded Bar
        rectangle_exclude = Rectangle(Point(550,480), Point(650,(480 - (exclude_count*15))))
        rectangle_exclude.setFill(color_rgb(210,182,181))
        rectangle_exclude.draw(win)
        exclude_text = Text(Point(600,500), "Excluded")
        exclude_text.setStyle("bold")
        exclude_text.setSize(16)
        exclude_text.setTextColor("slate gray")
        exclude_text.draw(win)

        #Adding Count to top of the Excluded bar
        text_excludeCount = Text(Point(600,((480-(exclude_count*15))-15)),f"{exclude_count}")
        text_excludeCount.setSize(18)
        text_excludeCount.setStyle("bold")
        text_excludeCount.setTextColor("slate gray")
        text_excludeCount.draw(win)

        #Text line for total outcomes
        text_outcome = Text(Point(250,550), f"{total_outcomes} Outcome/s in Total.")
        text_outcome.setSize(22)
        text_outcome.setStyle("bold")
        text_outcome.setTextColor("slate gray")
        text_outcome.draw(win)
        
        win.getMouse() # pause for click in window
        win.close()
    histogram()
