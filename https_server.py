import http.server
import ssl
import os
import argparse
import socket
import pyperclip

def get_local_ip():
    """Retrieve the actual local IP address used to connect to the network."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Connect to an external address (without sending data) to determine the correct interface
            s.connect(("203.0.113.1", 80))
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"  # Fallback if detection fails

def parse_args():
    parser = argparse.ArgumentParser(description='a simple https server')
    parser.add_argument('--directory', '-d', default=os.path.expanduser("~"), help='Specify the directory to serve')
    parser.add_argument('--port', '-p', type=int, default=4443, help='Specify the port number')
    args = parser.parse_args()
    return args

def init_server(args):
    os.chdir(args.directory)
    server_address = ('0.0.0.0', args.port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    return httpd

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cert_path = os.path.join(script_dir, 'cert.pem')
    key_path = os.path.join(script_dir, 'key.pem')

    server_args = parse_args()
    
    httpd = init_server(server_args)

    local_ip = get_local_ip()
    
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
