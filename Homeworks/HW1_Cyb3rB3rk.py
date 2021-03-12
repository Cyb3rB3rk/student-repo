# GLOBAL AI HUB TOP LEARNER HOMEWORKS
# https://github.com/Cyb3rB3rk/student-repo
# Homework #1

listOdd = [1,3,5,7,9]
listEven = [0,2,4,6,8]
listMerged = listEven + listOdd
listMerged.sort()
print(listMerged)

listMultiplication = [element * 2 for element in listMerged]
print(listMultiplication)

i = 0 # Assigned in order to check every index of listMultiplication

for i in range (len(listMultiplication)):
    print(listMultiplication[i], "'s type is", type(listMultiplication[i]))





