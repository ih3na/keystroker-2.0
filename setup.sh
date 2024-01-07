#!/bin/bash

cd client
python -m venv .
cd ../server
python -m venv .
cd ../

echo "setup done!"