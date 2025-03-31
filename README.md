# https_server
Run a small and quick https server for a local network.

### setup
`chmod +x setup.sh`

`./setup.sh`

`source ~/.bashrc`

The setup script does:
* generate an ssl certificate (`cert.pem`) and private key (`key.pem`) in the script directory
* add the alias "https" to ~/.bashrc

### run
`https [-h] [-d, --directory DIRECTORY] [-p, --port PORT]`

* default directory is the users home directory
* default port is 4443
* the local https server URL is copied to the clipboard
