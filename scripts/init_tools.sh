#!/bin/bash

echo -n "Downloading NATS Cli..."
wget https://github.com/nats-io/natscli/releases/download/v0.1.4/nats-0.1.4-amd64.deb
sudo dpkg -i nats-0.1.4-amd64.deb
rm nats-0.1.4-amd64.deb
echo -n "Downloading NSC Cli..."
curl -L https://raw.githubusercontent.com/nats-io/nsc/master/install.py | python
echo "Done"
