


import display,celcius,reamur,fahrenheit,kelvin

while True :
    
    display.disp()

    if   display.choose==1 :
        celcius.cel()
    elif display.choose==2 :
        reamur.rea()
    elif display.choose==3 :
        fahrenheit.fah()
    elif display.choose==4 :
        kelvin.kel()
    elif display.choose==5 :
        print("\nThank You and Fuck Off")
    else :
        print("\nwdym? your fucking choice doesn't exist here.")

    if (display.choose == 5) : break
