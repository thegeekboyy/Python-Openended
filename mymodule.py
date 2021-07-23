# CGPA Calculator
def cgpa_Calc(N):
    
    sem = N
    sgpa=[]
    creds=[]
    accumulator = []
    
    CGPA= -1.0
    percentage = -1.0
    print("""-------------------------------------------------------------------------""")
    # Data Collction
    for i in range(1,sem+1):
        print("Enter the SGPA in ",i," Semister \n")
        temp = eval(input())
        sgpa.append(float(temp))

        print("Enter the Credits in ",i,"Semister \n")
        tempp = eval(input())
        creds.append(float(tempp))
        print("""---------------------------------------------------------------------""")
    #Data Analysis and Computation
    for i in range(0,sem):
        sumCreds = sum(creds)
        newTemp = (sgpa[i]*creds[i])
        accumulator.append(newTemp)
        acc= sum(accumulator)

    CGPA = acc/sumCreds
    percentage = (CGPA-0.75)*10
    print("Your Aggregate CGPA is  :",CGPA)
    print("Your Aggregate Percentage is :",percentage,"%")
    return CGPA


#------------------------------------------------------------------------------------------
# Temperature scale conversions
def temperature():
    
    print("""
                    ----------------------------------------
                    |   Press 1 if input is in kelvin      |
                    |   press 2 if input is in Faranheit   |
                    |   Press 3 if input is in  celcius    |
                    ----------------------------------------
    """)   

    inp = int(input())

    if(inp==1):
       kelvin = eval(input("Enter the temperature in Kelvin scale: \n"))
       celcius = kelvin- 273.15
       Faranheit = celcius*(9/5) + 32
       output1 = {"Celcius":celcius, "Faranheit":Faranheit}
       print(output1)
       return output1

    elif(inp==2):
        Faranheit = eval(input("Enter the temperature in Faranheit scale \n"))
        celcius = (Faranheit - 32)/1.8000
        kelvin = celcius + 273.5
        output2 = {"Celcius":celcius, "Kelvin":kelvin}
        print(output2)
        return output2
    else:
        celcius = eval(input("Enter the temperature in celcius scale \n"))
        kelvin = celcius + 273.15
        Faranheit = celcius*(9/5)  + 32
        output3 = {"Kelvin":kelvin, "Faranheit":Faranheit}
        print(output3)
        return output3

#---------------------------------------------------------------------------------------------
# GST Calculator
def GST():
    rate = eval(input("Enter the Rate of intrest: \n"))
    base = eval(input("Enter the base amount: \n"))
    result = rate*base/100
    Final = base + result
    print("The Amount after GST is levied is :",Final)
    return Final

#-----------------------------------------------------------------------------------------------

# Currency Converter
def currency():
    print("""
    -------------------------------------------------------------------------
    |                    Press 1 if the input is in INR                     |
    |                    Press 2 if the input is in USD                     |
    |                    Press 3 if the input is in Yuans                   |
    |                    Press 4 if the input is in Euros                   |
    |                    Press 5 if the input is in Yens                    |
    --------------------------------------------------------------------------
    """)
    curr = {}
    inp = int(input())
    if inp == 1:
        val = eval(input("Enter your input in INR \n"))
        baseUSD=0.013
        USD = val*baseUSD
        curr['USD'] = USD

        baseEuro = 0.01
        Euro = baseEuro*val
        curr['Euro'] = Euro

        baseYuan = 0.09
        Yuan = baseYuan*val
        curr['Yuan']= Yuan

        baseYen = 1.46
        Yen = baseYen*val
        curr['Yen'] = Yen
        print(curr)
        return curr

    elif inp == 2:
        val = eval(input("Enter your input in USD \n"))
        curr1={}

        baseINR = 77
        INR = baseINR*val
        curr1['INR'] = INR

        baseEuro = 0.01
        Euro = baseEuro*INR
        curr1['Euro'] = Euro

        baseYuan = 0.09
        Yuan = baseYuan*INR
        curr1['Yuan']= Yuan

        baseYen = 1.46
        Yen = baseYen*INR
        curr1['Yen'] = Yen

        print(curr1)
        return curr1


        
    elif inp == 3:
        val = eval(input("Enter the input in Yuans \n"))
        curr2={}

        baseINR = 11.1111
        INR = baseINR*val
        curr2['INR'] = INR

        baseUSD=0.013
        USD = INR*baseUSD
        curr2['USD'] = USD

        baseEuro = 0.01
        Euro = baseEuro*INR
        curr2['Euro'] = Euro

        baseYen = 1.46
        Yen = baseYen*INR
        curr2['Yen'] = Yen

        print(curr2)
        return curr2




    elif inp == 4:
        val = eval(input("Enter the input in Euros \n"))
        curr3 = {}

        baseINR = 100
        INR = baseINR*val
        curr3[INR] =INR

        baseYuan = 0.09
        Yuan = baseYuan*INR
        curr3['Yuan']= Yuan

        baseYen = 1.46
        Yen = baseYen*INR
        curr3['Yen'] = Yen

        baseUSD=0.013
        USD = INR*baseUSD
        curr3['USD'] = USD

        print(curr3)
        return curr3


    elif inp == 5:
        val = eval(input("Enter the input in Yens \n"))
        curr4 = {}

        baseINR = 1.46
        INR = baseINR*val
        curr4[INR] = INR

        baseUSD=0.013
        USD = INR*baseUSD
        curr4['USD'] = USD

        baseYuan = 0.09
        Yuan = baseYuan*INR
        curr4['Yuan']= Yuan

        baseEuro = 0.01
        Euro = baseEuro*INR
        curr4['Euro'] = Euro

        print(curr4)
        return curr4

        

#------------------------------------------------------------------------------------------

def degTorad(val):
    ans=val/180*3.1416
    return ans
    


def radTodeg(val):
    ans=val*180/3.1416
    return ans

#--------------------------------------------------------------------------------------
