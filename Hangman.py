pic_0 = " ______    "  #Always Same
pic_1 = " |     |   "  #Always Same
pic_2 = " |         "
pic_3 = " |         "
pic_4 = " |         "
pic_5 = " |         "
pic_6 = " |         "  #Always Same
pic_7 = "_|_        "  #Always Same

pic_00 = " ______   "  #Always Same
pic_11 = " |     |  "  #Always Same
pic_22 = " |     o  "
pic_33 = " |     /\ "
pic_44 = " |     |  "
pic_55 = " |     /\ "
pic_66 = " |        "  #Always Same
pic_77 = "_|_       "  #Always Same

pic_000 = 0
pic_111 = 0
pic_222 = 0
pic_333 = 0
pic_444 = 0
pic_555 = 0
pic_666 = 0
pic_777 = 0


txt_0 = "_ "
txt_1 = "_ "
txt_2 = "_ "
txt_3 = "_ "
txt_4 = "_ "
txt_5 = "_ "

txt_00 = "c"
txt_11 = "h"
txt_22 = "a"
txt_33 = "i"
txt_44 = "r"
txt_55 = "s"

left = "6"

attempts = 0

correct = 0

txt_000 = False
txt_111 = False
txt_222 = False
txt_333 = False
txt_444 = False
txt_555 = False
txt_666 = False

limbs_left = 6

nxt = 0

print(pic_0)
print(pic_1)
print(pic_2)
print(pic_3)
print(pic_4)
print(pic_5)
print(pic_6)
print(pic_7)
print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)

left_leg = input("Welcome to Hangman! Enter a letter of the word to start!: ")

if left_leg == txt_00:
    left = "5"
    txt_000 = True
    nxt = 2
    correct = 1
    print("Correct! " + left + " More letters to go!")
if left_leg == txt_11 and left == "6":
    print("Correct! " + left + " More letters to go!")
    left = "5"
    txt_111 = True
    nxt = 2
    correct = 1
if left_leg == txt_22 and left == "6":
    print("Correct! " + left + " More letters to go!")
    left = "5"
    txt_222 = True
    nxt = 2
    correct = 1
if left_leg == txt_33 and left == "6":
    print("Correct! " + left + " More letters to go!")
    left = "5"
    txt_333 = True
    nxt = 2
    correct = 0
if left_leg == txt_44 and left == "6":
    print("Correct! " + left + " More letters to go!")
    left = "5"
    txt_444 = True
    nxt = 2
    correct = 1
if left_leg == txt_55 and left == "6":
    print("Correct! " + left + " More letters to go!")
    left = "5"
    txt_555 = True
    nxt = 2
    correct = 1

if left > "0":
    if left <= "5":
        if txt_000 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_00 + " " + txt_1, txt_2, txt_3, txt_4, txt_5)
        if txt_111 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0 + txt_11 + " " + txt_2, txt_3, txt_4, txt_5)
        if txt_222 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1 + txt_22 + " " + txt_3, txt_4, txt_5)
        if txt_3 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2 + txt_33 + " " + txt_4, txt_5)
        if txt_444 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2, txt_3 + txt_44 + " " + txt_5)
        if txt_555 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2, txt_3, txt_4 + txt_55)

if left == "6" and nxt == 0:
    limbs_left = 5
    print(pic_0)
    print(pic_1)
    print(pic_22)
    print(pic_3)
    print(pic_4)
    print(pic_5)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)
    pic_222 = 1
    attempts = 1
    right_leg = input("Enter another letter!: ")

    if right_leg == txt_00:
        left = "5"
        txt_000 = True
        nxt = 1
        print("Correct! " + left + " More letters to go!")
    if right_leg == txt_11 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_111 = True
        nxt = 1
    if right_leg == txt_22 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_222 = True
    if right_leg == txt_33 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_333 = True
        nxt = 1
    if right_leg == txt_44 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_444 = True
        nxt = 1
    if right_leg == txt_55 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_555 = True
        nxt = 1

if left == "5" and nxt == 1:
    limbs_left = 5
    print(pic_00)
    print(pic_1)
    if pic_222 == 1:
        print(pic_22)
    else:
        print(pic_2)
    print(pic_3)
    print(pic_4)
    print(pic_5)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)

    left_leg = input("Enter another letter!: ")

if attempts == 1 and correct == 0:
    limbs_left = 4
    print(pic_0)
    print(pic_1)
    print(pic_22)
    print(pic_33)
    print(pic_4)
    print(pic_5)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)
    pic_222 = 1
    pic_333 = 1
    attempts = 2
    right_leg = input("Enter another letter!: ")

if attempts == 2 and correct == 0:
    limbs_left = 2
    print(pic_0)
    print(pic_1)
    print(pic_22)
    print(pic_33)
    print(pic_44)
    print(pic_5)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)
    pic_222 = 1
    pic_333 = 1
    pic_444 = 1
    attempts = 3
    right_leg = input("Enter another letter!: ")

if attempts == 3 and correct == 0:
    limbs_left = 4
    print(pic_0)
    print(pic_1)
    print(pic_22)
    print(pic_33)
    print(pic_44)
    print(pic_55)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)
    pic_222 = 1
    pic_333 = 1
    pic_444 = 1
    pic_555 = 1
    attempts = 4
    print("You Lose!")

if correct == 1 and limbs_left == 6:
    print(pic_0)
    print(pic_1)
    print(pic_2)
    print(pic_3)
    print(pic_4)
    print(pic_5)
    print(pic_6)
    print(pic_7)
    print(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5)

    left_leg = input("Enter another letter!: ")

    if left_leg == txt_00:
        left = "5"
        txt_000 = True
        nxt = 2
        correct = 1
        print("Correct! " + left + " More letters to go!")
    if left_leg == txt_11 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_111 = True
        nxt = 2
        correct = 1
    if left_leg == txt_22 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_222 = True
        nxt = 2
        correct = 1
    if left_leg == txt_33 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_333 = True
        nxt = 2
        correct = 0
    if left_leg == txt_44 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_444 = True
        nxt = 2
        correct = 1
    if left_leg == txt_55 and left == "6":
        print("Correct! " + left + " More letters to go!")
        left = "5"
        txt_555 = True
        nxt = 2
        correct = 1

if left > "0":
    if left <= "5":
        if txt_000 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_00 + " " + txt_1, txt_2, txt_3, txt_4, txt_5)
        if txt_111 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0 + txt_11 + " " + txt_2, txt_3, txt_4, txt_5)
        if txt_222 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1 + txt_22 + " " + txt_3, txt_4, txt_5)
        if txt_3 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2 + txt_33 + " " + txt_4, txt_5)
        if txt_444 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2, txt_3 + txt_44 + " " + txt_5)
        if txt_555 == True:
            print(pic_0)
            print(pic_1)
            print(pic_2)
            print(pic_3)
            print(pic_4)
            print(pic_5)
            print(pic_6)
            print(pic_7)
            print(txt_0, txt_1, txt_2, txt_3, txt_4 + txt_55)

