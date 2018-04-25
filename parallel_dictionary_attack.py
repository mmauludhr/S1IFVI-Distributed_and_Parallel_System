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
def crackPassword(password_hash, list_password, part):
    if part/(len(list_password)/5) == 1:
        for index in range(0, part):
            check_md5 = md5.new(list_password[index]).hexdigest()
            if password_hash == check_md5:
                print "\nMatch Found! \nPassword is %s" % list_password[index]
                print "range awal"
                break
        else: print "\nNo Match Found!"

    if part/len(list_password) == 1:
        for index in range((part-(len(list_password)/5))+1, part):
            check_md5 = md5.new(list_password[index]).hexdigest()
            if password_hash == check_md5:
                print "\nMatch Found! \nPassword is %s" % list_password[index]
                print "range akhir"
                break
        else: print "\nNo Match Found!"

    if (part/(len(list_password)/5) != 1) and (part/len(list_password) != 1):
        for index in range((len(list_password)/5)*4, part):
            check_md5 = md5.new(list_password[index]).hexdigest()
            if password_hash == check_md5:
                print "\nMatch Found! \nPassword is %s" % list_password[index]
                print "range tengah"
                break
        else: print "\nNo Match Found!"
################################################################################
list_password = getListPassword()
a, b, c, d, e = splitIntoFive(list_password)
password_hash = "cd69b4957f06cd818d7bf3d61980e291"
crackPassword(password_hash, list_password, e)
