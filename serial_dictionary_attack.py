# Authors
# Muhammad Maulud Hidayatullah Rambe - Informatics Engineering, Telkom University, 2018

import md5
import time
import threading

################################################################################
def getListPassword():
    # counter = 0
    # password_file = "rockyou.txt"
    password_file = raw_input("Enter a dictionary file: ")
    print "Moving each password to a list.."

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
def crackPassword(password_hash, list_password):
    global isFound, start_time, end_time
    for index in range(0, len(list_password)):
        check_md5 = md5.new(list_password[index]).hexdigest()
        if password_hash == check_md5:
            isFound = True
            end_time = time.time()
            print "\nMatch Found! \nHash: %s --> Password %s, Index: %d" % (password_hash, list_password[index], index)
            print "\nTime to Complete: %fs" % (end_time - start_time)
            break
        # else: print "\nNo Match Found!"
################################################################################
################################################################################
if __name__ == '__main__':
    global isFound, start_time, end_time
    isFound = False
    list_password = getListPassword()
    a, b, c, d, e = splitIntoFive(list_password)
    # password_hash = "ad02c6d7e1456d47c134b7c60f89aae2"
    password_hash = raw_input("Input Hash: ")

    start_time = time.time()
    print "Starting Task.."
    crackPassword(password_hash, list_password)
