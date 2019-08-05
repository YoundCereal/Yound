
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
access_granted = False
access_denied = False
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Your Password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Access Denied")
    access_denied = True
else:
    print(" ")
    print("Access Granted")
    access_granted = True

    if access_denied:
        raise SystemExit

if access_granted:
    print(" ")
    print("Welcome")
    print(" ")
    x = int(input("What is Your User Password: "))

    if x == 112906:
        print(" ")
        print("Hello Eli")
        print(" ")
        print("Welcome to Chatbot 1.1.")
        z = str(input("How is your day going?: "))
        if z == ("good"):
                print("I am having a good day too!")
        if z == ("bad"):
                print("I hope it gets better")
        if z == ("great"):
                print("Me too!")
        if z == ("fantastic"):
                    fant = str(input("Why so?: " ))
                    print("Wow!")
        if z == ("ok"):
                print("Well thats still good!")
        if z == ("terrible"):
                    ant = str(input("Why so?: "))
                    print("Oh no!")

print(" ")
input("Press Enter to Exit the Program")
