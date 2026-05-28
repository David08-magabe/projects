subjects = ["Math", "Physics", "Chemistry","Biology","CS"]
# Adding another subject in the list
subjects.append("Programming")
print(subjects)

#Adding another subject in the list to the corresponding index
subjects.insert(1,"English")
print(subjects)

# removing one object from the list
subjects.remove("Programming")
print(subjects)

# removing object from the list and return to the index
subjects.pop(1)
print(subjects)

# arranging variables in the list in ascending order
subjects.sort()
print(subjects)

# reversing variables in the list starting from the last variable
subjects.reverse()
print(subjects)

# extending variables in the list
list = ["Python","Coding"]
subjects.extend(list)
print(subjects)

# copying
subjects.copy()
print(subjects)