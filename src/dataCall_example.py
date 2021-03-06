import json
from data.FactorQuery import FactorQuery as FQ
from data.SaveLoadJson import SaveLoadJson as SLJ
from data.GetParameters import GetParameters as GP

# Replace with statistics script -----------------------------------------------
from models.myStats import myStats as stats
# ------------------------------------------------------------------------------

movie = "0"

while movie != "":
    print(" ")
    movie = input("Enter a movie name! \n")
    print(" ")

    GP.find(movie,debug=True) #Danielle and Brandon's code

    FQ.getFactors(debug=True) #get ratings for those parameters //my code

    stats.analyze() #the ratings and get rating #Ari, Ivy, Jake's code
