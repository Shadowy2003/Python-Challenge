num = str(input("Enter number: "))

num = num.replace(" ", "")
num = num.replace(",", "")

num_sep = []
num_list = [x for x in num]
while len(num_list) > 3:
    x = "".join(num_list[len(num_list) - 3: ])
    num_sep.insert(0, x)
    del num_list[len(num_list) - 3: ]              
num_sep.insert(0, "".join(num_list))

import module1
number_in_words = ""
place_value = ["trillion, ", "billion, ", "million, ", "thousand, ", " "]

indx = 0
for y in num_sep:
    if y != '000':
        number_in_words += module1.get_name(y) + " " + place_value[indx - len(num_sep)]
    else:
        pass
    indx += 1
    
if number_in_words.endswith(", "):
    print(f"\n{number_in_words[:-2].capitalize()}")
elif (num_sep[-1][:2] == "00" or num_sep[-1][0] == "0") and num_sep[-1] != "000":
    number_in_words = number_in_words.replace((", " + module1.get_name(num_sep[-1])), " and " + module1.get_name(num_sep[-1]))
    print(f"\n{number_in_words.capitalize()}")
else:
    print(f"\n{number_in_words.capitalize()}")
 