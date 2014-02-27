# Project 1
# Version 0.0.1
# SERVER SOFTWARE (Will not be distributed)
# IM Software - Socketing
import socket
import sys
import thread

def socket1():    
    HOST = ''     # Symbolic name meaning all available interfaces
    PORT = 25565
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding port
    s.bind((HOST, PORT))
    # Listening to max. 10 connections.
    s.listen(10)
    conn, addr = s.accept()
def socket2():
    HOST = ''
    PORT = 25566
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind((HOST, PORT))
    s2.listen(10)
    conn2, addr = s2.accept()

thread.start_new_thread(socket1, ())
thread.start_new_thread(socket2, ())
#Receiving from client
data = s.recv(1024)
print data
s2.send(data)

