# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:10:37 2026

@author: cayden

Purpose: interactive function storage
"""

import math

def ApproximateIntegration(lowbound, upbound, slices, function):
    
    if "-" in lowbound:
        lowbound = lowbound.replace("-", "")
        lowbound = (-1) * float(lowbound)
    else:
        lowbound = float(lowbound)
        
    if "-" in upbound:
        upbound = upbound.replace("-", "")
        upbound = (-1) * float(upbound)
    else:
        upbound = float(upbound)
    
    slices = float(slices)
    
    i = 1
    
    cumsuml = 0
    
    cumsumu = 0
    
    while i <= slices:
        
        k = lowbound + (i * (upbound - lowbound) / slices)
        
        g = function.replace("x", f"({k})")
        
        l = eval(g)
        
        cumsuml += (l * (upbound - lowbound)) / slices
        
        k2 = upbound - (i * (upbound - lowbound) / slices)
        
        g2 = function.replace("x", f"({k2})")
        
        l2 = eval(g2)
        
        cumsumu += (l2 * (upbound - lowbound)) / slices
        
        i += 1
        
    average = (cumsuml + cumsumu) / 2
    
    n = int(math.log(slices, 10)) + 1
    
    newsuml = f"{cumsuml:.{n}f}"
    
    newsumu = f"{cumsumu:.{n}f}"
    
    newavg = f"{average:.{n}f}"
    
    return float(newsuml), float(newsumu), float(newavg)

def unitconversion(number, fromunit, tounit):
    if fromunit != "NM":
        fromunit = fromunit.strip().lower()
    if tounit != "NM":
        tounit = tounit.strip().lower()
    
    number = float(number)
    
    length = {
        "in": 0.0254,
        "inches": 0.0254,
        "inch": 0.0254,
        "feet": 0.3048,
        "ft": 0.3048,
        "foot": 0.3048,
        "yards": 0.9144,
        "yd": 0.9144,
        "yard": 0.9144,
        "miles": 1609.344,
        "mi": 1609.344,
        "mile": 1609.344,
        "millimeters": 0.001,
        "millimeter": 0.001,
        "mm": 0.001,
        "centimeter": 0.01,
        "cm": 0.01,
        "centimeters": 0.01,
        "meter": 1,
        "meters": 1,
        "m": 1,
        "kilometer": 1000,
        "kilometers": 1000,
        "km": 1000,
        "nanometer": 0.000000001,
        "nanometers": 0.000000001,
        "nm": 0.000000001,
        "micrometer": 0.000001,
        "micrometers": 0.000001,
        "micrometer": 0.000001,
        "μm": 0.000001,
        "nautical mile": 1852,
        "nautical miles": 1852,
        "NM": 1852,
        "nmi": 1852,
        }
    
    mass = {
        "ounce": 28.35,
        "ounces": 28.35,
        "oz": 28.35,
        "pound": 453.6,
        "pounds": 453.6,
        "lb": 453.6,
        "lbs": 453.6,
        "stone": 6350.29,
        "stones": 6350.29,
        "st": 6350.29,
        "ton": 907185,
        "tons": 907185,
        "tn": 907185,
        "imperial ton": 1160000,
        "imperial tons": 1160000,
        "tonne": 1000000,
        "tonnes": 1000000,
        "t": 1000000,
        "microgram": 0.000001,
        "micrograms": 0.000001,
        "μg": 0.000001,
        "milligram": 0.001,
        "milligrams": 0.001,
        "mg": 0.001,
        "g": 1,
        "gram": 1,
        "grams": 1,
        "kilogram": 1000,
        "kilograms": 1000,
        "kg": 1000,
        }
    
    time = {
        "hour": 1,
        "hr": 1,
        "hours": 1,
        "minute": 0.01666666667,
        "minutes": 0.01666666667,
        "min": 0.01666666667,
        "second": 0.00027777833333,
        "seconds": 0.00027777833333,
        "s": 0.00027777833333,
        "millisecond": 0.00000027777833333,
        "milliseconds": 0.00000027777833333,
        "microsecond": 0.00000000027777833333,
        "microseconds": 0.00000000027777833333,
        "nanosecond": 0.00000000000027777833333,
        "nanoseconds": 0.00000000000027777833333,
        "day": 24,
        "days": 24,
        "week": 168,
        "weeks": 168,
        "month": 730,
        "months": 730,
        "year": 8760,
        "years": 8760,
        "decade": 87600,
        "decades": 87600,
        "century": 876000,
        "centuries": 876000,
        }
    
    temp = ["fahrenheit", "celsius", "kelvin"]
    
    if fromunit in length and tounit in length:
        
        reference = number * length[fromunit]
        
        result = reference / length[tounit]
        
        return result
    
    elif fromunit in temp and tounit in temp:
        
        if fromunit == "fahrenheit":
            reference = (number - 32) * 5 / 9
        elif fromunit == "kelvin":
            reference = number - 273.15
        else:
            reference = number
        
        if tounit == "fahrenheit":
            result = (reference * 9 / 5) + 32
        elif tounit == "kelvin":
            result = reference + 273.15
        else:
            result = reference
        
        return result
        
    elif fromunit in mass and tounit in mass:
        
        reference = number * mass[fromunit]
        
        result = reference / mass[tounit]
        
        return result
    
    elif fromunit in time and tounit in time:
        
        reference = number * time[fromunit]
        
        result = reference / time[tounit]
        
        return result
    
    else:
        
        return "\nUnsupported Conversion."

def gmole(element):
    atomicsymbol = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]

    atomicmass = [
        1.0078, 4.0026, 6.941, 9.0122, 10.811, 12.011, 14.007, 15.999,
        18.998, 20.180, 22.990, 24.305, 26.982, 28.086, 30.974, 32.06,
        35.45, 39.948, 39.098, 40.078, 44.956, 47.867, 50.942, 51.996,
        54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630,
        74.922, 78.971, 79.904, 83.798, 85.468, 87.62, 88.906, 91.224,
        92.906, 95.95, 98, 101.07, 102.906, 106.42, 107.868, 112.414,
        114.818, 118.710, 121.760, 127.60, 126.904, 131.293, 132.905,
        137.327, 138.905, 140.116, 140.908, 144.242, 145, 150.36, 151.964,
        157.25, 158.925, 162.500, 164.930, 167.259, 168.934, 173.045,
        174.967, 178.49, 180.948, 183.84, 186.207, 190.23, 192.217,
        195.084, 196.967, 200.592, 204.383, 207.2, 208.980, 209, 210,
        222, 223, 226, 227, 232.038, 231.036, 238.029, 237, 244, 243,
        247, 247, 251, 252, 257, 258, 259, 262, 267, 268, 271, 272,
        270, 278, 281, 282, 285, 286, 289, 289, 293, 294, 294
    ]
    for i in range(len(atomicsymbol)):
        if atomicsymbol[i] == element:
            return atomicmass[i]

def molemass(compound):
    
    capital = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
        "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
    
    lowercase = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q", "r", 
        "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    
    Elementlist = []
    
    AMUlist = []
    
    compoundamu = 0
    
    for i in range(len(compound)):
        if compound[i] in capital:
            if i > 0 and compound[i-1].isdigit():
                Elementlist.append(compound[i])
            else:
                Elementlist.append("1")
                Elementlist.append(compound[i])
        elif compound[i] in lowercase:
            Elementlist[-1] += compound[i]
        elif compound[i].isdigit():
            if compound[i-1].isdigit():
                Elementlist[-1] += compound[i]
            else:
                Elementlist.append(compound[i])
        else:
            print(
                "Error, please note that polyatomic ions must be simplified"
                "and that coefficients must be carried beforehand"
                )
            return "Error"
        if i == (len(compound)-1):
            if not compound[i].isdigit():
                Elementlist.append("1")
    
    for i in range(len(Elementlist)):
        if not Elementlist[i].isdigit():
            newvalue = gmole(Elementlist[i]) * int(Elementlist[i+1])
            AMUlist.append(newvalue)
            
    for i in range(len(AMUlist)):
        compoundamu = compoundamu + AMUlist[i]
    
    return compoundamu

def gramstomoles(compound, grams):
    return grams / molemass(compound)

def molestograms(compound, moles):
    return moles * molemass(compound)

def molestoparticles(moles):
    avocados = 6.02214076 * 10**23
    return moles * avocados

def particlestomoles(particles):
    avocados = 6.02214076 * 10**23
    return particles / avocados

def approximate(decimal, precision, mode):
    decimal = float(decimal)
    precision = float(precision)
    if decimal < 0:
        negative = -1
    else:
        negative = 1
    decimal = abs(decimal)
    a = 0
    b = 1
    if mode == "mixed":
        mixed = 0
        while decimal > 1:
            decimal = decimal - 1
            mixed = mixed + 1
        while abs(a/b - decimal) > precision:
            if a/b < decimal:
                a = a + 1
            if a/b > decimal:
                b = b + 1
        original = (mixed+decimal) * negative
        if mixed == 0:
            if a/b == decimal:
                return f"{original} = {negative * a}/{b}"
            else:
                return f"{original} = ~ {negative * a}/{b}"
        else:
            if a/b == decimal:
                return f"{original} = {negative * mixed} {a}/{b}"
            else:
                return f"{original} = ~ {negative * mixed} {a}/{b}"
    elif mode == "improper":
        while abs(a/b - decimal) > precision:
            if a/b < decimal:
                a = a + 1
            if a/b > decimal:
                b = b + 1
        decimal = decimal * negative
        if a/b == decimal:
            return f"{decimal} = {negative * a}/{b}"
        else:
            return f"{decimal} = ~ {negative * a}/{b}"
    elif mode == "debugmixed":
        mixed=0
        while decimal > 1:
            decimal = decimal - 1
            mixed = mixed + 1
        while abs(a/b - decimal) > precision:
            if a/b < decimal:
                a = a + 1
            if a/b > decimal:
                b = b + 1
            print(f"{negative * a}, {b}, {negative * a/b}")
        original = (mixed+decimal) * negative
        if mixed == 0:
            if a/b == decimal:
                print(f"{original} = {negative * a}/{b}")
            else:
                print(f"{original} = ~ {negative * a}/{b}")
        else:
            if a/b == decimal:
                print(f"{original} = {negative * mixed} {a}/{b}")
            else:
                print(f"{original} = ~ {negative * mixed} {a}/{b}")
    elif mode == "debugimproper":
        while abs(a/b - decimal) > precision:
            if a/b < decimal:
                a = a + 1
            if a/b > decimal:
                b = b + 1
            print(f"{negative * a}, {b}, {negative * a/b}")
        decimal = decimal * negative
        if a/b == decimal:
            print(f"{decimal} = {negative * a}/{b}")
        else:
            print(f"{decimal} = ~ {negative * a}/{b}")
    else:
        print("error: invalid mode")
        print("")
        print("valid modes include:")
        print("mixed")
        print("improper")
        print("debugmixed")
        print("debugimproper")

def gcd(highnumber, lownumber):
    devisor = lownumber
    while devisor > 1:
        if abs(int(highnumber / devisor) - (highnumber / devisor)) == 0 and abs(int(lownumber / devisor) - (lownumber / devisor)) == 0:
            return devisor
        else:
            devisor = devisor - 1
    return 1

def lcm(n1, n2):
    originalmultiple = n1 * n2
    mult = 1
    while mult < (n1 * n2):
        if int(mult / n1) == (mult / n1) and int(mult / n2) == (mult / n2):
            return mult
        else:
            mult = mult + 1
    return originalmultiple

def quadzeros(a, b, c):
    zeros = []
    zero1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    zero2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    zeros.append(zero1)
    zeros.append(zero2)
    return zeros

def inttoroman(integer):
    romannumeral = ""
    while integer - 1000 >= 0:
        integer -= 1000
        romannumeral += "M"
    while integer - 900 >= 0:
        integer -= 900
        romannumeral += "CM"
    while integer - 500 >= 0:
        integer -= 500
        romannumeral += "D"
    while integer - 400 >= 0:
        integer -= 400
        romannumeral += "CD"
    while integer - 100 >= 0:
        integer -= 100
        romannumeral += "C"
    while integer - 90 >= 0:
        integer -= 90
        romannumeral += "XC"
    while integer - 50 >= 0:
        integer -= 50
        romannumeral += "L"
    while integer - 40 >= 0:
        integer -= 40
        romannumeral += "XL"
    while integer - 10 >= 0:
        integer -= 10
        romannumeral += "X"
    while integer - 9 >= 0:
        integer -= 9
        romannumeral += "IX"
    while integer - 5 >= 0:
        integer -= 5
        romannumeral += "V"
    while integer - 4 >= 0:
        integer -= 4
        romannumeral += "IV"
    while integer - 1 >= 0:
        integer -= 1
        romannumeral += "I"
    return romannumeral

def basea(integer, a):
    
    if a <= 1:
        return "error: invalid base"
    
    baseAnumber = []
    i = 0
    
    while (integer - (a**i)) >= 0:
        i += 1
    
    for j in range(i):
        baseAnumber.append(0)
    
    for j in range(i, -1, -1):
        while integer - a**j >= 0:
            integer -= a**j
            baseAnumber[(len(baseAnumber) - (j + 1))] += 1
    
    return baseAnumber

def calculate(calc):
    
    e = math.e
    
    allowed = {
        "__builtins__": None,
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "pi": math.pi,
        "tan": math.tan,
        "abs": abs,
        "e": e
        }
    
    if (calc, allowed) != None:
        evaluation = eval(calc, allowed)
    else:
        evaluation = "Error, invalid formula"
    
    return evaluation

from datetime import datetime, time

now = datetime.now().time()

date = datetime.now().date()

if time(0, 0, 0) <= now and now < time(12, 0, 0):
    print("Good Morning User")
elif time(12, 0, 0) <= now and now < time(18, 0, 0):
    print("Good Afternoon User")
else:
    print("Good Evening User")

user_name = input("What is your name: \n")

print(
      "\n"
      f"Hello {user_name}. \n"
      "Applicable queries include:\n\n"
      "What functions does this program include\n"
      "What is the purpose of this program\n"
      "Who created this program\n"
      "Extended questions\n"
      "To end this program input 'end'\n"
      )

query = input("What is your query: \n")

while query != "end":

    match query:
        case "What functions does this program include":
            print(
                "\n"
                "This program includes the following functions:\n"
                "gmole function\n"
                "molemass function\n"
                "gramstomoles function\n"
                "molestograms function\n"
                "molestoparticles function\n"
                "particlestomoles function\n"
                "approximate function\n"
                "gcd function\n"
                "lcm function\n"
                "quadzeros function\n"
                "inttoroman function\n"
                "basea function\n"
                "calculate function\n"
                "unitconversion function\n"
                "ApproximateIntegration function \n"
                )
            
            info = input("Would you like to know more about a given function (yes/no):\n")
            
            if info == "yes":
                
                info = input("please input the function name:\n")
                
                while info != "no":
                    
                    match info:
                        case "gmole":
                            print(
                                "\n"
                                "The gmole function is rather simple\n"
                                "By inputting any given element\n"
                                "The function returns that element's atomic mass\n"
                                "In other words it's grams per mole\n"
                                )
                        case "molemass":
                            print(
                                "\n"
                                "The molemass function takes a given compound\n"
                                "In the format of C6H12O6 for instance\n"
                                "And returns the molar mass of that compound\n"
                                "It does not implicitely work with polyatomic ions\n"
                                "And to calculate the molar mass of such a compound\n"
                                "One must multiply through the parenthesis\n"
                                "For instance 'Ca(OH)2'\n"
                                "Would be simplified as 'CaO2H2' for the purposes of the function\n"
                                )
                        case "gramstomoles":
                            print(
                                "\n"
                                "The grams to moles function takes a number of grams\n"
                                "Along with the compound being measured\n"
                                "And outputs the moles\n"
                                "It has the same restrictions as the 'molemass' function\n"
                                "Please refer to the molemass function for more info\n"
                                )
                        case "molestograms":
                            print(
                                "\n"
                                "The moles to grams function takes a number of moles\n"
                                "Along with the compound being measured\n"
                                "And outputs the grams\n"
                                "It has the same restrictions as the 'molemass' function\n"
                                "Please refer to the 'molemass' function for more info\n"
                                )
                        case "molestoparticles":
                            print(
                                "\n"
                                "The moles to particles function takes a given number of moles\n"
                                "And outputs the appropriate number of particles\n"
                                )
                        case "particlestomoles":
                            print(
                                "\n"
                                "The particles to moles function takes a given number of particles\n"
                                "And outputs the appropriate number of moles\n"
                                )
                        case "approximate":
                            print(
                                "\n"
                                "The approximate function converts decimals to fractions\n"
                                "The approximate function takes 3 inputs\n"
                                "The decimal as input one\n"
                                "The precision as input two\n"
                                "And the mode as input three\n"
                                "The decimal can be any real number\n"
                                "The precision is the number of decimal places to which the function will approximate (enter 0 for exact approximation)\n"
                                "And the mode defines how the output is displayed\n"
                                "The modes include 'improper' and 'mixed'\n"
                                "As well as debug modes which should be used sparringly\n"
                                )
                        case "gcd":
                            print(
                                "\n"
                                "The gcd function approximates the greatest common devisor of two numbers\n"
                                "For its input please input the larger number first and the smaller one second\n"
                                )
                        case "lcm":
                            print(
                                "\n"
                                "The lcm function finds the least common multiple of two numbers\n"
                                )
                        case "quadzeros":
                            print(
                                "\n"
                                "The quadzeros function outputs the zeros of a quadratic\n"
                                "The input is the a b and c values of that quadratic\n"
                                )
                        case "inttoroman":
                            print(
                                "\n"
                                "The inttoroman function converts integers to roman numerals\n"
                                )
                        case "basea":
                            print(
                                "\n"
                                "The basea function takes a base 10 integer\n"
                                "As well as a different base\n"
                                "And outputs the equivalent integer for that base\n"
                                )
                        case "calculate":
                            print(
                                "\n"
                                "The calculate function acts as a basic calculator\n"
                                "Though it doesn't support advanced functions like square root\n"
                                )
                        case "unitconversion":
                            print(
                                "\n"
                                "The unitconversion function converts between any two supported units\n"
                                )
                            unitlist = input("Would you like a list of units (yes/no):\n")
                            if unitlist == "yes":
                                print(
                                    "\n"
                                    "Inches, Feet, Yards, Miles, Millimeters, Centimeters, Meters, Kilometers, as well as likewise mass, time and temperature units\n"
                                    )
                        case "ApproximateIntegration":
                            print(
                                "\n"
                                "Approximate integration uses the summation definition of an integral\n"
                                "To approximate a numerical value for the integral within specified bounds\n"
                                )
                        case _:
                            print(
                                "\n"
                                "invalid function\n"
                                )
                    
                    info = input("Would you like info on another function (yes/no):\n")
                    
                    if info == "yes":
                        
                        info = input("please input the function name:\n")
            
            f = input("Would you like to use one of these functions (yes/no):\n")
            
            if f == "yes":
                
                function = input("Please input the function name:\n")
            
                while f != "no":
                
                    match function:
                        case "gmole":
                            element = input("Please input the element:\n")
                            l = gmole(element)
                            print(
                                "\n"
                                f"{l}"
                                "\n"
                                )
                        case "molemass":
                            compound = input("Please input the compound:\n")
                            l = molemass(compound)
                            print(
                                "\n"
                                f"{l}"
                                "\n"
                                )
                        case "gramstomoles":
                            compound = input("Please input the compound:\n")
                            grams = input("Please input the grams:\n")
                            grams = float(grams)
                            print(
                                "\n"
                                f"{gramstomoles(compound, grams)}"
                                "\n"
                                )
                        case "molestograms":
                            compound = input("Please input the compound:\n")
                            moles = input("Please input the moles:\n")
                            moles = float(moles)
                            print(
                                "\n"
                                f"{gramstomoles(compound, moles)}"
                                "\n"
                                )
                        case "molestoparticles":
                            moles = input("Please input the moles:\n")
                            moles = float(moles)
                            print(
                                "\n"
                                f"{molestoparticles(moles)}"
                                "\n"
                                )
                        case "particlestomoles":
                            particles = input("Please input the particles:\n")
                            particles = float(particles)
                            print(
                                "\n"
                                f"{particlestomoles(particles)}"
                                "\n"
                                )
                        case "approximate":
                            decimal = input("Please input the decimal you would like to convert:\n")
                            precision = input("Please input the precision you'd like for the conversion:\n")
                            mode = input("Please input the desired mode:\n")
                            if mode == "improper" or mode == "mixed":
                                print(
                                    "\n"
                                    f"{approximate(decimal, precision, mode)}"
                                    "\n"
                                    )
                            else:
                                print(
                                    "\n"
                                    "Invalid mode\n"
                                    "If you were attempting to use a debug mode\n"
                                    "Please type directly into the input\n"
                                    "As this form of the program cannot access debug modes\n"
                                    )
                        case "gcd":
                            n1 = input("Please input the higher number:\n")
                            n2 = input("Please input the lower number:\n")
                            n1 = int(n1)
                            n2 = int(n2)
                            print(
                                "\n"
                                f"{gcd(n1, n2)}"
                                "\n"
                                )
                        case "lcm":
                            n1 = input("Please input the first number:\n")
                            n2 = input("Please input the second number:\n")
                            n1 = int(n1)
                            n2 = int(n2)
                            print(
                                "\n"
                                f"{lcm(n1, n2)}"
                                "\n"
                                )
                        case "quadzeros":
                            a = input("Please input a for your quadratic:\n")
                            b = input("Please input b for your quadratic:\n")
                            c = input("Please input c for your quadratic:\n")
                            a = float(a)
                            b = float(b)
                            c = float(c)
                            print(
                                "\n"
                                f"{quadzeros(a, b, c)}"
                                "\n"
                                )
                        case "inttoroman":
                            integer = input("Please input the integer:\n")
                            integer = int(integer)
                            print(
                                "\n"
                                f"{inttoroman(integer)}"
                                "\n"
                                )
                        case "basea":
                            integer = input("Please input the base 10 integer:\n")
                            base = input("Please input the desired base:\n")
                            integer = int(integer)
                            base = int(base)
                            print(
                                "\n"
                                f"{basea(integer, base)}"
                                "\n"
                                )
                        case "calculate":
                            calc = input("Please input your calculation:\n")
                            print(
                                "\n"
                                f"{calculate(calc)}"
                                "\n"
                                )
                        case "unitconversion":
                            number = input("Please input the number for the initial unit:\n")
                            fromunit = input("Please input the initial unit:\n")
                            tounit = input("Please input the final unit:\n")
                            print(f"\n{unitconversion(number, fromunit, tounit)}\n")
                        case "ApproximateIntegration":
                            lowbound = input("Please input the leftmost bound of x:\n")
                            upbound = input("Please input the rightmost bound of x:\n")
                            slices = input("Please input the number of slices the function should use:\n")
                            fun = input("Please input the function in terms of x:\n")
                            print(f"\n{ApproximateIntegration(lowbound, upbound, slices, fun)}\n")
                        case _:
                            print(
                                "\n"
                                "Invalid function"
                                "\n"
                                )
                    
                    f = input("Would you like to use another function (yes/no):\n")
                    
                    if f == "yes":
                        
                        function = input("Please input the function name:\n")
                    
        case "What is the purpose of this program":
            print(
                "\n"
                "This program is meant to make several tasks easier\n"
                "It is made to help especially with math and chemistry\n"
                "Though it contains many functions outside that domain\n"
                )
        case "Who created this program":
            print(
                "\n"
                "This program was created by Cayden Hinson\n"
                )
        case "Extended questions":
            print(
                "\n"
                "Extended queries include:\n"
                "What is the current time\n"
                "What is the current date\n"
                "What order were the functions in this program created\n"
                "What other projects have been created by this creator\n"
                "Where can I access other projects\n"
                "When was this program created\n"
                )
        case "What is the current time":
            print(
                "\n"
                f"{now}"
                "\n"
                )
        case "time":
            print(
                "\n"
                f"{now}"
                "\n"
                )
        case "What is the current date":
            print(
                "\n"
                f"{date}"
                "\n"
                )
        case "date":
            print(
                "\n"
                f"{date}"
                "\n"
                )
        case "What order were the functions in this program created":
            print(
                "\n"
                "The first program was the approximate function\n"
                "From there the chemistry functions were created\n"
                "And from there the math functions were created\n"
                )
        case "What other projects have been created by this creator":
            print(
                "\n"
                "This creator has made several languages\n"
                "As well as many songs\n"
                "Though this is primarily the first large program\n"
                )
        case "Where can I access other projects":
            print(
                "\n"
                "Currently there is no way to access other projects\n"
                )
        case "When was this program created":
            print(
                "\n"
                "This program was created on Fri Oct 2nd 23:10:37 2026\n"
                )
        case "function":
            print(
                "\n"
                "This program includes the following functions:\n"
                "gmole function\n"
                "molemass function\n"
                "gramstomoles function\n"
                "molestograms function\n"
                "molestoparticles function\n"
                "particlestomoles function\n"
                "approximate function\n"
                "gcd function\n"
                "lcm function\n"
                "quadzeros function\n"
                "inttoroman function\n"
                "basea function\n"
                "calculate function\n"
                "unitconversion function\n"
                "ApproximateIntegration function \n"
                )
            
            info = input("Would you like to know more about a given function (yes/no):\n")
            
            if info == "yes":
                
                info = input("please input the function name:\n")
                
                while info != "no":
                    
                    match info:
                        case "gmole":
                            print(
                                "\n"
                                "The gmole function is rather simple\n"
                                "By inputting any given element\n"
                                "The function returns that element's atomic mass\n"
                                "In other words it's grams per mole\n"
                                )
                        case "molemass":
                            print(
                                "\n"
                                "The molemass function takes a given compound\n"
                                "In the format of C6H12O6 for instance\n"
                                "And returns the molar mass of that compound\n"
                                "It does not implicitely work with polyatomic ions\n"
                                "And to calculate the molar mass of such a compound\n"
                                "One must multiply through the parenthesis\n"
                                "For instance 'Ca(OH)2'\n"
                                "Would be simplified as 'CaO2H2' for the purposes of the function\n"
                                )
                        case "gramstomoles":
                            print(
                                "\n"
                                "The grams to moles function takes a number of grams\n"
                                "Along with the compound being measured\n"
                                "And outputs the moles\n"
                                "It has the same restrictions as the 'molemass' function\n"
                                "Please refer to the molemass function for more info\n"
                                )
                        case "molestograms":
                            print(
                                "\n"
                                "The moles to grams function takes a number of moles\n"
                                "Along with the compound being measured\n"
                                "And outputs the grams\n"
                                "It has the same restrictions as the 'molemass' function\n"
                                "Please refer to the 'molemass' function for more info\n"
                                )
                        case "molestoparticles":
                            print(
                                "\n"
                                "The moles to particles function takes a given number of moles\n"
                                "And outputs the appropriate number of particles\n"
                                )
                        case "particlestomoles":
                            print(
                                "\n"
                                "The particles to moles function takes a given number of particles\n"
                                "And outputs the appropriate number of moles\n"
                                )
                        case "approximate":
                            print(
                                "\n"
                                "The approximate function converts decimals to fractions\n"
                                "The approximate function takes 3 inputs\n"
                                "The decimal as input one\n"
                                "The precision as input two\n"
                                "And the mode as input three\n"
                                "The decimal can be any real number\n"
                                "The precision is the number of decimal places to which the function will approximate (enter 0 for exact approximation)\n"
                                "And the mode defines how the output is displayed\n"
                                "The modes include 'improper' and 'mixed'\n"
                                "As well as debug modes which should be used sparringly\n"
                                )
                        case "gcd":
                            print(
                                "\n"
                                "The gcd function approximates the greatest common devisor of two numbers\n"
                                "For its input please input the larger number first and the smaller one second\n"
                                )
                        case "lcm":
                            print(
                                "\n"
                                "The lcm function finds the least common multiple of two numbers\n"
                                )
                        case "quadzeros":
                            print(
                                "\n"
                                "The quadzeros function outputs the zeros of a quadratic\n"
                                "The input is the a b and c values of that quadratic\n"
                                )
                        case "inttoroman":
                            print(
                                "\n"
                                "The inttoroman function converts integers to roman numerals\n"
                                )
                        case "basea":
                            print(
                                "\n"
                                "The basea function takes a base 10 integer\n"
                                "As well as a different base\n"
                                "And outputs the equivalent integer for that base\n"
                                )
                        case "calculate":
                            print(
                                "\n"
                                "The calculate function acts as a basic calculator\n"
                                "Though it doesn't support advanced functions like square root\n"
                                )
                        case "unitconversion":
                            print(
                                "\n"
                                "The unitconversion function converts between any two supported units\n"
                                )
                            unitlist = input("Would you like a list of units (yes/no):\n")
                            if unitlist == "yes":
                                print(
                                    "\n"
                                    "Inches, Feet, Yards, Miles, Millimeters, Centimeters, Meters, Kilometers, as well as likewise mass, time and temperature units\n"
                                    )
                        case "ApproximateIntegration":
                            print(
                                "\n"
                                "Approximate integration uses the summation definition of an integral\n"
                                "To approximate a numerical value for the integral within specified bounds\n"
                                )
                        case _:
                            print(
                                "\n"
                                "invalid function\n"
                                )
                    
                    info = input("Would you like info on another function (yes/no):\n")
                    
                    if info == "yes":
                        
                        info = input("please input the function name:\n")
            
            f = input("Would you like to use one of these functions (yes/no):\n")
            
            if f == "yes":
                
                function = input("Please input the function name:\n")
            
                while f != "no":
                
                    match function:
                        case "gmole":
                            element = input("Please input the element:\n")
                            l = gmole(element)
                            print(
                                "\n"
                                f"{l}"
                                "\n"
                                )
                        case "molemass":
                            compound = input("Please input the compound:\n")
                            l = molemass(compound)
                            print(
                                "\n"
                                f"{l}"
                                "\n"
                                )
                        case "gramstomoles":
                            compound = input("Please input the compound:\n")
                            grams = input("Please input the grams:\n")
                            grams = float(grams)
                            print(
                                "\n"
                                f"{gramstomoles(compound, grams)}"
                                "\n"
                                )
                        case "molestograms":
                            compound = input("Please input the compound:\n")
                            moles = input("Please input the moles:\n")
                            moles = float(moles)
                            print(
                                "\n"
                                f"{gramstomoles(compound, moles)}"
                                "\n"
                                )
                        case "molestoparticles":
                            moles = input("Please input the moles:\n")
                            moles = float(moles)
                            print(
                                "\n"
                                f"{molestoparticles(moles)}"
                                "\n"
                                )
                        case "particlestomoles":
                            particles = input("Please input the particles:\n")
                            particles = float(particles)
                            print(
                                "\n"
                                f"{particlestomoles(particles)}"
                                "\n"
                                )
                        case "approximate":
                            decimal = input("Please input the decimal you would like to convert:\n")
                            precision = input("Please input the precision you'd like for the conversion:\n")
                            mode = input("Please input the desired mode:\n")
                            if mode == "improper" or mode == "mixed":
                                print(
                                    "\n"
                                    f"{approximate(decimal, precision, mode)}"
                                    "\n"
                                    )
                            else:
                                print(
                                    "\n"
                                    "Invalid mode\n"
                                    "If you were attempting to use a debug mode\n"
                                    "Please type directly into the input\n"
                                    "As this form of the program cannot access debug modes\n"
                                    )
                        case "gcd":
                            n1 = input("Please input the higher number:\n")
                            n2 = input("Please input the lower number:\n")
                            n1 = int(n1)
                            n2 = int(n2)
                            print(
                                "\n"
                                f"{gcd(n1, n2)}"
                                "\n"
                                )
                        case "lcm":
                            n1 = input("Please input the first number:\n")
                            n2 = input("Please input the second number:\n")
                            n1 = int(n1)
                            n2 = int(n2)
                            print(
                                "\n"
                                f"{lcm(n1, n2)}"
                                "\n"
                                )
                        case "quadzeros":
                            a = input("Please input a for your quadratic:\n")
                            b = input("Please input b for your quadratic:\n")
                            c = input("Please input c for your quadratic:\n")
                            a = float(a)
                            b = float(b)
                            c = float(c)
                            print(
                                "\n"
                                f"{quadzeros(a, b, c)}"
                                "\n"
                                )
                        case "inttoroman":
                            integer = input("Please input the integer:\n")
                            integer = int(integer)
                            print(
                                "\n"
                                f"{inttoroman(integer)}"
                                "\n"
                                )
                        case "basea":
                            integer = input("Please input the base 10 integer:\n")
                            base = input("Please input the desired base:\n")
                            integer = int(integer)
                            base = int(base)
                            print(
                                "\n"
                                f"{basea(integer, base)}"
                                "\n"
                                )
                        case "calculate":
                            calc = input("Please input your calculation:\n")
                            print(
                                "\n"
                                f"{calculate(calc)}"
                                "\n"
                                )
                        case "unitconversion":
                            number = input("Please input the number for the initial unit:\n")
                            fromunit = input("Please input the initial unit:\n")
                            tounit = input("Please input the final unit:\n")
                            print(f"\n{unitconversion(number, fromunit, tounit)}\n")
                        case "ApproximateIntegration":
                            lowbound = input("Please input the leftmost bound of x:\n")
                            upbound = input("Please input the rightmost bound of x:\n")
                            slices = input("Please input the number of slices the function should use:\n")
                            fun = input("Please input the function in terms of x:\n")
                            print(f"\n{ApproximateIntegration(lowbound, upbound, slices, fun)}\n")
                        case _:
                            print(
                                "\n"
                                "Invalid function"
                                "\n"
                                )
                    
                    f = input("Would you like to use another function (yes/no):\n")
                    
                    if f == "yes":
                        
                        function = input("Please input the function name:\n")
                    
        case _:
            print(
                "\n"
                "Unrecognized Query\n"
                )
    
    query = input("What is your query (input 'end' to end): \n")

