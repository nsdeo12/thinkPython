try:
    testfile = open('myfile.txt')
    try:
        txns = testfile.readlines()
        print("File data = ", txns)
    finally:
        print("In Inner finally")
except IOError:
    print('unable to access test file\n')
finally:
    print("In Outer finally")
