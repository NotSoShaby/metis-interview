# metis-interview
Refael's Interview project for Metis Data


# prequisites

install docker-compose as shown in the documentations [here](https://docs.docker.com/compose/install/)

# Set up & run the project
clone the repo:

`$ git clone git@github.com:NotSoShaby/metis-interview.git`

go into project directory:

`$ cd metis-interview`


build the container and run the server using docker-compose:

`$ docker-compose up`

Note: the first time will build the container from scratch and will take a few minutes.

# test

Use any browser or HTTP tool (such as postman) to run the Exceptence tests on `http://127.0.0.1/` (note that `localhost` is not an allowed host) 

for example, go to your browser and run `http://127.0.0.1:8000/facts/?tableName=Students`




# A bit about the project and choices I made

I decided to use the [django-rest framework](https://www.django-rest-framework.org/) (which is an extention of the very famous [django](https://docs.djangoproject.com/en/4.0/) open source framework) to build this server as it gives a lot out of the box while allowing a lot of flexibilty and scale. 

I've created a custom Dockerfile and added docker-compose for easy and scalable delivery. Editing and saving the code locally will update and rerun the code in the container automatically for easy development. 

Most of the code is self explained as I believe in clean code. Where I thought clarification is needed, I added in comments in the code. 

Logging: I used the django logger as its works and integrates very well with python's logging package. 
I created a custom decorator inside the Utils class that logs every function that will be decorated with it and will also log execution time for that function. 
log file will be created in the `MetisInterview/logger.log` location. 
Currently log level is `INFO`, this can be changed in the settings.py to allow more\less verbose logging. 

Conditional results as suggested in the bunos section of the tasks were added. 

One unit test was added but it fails as django does not allow the main db to be used for tests and I didn't have time to arrange an automatic test db to be created.



Please feel free to let me know if you have any more questions/issues about the projects.

Lets kick some ass ;)
