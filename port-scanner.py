#! /bin/python
"""
  It will be used to scan all open ports of a particular host
"""

import sys
import socket
from datetime import datetime

def banner(text, pattern = '-'):
  print(pattern * 16)
  print(text)
  print(pattern * 16)

def scan_ports(host):
  banner("Scanning Target " + host)
  try:
    for port in range(1, 65535):
      s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      result = s.connect_ex((host, port)) # returns an error indicator
      if result == 0:
        print("Port {} is open".format(port))
      s.close()
  except Exception as e:
    banner("\nException occurred", '*')
  except KeyboardInterrupt:
    banner("\n Exiting Program.", '*')
  except socket.gaierror:
    banner("\n Hostname could not resolved.", '*')
  except socket.error:
    banner("\n Could not connect to server.", '*')
  finally:
    sys.exit()



def main():
  if len(sys.argv) == 2:
    host = socket.gethostbyname(sys.argv[1]) # get host name from parameter
    scan_ports(host)
  else:
    banner("Invalid Syntax: python scanner.py <ip/host>")


if __name__ == '__main__':
  main()
