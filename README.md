# Docker NATS Cluster

A simple docker compose collection for setting up a NATS Cluster.

## Setup

* Create a `.env` file with the following:
    * NATS_IMAGE_VERSION

    > NOTE: You can copy the `.env.example` file and rename it to `.env`

* Create docker network

    `docker network create nats`

* Install tools

    `./scripts/init_tools.sh`

* Setup NATS environment

    ```
    nsc init -i
    ./scripts/init_resolver.sh
    ```

* Run the container

    `docker-compose -f nats-cluster.yml up -d`

## Links

Find out more about NATS here https://nats.io/
