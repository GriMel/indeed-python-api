Indeed-Python-API
=================

Simple API for [Indeed](http://indeed.com)  
To get a key:  
1. Register **Publisher** account [here](http://www.indeed.com/publisher)  
2. Go to your [XMLFeed](https://ads.indeed.com/jobroll/xmlfeed) page  
3. Find here a string like **Your publisher ID is "1234567890123456789"**  
4. **12345678901234567890** is your key  

Simple query
```python
from indeed import Indeed

key = "PUBLISHER_KEY"
indeed = Indeed(key)
indeed.search_jobs(query="Python")
for job in indeed.results:
    print(job)
```

Advanced search
```python
from indeed import Indeed, construct_query

key = "PUBLISHER_KEY"
indeed = Indeed(key)
query = construct_query(all_words="Python Django", none="Senior", company="EPAM")
indeed.search_jobs(query=query)
for job in indeed.results:
    print(job)
```