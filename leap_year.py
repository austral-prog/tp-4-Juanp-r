def leap_year():
    print("TO DO")
    año=int(input("Ingrese un año:  "))
    if (año%100)==0 and(año%400)==0:
            print(f"el año {año} es biciesto")
    elif (año%4)==0 and (año%100!=0):
        print(f"el año {año} es biciesto")
    else :
        print("el año no es biciesto")


