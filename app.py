import argparse
import requests
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser(description = "Chimas client command line interface.")

parser.add_argument('-s','--server', metavar="SERVER", help="Chimas server to connect to", required=True)
parser.add_argument('-u','--user', metavar="USERNAME", help="Username to log in", required=True)
parser.add_argument('-p','--password', metavar="PASSWORD", help="Password to log in", required=True)
parser.add_argument('-b','--board', metavar="BOARD", help="Board id")
parser.add_argument('-t','--topic', metavar="TOPIC", help="Topic id")
parser.add_argument('-g','--get', metavar="GET", help="Get command")
parser.add_argument('-x','--send', metavar="POST", help="Post command")
parser.add_argument('-n','--number', metavar="NUMBER", help="Post command")

if __name__ == "__main__":
    pass
