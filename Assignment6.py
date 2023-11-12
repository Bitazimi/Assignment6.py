while True:
    print("To stop the code Enter a number bigger than 11 or smaller than 2!")
    m = int(input("Enter row:"))
    n = int(input("Enter col:"))

    if m>11 or n>11  or m<2 or n<2:
        print("The multipication table is just for numbers between 1 and 10!")
        break
    
    multipication_table = [["x",2,3,4,5,6,7,8,9,10,11],
                           [2,"-","-","-","-","-","-","-","-","-","-"],
                           [3,"-","-","-","-","-","-","-","-","-","-",],
                           [4,"-","-","-","-","-","-","-","-","-","-",],
                           [5,"-","-","-","-","-","-","-","-","-","-"],
                           [6,"-","-","-","-","-","-","-","-","-","-"],
                           [7,"-","-","-","-","-","-","-","-","-","-",],
                           [8,"-","-","-","-","-","-","-","-","-","-"],
                           [9,"-","-","-","-","-","-","-","-","-","-"],
                           [10,"-","-","-","-","-","-","-","-","-","-"],
                           [11,"-","-","-","-","-","-","-","-","-","-"]]
    
    for i in range(m):
        for j in range(n):
            multipication_table[i+2][j+2] = (multipication_table[i+2][0]) * (multipication_table[0][j+2])
     for i in range(m):
        for j in range(n):
            print(multipication_table[i][j], end = " ")
     print()  

                           

                        