# Memcached-server Testing with Docker #

### Task ###

##### Container #1: #####
 * SSH Server – listening on port 22
 * memcached v1.4.33


##### Container #2: #####
*  SSH Server – listening on port 10023
* memcached benchmark client (mcperf)
* Expose port for SSH Server

##### Docker compose #####
* Use Docker compose to get the communication between the containers running as well as the experiment.

##### The experiment script/work flow #####
* ```dude run```:
* ssh to the memcached server (container #1) to launch memcached
* Launch the benchmark client (locally - container #2)
* Grab the output from the benchmark client using cut etc. magic: "Response rate", "Response time [ms] avg" - Dude dimensions: rate 
* ```dude sum```: summarizes the output - single csv file
* The plot the graphs ```$ Rscript ….R```

Test it using the following command sequence:
```
#!/bin/bash

sudo docker-compose up
ssh 127.0.0.1 -p 10023 "./run.sh"
scp –P 10023 127.0.0.1:~/graph*.pdf .
evince graph*.pdf
```
