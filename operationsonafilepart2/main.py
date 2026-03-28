with open("spidey.txt","w") as file:
    file.write("Hi I am spidey and i am loved by everyone")
    file.close()

with open("spidey.txt","r") as file:
    data = file.readlines()
    print("Words in the file are ......")

    for line in data:
        word = line.split()
        print(word)
        file.close()