# API_FELLOWSHIP

API's:

The API's in this application are designed to manage the functionality of choosing a fruit of th users choice, displaying it in a list that is in an HTML form. This selection gets stored in a local database. The Endpoints offer each one of the CRUD operations functionality.

Database:

The database used to store this data in is MySQL and the in-memery database.

How to run your server:

The backend FastAPI and frontend react applications are supposed to be in seperate servers. This means that the backend has to allow the front end to be served with it. At the present moment it is simplest to use npm run dev / npm start for the frontend React application, and then uvicorn main:app for the backend FastAPI application.

How to interact with your API:

In order to interact with the API the user would be able to make use of the login credentials page. then from the form that is on the landing page, be able to populate the database by creatin a list of fruits that is visible on the UI interface.

How to run tests (testing frameworks):

The testing frameworks used to test this application are;
1. pytest (frontend)
2. cypress (backend)
3. jest (backend)

Depending on the test that you would like to run, you could use one of the following commands in the root directory of the application:
1. to run backend tests - pytest -q <filename>.py
2. to run frontend tests - npx cypress open OR npm test 

