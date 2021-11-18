# Auth and Tests in Django
This repo introduces a simple web-application that uses Django auth system and 
contains a simple test suite.

## Django Auth System
The default Django authentication system has been used to provide user 
authentication and authorization on a few places in the app (see 
kasa\_view.py for the demo).

## Django Tests
In order to run provided Django test suite, run the following commands:
```console
cd prodavnicesajt
python manage.py test prodavnice.tests --noinput
```
Option `--noinput` automatically destroys the test database before each run.

Follow the instructions in the README.txt document in order to build and run 
the Django app itself.

## CI
This repo specifies a Django workflow that enables some sort of basic CI/CD.

## Containerize the App
This app can be containerized by using the docker.

### Docker installation
This document assumes that the docker is preinstalled on your system. 
If not, follow [the official documentation](https://docs.docker.com/get-docker/)

### Run from local build
Build the docker image:
```console
docker build -t djangoapp:latest .
```

Run the docker container locally
```console
docker run --name djangoappcont -d -p 8000:8000 djangoapp
```

### Run from Docker Hub

#### Upload the local image to Docker Hub
To upload the image on Docker Hub, you need to create an account on Docker Hub platform and [create a repository](https://docs.docker.com/docker-hub/repos/).
Then, the image needs to build locally by using the following command:
```console
docker build -t <hub-user-name>/<repo-name> .
```
After that, the image can be pushed to the repository by running the command:
```console
docker push <hub-user-name>/<repo-name>:latest
```
Other tags can be used instead of `latest`.


#### Run the docker container from the image hosted on Docker Hub
To start the docker container by using the image hosted on Docker Hub, use the following command.
```console
docker run --name djangoappcont -d -p 8000:8000 vladaindjic/simple-django-app
```

### Some more docker examples and useful docker links:
- [Flask app in docker container that introduces volumes](https://github.com/MilosSimic/First-Docker-app?fbclid=IwAR2aUNHOLNqPL4K3wLYYIhtB7LxT0VRDOAQNyjBeOyHLRox7QC9SENEuhEA)
- [removing containers, images, volumes](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)
