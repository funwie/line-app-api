The requirements are implemented as described but there is still much to work to do to refine the app for production
There are 2 separate projects. The Backend Microservice API and the Frontend React App

**Backend Microservice API - line-up-app**
- Python 3.8
- see requirements.txt for python packages used
- Docker is setup and can be initiated with Docker Run command 

**Frontend React App - user-frontend**
- create react app
- Grommet
- routing
- see packages.json for frontend packages used

**How to run**
- Run the Backend Microservice API first
- Visit {host}/api/ and try out the backend api
- Copy api host:port and change the host:port of the baseUrl in src/components/UserCard in user-frontend app.
  It definitely needs to be in config or env var. Please use this for now.

- Run the user-frontend app. npm start in the user-frontend folder

When app frontend app lauches, visit the users page, add /id to the url and press enter
Ensure the backend app is running and the host:port is correct in the frontend app

**Consideration**
- Not much test has been written but test is essential for any production app
- It's better to cach the user data  and use for subsequent request instead of requested from the service on each request.

