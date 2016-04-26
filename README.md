# Scrape-Hub
Scrape-Hub is a project which can list details about issues for any given public repo.
### Version
1.0.0

### Tech

Scrape-Hub uses the following:-

* [Django and DjangoREST] - For creating simple RESTful API 
* [Twitter Bootstrap] - Simple and Responsive UI
* [PostgreSQL] - Faster database access
* [jQuery and js] - duh


### Installation

You need pip installed globally:

```sh
$ sudo apt-get install python-pip
```

```sh
$ pip install virtualenv
$ virtualenv scraper_env
$ cd scraper_env/bin
$ source activate
```
Clone the repository to get access to the source code
```sh
$ git clone https://github.com/goodhamgupta/github-scraper.git
$ cd github-scraper
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
### NOTE
---
- Change the settings for the database in github-scraper/settings.py
- To collect the static files, execute `python manage.py collectstatic`
---
To deactivate the virtual environment use:
```sh
deactivate
```

### Todos

 - Write Tests
 - Integrate Github OAuth
 - More reponsive and user-attractive UI
 - Caching for quicker responses.
 - Ansible for hassle-free deployment

License
----

**Free Software, Hell Yeah!**

