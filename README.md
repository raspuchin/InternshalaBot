# InternshalaBot
A bot that will log in to internshala and will keep applying for internships. Uses Selenium, BeautfulSoup and ConfigParser


# To add/change
- Use a Scheduler or Threading to run the apply() function
- Instead of using sleep() use selenium waits
- Currently, out of 10 I am experiencing that it fails to apply for more than 4 so need to debug and fix
- answer3, figuring out wether it's projects or comments and then building specific answers
- income of internships
- duration of internships

# How to use

1. Update internshalaConfig as follows:
   - email: contains your internshala email id
   - password: your internshala password
   - answer1: text answer to why you are fit for a particular internship
   - answer2: are you available for an internship asap
   - answer3: Link to projects/Comments on their website/product
   - answer4: can you accomodate yourself in a particular area because the company cannot pay you back for rent, etc
   
   Note: answer 3 can be a hit or a miss due to ambiguity, trying to work on a fix currently but you will probably fill wrong answers once in a while
   
2. On your internshala page update your preferences for your internships, the script will then only give focused responses to these pages thereby bypassing the issue of giving an answer for photoshop in digital marketing for example

   Note: The script currently does not support features like looking at duration of the internship and income as they were irrelevant to me currently, I will be adding something soon hopefully
   
3. Download chrome webdriver from here: https://chromedriver.chromium.org/downloads download for your version of chrome, if you are using firefox download from here https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html. Also, comment the chrome driver line and uncomment the firefox line

4. install the requirements and you are ready to go (you can change how many you want to be done by sending 'repeat' parameter and the duration in the 'hours' parameter in the run function, default is 10 every hour)
