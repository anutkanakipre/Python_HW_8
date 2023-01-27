import view

# students:
{1: {'First Name': 'Иван', 'Last Name': 'Иванов', 'Birthday': '2000-01-01', 'Class Name': '1a' },}

# class:
{'1a': [], '1b': []}

student_id_counter = 1
students = {}
classes = {}


def AddNewStudent():
    new_student = dict()
    new_student['id'] = GetNewId()
    new_student['First name'] = view.GetNewStudentInfo('students first name')
    new_student['Last name'] = view.GetNewStudentInfo('students last name')
    new_student['Birthday'] = view.GetNewStudentInfo('students birthday')
    AddStudentsInClasses(new_student['id'])
    return new_student

def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def SaveStudents(student):
    with open('students.csv', 'a') as file:
        file.write(f"{student['id']};{student['First name']};{student['Last name']};{student['Birthday']}\n")


def AddStudentsInClasses(student_id):
    global classes
    student_class = view.GetNewStudentInfo('students class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]

def GetLastStudentId():
    global student_id_counter
    with open('last_student_id.txt', 'r',encoding='utf-8') as file:
        student_id_counter = int(file.read())

def SaveLastStudentId():
    global student_id_counter 
    with open('last_student_id.txt', 'w',encoding='utf-8') as file:
        file.write(str(student_id_counter))


def SaveClasses():
    with open('classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')


def GetClasses():
    with open('classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)