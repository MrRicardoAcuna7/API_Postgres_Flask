# API_Postgres_Flask
This is a API done using Flask and Postgres, the example is for communicating your API with an account table.

1. Set up the app through Flask, and creating connection with postgres using app.config['SQLALCHEMY_DATABASE_URI'].
2. Create the meta for the new table that would store the data and using SQLAlchemy create_all() would create it.
3. Create for each method a function to read the input and push to postgres. The endpoint should be localhost:5000/accounts for post.
4. Test it with post man sending one try in json format.
5. Query that table in postgres.
