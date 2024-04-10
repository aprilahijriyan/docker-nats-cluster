# Installation

* Create a `.env` file with the following:
    * NATS_IMAGE_VERSION

    > NOTE: You can copy the `.env.example` file and rename it to `.env`

* Create docker network

    `docker network create nats`

* Run the container

    `docker-compose -f nats-cluster.yml up -d`
