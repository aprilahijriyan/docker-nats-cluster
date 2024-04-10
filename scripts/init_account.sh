#!/bin/bash

read -p "Account name: " accountName
echo "Setting up $accountName Account..."
nsc add account $accountName
echo "Generate the signing key..."
nsc edit account -n $accountName --sk generate
echo "Done"