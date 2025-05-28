"""
TO DO:
 1. Properly implement BIDMAS/BODMAS:
  a. Move main calc (non brackets) into new function. Y
  b. Keep basic processing ability in def calc(calc) for brackets. 50%
    i. Put all prioritising in maincalc. N: v2
  c. After bracket check, I must look for ÷* first. Append the to calcin list like brackets (send list to maincalc W/ co-ords). Y: v1
  d. once all brackets and ÷* are complete, hand over to +- calculator (send list to maincalc W/O co-ords). Not needed
  e. Update brackets with same algorythm. N: v2
    i. make brakets create a list containing only insides of brakets (to process like a normal string). N: v2
    ii. make the brackets list be passed to maincalc. N: v2
"""

cList = ['','',''] # Defining the list of items for a single calculation [0]=# [1]=+-/* [2]=#
i = 0
def replaceParethesisWCalc(Loc, Loc2):
    calcIn.pop(Loc)
    cList[0] = calcIn.pop(Loc)
    cList[1] = calcIn.pop(Loc)
    cList[2] = calcIn.pop(Loc)
    calcIn.pop(Loc)

    if cList[1] == "+":
        print("Addition")
        cOut = int(cList[0]) + int(cList[2])
    elif cList[1] == "-":
        print("Subtraction")
        cOut = int(cList[0]) - int(cList[2])
    elif cList[1] == "*":
        print("Multiplication")
        cOut = int(cList[0]) * int(cList[2])
    elif cList[1] == "/":
        print("Division")
        cOut = int(cList[0]) / int(cList[2])
    calcIn.insert(Loc, cOut)
    print(calcIn)

def maincalc(Loc):
    global cOut
    global calcIn
    cList[0] = calcIn.pop(Loc)
    cList[1] = calcIn.pop(Loc)
    cList[2] = calcIn.pop(Loc)
    if cList[1] == "+":
        print("Addition")
        cOut = int(cList[0]) + int(cList[2])
    elif cList[1] == "-":
        print("Subtraction")
        cOut = int(cList[0]) - int(cList[2])
    elif cList[1] == "*":
        print("Multiplication")
        cOut = int(cList[0]) * int(cList[2])
    elif cList[1] == "/":
        print("Division")
        cOut = int(cList[0]) / int(cList[2])
    calcIn.insert(Loc, cOut)
    print(calcIn)
    print("Calculation complete.")
def calc(calc):
    if len(calc) == 1:
        return("No input detected.")
    i = 0
    global cOut
    global calcIn
    calcIn = calc
    calcIn = calcIn.split(" ")
    if len(calcIn) == 1:
        return(calcIn[0])
    else:
        print(calcIn)
        while True:
            if "(" in calcIn:
                loc = calcIn.index("(")
                loc2 = len(calcIn) - 1 - calcIn[::-1].index(")")
                try:
                    loc = len(calcIn) - 1 - calcIn[::-1].index("(")
                    loc2 = calcIn.index(")")
                except ValueError:
                    print("no more Parenthesis detected, but not closed. Check your input.")
                print("Parenthesis detected. Prioritising. found at: "+str(loc) + " and " + str(loc2))
                replaceParethesisWCalc(loc, loc2)
            else:
                while len(calcIn) >= 2:
                    if "*" in calcIn or "/" in calcIn:
                        Loc = 0
                        if "*" in calcIn:
                            Loc = (calcIn.index("*")-1)
                        elif "/" in calcIn:
                            Loc = (calcIn.index("/")-1)
                        maincalc(Loc)
                    else:
                        maincalc(0)
                else:
                    print("Calculation complete.")
                    break
    try:
        if "69" in str(cOut) or "420" in str(cOut):
            return(str(cOut)+" Ha Ha")
        else:
            return(cOut)
    except NameError:
        print("Calculation failed. Check your input.")
#num + operator + num
print("Text Input Calculator: V1.0") 