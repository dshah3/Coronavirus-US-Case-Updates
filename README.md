# Coronavirus US Case Updates
Scrapy Web Scraper with Slack Webhooks to Periodically Send US Coronavirus Case Updates to a Desired Slack Channel

**Table of Contents**
  * Installation of Necessary Modules and Packages
  * Slack Integration
  * deferLater and sleep Capabilities
  * Resources
 
 **Installation of Modules and Packages** <br/>
 For webscrapers, I recommend using Scrapy: it has great documentation, fairly easy to use, and supports lots of integrations to 
 3rd party software. However, it does not support periodic jobs, so you can integrate Scrapy with [Scrapy-Do](https://pypi.org/project/scrapy-do/) or the [deferLater function](https://twistedmatrix.com/documents/14.0.2/api/twisted.internet.task.deferLater.html).
 You can use pip to install Scrapy and the integrated terminal in your IDE to check the version of Scrapy.
 
  **Slack Integration** <br/>
  We can integrate Slack into our project using the [Slack API](https://api.slack.com/) and Slack Webhooks. Create a Slack app and
  webhook for the desired channel, and authorize your app to have access to a certain channel. Insert your webhook url into 
  the proper section of the project, and use a cURL command to send a message to slack. You can convert a cURL command to python using
  [this website](https://curl.trillworks.com/).
  
  **deferLater and sleep Capabilities** <br/>
  Since we are running Scrapy through a script, we must use a Twisted Crawler and Twisted deferLater in order to start and stop 
  our process, and also run the spider periodically. I use a Callback function to add a delay through a [deferLater function](https://twistedmatrix.com/documents/14.0.2/api/twisted.internet.task.deferLater.html)..

  **Resources**
    - [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
    - [Scrapy-Do](https://pypi.org/project/scrapy-do/)
    - [Slack Webhooks](https://api.slack.com/messaging/webhooks)
    - [Crawler Process](https://kite.com/python/docs/scrapy.crawler.CrawlerProcess)
    - [cURL Command Converter](https://curl.trillworks.com/)
