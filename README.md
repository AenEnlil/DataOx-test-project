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
# How to run application
 ## with Docker
- check deploy README (./docker/README.md)
 ## manual
- check application README (./app/README.md)
 