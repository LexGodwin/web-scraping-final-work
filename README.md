 ![header](https://user-images.githubusercontent.com/68532133/140015898-0e3d123c-3fb6-4113-9723-ea4c4147fcf0.png)
  
  #  installing  
  
_for running the projcet one must have the lastest vision of anaconda programming. to download  anaconda programming one should go to google and put  anacondaand download it and install it on your computer run anaconda as **Admin** open it and yourready to Go when the anaconda opens open jupyterNoteBook to run the project_ 

## How to run the project 
_COPY THE CODE BELOW_
```python 

from bs4 import BeautifulSoup
import  requests
import csv
import pandas as pd

url ="https://www.webometrics.info/en/africa/uganda?sort=asc&order=World%20Rank"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
university_table = soup.find('table',class_ = 'sticky-enabled')
data = []

for university in university_table.find_all('tbody'):
    rows = university.find_all('tr')
    for row in rows:
        ug_rank = row.find_all('td', class_ = '')[0].text
        world_rank = row.find_all('td',class_ = '')[1].text
        univervesity_name = row.find_all('td',class_ = '')[2].text
        impact_rank = row.find_all('td',class_ = '')[4].text
        opennes_rank = row.find_all('td',class_ = '')[5].text
        excellence_rank = row.find_all('td',class_ = '')[6].text        
              
        data.append((ug_rank,world_rank,univervesity_name,impact_rank,opennes_rank,excellence_rank))     

df = pd.DataFrame(data,columns=['Ug. Ranking', 'Worl Ranking', 'University Name','Imapct Rank','Oppennes Rank','Excellence Rank'])
df.to_csv('D:/webscraping/uni.csv',index = False,encoding = 'utf-8')
```
_copy the code above And pate the code in jupyterNoteBook in the anaconda ide then create a new project of pyhon in it and name it anyt title of your choice and run the code code, the ``code`` will run thus copying  all the data from the website into a csv file format that is stored on to the computer_
``NOTE the best web broswer to use to run the project is google chrome ``

## link 
 [Visit webstie](https://www.webometrics.info/en/africa/uganda?sort=asc&order=World%20Rank "click me") 

## Building
_In order to build the TypeScript compiler, ensure that you have Git and Node.js installed Clone a copy of the repo_

_[git clone] (https://github.com/microsoft/TypeScript.git)
Change to the TypeScript directory_
```
cd TypeScript
Install Gulp tools and dev dependencies:

npm install -g gulp
npm ci
```

#### use one of the folowing to build and test:
```
gulp local             # Build the compiler into built/local.
gulp clean             # Delete the built compiler.
gulp LKG               # Replace the last known good with the built one.
                       # Bootstrapping step to be executed when the built compiler reaches a stable state.
gulp tests             # Build the test infrastructure using the built compiler.
gulp runtests          # Run tests using the built compiler and test infrastructure.
                       # You can override the specific suite runner used or specify a test for this command.
                       # Use --tests=<testPath> for a specific test and/or --runner=<runnerName> for a specific suite.
                       # Valid runners include conformance, compiler, fourslash, project, user, and docker
                       # The user and docker runners are extended test suite runners - the user runner
                       # works on disk in the tests/cases/user directory, while the docker runner works in containers.
                       # You'll need to have the docker executable in your system path for the docker runner to work.
gulp runtests-parallel # Like runtests, but split across multiple threads. Uses a number of threads equal to the system
                       # core count by default. Use --workers=<number> to adjust this.
gulp baseline-accept   # This replaces the baseline test results with the results obtained from gulp runtests.
gulp lint              # Runs eslint on the TypeScript source.
gulp help              # List the above commands.
```

## Usage
```
node built/local/tsc.js hello.ts
```

## RoadMap
```
For more details on our planned features and future direction please refer to our site
```
# Contribute 
There are many ways to ``contribute`` to TypeScript.

- Submit bugs and help us verify fixes as they are checked in.

- Review the source code changes.

- Engage with other TypeScript users and developers on StackOverflow.

- Help each other in the TypeScript Community Discord.

- Join the #typescript discussion on Twitter.

- Contribute bug fixes.

- Read the archived language specification (docx, pdf, md).

>This project has adopted the Microsoft Open Source Code of Conduct. For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments

# Documention 
````
- TypeScript in 5 minutes
- Programming handbook
- Homepage
````
***********
 > - open jupyterNoteBook 
 >  - paste the code
 >  - Run code
 **********
 ## About the project 
 _the project is about webscraping a university site and collecting data from the site and saving it in a csv or jsonfile format, the python language was used to scrape the website and jupyter notebook which makes the work easty to run_
 > **```note```**
 > - pychram
 > - vs code
 > - sypder
 > - qt console
 > - orange 
 > - Rstudio
 > - Glueviz 
 > - sublime 
  can also be used to webscrape and run python files and are important in data collection 
  ***********************************************************






  
 


