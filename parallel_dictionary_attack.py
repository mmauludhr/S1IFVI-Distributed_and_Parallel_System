# Authors
# Muhammad Maulud Hidayatullah Rambe - Informatics Engineering, Telkom University, 2018
# Chando Anggara Natanael Batubara - Informatics Engineering, Telkom University, 2018


import md5
import time
import threading

################################################################################
def getListPassword():
    # password_file = "rockyou.txt"
    password_file = raw_input("Enter a dictionary file: ")

    try:
        password_file = open(password_file, "r")
    except:
        print "\nFile Not Found"
        quit()

    list_password = []
    for password in password_file:
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
    global isFound, start_time, end_time
    if part/(len(list_password)/5) == 1:
        for index in range(0, part):
            check_md5 = md5.new(list_password[index]).hexdigest()
            if password_hash == check_md5:
                isFound = True
                end_time = time.time()
                print "\nMatch Found! \nHash: %s --> Password %s, Index: %d" % (password_hash, list_password[index], index)
                print "\nTime to Complete: %fs" % (end_time - start_time)
                break
        # else: print "\nNo Match Found!"
    else:
        for index in range((part-(len(list_password)/5))+1, part):
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
    print "Moving each password to a list.."
    list_password = getListPassword()
    a, b, c, d, e = splitIntoFive(list_password)
    # password_hash = "ad02c6d7e1456d47c134b7c60f89aae2"
    password_hash = raw_input("Input Hash: ")
    numofthreads = 5
    # threadList = []

    start_time = time.time()
    print("Starting Task..")
    for i in range(numofthreads):
        t1 = threading.Thread(target=crackPassword, args=(password_hash, list_password,a))
        t2 = threading.Thread(target=crackPassword, args=(password_hash, list_password, b))
        t3 = threading.Thread(target=crackPassword, args=(password_hash, list_password, c))
        t4 = threading.Thread(target=crackPassword, args=(password_hash, list_password, d))
        t5 = threading.Thread(target=crackPassword, args=(password_hash, list_password, e))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # threadList.append(t1)
    # threadList.append(t2)
    # threadList.append(t3)
    # threadList.append(t4)
    # threadList.append(t5)
