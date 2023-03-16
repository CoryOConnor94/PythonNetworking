# PythonNetworking
Various Python scripts for networking

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#script-briefs">Script briefs</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Various Python scripts for performing networking tasks.



<p align="right">(<a href="#top">back to top</a>)</p>



### Python Libraries used

To use these scripts the following libraries are required.

* [json](https://github.com/python/cpython/tree/3.10/Lib/json/__init__.py)
* [socket](https://github.com/python/cpython/tree/3.10/Lib/socket.py)
* [re](https://github.com/python/cpython/tree/3.10/Lib/re.py)
* [sys](https://docs.python.org/3/library/sys.html)
* [pexpect](https://github.com/pexpect/pexpect)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
Check that you have python 3.7 or newer.


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- SCRIPT BRIEFS -->
## Script briefs

### JSONtoDICT.py
Reads in json file, converts to python dictionary, accesses data and changes value, wites out new values to new json file

### TCPEchoClient.py
Creates TCP client socket, connects to server socket that's waiting for connection and sends user input from command line to server and receives message back.

### TCPEchoServer.py
Creates TCP server socket and waits for connection. Recieves message from client and sends back. Loops so always listening for new connection

### TCPtoUpperClient.py
Creates TCP client socket, connects to server socket that's waiting for connection and sends a message and receieves message back from server.

### TCPtoUpperServer.py
Creates TCP server socket and waits for connection. Receives message from client, changes the message to uppercase and send the message back. Loops so always listening for new connection.

### dnsLookUp.py
Takes in a domain name from command line and performs a DNS lookup, returns all IPs associated with that domain

### findMTU.py
Reads inputted interface name from command line, using pexpect module to automate ifconfig command, parse for MTU of interface

### getMAC.py
uses socket module functions to extract MAC address of given interface 

### ipconvert.py
Receives IP from user and converts IPv4 address to 32 binary HEX value

### iplookup.py
takes user inputted domain name and returns IP address' associated

### pexpectTelnet.py
Automates Telnet login and uses regular expression to return hop value

### portScan.py
Scans ports 1-1024 and returns protocol used, port number and service 

### regularExpressionIP.py
Uses regular expression to search file for IP addresses

### tcpClient.py
Creates TCP client socket, connects to server socket that's waiting for connection and sends user input from command line to server and receives message back.

### tcpPortScanner.py
Scans networks ports and returns open ports

### tcpServer.py
Creates TCP server socket and waits for connection. Recieves message from client and sends back. Loops so always listening for new connection

### udpClient.py
Creates UDP client socket, connects to server socket that's waiting for connection and sends user input from command line to server and receives message back.

### udpServer.py
Creates UDP server socket and waits for connection. Recieves message from client and sends back. Loops so always listening for new connection

### udpimageClient.py
Creates UDP client socket, connects to server socket that's waiting for connection and sends image to server and receives copy sent back

### udpimageServer.py 
Creates UDP server socket and waits for connection. Recieves image from client and sends back a copy. Loops so always listening for new connection

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Email - CoryOConnor1994@gmail.com

Linkedin - (https://linkedin.com/in/cory-o-connor-7b16911a)

Project Link - (https://github.com/CoryOConnor94/PythonNetworking)

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
