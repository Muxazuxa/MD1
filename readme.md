
#Youtube video downloader on one click 


###Installation 

1.Install Python 3.6 and newer

2.Clone the reposiory: `git clone https://github.com/Muxazuxa/MD1`

3.`cd` into `task1`

4.Install virtualenv

5.Create a new environment:`virtualenv env`

6.Activate env: `source env/bin/activate`

7.Install required packages: `pip install -r requirements.txt`

8.`cd downloader`

9.Make migrations to DB: `python manage.py makemigrations` and `python manage.py migrate`

10.Run Server: `python manage.py runserver`