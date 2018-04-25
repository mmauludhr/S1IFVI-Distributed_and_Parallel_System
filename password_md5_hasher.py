import hashlib

num_of_hash = raw_input("Number of password to hash: ")
try:
    for i in range(0, int(num_of_hash)):
        password = raw_input("\nEnter a Password to Hash: ")
        print "Hash: " + hashlib.md5(password).hexdigest()
except:
    print "You've entered wrong input."
