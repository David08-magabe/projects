# def numbers(a,b):
#     c=a+b
#     return c
# output=numbers(1,2)
# print(output)

def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name= format_name("David","Magabe")
print(formatted_name)