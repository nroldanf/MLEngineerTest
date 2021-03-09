# MLEngineerTest

Code from the entry test for a Machine Learning Engineer Position.

__NOTE__: To run the project download first the data.csv file with all the data and move to your working directory, in this case, the current.

## Steps to run the project (EDA and training)

Once this repo has been cloned, change directory to __research__ where the EDA files are.

### Build and image or pull it from Ducker Hub

You can pull the image nroldanf/loka_test from ducker hub or build and image from the __Dockerfile__ in [this repo](https://hub.docker.com/r/nroldanf/loka_test).

### Run the docker container

Check first if the 8888 port is busy before running any of the following commands.

If you pulled the image from DockerHub:

```shell
docker run -p 8888:8888 -v $(pwd):/ml_app nroldanf/loka_test
```

Otherwise, if you build it from the Docker file, specify the name you gave before building:

```shell
docker run -p 8888:8888 -v $(pwd):/ml_app name_of_image
```
