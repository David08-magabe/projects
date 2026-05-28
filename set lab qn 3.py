languages = {"Python","Java","C++","Javascript","Go"}

# adding item in the set
languages.add("Ruby")
print(languages)

#removing item in the set
languages.remove("Ruby")
print(languages)

# discarding items in the set
languages.discard("Java")
print(languages)

#combining two sets together
languages2 = {"Ruby","HTML"}
print(languages|languages2)

# find items that intercept in both two sets
languages3 = {"Ruby","Java","C++","Javascript","Go"}
print(languages3&languages)

# checking elements which are in one set and not in another set
print(languages-languages3)