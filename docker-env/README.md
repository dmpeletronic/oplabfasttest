### 1. Oplab Development Enviromnet

To guarantee that everyone can compile/run/test the projects inside this repository, it is recommended to use the same environment.
So we decided to create a Docker Container with the required dependencies and tools. 

To create this container, run the following command:

docker build -t oplabdev .

To run the image with the developed solutions, please add the root folder into the created container with the command below:

docker run -v .:/opt/oplab/ oplabdev --it
