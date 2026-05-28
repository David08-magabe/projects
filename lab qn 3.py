Students ={
    "Alice": 78,
    "Bob": 65,
    "Carol": 82,
    "David": 59,
}

# access values by key
print(Students["Alice"])

# access using get()
print(Students.get("Bob"))
print(Students.get("Carol"))
print(Students.get("David"))
print(Students.get("Alice"))

# acess using keys()
print(Students.keys())

# access using values()
print(Students.values())

# acess both values and keys
print(Students.items())

# adding new key and value
Students["Dan"] = 77
print(Students)

Students.update({"Alice": 1000})
print(Students)

Students.update({"Emmy": 1001})
print(Students)

# removing key from dictionary
Students.pop("Alice")
print(Students)
