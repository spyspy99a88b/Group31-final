### Squirrel Tracker Web Application -- Tools For Analytics Section 2, Group 31

#### Description:
This web application provides: 
1. An OSM-based map of the squirrels' sighting locations in Central Park. 
2. A visualization of the squirrel sighting database which allows users to update or add sightings, and can print a summary of important stats. 

#### Notes:
1. The sighting map displays exactly 100 sightings.
2. The summary stats includes the following attributes:   
	max longitude, min latitude, latest date, counts for age and counts for primary fur color. 
3. Database Settings:  
	usi(Unique Squirrel ID), Primary Key  
	date, type = DateField<br/>    	
	latitude, type = DecimalField  
	location, type = CharField  
	
#### Admin users:  
user1:spy  
password:123456  
user2:fugarli  
password:123456  

#### Group Name and Section:  
Project Group 31, Section 002

#### Team Member UNIs:  
UNIs: ps3142, sl4654
    
#### Link to Application:  
For location map visit: https://squirrel-261302.appspot.com/map/  
For list of sightings visit : https://squirrel-261302.appspot.com/sightings/

### Side Notes For Graders:  
1. We are sorry for the millions of ++s and --s in the summary page because we mistakenly included pycache files in early commits. We have shown the commit history to Professor on Saturday and he said this was fine.
2. Our app folder locates in the deeper diretory "final project/", not at the root. Sorry for any inconvinence. Also, as required in the specs, we have also copied the database file to the root of the repo just in case.
Thank you!


