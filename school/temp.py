def GetClasses():
    with open('\python\4\seminar_8\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)

#a = {'1a': [1,2,3], '1b': [4,5,6]}

GetClasses() 