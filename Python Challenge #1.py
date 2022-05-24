#Python Challenge 1

users = ["Anderson", "Ifeoma", "Olakunle", "Lee", "Margaret", "Olakunle", "Musa", "Musa", "Lee", "Anderson", "Yvonne", "Albert", "Ofori", "Ofori", "Rofiyat", "Rofiyat", "Dele", "Muhammed", "Rofiyat", "Ofori", "Lee", "Ifeoma"]
new_users = []

[new_users.append(i) for i in users if i not in new_users]

file = open("users.txt", "w")
content = ""
new_content = ""
for x in users:
    content = content + f"{x}\n"
file = file.write(content)

for x in new_users:
    new_content = new_content + f"{x}\n"
file = open("new.txt", "w").write(new_content)