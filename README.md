# code-foo-backend
This is my submission for IGN Code Foo 2022, a sample backend API service.


### But first, a little about me!
I'm Joseph Barroso, a Computer Science major studying @ IIT at the tail end of my second year. A few of my main interests are biking, gaming, and programming!

After hearing that, it's probably not too surprising that I was interested in applying for an internship opportunity at IGN. I've known about IGN for a long time now seeing as it is heavily involved with gaming related news and happenings, and I think the only thing that sounds better than a programming internship is a programming internship at a gaming-adjacent company. =]

### Why should you choose me to participate?
One reason I am an ideal candidate is because I look forward to learning new languages, technologies and frameworks, and I pick them up quickly! This project demonstrates that; I learned the Python frameworks *FastAPI* and *pytest* to put this project together because I felt that they were the best tools for the task.

As the name implies, FastAPI is focused on making a simple yet effective process for creating basic but extendable REST APIs. As for pytest, I wanted to practice Test Driven Development during the making of this project so I could be sure of things like the proper data being exposed for the API's endpoints. Three hundred and forty seven entries of data are a few too many to effectively manually parse to ensure proper behavior.

Another reason I'm a great choice for the program is that I am eager to work on any given project with a team! I would be very beneficial to the team I work with because I am well-spoken, excellent at articulating specific issues I run into if I hit a wall, and above all, I place great importance on treating others respectfully and kindly.

And when I say *any* project, I mean it; I have relatively equal interest in mobile app development, web development (both front end and back end), more specific services such as APIs, etc. I would honestly love to learn much more about any of these focuses.


# Hisui's Power Plant!
Professor Laventon has requested my help, and I will not disappoint. Here is my plan to complete the objective:

### 1. Gather concrete requirements
How am I supposed to figure out how many Voltorbs I need to catch without even knowing how much power the power plant needs to generate? Thus, step one is to speak to the Galaxy Team about a specific range in terms of the amount of power they'll need this new plant to generate. Specific project requirements are important.

### 2. Conduct experiments!
We're not trying to waste time here. Because of this, it doesn't sound like a great idea to go to the Sacred Plaza, catch an arbitrary number of Voltorbs and leave, hoping that they end up being sufficient enough for the amount of power we require! To avoid this scenario, I think it would be best to run tests to figure out how much power a single Voltorb can generate over a given time period, i.e. for one day. Only then can we come up with an estimate on how many Voltorb's the power plant will require in order to generate enough power.

### 3. Acquire the Voltorb's!
After we have a good idea of how many Voltorb's the power plant will require, it only makes sense to collect the Voltorb's required (of course, in the most efficient and feasible manner!).

Finally, we'll have collected and transported all the necessary Voltorb's to the power plant. They'll produce the required electricity in exchange for being treated well, far past the standards set by the ethical committee.


# The Project
This project is a **FastAPI** application, making use of an **sqlite3** database to store the data the API's endpoints expose! It is also unit tested with **pytest** to ensure the application exhibits expected behavior. **Pandas** also plays a role, reading the given csv file into a dataframe which is then input into a table in the **sqlite3** database. 

Because of the library taking care of parsing the csv file into an SQL table, I did not have to put much thought into parsing the original data past making sure that no data was being lost in the process.

### How do I properly start the service?
Dependencies are required in order to use the application! You can install them (I recommend doing it in a virtual environment) by using the command ```py -m pip install -r requirements.txt``` on Windows, or ```python -m pip install -r requirements.txt``` on Unix/macOS, per the pip docs.

Next, start it up in the command line using the following command: ```uvicorn main:app --reload```. This will run a local server at the address ```http://127.0.0.1:8000```. This can be accessed through any web browser.

Here are the available endpoints the application offers:

**/score/** - returns all media entries, sorted by the order of their IGN review scores!

**/id/{id}** - returns a single entry based on it's id; valid ids range from 1 to 347, inclusive.

**/type/{type}** - returns all entries of a queried type; valid inputs include *Movie*, *Show*, *Comic*, and *Game*.

For example, if you would like to see data on the 47th media entry, enter the following URL in your browser: **http://127.0.0.1:8000/id/47/**
Of course, it's not the prettiest sight or easy to read, but it's made for other programs to read the data and use so that's okay. =]


### How do I run the unit tests?
There are two files with tests in them, ```api_test.py``` and ```db_test.py```. The tests in a single file can either be ran individually, or all tests written across both files can be ran simultaneousely. Before all tests can properly pass, **make sure to begin the local server.** The tests making sure the API returns correct data and gives expected response codes will fail if requests cannot be made to the local server.

In order to run all tests at once, simply use the command line command ```pytest tests/```. If you would like to run the tests only in a given file, use ```pytest tests/db_test.py``` or ```pytest tests/api_test.py```.


### Implementation Details
For the three sample endpoints, I felt as though it were logical to represent three different situations; one where the user wants a specific entry (the /id/ endpoint), another where the user wants a set of data based on specific grouping (the /type/ endpoint), and finally one where all media entries are returned (the /score/ endpoint).

Following typical REST API protocols, each endpoint responds with a status code of 200 by default, but in the case where an invalid parameter is given, i.e. an attempt to reach /id/500 is made, but only 347 entries exist, a status code of 404 will be returned instead. This signals that the data that the user was looking for is not found. This can also arise if invalid input is given to the *type* endpoint.

On more specific matters, I split up operations more focused on the user-facing side of the API versus the internal database implementation into several modules (main.py and database.py respectively) because it becomes far easier to extend existing functionality when portions of code focused on separate general topics are compartmentalized.

Finally, I decided to write unit tests covering both the data in the database, and the data that the API returns because, among other benefits, proper tests allow you to be more confident that a certain piece of any given program still works as expected after changing the way it works. It isn't a silver bullet for preventing all bugs in a program, but it can certainly help prevent them, or at the very least give its maintainers a better understanding of their source.