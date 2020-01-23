Only what you need to do:

- install docker
- install docker-compose
- do docker-compose up -d
- go to 0.0.0.0:5700, and see responses

What I used:
 - Used alembic for auto-generate DB table.
 - Used sqlalchemy models to fill and get values from DB
 - Used flask for build api? for getting data from DB.
    
For sorting and paging http://0.0.0.0:5700/?sort_order=asc&page=4:
 - Sort add by adding in url sort_order with params 'asc' or 'desc'.
 - Paging add by adding to url 'page' and  'page_limit', they need to be grater that 1
 
On start:
 - use alembic to generate DB
 - upload data from github-api
 - start flask api 