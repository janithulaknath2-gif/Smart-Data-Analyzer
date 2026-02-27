def Student_mark_Analyzer():
    Student_marks = {}

    Student_details = {}

    print("Welcome to Student Marks Analyzer ")
    subject = input("Enter the Subject name ").lower()
    while True:
        # student
        student_name = input("Enter the Student name :").lower()

        # get Valid Mark
        while True:
            try:
                mark = int(input(f"Enter {subject} mark :  "))
                if mark < 0 or mark > 100:
                    print("Mark must be 0 to 100 ")
                else:
                    break
            except ValueError:
                print("Plese use Numbers !")
            except Exception as e:
                print(f"Error is {e} ")
        # store data in Dictonary
        Student_marks[student_name] = mark

        # checker
        while True:
            try:
                check_more = input(
                    "do you want to add Another students mark (yes/no)"
                ).lower()
                if check_more != "yes" and check_more != "no":
                    print("please use yes or no ")
                else:
                    break
            except Exception as e:
                print(f"Error is {e}")
        if check_more == "yes":
            continue
        else:
            break
    sum = 0
    count_students = 0

    # find Avarage
    for student in Student_marks:
        sum += Student_marks[student]
        count_students += 1
    average = 0
    if count_students > 0:
        average = sum / count_students

    # find highest mark student
    highest_student = max(Student_marks, key=Student_marks.get)

    # Find Grade

    for student in Student_marks:
        if Student_marks[student] >= 75:
            Grade = "A"
            Status = "Pass"

        elif Student_marks[student] >= 50:
            Grade = "B"
            Status = "Pass"

        else:
            Grade = "F"
            Status = "Fail"

        Student_details[student] = {
            "Mark": Student_marks[student],
            "Grade": Grade,
            "Status": Status,
        }

    # pass Students
    Pass_students = []
    fail_students = []
    for student in Student_details:
        if Student_details[student]["Status"] == "Pass":
            Pass_students.append(student)
        else:
            fail_students.append(student)

    # show All Result
    print("-----------Students Mark Analyze-----------")
    print("")
    print("Avarage Mark : ", average)
    print(f"Top student : {highest_student} |  Mark : {Student_marks[highest_student]}")
    print("Pass Students Count: ", len(Pass_students))
    print("fail Students Count: ", len(fail_students))
    print("")
    print("-----------All Students Details------------")
    for student in Student_details:
        print(
            f"Student Name : {student} |  Mark :{Student_details[student]['Mark']} |  Grade : {Student_details[student]['Grade']} |  Status :{Student_details[student]['Status']} "
        )
        print(
            "--------------------------------------------------------------------------------------------------"
        )


def sales_Data_analyzer():

    sales_details = {}
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # Get year sales
    for month in months:
        while True:
            try:
                monthly_sale = int(input(f"Enter the {month} month sales :"))
                break
            except Exception as e:
                print(f"Error is {e}")

        sales_details[month] = monthly_sale

    # find avarage and Total
    def avarage_and_Total(sales_details):
        Total = sum(sales_details.values())
        avarage = Total / len(sales_details.items())
        return Total, avarage

    Total, avarage = avarage_and_Total(sales_details)

    # best month
    best_sale_month = max(sales_details, key=sales_details.get)

    # lowest sale month
    Lowest_sale_month = min(sales_details, key=sales_details.get)

    # Count days above 1000
    count_days = 0
    for x in sales_details.values():
        if x >= 1000:
            count_days += 1

    # Category
    sale_analyze = {}
    for month, sale in sales_details.items():
        if sale > 1500:
            sale_analyze[month] = {"sale": sale, "Category": "High"}
        elif sale > 1000 and sale < 1500:
            sale_analyze[month] = {"sale": sale, "Category": "Medium"}
        else:
            sale_analyze[month] = {"sale": sale, "Category": "low"}

    print(
        "----------------------------Sales Analyze-----------------------------------"
    )
    print("Year sales  : ", Total)
    print("Avarage monthly sale  : ", avarage)
    print(
        f"Best sales  month : {best_sale_month}  | sales : {sales_details[best_sale_month]}"
    )
    print(
        f"lowest sales  month : {Lowest_sale_month}  | sales : {sales_details[Lowest_sale_month]}"
    )
    print(
        "----------------------------------------------------------------------------------"
    )
    print("")
    print("-----------------Monthly Sales Details--------------------")
    for x in sale_analyze:
        print(
            f"Month : {x}  |   sales : {sale_analyze[x]['sale']}  |  Category : {sale_analyze[x]['Category']}"
        )
        print(
            "-------------------------------------------------------------------------------------"
        )


sales_Data_analyzer()
