Phone_no = {
    "ram":1234,
    "Angel":2345,
    "Daniel":345,
}
# Phone_no.keys()
# for i in Phone_no:
#  print(i)
# print("**************")
#
# phone_no = Phone_no.items()
# for i in phone_no:
#     print(i)
Phone_no["david"] = 5678
print(Phone_no)

del Phone_no["ram"]
print(Phone_no)

Phone_no.pop("Angel")
print(Phone_no)

print(Phone_no.get("Angel"))
print(Phone_no.get("Daniel"))
