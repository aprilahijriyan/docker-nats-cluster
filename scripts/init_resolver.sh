#!/bin/bash

echo -e "Setting up resolver config... "
nsc generate config --nats-resolver --sys-account SYS > config/resolver.conf
