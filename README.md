# https_server
run a small and quick https server for a local network

## to setup:
`chmod +x setup.sh`
`./setup.sh`
`source ~/.bashrc`

The setup script does:
* generate an ssl certificate (cert.pem) and private key (key.pem) in the script directory
* add the alias "https" to ~/.bashrc

## to run:
`https [-d, --directory | -p, --port]`

* default directory is the users home directory
* default port is 4443
