# coding: utf-8

import sys
import os
import time
from mykeyboard.scan_keyboard import KeyScanner
from client.ws_client import WebsocketHandler, WebsocketHandlerReceiver
import threading

def main():
    
    while True:
        print("start scan")
        ws = WebsocketHandler()
        wsr = WebsocketHandlerReceiver()
        key_scanner = KeyScanner(ws, wsr)
        key_scanner.start_scan()
        ws.close()
        
        time.sleep(1)

if __name__ == "__main__":
    main()