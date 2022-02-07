# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

# Copy code
COPY brise_plandok/__init__.py brise_plandok/
COPY brise_plandok/utils.py brise_plandok/
COPY brise_plandok/constants.py brise_plandok/

COPY brise_plandok/services/__init__.py brise_plandok/services/
COPY brise_plandok/services/full_extractor.py brise_plandok/services/
COPY brise_plandok/services/utils.py brise_plandok/services/


# Install packages
COPY setup_service.py ./setup.py
RUN pip install .


# Donwload data
RUN apt-get update
RUN apt-get install -y wget unzip
RUN wget https://owncloud.tuwien.ac.at/index.php/s/Dsxxvmsk7GyFMDQ/download
RUN unzip download


# Run service
CMD [  "python3" , "brise_plandok/services/full_extractor.py", "-d", "full_data" ]
