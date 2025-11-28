# EFSTA Datamanipulator
Tool for manipulating large amounts of data in **EFSTA**.

This Tool is currently **only for testing** the functionality of the efsta API.
Efsta **runs** completely **inside a docker** container.

## Installation / How to use

1. clone this repository

    `git clone https://github.com/F4bianKoch/efsta-test-env`

2. move [efsta installer](https://public.efsta.net/EFR/install/DE/2.7.1/EFR_DE_2.7.1_install_linux64.zip) .zip inside the ./installer directory
3. build the Dockerfile

    `docker build -t efsta-test-env .`

4. start dockercontainer from image

    `./startDocker.sh`

    or

    `docker run -p 5618:5618 efsta-test-env`


5. execute tool that fits needs

    `python3 /src/<path-to-tool>.py`

## Tools
-- comming soon --
