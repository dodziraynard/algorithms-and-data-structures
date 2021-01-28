# Number of students
n = int(input())

common_languages = set()
languages = set()
for _ in range(n):
    # Enter number and names of languages separated by space
    student_data = input()
    languages.update(student_data.strip().split()[1:])

print(len(languages), *languages)

print(sorted(languages))
