# Description:
    Test task for 'DataOx' company
# Main functionality:
    - Scraping Financial Time articles
    - Saving scraped data to database
    - API
# Technologies:
    - Python: 3.10
    - FastAPI: 0.116.1
    - Postgresql: 14.7
    - Redis: 8.0
    - Celery: 5.5.3
    - Docker 27.3.1
    - docker-compose 1.29.2
# Project structure:
    ├── app/      # Application
    ├───── api/   # FastApi application
    ├───── database/ # Database
    ├───── scraping/ # Scraper
    ├───── settings/ # Application settings
    ├── docker/   # Docker deployment
# Scraping process
    Application requires an active subscription to the Financial Times. The application uses the user`s session to 
    access articles(the user is given ~10 free articles per month, so scraping uses a subscription that gives unlimited 
    access to articles) by putting the user`s session in cookies. Therefore, before using the application, you must 
    define the FTSESSION_S_COOKIE and FTSESSION_S_COOKIE_EXPIRES environment variables, which you can find in the 
    browser cookie under the name FTSession_s for the site https://www.ft.com
    
    Right now scraper is able to scrape default articles, x live blogs and visual investigation articles.
    Scraper scrape article from 'world' tab.
    Scraping process descriptions:
        1. Scraper collects preliminary articles information(title, link, publication date and subtitle). This stage 
            continues until craper reaches an article that is published after the cut-off date(30 days or 1 hour from 
            the current date)
        2. Articles splitted into batches that will be processed asynchronously. Scraper collects and updated article 
            details for every article in batch.
        3. List of articles is cleared of articles withot text (articles skipped during scraping of details)
        4. Scraping finished and list of articles is returned

# Retry and exception handling logic
    Retry logic is implemented on scraper level, for preliminary and details scraping stages
    1. Preliminary scraping. If the page has not loaded, there will be attempts to load it again. If attempts have been 
        exhausted, the page will be skipped, then the preliminary scraping stage will be ended
    2. Details scraping. If the article has not loaded, there will be attempts to load it again. If attempts have been 
        exhausted, the article will be skipped. If any exception occured during article scraping, article will be 
        skipped

# How to run application
 ## with Docker
- [check deploy README] (./docker/README.md)
 ## manual
- [check application README] (./app/README.md)
 