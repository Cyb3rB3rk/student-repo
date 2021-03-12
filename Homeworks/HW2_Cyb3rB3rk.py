# GLOBAL AI HUB TOP LEARNER HOMEWORKS
# https://github.com/Cyb3rB3rk/student-repo
# Homework #2
# !! Line 20'den sonrasının da değerlendirilmesini rica ederim. !!

Cv1 = {"Name": "Jack", "Surname": "Smith.", "Age": "23", "Phone": "5551112233", "Graduate": "2.95", "Job": "DevOps."}
Cv2 = {"Name": "Toby", "Surname": "Lum.", "Age": "21", "Phone": "5551122334", "Graduate": "3.88", "Job": "R&D."}
Cv3 = {"Name": "Emily", "Surname": "Boatwright.", "Age": "22", "Phone":"5512345123","Graduate": "3.21", "Job": "AI Developer."}
Cv4 = {"Name": "Emilia", "Surname": "Benbow.", "Age": "23", "Phone": "5564568542", "Graduate": "2.41", "Job": "R&D."}
Cv5 = {"Name": "Sherrie", "Surname": "Tyson.", "Age": "22", "Phone": "5306666666", "Graduate": "1.18", "Job": "Network."}

# Ödev açıklamasını yaparken Ömer hocam her Cv'nin bilgisini ayrı ayrı çağırın demişti. Bu sebeple aşağıdaki gibi düzenldim kodumu.
print("1st person's name is:", Cv1["Name"], Cv1["Surname"], "He is", Cv1["Age"], "years old and applied to title:", Cv1["Job"], "Grade is:", Cv1["Graduate"], "No:", Cv1["Phone"])
print("2nd person's name is:", Cv2["Name"], Cv2["Surname"], "He is", Cv2["Age"], "years old and applied to title:", Cv2["Job"], "Grade is:", Cv2["Graduate"], "No:", Cv2["Phone"])
print("3rd person's name is:", Cv3["Name"], Cv3["Surname"], "She is", Cv3["Age"], "years old and applied to title:", Cv3["Job"], "Grade is:", Cv3["Graduate"], "No:", Cv3["Phone"])
print("4th person's name is:", Cv4["Name"], Cv4["Surname"], "She is",Cv4["Age"], "years old and applied to title:", Cv4["Job"], "Grade is:", Cv4["Graduate"], "No:", Cv4["Phone"])
print("5th person's name is:",Cv5["Name"],Cv5["Surname"],"She is",Cv5["Age"],"years old and applied to title:", Cv5["Job"], "Grade is:", Cv5["Graduate"],"No:", Cv5["Phone"])
#--------------------------------------------------------------------------------------------------------------------------------

# Advance deneme : Kullanıcıdan bilgi isteme ve o dictionaryden bilginin gelmesi

select = int(input("Enter the number of CV: "))

if select == 1:
    request = str(input(("What do you want to know: ")))
    print(Cv1[request])
    #print(Cv5.items()) --- Doğruden itemlerini de isteyebilirdim ama çıktısı estetik gözükmedi. ---

elif select == 2:
    request = str(input(("What do you want to know: ")))
    print(Cv2[request])
    #print(Cv5.items())

elif select == 3:
    request = str(input(("What do you want to know: ")))
    print(Cv3[request])
    #print(Cv5.items())

elif select == 4:
    request = str(input(("What do you want to know: ")))
    print(Cv4[request])
    #print(Cv5.items())

elif select == 5:
    request = str(input(("What do you want to know: ")))
    print(Cv5[request])
    #print(Cv5.items())

elif select == 0 | select > 5:
    print("Access denied.")

