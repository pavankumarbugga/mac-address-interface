# mac-address-interface
Docker image to accept mac-address and find associated company

## Components
- `main.py` script will process api to provide associated company
- `Dockefile` added to have set of instructions to build the image required
- `.gitignore` files added to ignore to commit to GitHub
- `.dockerignore` added with files to ignore during docker build

## Secrets
- Api keys are store in a file called `creds.py` and been ignored to commit into GitHub. 

## Steps to build the container image
`docker build -t mac-interface .`

## Start created container 
- `docker run mac-interface <<MAC-ADDRESS>>` 
- Replace `MAC-ADDRESS` above like below
- Ex: `docker run mac-interface '44:38:39:ff:ef:57'`

## Arguments
- Mandatory argument of `MAC-ADDRESS` to be provided

## Result
- Company name is provided as console output