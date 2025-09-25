def mikimoko(n:int, m:int):
    i = 0
    for i in range(n,m+1): # i = 6
        if i % 3 == 0 and i % 5 == 0:
            print ("mikimoko", end=", ")
            break
        if i % 3 == 0:
            print ("miki", end=", ")
            continue
        if i % 5 == 0:
            print("moko", end=", ")
            continue
        print(i, end=", ")
    print(" ")
    print("FIN")

mikimoko(1,500)
