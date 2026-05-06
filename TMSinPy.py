UserList = [
    ("Admin", {"password": "admin123", "role": "admin"}),
    ("John", {"password": "recep123", "role": "receptionist"}),
    ("Jack", {"password": "recep234", "role": "receptionist"}),
    ("Wong", {"password": "tutor123", "role": "tutor"}),
    ("Wee", {"password": "tutor234", "role": "tutor"}),
    ("David", {"password": "tutor345", "role": "tutor"}),
    ("Ali", {"password": "student123", "role": "student"}),
    ("Akau", {"password": "student123", "role": "student"}),
    ("Muthu", {"password": "student123", "role": "student"})
    ]

TutorList = [
    ("Wong",{
        "subject": ["Math"],
        "level": ["Form3"]}),
    ("Wee",{
        "subject": ["Science"],
        "level": ["Form2"]}),
    ("David",{
        "subject": ["Biology"],
        "level": ["Form5"]})
    ]

ReceptionistList = [["John"],["Jack"]]

StudentList = [
    ("Ali",{
        "name":"Ali",
        "personal_info": {
            "IC_number": "091230550124",
            "email": "ali1234@gmail.com",
            "enroll_month": "11,2023",
            "level": "Form4"},
            
        "subjects":[
            {"name": "Math",
             "level": "Form4",
             "enroll_month": "11,2023",
             "fee_paid": 300},
            {"name": "Science",
             "level": "Form4",
             "enroll_month": "11,2023",
             "fee_paid": 300}],
        "balance": 100}),
    ("Akau",{
        "name":"Akau",
        "personal_info": {
            "IC_number": "070311220125",
            "email": "akau1234@gmail.com",
            "enroll_month": "10,2021",
            "level": "Form5"},
        "subjects":[
            {"name": "Math",
             "level": "Form3",
             "enroll_month": "10,2021",
             "fee_paid": 300},
            {"name": "Biology",
             "level": "Form5",
             "enroll_month": "04,2022",
             "fee_paid": 500}],
        "balance": 0}),
    ("Muthu",{
        "name":"Muthu",
        "personal_info": {
            "IC_number": "071028140123",
            "email": "muthu1234@gmail.com",
            "enroll_month": "03,2021",
             "level": "Form4"},
        "subjects":[
            {"name": "Science",
             "level": "Form4",
             "enroll_month": "12,2022",
             "fee_paid": 400},
            {"name": "Biology",
             "level": "Form4",
             "enroll_month": "05,2022",
             "fee_paid": 300}],
        "balance": 200})
    ]

SubjectList = [
    ("Math",{
        "level": ["Form1","Form2","Form3","Form4","Form5"],
        "fee": 300}),
    ("Science",{
        "level": ["Form1","Form2","Form3","Form4","Form5"],
        "fee": 400}),
    ("Biology",{
        "level": ["Form3","Form4","Form5"],
        "fee": 500})
    ]

PaymentList = [
    {"student":"Ali", "amount":300, "subject":"Math", "level":"Form4"},
    {"student":"Ali", "amount":300, "subject":"Science", "level":"Form4"},
    {"student":"Akau", "amount":300, "subject":"Math", "level":"Form3"},
    {"student":"Akau", "amount":500, "subject":"Biology", "level":"Form5"},
    {"student":"Muthu", "amount":400, "subject":"Science", "level":"Form4"},
    {"student":"Muthu", "amount":300, "subject":"Biology", "level":"Form4"},
    ]

ScheduleList = [
    ("Form1",{
        "Subject": ["Math"],
        "Time":1000}),
    ("Form1",{
        "Subject": ["Science"],
        "Time":[1100]}),
    ("Form2",{
        "Subject": ["Math"],
        "Time":[1200]}),
    ("Form2",{
        "Subject": ["Science"],
        "Time":[1015]}),
    ("Form3",{
        "Subject": ["Math"],
        "Time":[1115]}),
    ("Form3",{
        "Subject": ["Science"],
        "Time":[1215]}),
    ("Form3",{
        "Subject": ["Biology"],
        "Time":[1030]}),
    ("Form4",{
        "Subject": ["Math"],
       "Time":[1130]}),
    ("Form4",{
        "Subject": ["Science"],
        "Time":[1230]}),
    ("Form4",{
        "Subject": ["Biology"],
        "Time":[1045]}),
    ("Form5",{
        "Subject": ["Math"],
        "Time":[1145]}),
    ("Form5",{
        "Subject": ["Science"],
        "Time":[1245]}),
    ("Form5",{
        "Subject": ["Biology"],
        "Time":[1300]})                  
    ]

users = dict(UserList)
tutors = dict(TutorList)
receptionists = ReceptionistList
students = dict(StudentList)
subjects = dict(SubjectList)
payments = PaymentList
Schedule = ScheduleList

def login():
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        user = users.get(username)
        if user and user["password"] == password:
            return username
        attempts -= 1
        print("Invalid Username or Password,",attempts,"attempts left.")
    return

def admin_menu(username):
    while True:
        print("\nADMIN MENU")
        print("1. Register Tutor")
        print("2. Delete Tutor")
        print("3. Register Receptionist")
        print("4. Delete Receptionist")
        print("5. View Income Report")
        print("6. Update Profile")
        print("7. Logout")
        choice = input("Choose: ")
        
        if choice == "1":
            username = input("New tutor username: ")
            if username in users:
                print("Username already exist")
                continue
            users[username] = {"password": "welcome123", "role": "tutor"}
            tutors[username] = {"subjects":[]}
            print("\nPlease assign subject for tutor")
            subject = input("Enter subject to assign: ")
            if subject not in subjects:
                print("Error, Invalid Subject")
                continue
            level = input("Enter level to assign: ")
            if level not in subjects[subject]["level"]:
                print("Error, Invalid Level")
                continue
            tutors[username]["subjects"].append({
                        "subject":subject,
                        "level":level
                    })
            print("Tutor registered.")

        elif choice == "2":
            username = input("Tutor username to delete: ")
            if username not in users:
                print("Error, Invalid Username")
                continue
            if users[username]["role"] != "tutor":
                print("Error, Only tutor can be deleted here")
                continue
            if username in users and users[username]["role"] == "tutor":
                del users[username]
                print("Tutor deleted.")
        
        elif choice == "3":
            username = input("New receptionist username: ")
            if username in users:
                print("Username already exist")
                continue
            users[username] = {"password": "welcome123", "role": "receptionist"}
            receptionists.append([username])
            print("Receptionist registered.")

        elif choice == "4":
            username = input("Receptionist username to delete: ")
            if username not in users:
                print("Error, Invalid Username")
                continue
            if users[username]["role"] != "receptionist":
                print("Error, Only receptionist can be deleted here")
                continue
            if username in users and users[username]["role"] == "receptionist":
                del users[username]
                print("Receptionist deleted.")
        
        elif choice == "5":
            income_report()
        
        elif choice == "6":
            print("1.Change Username")
            print("2.Change Password")
            print("3.Back")
            update_choice = input("Choose: ")
            if update_choice == "1":
                new_username = input("Enter new username: ")
                if new_username in users:
                    print("Username already exist")
                else:
                    new_user = users[username]
                    del users[username]
                    users[new_username] = new_user
                    username = new_username
                    print("Username Updated")

            elif update_choice == "2":
                new_password = input("Enter new password: ")
                comfirm_password = input("Confirm new password: ")
                if new_password == comfirm_password:
                    users[username]["password"] = new_password
                    print("Password Updated")
                else:
                    print("Password do not match. Please Try Again")

            elif update_choice == "3":
                continue

        elif choice == "7":
            print("Logging out...")
            break

def income_report():
    print("\nINCOME REPORT")
    total = sum(payment["amount"] for payment in payments)
    print("Total Income: RM",total)
    total_by = input("\nTotal by:\n1. Subject\n2. Level\n3. Back\nChoose: ")
    if total_by == "1":
        subject_total = {}
        for payment in payments:
            subject = payment["subject"]
            subject_total[subject] = subject_total.get(subject, 0) + payment["amount"]
        print("\nIncome by Subject:")
        for subject in subject_total:
            print(subject,": RM",subject_total[subject])
            continue

    if total_by == "2":
        level_total = {}
        for payment in payments:
            level = payment["level"]
            level_total[level] = level_total.get(level, 0) + payment["amount"]
        print("\nIncome by Level:")
        for level in level_total:
            print(level,": RM",level_total[level])

    elif total_by == "3":
        return

def receptionist_menu(username):
    while True:
        print("\nRECEPTIONIST MENU")
        print("1. Register Student")
        print("2. Update Student Subject Enrollment")
        print("3. Payments from student and Receipts")
        print("4. Delete student")
        print("5. Update Profile")
        print("6. Logout")
        choice = input("Choose: ")
        

        if choice == "1":
            student_name = input("Enter student name: ")
            if student_name in students:
                print("Student already exists.")
                continue
            ic = input("IC/Passport Number: ")
            email = input("Email: ")
            phone = input("Contact Number: ")
            address = input("Address: ")
            level = input("Academic Level (e.g., Form3): ")
            enroll_month = input("Enrollment Month (MM,YYYY): ")

            students[student_name] = {
                "name": student_name,
                "personal_info": {
                    "IC_number": ic,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "level": level,
                    "enroll_month": enroll_month
                },
                "subjects": [],
                "balance": 0
            }

            users[student_name] = {"password": "student123", "role": "student"}

            print("Enroll up to 3 subjects")
            for i in range(3):
                subject = input(f"Subject {i+1} (leave blank to skip): ")
                if subject == "":
                    break
                if subject not in subjects:
                    print("Invalid subject.")
                    continue
                if level not in subjects[subject]["level"]:
                    print("Subject not available at this level.")
                    continue
                fee = subjects[subject]["fee"]
                students[student_name]["subjects"].append({
                    "name": subject,
                    "level": level,
                    "enroll_month": enroll_month,
                    "fee_paid": fee
                })
                students[student_name]["balance"] += fee
                payments.append({
                    "student": student_name,
                    "amount": fee,
                    "subject": subject,
                    "level": level
                })
            print("Student registered and enrolled.")

        elif choice == "2":
            student_name = input("Student name to update: ")
            if student_name not in students:
                print("Student not found.")
                continue
            print("Current subjects:")
            for s in students[student_name]["subjects"]:
                print(f"- {s['name']} ({s['level']})")

            print("\n1. Add Subject")
            print("2. Remove Subject")
            action = input("Choose: ")

            if action == "1":
                subject = input("New subject to add: ")
                level = students[student_name]["personal_info"]["level"]
                if subject not in subjects or level not in subjects[subject]["level"]:
                    print("Invalid subject or level.")
                    continue
                fee = subjects[subject]["fee"]
                enroll_month = input("Enroll Month (MM,YYYY): ")

                students[student_name]["subjects"].append({
                    "name": subject,
                    "level": level,
                    "enroll_month": enroll_month,
                    "fee_paid": fee
                })
                students[student_name]["balance"] += fee
                payments.append({
                    "student": student_name,
                    "amount": fee,
                    "subject": subject,
                    "level": level
                })
                print("Subject added and fee recorded.")

            elif action == "2":
                subject = input("Enter subject to remove: ")
                removed = False
                for sub in students[student_name]["subjects"]:
                    if sub["name"] == subject:
                        students[student_name]["subjects"].remove(sub)
                        students[student_name]["balance"] -= sub["fee_paid"]
                        removed = True
                        break
                if removed:
                    print("Subject removed.")
                else:
                    print("Subject not found.")

        elif choice == "3":
            student_name = input("Enter student name: ")
            if student_name not in students:
                print("Student not found.")
                continue
            amount = int(input("Enter amount paid: RM "))
            students[student_name]["balance"] -= amount
            print("Receipt")
            print("--------")
            print(f"Student: {student_name}")
            print(f"Amount Paid: RM{amount}")
            print("Thank you!")

        elif choice == "4":
            student_name = input("Enter student name to delete: ")
            if student_name not in students:
                print("Student not found.")
                continue
            confirm = input(f"Are you sure you want to delete {student_name}? (y/n): ")
            if confirm.lower() == 'y':
                del students[student_name]
                if student_name in users:
                    del users[student_name]
                print("Student deleted.")

        elif choice == "5":
            print("1. Change Username")
            print("2. Change Password")
            print("3. Back")
            update_choice = input("Choose: ")
            if update_choice == "1":
                new_username = input("Enter new username: ")
                if new_username in users:
                    print("Username already exists")
                else:
                    new_user = users[username]
                    del users[username]
                    users[new_username] = new_user
                    username = new_username
                    print("Username updated.")
            elif update_choice == "2":
                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")
                if new_password == confirm_password:
                    users[username]["password"] = new_password
                    print("Password updated.")
                else:
                    print("Passwords do not match.")

        elif choice == "6":
         print("Logging out...")
         break

def tutor_menu(username):
    while True:
        print("\nTUTOR MENU")
        print("1. Add Class")
        print("2. Update Class")
        print("3. Delete Class")
        print("4. View Students")
        print("5. Update Profile")
        print("6. Log out")
        choice = input("Enter choice: ")
        
        if choice == "1":
            Add_Class = input("Enter class subject to add: ")
            if Add_Class not in subjects:
                print("Error: Subject does not exist")
                continue
            level = input("Enter level: ")
            time = input("Enter time: ")
            # Add the class with the recently_added flag set to True
            ScheduleList.append((level, {"Subject": [Add_Class], "Time": [time], "recently_added": True}))
            print("Class Added")
            
        elif choice == "2":
            Update_Class = input("Enter class subject to update: ")
            if Update_Class not in subjects:
                print("Error: Subject does not exist")
                continue
            Update_time = input("Enter time to update: ")
            print("Class Updated")
            
        elif choice == "3":
            delete_class = input("Class to delete: ")
            found = False
            tutor_subjects = tutors[username]["subject"]  
            
            
            if delete_class not in tutor_subjects:
                print("Error: You can only delete classes you are assigned to.")
                continue
            
            
            for schedule in ScheduleList[:]: 
                if delete_class in schedule[1]["Subject"] and schedule[1].get("recently_added", False):
                    ScheduleList.remove(schedule)  
                    found = True
                    print(f"Class '{delete_class}' deleted.")
                    break
            
            if not found:
                print("Error: Class does not exist or was not added recently.")
            
        elif choice == "4":
            print("students: /n",students)
            
        elif choice == "5":
            while True:
                print("\nUpdate Profile")
                print("1. Change Username")
                print("2. Change Password")
                print("3. Back")
                update_choice = input("Choose: ")
                
                if update_choice == "1":
                    new_username = input("Enter new username: ")
                    if new_username in users:
                        print("Username already exists")
                    else:
                        new_user = users[username]
                        del users[username]
                        users[new_username] = new_user
                        username = new_username
                        print("Username Updated")
                    
                elif update_choice == "2":
                    new_password = input("Enter new password: ")
                    confirm_password = input("Confirm new password: ")
                    if new_password == confirm_password:
                        users[username]["password"] = new_password
                        print("Password Updated")
                    else:
                        print("Passwords do not match. Please Try Again")
                        
                elif update_choice == "3":
                    break
                else:
                    print("Invalid choice")
                    
        elif choice == "6":
            print("Logging out...")
            break
            
        else:
            print("Invalid choice, please try again.")

def student_menu(username):
    while True:
        print("\nSTUDENT MENU")
        print("1. View Schedule")
        print("2. Send Subject Change Request To Receptionist")
        print("3. Delete Pending Request")
        print("4. View Payment Status")
        print("5. update profile")
        print("6. logout")
        choice = input("Choose: ")

        if choice == "1":
                    print("schedules:",Schedule)
                    return 
        elif choice == "2":
             username = input("send request to which receptionist:")
             if username not in users:
                    print("Error, Invalid username")
                    continue
             if users[username]["role"] != "receptionist":
                    print("Error,can only send request to receptionist")
                    continue
             if username in users and users[username]["role"] == "receptionist":
                    print("request pending")
                    return 
        elif choice == "3":
             username = input("choose request to delete from which receptionist:")
             if username not in users:
                    print("Error, Invalid username")
                    continue
             if users[username]["role"] != "receptionist":
                    print("Error,request only with receptionists")
                    continue
             if username in users and users[username]["role"] == "receptionist":
                    print("request deleted")
                    return
        elif choice == "4":
             if username in students:
                student = students[username]
                total_paid = sum(subject["fee_paid"] for subject in student["subjects"])
                print(username,"'s balance:", {student['balance']})
                print("Total amount paid:",total_paid)
             else:
                print("Student not found")
             return
        elif choice == "5":
             print("1.Change Username")
             print("2.Change Password")
             print("3.Back")
             update_choice = input("Choose: ")
             if update_choice == "1":
                 new_username = input("Enter new username: ")
             if new_username in users:
                    print("Username already exist")
             else:
                    new_user = users[username]
                    del users[username]
                    users[new_username] = new_user
                    username = new_username
                    print("Username Updated")
                    continue

             if update_choice == "2":
                 new_password = input("Enter new password: ")
                 comfirm_password = input("Comfirm new password: ")
             if new_password == comfirm_password:
                    users[username]["password"] = new_password
                    print("Password Updated")
             else:
                    print("Password do not match. Please Try Again")

             if update_choice == "3":
                 return
        
        elif choice == "6":
              break

# Main Logic
print("TUITION CENTRE SYSTEM")
while True:
    print("\nMAIN MENU")
    print("1. Login")
    print("2. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        username = login()
        if username:
            role = users[username]["role"]
            
            if role == "admin":
                admin_menu(username)
            elif role == "receptionist":
                receptionist_menu(username)
            elif role == "tutor":
                tutor_menu(username)
            elif role == "student":
                student_menu(username)

    elif choice == "2":
        print("Goodbye!")
        break
