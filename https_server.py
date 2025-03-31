import http.server
import ssl
import os
import argparse
import socket
import pyperclip

def get_local_ip():
    """
    The function `get_local_ip` retrieves the actual local IP address used to connect to the network by
    connecting to an external address.
    :return: The function `get_local_ip()` will return the actual local IP address used to connect to
    the network if successful. If an exception occurs during the process, it will return the loopback
    address "127.0.0.1".
    """
    """Retrieve the actual local IP address used to connect to the network."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Connect to an external address (without sending data) to determine the correct interface
            s.connect(("203.0.113.1", 80))
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"  # Fallback if detection fails

def parse_args():
    """
    The function `parse_args` defines a command-line argument parser for a simple HTTPS server.
    :return: The function `parse_args()` is returning the parsed arguments from the command line using
    the `argparse` module in Python.
    """
    parser = argparse.ArgumentParser(description='a simple https server')
    parser.add_argument('--directory', '-d', default=os.path.expanduser("~"), help='Specify the directory to serve')
    parser.add_argument('--port', '-p', type=int, default=4443, help='Specify the port number')
    args = parser.parse_args()
    return args

def init_server(args):
    """
    The `init_server` function initializes an HTTP server with SSL/TLS support based on the provided
    arguments.
    
    :param args: The `args` parameter in the `init_server` function is expected to be a dictionary-like
    object containing the CLI parameters provided with the `https` command. The possible options that
    can be included in the `args` dictionary are `--directory` and `--port`
    :return: The function `init_server` is returning an HTTP server instance that is configured to serve
    files from a specified directory over HTTPS.
    """

    try:
        os.chdir(args.directory)
    except FileNotFoundError:
        print(f"Error. The path '{args.directory}' does not exist.")
        return None

    server_address = ('0.0.0.0', args.port)
    try:
        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    except OverflowError:
        print('Error. The port number must be 0-65535.')
        return None
    except PermissionError:
        print(f'Error. Maybe port {args.port} is already in use?')
        return None
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return None
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    return httpd

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cert_path = os.path.join(script_dir, 'cert.pem')
    key_path = os.path.join(script_dir, 'key.pem')

    server_args = parse_args()
    if (httpd:=init_server(server_args)):
        local_ip = get_local_ip()
    else:
        exit(1)
    
    server_url = f"https://{local_ip}:{server_args.port}"

    pyperclip.copy(server_url)

    print(f"Serving on {server_url} from {server_args.directory}")
    print("Server URL copied to clipboard!")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
        print("Server stopped.")
