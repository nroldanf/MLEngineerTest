# MLEngineerTest

Code from the entry test for a Machine Learning Engineer Position.

__NOTE__: To run the project download first the data.csv file with all the data and move to your working directory, in this case, the current.

## Steps to run the project (EDA and training)

Once this repo has been cloned, change directory to __research__ where the EDA files are.

### Build and image or pull it from Ducker Hub

You can pull the image nroldanf/loka_test from ducker hub or build and image from the __Dockerfile__ in [this repo](https://hub.docker.com/r/nroldanf/loka_test).

### Run the docker container

Check first if the 8888 port is busy before running the following command. In your terminal, run the following command:

```shell
docker run -p 8888:8888 -v $(pwd):ml_app jupyter lab
```
