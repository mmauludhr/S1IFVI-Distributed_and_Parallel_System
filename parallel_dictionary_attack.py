import md5
import os
import sys
import multiprocessing

################################################################################
def getListPassword():
    # counter = 0
    password_file = raw_input("Enter a dictionary file: ")

    try:
        password_file = open(password_file, "r")
    except:
        print "\nFile Not Found"
        quit()

    list_password = []
    for password in password_file:
        # counter += 1
        pswrd = password.strip()
        list_password.append(pswrd)

    return list_password
################################################################################
def splitIntoFive(list_password):
    part1 = len(list_password)/5
    part2 = part1*2
    part3 = part1*3
    part4 = part1*4
    part5 = len(list_password)

    return part1, part2, part3, part4, part5
################################################################################
def crackPassword(list_password, part):
    counter = 1

    if part/(len(list_password)/5) == 1:
        print "range awal"
    elif part/len(list_password) == 1:
        print "range akhir"
    else:
        print "range tengah"
################################################################################
list_password = getListPassword()
a, b, c, d, e = splitIntoFive(list_password)
crackPassword(list_password, e)
