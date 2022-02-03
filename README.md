# API_Postgres_Flask
This is an API done using Flask and Postgres, the example is for communicating your API with an account table.

1. Set up the app through Flask, and create a connection with postgres using app.config['SQLALCHEMY_DATABASE_URI'].
2. Create the meta for the new table that would store the data and using SQLAlchemy create_all() would create it.
3. Create for each method a function to read the input and push to postgres. The endpoint should be localhost:5000/accounts for method POST.
4. Test it with POSTMAN sending one entry in JSON format.
![alt text](https://github.com/MrRicardoAcuna7/API_Postgres_Flask/blob/main/postman_snapshot.PNG)
5. Check that table in postgres.
![alt text](https://github.com/MrRicardoAcuna7/API_Postgres_Flask/blob/main/postgres_snapshot.PNG)
