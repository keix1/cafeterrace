# coding: utf-8

import keyboard
import time
from scan_keyboard import KeyScanner

def main():
    key_scanner = KeyScanner()
    key_scanner.start_scan()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()