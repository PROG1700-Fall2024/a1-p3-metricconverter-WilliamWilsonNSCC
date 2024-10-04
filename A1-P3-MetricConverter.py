#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

"""
Student Name: William Wilson
Program Title: Logic and Programming
Description: Assignment 1 Metric Converter
"""

def main():
    # numbers of tons, stones, pounds, and ounces are input by the user
    tons= int(input("1"))
    stones=int(input("2"))
    pounds=int(input("3"))
    ounces=int(input("4"))
    
    #total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces 5/20/2/4
    totalOunces=35840*tons+224*stones+16*2+ounces
    # print(totalOunces)
    
    # total kilos = total ounces / 35.274
    totalKilos= totalOunces/35.274
    # print(totalKilos)
    
    # metricTons= Kilos/1000
    metricTons= int(totalKilos/1000)

    #1 ton = 1000kg 
    kilos= (totalKilos%1000)
    print(kilos) #288
    
    #1kilo = 1000grams
    remainder= kilos%int(kilos)
    print(remainder)
    
    grams= remainder * 1000
    print(grams)
    
    # output metric weight in tons, kilos, and grams
    print("The metric weight is {0} metric tons, {1:.0f} kilos, and {2:.1f} grams".format(metricTons, kilos, grams))
    
    # YOUR CODE ENDS HERE

main()