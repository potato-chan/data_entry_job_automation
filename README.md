# Data Entry Job Automation
The script automatically fills in google-forms with the fields of monthly rent, address and link to the ad, based on data taken from [otodom.pl](https://www.otodom.pl/)

---
### Supported Browser
Google Chrome
### Variables

*GOOGLE_FORM_LINK* - your link to google form

*LIMIT* - how many ads do you want to find

*OTODOM_LINK* - your link to the site otodom.pl


### Instruction

1. You have to create a google form in this format: the first field takes the address of the apartment, the second field takes the monthly rent, the third field takes the link. Copy the link to the google form and add it to the *GOOGLE_FORM_LINK* variable.
![alt text](https://i.imgur.com/Y0DuNX7.png "google form example")
2. You have to go to [otodom.pl](https://www.otodom.pl/) and select all the parameters you want (city, price, number of rooms, etc.). Copy the link from your browser and add it to the *OTODOM_LINK* variable.
3. Add a value for how many results you want to get in the *LIMIT* variable.

### Modules for Python

* Selenium Webdriver
* Beautiful Soup