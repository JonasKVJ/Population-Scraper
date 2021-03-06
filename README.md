# Population-Scraper
Small prototype project that scrapes population sizes from countries on Wikipedia and converts the scraped data to a usable format. The project was hosted on AWS Lightsail, using an Apache vHost server which communicates with Django through the WSGI interface. 

The project was set up in 2 weeks and could be expanded in the future, by for example running the script at a timed interval and then maybe follow up with analytics on selected population sizes.  
The two picked countries were United States and India, but any countries could be chosen for any kind of purpose. 

## Security
The AWS instance of the project has been assigned a static ip address with a firewall configured to an exclusive public ip address. As the project expands, the website should be hosted on a HTTPS domain, which could for example be done with an AWS load balancer to ensure scalability. 

## Images
This is a screenshot of the project website, from the short amount of time when it was live. It is now taken down due to security concerns, as well as cost. 

![Image of Scraped Population Data](https://github.com/JonasKVJ/Population-Scraper-AWS-Lightsail/blob/master/Embedded-ScrapedProjectData.png)


## Technologies
Django, Python, AWS Lightsail, Apache, VIM, Bash, Beautiful Soup, WSGI, HTML
