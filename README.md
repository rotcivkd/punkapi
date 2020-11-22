# punkapi

# prerequisite
To run this code below mentioned python libraries should be installed as "prerequisite"

requests

json

sys

# Installation 
a. Download ".py" file to local desktop

b. Open the command prompt or anaconda prompt

c. Change the directory to where python code is downloaded (example: cd C:\Users\Victor\Desktop\punkapi)

d. This code can be executed locally via CLI by using below mentioned run command
	

> **1. Requirement - Get a beer list brewed between a give date interval**

> punkapi.py beer-list from=10-2011 until=12-2020 <Output Location where to write the results>

> _Run Command: punkapi.py beer-list from=10-2011 until=12-2020 C:\Users\Victor\Desktop\punkapi_

> **2. Requirement - Given a beer id, retrieve all data of a beer with that exact id**

> punkapi.py beer-id <Give a beer id> <Output Location where to write the results>

> _Run Command: punkapi.py beer-id 10 C:\Users\Victor\Desktop\punkapi_

> **3. Requirement - Given a beer name, retrieve the beers with partial match of the name**

> punkapi.py beer-name <Give a beer name> <Output Location where to write the results>

> _Run Command: punkapi.py beer-name Buzz C:\Users\Victor\Desktop\punkapi_
