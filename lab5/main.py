import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    for e in list:
        users = e
        for key, value in users.items():
            if str(key) == "Mailed" and str(value) == "False":
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = ', '.join(recipients)
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
                smtp_server.quit()





def loadFile(filepath, list):
    with open(filepath) as file_object:
        for line in file_object:
            temp = line.split(",")

            # email imie nazwisko pkt + ewentualnie graded, mailed
            if temp.__len__() == 4:
                points = temp[3].rstrip("\n")
                users = {"Email": temp[0], "Imie": temp[1], "Nazwisko": temp[2], "Punkty": points,
                         "Graded": str(returnGrade(points)), "Mailed": "Mailed"}
                list.append(users)
            else:
                users = {"Email": temp[0], "Imie": temp[1], "Nazwisko": temp[2], "Punkty": temp[3], "Graded": temp[4],"Mailed": temp[5].rstrip("\n")}
                list.append(users)


def saveFile(list):
    filepath = "studentsOut.txt"

    with open(filepath, "w") as file_object:  # w as write
        for e in list:
            users = e
            line=""
            for key, value in users.items():
                if key=="Mailed":
                    line=line+value
                else:
                    line = line + value + ","

            file_object.write(line)
            file_object.write("\n")


def returnGrade(gradeString):
    points = int(gradeString)
    if (points < 50): return 2.0
    if (points > 50 and points < 61): return 3.0
    if (points > 60 and points < 71): return 3.5
    if (points > 70 and points < 81): return 4.0
    if (points > 80 and points < 91): return 4.5
    if (points > 90): return 5.0


def addStudent(list, dict):
    temp = dict.split(",")
    points = temp[3].rstrip("\n")
    mailId=temp[0]

    for e in list:
        users = e
        for key, value in users.items():
            if ( str(value) == mailId):
                return

    users = {"Email": temp[0], "Imie": temp[1], "Nazwisko": temp[2], "Punkty": points,"Graded": str(returnGrade(points)), "Mailed": "Mailed"}
    list.append(users)
    saveFile(list)

def printStudentList(list):
    for e in list:
        print(e)


def removeStudent(list, mailId):
    iterator = 0
    for e in list:
        users = e
        for key, value in users.items():
            if str(value) == mailId:
                list.pop(iterator)
                break
            print(str(key) + ":" + str(value))
        iterator = iterator + 1
    print("-------------------------------------------------")
    saveFile(list)




# ------------------------------------------------------MAIN--------------------------------------------------------------------------------------
list = []
loadFile("students.txt", list)

dict = "-xx@xxx.x-,-NaMe-,-SuRnAmE-,1111"

addStudent(list, dict)
addStudent(list, dict)
removeStudent(list, "-xx@xxx.x-")

printStudentList(list)
saveFile(list) # its already saved


# Ocena końcowa:
# 50 i mniej -    2
# 51 -60 pkt  -   3
# 61 – 70 pkt – 3.5
# 71 – 80 pkt -  4
# 81 -  90 pkt – 4.5
# 91 -  100 pkt – 5
