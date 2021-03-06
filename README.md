![Alt text](/TitlePoster.png?raw=true "Movie Rating Prediction")
# REEL RATINGS
### Contributors: 
+ Andrew Polk
+ Ari Gilmore
+ Brandon Tran
+ Danielle Robinson
+ Ivy Tran
+ Jake Hickey
+ Victoria Sneddon (Project Manager)

## Abstract
We want to be able to predict the rating of a movie before it is released. We want to be able to input a movie or upcoming movie title and output the predicted movie rating.
#
# Table of Contents
* [Flowchart](#flowchart)
* [Aspects](#aspects)
* [Datasources](#datasources)
* [Languages](#languages)
* [Blockers](#blockers)
* [Setting Up Virtual Environment](#virtenv)
* [Running the Code](#runcode)
* [Structure](#structure)
<details><summary>Timeline</summary>
<details><summary>Fall 2017</summary>
	
* [Week 1-3](#weekone-three)
* [Week 4-6](#weekfour-six)
* [Week 7-10](#weekseven-ten)
</details>

[Winter 2018](#winterquarter)
</details>
	

# <a name='flowchart'></a>Project Flowchart
![Alt Text](/MovieRatings.png?raw=true "flow chart")

# <a name='aspects'></a>Aspects
+ Rotten Tomatoes API (Kaggle, IMDB) -previous movies of that genre and their rating
+ Data Algorithms (weighting actors vs. directors vs. budget…)
+ Query data about movie title or movie id to get parameters 
+ Query previous ratings of rating parameters
+ Create a method of storing data and accessing it from different parts of the program 
+ Some sort of statistical analysis on ratings (Data algorithms) 
+ Create an interface or web app to take input and display results
#
+ Paramaters available to use: 
  + Average movie rating
  + Actors
  + Director
  + Producers
  + Budget
  + Studio
  + Writers
  + Genre
  + Cinematographer
  + Music
  + etc..

# <a name='datasources'></a>Data Sources
+ IMDb
+ TheMovieDB

# <a name='languages'></a>Languages
+ Python - scripting
+ HTML - website
+ Java - AWS API

# <a name='blockers'></a>Blockers
+ TheMovieDB has a 40 query per 10 second limit per api key.
+ AWS requires paid subscription
+ IMDb data must be refreshed manually

# <a name='virtenv'></a>Creating a virtual environment
+ ### First time run:
   	+ > sudo apt install virtualenv (if needed)
   	+ > virtualenv peerenv
+ ### Starting virtualenv
   	+ > source peerenv/bin/activate
	+ > pip install -r requirements.txt
+ ### Closing virtualenv
	+ > deactivate

# <a name='runcode'></a>Running the code
+ ### Make sure you have:
	+ api_keys.txt
	+ IMDBRatings.tsv
	+ TMDBRatings.tsv
+ ### Running in terminal
	+ Start virtual environment
	+ > cd movie_rating_prediction/src/
	+ > python3 dataCall_example.py
	+ Enter Movie Name
+ ### Running in Idle
	+ Start virtual environment
	+ > cd movie_rating_prediction/src/
	+ > idle3
	+ Open dataCall_example.py
	+ Run Module
	+Enter Movie Name

# Project Timeline
  ## <a name='fallquarter'></a>Fall 2017
  ## <a name='weekone-three'></a>Week 1-3:
  + Create an outline for the project
  + Split into smaller groups (Pair up)  to work on individual sections of the project
  + ### Week 1-3 Update:
  	+ #### Brandon/Danielle:
		+ Made an account for Amazon Web Services (AWS)
		+ Downloaded AWS SDK for Java
		+ Downloaded legacy Java 6 for Eclipse
		+ Downloaded JVM 1.8 for Eclipse
		+ Configured AWS Toolkit for Eclipse, and samples successfully
		+ https://569112368633.signin.aws.amazon.com/console log in
  	+ #### Ari/Ivy/Jake:
		+ Will weight the ratings of directors previous films based on date.
		+ Take the sample mean of the ratings of the director’s movies and that will be the prediction
		+ Award data? (how many oscars won) (later)
		+ Age of the director (later)
		+ Regression chart for when other factors come in
  	+ #### Andrew/Victoria:
		+ Created a simple script in python, using libraries: json, requests, datetime
		+ The script accesses themoviedb and get the works and ratings for a director parsed into json
		+ Working on ways to pass the information from the script to the stats team
		+ Still need to get director age, awards and any other data the stats team wants
		+ Get data from rottenTomatoes/IMDB ect...?

  ## <a name='weekfour-six'></a>Week 4-6:
  + Start putting together the different portions that the smaller groups have been working on
  + ### Week 4-6 Update:
  	+ #### Brandon/Danielle:
		+ Downloaded IMDb's datasets using AWS S3 services
		+ Gave Andrew the data to merge
  	+ #### Ari/Ivy/Jake:
		+ Considering date of directors' previous movies as a factor in rating
		+ Using number of ratings per movie rating to calculate mean value of directors' previous films
  	+ #### Andrew/Victoria:
		+ Created script to access IMBDb's title names, ratings, etc.
		+ Created script to merge ratings and title info tsv files
		+ Will utilize both Movie DB and IMDb as foundation of project's data
		
  ## <a name='weekseven-ten'></a>Week 7-10:
  + Finish merging different sections of the project
  + ### Week 7-10 Update:
  	 + #### All:
  		+ Wrote data regression algorithm to weigh directors' previous films
		+ Wrote scripting programs to input movie ID number and output parameters
  #
  ## <a name='winterquarter'></a>Winter 2018
  ## <a name='goals'></a>Goals:
  + Finish scripting programs to fetch parameters from movie names
  + Focus on documentation, here and on Inertia7

# <a name='structure'></a>Structure

	├── LICENSE
	├── README.md          <- The top-level README for developers using this project.
	│
	├── data	<- We cant save the data online so this is empty
	│   ├── external       <- Data from third party sources.
	│   ├── interim        <- Intermediate data that has been transformed.
	│   ├── processed      <- The final, canonical data sets for modeling.
	│   └── raw            <- The original, immutable data dump.
	│
	├── references         <- Data dictionaries, manuals, and all other explanatory materials.
	│
	├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
	│   └── figures        <- Generated graphics and figures to be used in reporting
	│
	├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
	│                         generated with `pip freeze > requirements.txt`
	│
	└── src                <- Source code for use in this project.
	    ├── __init__.py    <- Makes src a Python module
	    ├── dataCall_example.py    <- Whole script run from here
	    │
	    ├── api_keys.txt 	<- stores api keys to be used in query (Not online)
	    ├── IMDBRatings.tsv <- stores the ratings sorted by IMDB ids
	    ├── TMDBRatings.tsv <- stores the ratings sorted by TMDB ids
	    │
	    ├── data           <- Scripts to download or generate data
	    │   └── GetParamters.py 	<- downloads parameters from movie name
	    │   └── FactorQuery.py 	<- downloads paramter info and finds movie ratings
	    │   └── LineCount.py 	<- counts the lines in a file, used for searching IMDB ratings
	    │   └── Search.py 		<- searches the IMDB rating files with either IMDB id or TMDB id
	    │   └── SaveLoadJson.py 	<- standardizes the saving and loading of Json data between scripts
	    |
	    ├── models         <- Scripts to train models and then use trained models to make
	    │   │                 predictions
	    │   └── Stats.py <- generates some guess based on ratings.txt
	    │
	    └── visualization  <- Scripts to create exploratory and results oriented visualizations
	        └── visualize.py
