Hello App - Yet Another Docker Tutorial
=======================================

This is not actually *another* Docker tutorial...
It's just a part of [the official Docker tutorial](https://docs.docker.com/get-started/), slightly modified.
So go ahead and read the content of the official tutorial, and use this repo just for the app part.

## tl;dr

```sh
# Check Docker version & info
$ docker version
$ docker info

# Run the most basic image (sanity check)
$ docker run hello-world

# List images and containers
$ docker images
$ docker ps -a

# Review the app code, under hello-app directory
$ cd hello-app
# Dockerfile is the recipe for building the app image (it's a Python Flask app)
# requirements.txt lists Python dependencies
# app.py is the entire app Python code

# Build the app
$ export TAG="<your-name>"
$ docker build -t hello-app:$TAG .
# See the image listed
$ docker images

# Run the app locally
$ docker run -p 8080:5000 hello-app:$TAG
# Browse to http://localhost:8080/ or use curl
$ curl -i http://localhost:8080/
$ curl -i http://localhost:8080/healthz
# ctrl+c to stop the running container

# Share the app via GCR, assuming you have a project set up
$ export PROJECT_ID="<your Google Cloud Project ID>"
$ docker tag hello-app:$TAG gcr.io/$PROJECT_ID/hello-app:$TAG
$ gcloud docker -- push gcr.io/$PROJECT_ID/hello-app:$TAG

# Check that you can run an image shared by someone else too
$ docker run -p 8080:5000 hello-app:<someone-else>
```
