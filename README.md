# Population-Scraper
Small prototype project that scrapes population sizes from countries on Wikipedia and converts the scraped data to a usable format. The project is hosted on AWS Lightsail, using an Apache vHost server which communicates with Django through the WSGI interface. 

The project was set up in 2 weeks and could be expanded in the future, by for example running the script at a timed interval and then maybe run analytics on many different population sizes and for example their changes over time.  
The two chosen countries were United States and India, but any number of countries could be chosen for any kind of purpose. 

## Security
The project is hosted on a static ip address with a firewall configured to an exclusive public ip address, but as the project 
expands, scraping with a proxy should be required. 

## Images

This is a screenshot of the project website, which is currently: live and hosted on AWS Lightsail
![Image of Scraped Population Data](https://github.com/JonasKVJ/Population-Scraper-AWS-Lightsail/blob/master/Embedded-ScrapedProjectData.png)


## Technologies
Django, Python, AWS Lightsail, Apache, VIM, Bash, HTML
