import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'Student.txt'
            inFile = open(filename, 'r')
            lines = inFile.readlines()
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

lines = getLines()
courses = {}
for line in lines:
    course = re.split(r'\s+', line)[0]
    if course == 'Class':
        continue
    if course not in courses:
        courses[course] = 1
    else:
        courses[course] += 1

print('Course summary:')
print('Course'.ljust(15,' '), 'Count'.ljust(15,' '))
for course in sorted(courses.keys()):
    print(course.ljust(15,' '), str(courses[course]).ljust(15,' '))