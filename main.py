# coding: utf-8

import sys
import os
import time
from mykeyboard.scan_keyboard import KeyScanner
from client.ws_client import WebsocketHandler, WebsocketHandlerReceiver
import threading

def main():
    ws = WebsocketHandler()
    
    key_scanner = KeyScanner(ws)
    key_scanner.start_scan()
#     thread = threading.Thread(target=key_scanner.start_scan)
#     thread.start()

    wsr = WebsocketHandlerReceiver()
    wsr.start_receive()
#     thread = threading.Thread(target=wsr.start_receive)
#     thread.start()
#     while True:
#         time.sleep(1)

if __name__ == "__main__":
    main()