names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for i in names:  # write your for loop here
    usernames.append(i.lower().replace(" ", "_"))
    print(usernames)

print(usernames)