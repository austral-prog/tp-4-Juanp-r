def leap_year():
    print("TO DO")
    año=int(input("Ingrese un año:  "))
    if (año%100)==0 and(año%400)==0:
            print(f"El año {año} es biciesto")
    elif (año%4)==0 and (año%100!=0):
        print(f"El año {año} es biciesto")
    else :
        print("El año no es biciesto")


