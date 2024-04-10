#!/bin/bash

read -p "Operator name: " operatorName
echo "Setting up $operatorName Operator..."
nsc add operator --sys --generate-signing-key $operatorName
nsc edit operator -n nats://localhost:4222
