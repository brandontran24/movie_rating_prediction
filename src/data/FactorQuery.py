import requests #used for query
import json     #used for parsing data
import datetime #used to get current date
import copy
from data.SaveLoadJson import SaveLoadJson
from data.Search import Search

class FactorQuery:
    debug = False
    filename = 'parameters.txt'
    api_key_file = 'api_keys.txt'
    outputFile = 'ratings.txt'
    
    resultStruct = {
                    "name":"",
                    "total_works":0,
                    "works":[]
                     }

    dateMovie = 0
    
    def getPerson(id, api_key):
        response = requests.get("https://api.themoviedb.org/3/person/" + str(id) + "/combined_credits?api_key=" + api_key + "&language=en-US") #query
        if(response.status_code != 200):
            return "NULL"
        
        return response.json() #parse data into json

    def getName(id, api_key):
        response = requests.get("https://api.themoviedb.org/3/person/" + str(id) + "?api_key=" + api_key + "&language=en-US")
        if(response.status_code != 200):
            return "NULL"
        
        return response.json()["name"]

    def getMovie(id, api_key):
        response = requests.get("https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=" + api_key + "&language=en-US") #query
        if(response.status_code != 200):
            return "NULL"
        
        return response.json() #parse data into json


    # Get Job -----------------------------------------------------
    def getJob(id, api_key, job):

        now = datetime.datetime.now()                                   #get current time to compare release date to
        total = 0                                                       #int for total works
        data = FactorQuery.getPerson(id, api_key)
        results = copy.deepcopy(FactorQuery.resultStruct)

        for val in data["crew"]:                                                                        #loop through all keys in json dictionary
            if(val["media_type"] == "movie" and val["job"] == job and "release_date" in val):    #check movie type, if director, and contains release date						#divide release date up into comparable parts
                dateNow = int(str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2))
                date = dateNow
                if FactorQuery.dateMovie != 0:
                    dateNow = FactorQuery.dateMovie
                if(val["release_date"] != ""):
                    date = int(val["release_date"].replace("-", ""))                                    #TODO: replace dateNow with date of movie being looked at
                if(dateNow > date):
                    rating = "0\t0\t0\t0\n"
                    temprating = Search.find(val["id"])
                    if temprating != "NULL":
                        rating = temprating
                    rating = rating.split('\t')                        
                    temp = {"title":val["original_title"],                                              #create a temp dict with wanted values
                            "rating":rating[2],
                            "votes":rating[3][:-1],
                            "release_date":val["release_date"]}     
                    results["works"].append(temp)                                                       #add temp dict to list of all works
                    total += 1                                                                          #add work to total

        results["total_works"] = total;#add total to list of works
        results["name"] = FactorQuery.getName(id, api_key)
        if FactorQuery.debug == True:
            print("Found " + str(total) + " work(s) for " + results["name"])
        return results                                                                                  #return json data

    # Get Actor -----------------------------------------------------
    def getActor(id, api_key):
        
        now = datetime.datetime.now()
        total = 0
        data = FactorQuery.getPerson(id, api_key)
        results = copy.deepcopy(FactorQuery.resultStruct)

        for val in data["cast"]:
            if(val["media_type"] == "movie" and "release_date" in val):                                 #check movie type, if director, and contains release date
                dateNow = int(str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2))          #TODO: replace dateNow with date of movie being looked
                date = dateNow
                if FactorQuery.dateMovie != 0:
                    dateNow = FactorQuery.dateMovie
                if(val["release_date"] != ""):
                    date = int(val["release_date"].replace("-", ""))
                if(dateNow > date):                                                                     #check if movie has been released yet....
                    rating = "0\t0\t0\t0\n"
                    temprating = Search.find(val["id"])
                    if temprating != "NULL":
                        rating = temprating
                    rating = rating.split('\t')                        
                    temp = {"title":val["original_title"],                                              #create a temp dict with wanted values
                            "rating":rating[2],
                            "votes":rating[3][:-1],
                            "release_date":val["release_date"]}     
                    results["works"].append(temp)                                                       #add temp dict to list of all works
                    total += 1    
                    
        results["total_works"] = total;
        results["name"] = FactorQuery.getName(id, api_key)
        if FactorQuery.debug == True:
            print("Found " + str(total) + " work(s) for " + results["name"])
        return results

    # Get Department -----------------------------------------------------
    def getDepartment(id, api_key, department):

        now = datetime.datetime.now()                                   #get current time to compare release date to
        total = 0                                                       #int for total works
        data = FactorQuery.getPerson(id, api_key)
        results = copy.deepcopy(FactorQuery.resultStruct)

        for val in data["crew"]:                                                                        #loop through all keys in json dictionary
            if(val["media_type"] == "movie" and val["department"] == department and "release_date" in val):    #check movie type, if director, and contains release date						#divide release date up into comparable parts
                dateNow = int(str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2))
                date = dateNow
                if FactorQuery.dateMovie != 0:
                    dateNow = FactorQuery.dateMovie
                if(val["release_date"] != ""):
                    date = int(val["release_date"].replace("-", ""))                                    #TODO: replace dateNow with date of movie being looked at
                if(dateNow > date):
                    rating = "0\t0\t0\t0\n"
                    temprating = Search.find(val["id"])
                    if temprating != "NULL":
                        rating = temprating
                    rating = rating.split('\t')                        
                    temp = {"title":val["original_title"],                                              #create a temp dict with wanted values
                            "rating":rating[2],
                            "votes":rating[3][:-1],
                            "release_date":val["release_date"]}     
                    results["works"].append(temp)                                                       #add temp dict to list of all works
                    total += 1                                                                          #add work to total

        results["total_works"] = total;#add total to list of works
        results["name"] = FactorQuery.getName(id, api_key)
        if FactorQuery.debug == True:
            print("Found " + str(total) + " work(s) for " + results["name"])
        return results                                                                                  #return json data

    # Get Factor ------------------------------------------------------    
    def getFactors(debug=False):
        FactorQuery.debug = debug
        if debug == True:
            print("Getting factors")
        api_key = SaveLoadJson.load(FactorQuery.api_key_file)["TMDB"]["key"]                         # get api key to be used for all queries
        parameters = SaveLoadJson.load(FactorQuery.filename)                                                #set data to something to prevent error
        
        data = {
            "Directors":[],
            "Actors":[],
            "Writers":[],
            "Producers":[]
            }
        if "Date" in parameters:
            FactorQuery.dateMovie = parameters["Date"]

        if "Directors" in parameters:
            if debug == True:
                print("Getting works for " + str(len(parameters["Directors"])) + " director(s)")
            for dctr in parameters["Directors"]:
                data["Directors"].append(FactorQuery.getJob(dctr, api_key, "Director"))
        if "Actors" in parameters:
            if debug == True:
                print("Getting works for " + str(len(parameters["Actors"])) + " actor(s)")
            for actr in parameters["Actors"]:
                data["Actors"].append(FactorQuery.getActor(actr, api_key))
        if "Writers" in parameters:
            if debug == True:
                print("Getting works for " + str(len(parameters["Writers"])) + " writer(s)")
            for wrtr in parameters["Writers"]:
                data["Writers"].append(FactorQuery.getDepartment(wrtr, api_key, "Writing"))
        if "Producers" in parameters:
            if debug == True:
                print("Getting works for " + str(len(parameters["Producers"])) + " producer(s)")
            for prdcr in parameters["Producers"]:
                data["Producers"].append(FactorQuery.getDepartment(prdcr, api_key, "Producer"))
        #print(json.dumps(data, indent=2))
        SaveLoadJson.save(FactorQuery.outputFile, data)
