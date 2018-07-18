# This will be the cipher's dictionary, from which it will pull random words to mask the message's words
dictionary = ["this", "that", "those", "these", "them", "those", "they",
              "though", "thought", "threw", "tough", "tease", "temptation", "tickle", "tackle"]

while True:
    choice = input("Would you like to send or receive a message? ")
    if choice == "send":
        # We then will get the intended message from the sender
        message = input("Enter the message you would like to encrypt: ").split()
        
        # Write the cipher to a text file and encrypt the message
        cipher = open("cipher.txt", "w", encoding="utf-8")
        for w in range(len(message)):
            cipher.writelines(message[w] + " " + dictionary[w] + "\n")
            message[w] = dictionary[w]  

        print("Your message has been encrypted to: ", message)
    
    elif choice == "receive":
        cipher = open("cipher.txt", "r", encoding="utf-8")
        message = cipher.read().split()
        message = message[::2]
        print(message)

    else:
        continue
