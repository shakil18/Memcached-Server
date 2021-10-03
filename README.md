## Table of Contents

- [Memcached Server <a name = "about_the_project"></a>](#memcached-server-)
  - [Directory Structure <a name = "directory_structure"></a>](#directory-structure-)
  - [Requirements <a name = "requirements"></a>](#requirements-)
  - [Deployment <a name = "deployment"></a>](#deployment-)
  - [Contact <a name = "contact"></a>](#contact-)
---

<!-- ABOUT THE PROJECT -->
# Memcached Server <a name = "about_the_project"></a>

This [Memcached server](https://memcached.org/) GitHub repository is about to deploy a Memcached server, measure the performance of the request stream's load, and then export the result as graphs.

> ### Task ###
> ##### Container #1: #####
> * SSH Server – listening on port 22
> * memcached v1.4.33
> ##### Container #2: #####
> *  SSH Server – listening on port 10023
> * memcached benchmark client (mcperf)
> * Expose port for SSH Server
> ##### Docker compose: #####
> * Docker compose is used to get the communication between the containers running as well as the experiment.

<!-- DIRECTORY STRUCTURE -->
## Directory Structure <a name = "directory_structure"></a>

Here's a project's directory structure:

```text
Memcached-server
├── Container1
│   └── Dockerfile          # Memcached server
├── Container2
│   ├── Benchmark.py        
│   ├── Dockerfile          # Memcached mcperf (measuring memcached server performance)
│   ├── Dudefile            
│   ├── graphs.R            
│   └── run.sh              # automation script (generating graphs using dude, and graphs.R)
├── docker-compose.yml      # Docker-compose file for containers
├── graph1.pdf
├── graph2.pdf
└── README.md
```

<!-- REQUIREMENTS  -->
## Requirements <a name = "requirements"></a>

- [Docker <a href="https://docs.docker.com/get-docker/"> </a>](docker_download)
- [Docker Compose <a href="https://docs.docker.com/compose/install/"> </a>](docker_compose_download)

<!-- DEPLOYMENT  -->
## Deployment <a name = "deployment"></a>

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

<!-- CONTACT -->
## Contact <a name = "contact"></a>

**Azizul Hakim Shakil** - [@ShakilAzizul](https://twitter.com/ShakilAzizul) - azizulhakim.shakil18@gmail.com

Project Link: [https://github.com/shakil18/Memcached-Server](https://github.com/shakil18/Memcached-Server)
