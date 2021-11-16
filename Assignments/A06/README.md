http://167.99.6.44:8003/

# What is this project:
  - This project is an introduction to mongo db using resteraunt data based out of NYC. This also uses geo spacial data for querries to find places in a specific radius around a given area of the other resteraunts. This also showed how you can upload entire JSON files into mongo unlike SQL where you would need to import one row at a time.

# Why is this project important:
  - This project is important in that it:
      - Showed me the benefits to that of mango versus other databases
      - Introduced me to a new query style completly diffrent the the typical SQL that I was used to
      - Showed me that there is a way to use coordinate data to find spacial data
      - Introduced me to the power of JSON and it O(1) lookup time
      - Showed the downside of mango in its security and it's openess
      - Gave me an inroduction to the ease that mango comes with
      - Showed me the pain in error checking with how mongo will do anything

# Where did I struggle doing this project:
  - I struggled at first learning how indexes work with mango id's
  - I struggled with how there are no real errors with running queries and making tables with mongo
  - I struggled with the new query style that comes with mongo  
  - I struggled to understand why the FastAPI would not work with how mongo Id objects are formated
  - I struggled with locking down my server and making it secure

# What issues did I enconter:
  - Some issues that I encountered were: 
    - FastAPI doesnt work with the object id in mongo
    - Some querries that would return nothing becuase I messed up spelling
    - Installing mongo properly on my server 
    - Learning a new library to do mongo queries
    - Understanding the data given with the vagueness of the columns

# What I did to combat these issues:
  The biggest thing that I did to combat all of these issues was to read the documentation for both mongo and the libraries I used. Reading many forum posts that would help me to realize where it is that I was going wrong and to guide me back on the right track. I also decided to get a book on mongo so that I could get and expert opinion on how to query and the common practices of mongo. Lastly, asking my professor and classmates for help with mongo really assisted me in getting my task done.

# How was this project relevant to the real world:
  - This project is relevent to the real world in that it uses a new database that is more guided to that of effiecincy and using the right tools for the task.
  - It is also relevent in that it uses geospacial data to help the users find resteraunts close to them
  - It is also relevent in that it used to speed up the time of development with loading a file directly into the database
