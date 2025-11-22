#!/usr/bin/env python3

import os
import sys
import subprocess

BANNER = r"""
  ███████╗██████╗ ███████╗███████╗██████╗ ██╗██████╗ ███████╗██╗███╗   ██╗ ██████╗ 
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝██║████╗  ██║██╔════╝ 
  ███████╗██████╔╝█████╗  █████╗  ██║  ██║██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ███╗
  ╚════██║██╔══██╗██╔══╝  ██╔══╝  ██║  ██║██║██╔══██╗██╔══╝  ██║██║╚██╗██║██║   ██║
  ███████║██║  ██║███████╗███████╗██████╔╝██║██║  ██║███████╗██║██║ ╚████║╚██████╔╝
  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

                Speeping — Internet Speed Tool
"""

def run_speedtest():
    # مسح الشاشة
    os.system("clear")

    print(BANNER)
    print("\n[+] Running internet speed test...\n")

    try:
        # نشغّل أمر speedtest --simple وناخذ ناتجه
        result = subprocess.run(
            ["speedtest", "--simple"],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print("[!] 'speedtest' command not found.")
        print("    Please install it with: sudo apt install speedtest-cli")
        sys.exit(1)

    if result.returncode != 0:
        print("[!] Speedtest failed.")
        print(result.stderr)
        sys.exit(1)

    # نعرض الناتج كما هو (Ping / Download / Upload)
    print("------ Speeping Results ------")
    print(result.stdout.strip())
    print("------------------------------")

def main():
    if len(sys.argv) < 2:
        print("Usage: speeping test")
        sys.exit(0)

    command = sys.argv[1]

    if command == "test":
        run_speedtest()
    else:
        print("Invalid command.")
        print("Usage: speeping test")

if __name__ == "__main__":
    main()
