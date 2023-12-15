
git remote set-url origin https://NagulShareefPhatan123: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@github.com/NagulShareefPhatan123/pythonconnectpostgress.git
-=============
BELOW COMMNDS FOR DB TABLES UPDATE(AFTER CREATING TABLE IF YOU WANT TO ADD NEW COLUMN THEN BELOW 3 COMMANDS NEED TO INSTALL)
-=============

flask db init
flask db migrate
flask db upgrade

-=============
depedencies:
pip3 install Flask
pip3 install Flask-SQLAlchemy
pip3 install python-dotenv
pip3 install psycopg2-binary

pip3 show Flask-SQLAlchemy

pip install Flask-SQLAlchemy :this command not working

Install Flask:
Make sure you have Flask installed. You can install it using the following command:

-=============
to run this app: python app.py
-=============

-=============
post API:http://127.0.0.1:5000/todos
{
    "task": "migration issue stoty 2472559",
    "done": false,
    "comments": null,
    "created_date": "2023-12-15",
    "end_date": "2023-12-20"
}
-=============
Get by Id:http://127.0.0.1:5000/todos/1
-=============

-=============
Get LIST::http://127.0.0.1:5000/todos
-=============

PUT API:http://127.0.0.1:5000/todos/1
{
    "task": "migration issue stoty 2472559",
    "done": false,
    "comments": null,
    "created_date": "2023-12-15",
    "end_date": "2023-12-20"
}


