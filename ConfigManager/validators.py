import socket

def validate_ip(ip):
    try:
        ip = str(ip)
        socket.inet_aton(ip)
        return ip
    except Exception:
        return False

def validate_port(port):
    try:
        port = int(port)
    except Exception:
        return False

    if port >= 1024 and port <= 49151:
        return port
    else:
        return False
