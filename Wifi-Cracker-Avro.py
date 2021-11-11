# ====================================================================================================================

#                                                   WiCrackFi

#                                                     v1.2

#                           WiFi Security Testing Tool Created By Pedro "ShineZex" Gomes

#                                       Copyright 2021 - All Rights Reserved

# ====================================================================================================================

# WiFi Security Testing Tool that automates the use of Aircrack-ng suit and makes testing WiFi Security much easier!

# ====================================================================================================================

import os

import time

import subprocess

import shlex

import os.path

import csv

import datetime

 

 

# Setup (updates and installs)

def instal_setup():

    os.system("clear")

    print("Installing everything that is required:")

    time.sleep(2)

    print("Updating...")

    os.system("sudo apt-get update")

    time.sleep(1)

    os.system("clear")

    print("Upgrading...")

    os.system("sudo apt-get upgrade")

    time.sleep(1)

    os.system("clear")

    print("Installing Aircrack-ng...")

    os.system("sudo apt-get install aircrack-ng")

    time.sleep(1)

    print("FINISHED!")

    print("EVERYTHING THAT IS NEEDED IS INSTALLED! HAVE FUN!")

    time.sleep(2)

    os.system("clear")

    menu()

 

 

# Starts the interface in monitor mode

def start_monitor_mode():

    os.system('clear')

    print("Your network interfaces are...")

    # This line is just to make sure there is no bugs, restarts all the connections to run in a fresh environment

    os.system('service networking restart')

    time.sleep(3)

    os.system("airmon-ng")

    time.sleep(.5)

    # Debugs

    os.system("airmon-ng check kill")

    time.sleep(.5)

    i = input("Enter your network interface: ")

    time.sleep(.5)

    os.system("airmon-ng stop " + i + "mon")

    time.sleep(.5)

    command = "airmon-ng start " + i

    os.system(command)

    time.sleep(.5)

    # Debugs

    os.system("airmon-ng check kill")

    # Creates a dir to store all the config files (more organized)

    if not os.path.exists('configs'):

        os.system("mkdir configs")

    # Saves the interface name in a file to use multiple times in the script later

    l = open("configs/NODELETE.txt", "w")

    l.write(i + "mon")

    l.close()

    time.sleep(1)

    print("DONE!")

    time.sleep(.5)

    os.system("clear")

    menu()

 

 

# Clean File

def clean_indv():

    os.system("mv configs/WiFi__List-01.csv configs/WiFi__List-00.csv")

    # Cleans all the devices info, only shows the networks available

    # Cleans first blank line of the file

    os.system("sed '/Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs/,$d' "

              "configs/WiFi__List-00.csv > configs/WiFi__List-01.csv; sed -i '1d' configs/WiFi__List-01.csv")

 

    os.system("rm -rf configs/WiFi__List-00.csv")

    menu()

 

 

# If wifi list not created, creates a new one

def networks_arround():

    l = open("configs/NODELETE.txt", "r")

    il = l.read()

    time.sleep(.5)

    # Creates a dir to store all the config files (more organized)

    if not os.path.exists('configs'):

        os.system("mkdir configs")

 

    # Check if exists any older file and if yes removes it

    if os.path.exists('configs/WiFi__List-01.csv'):

        os.system("rm -rf configs/WiFi__List-*")

 

    # Command to get the networks around info

    command = "airodump-ng -w configs/WiFi__List --output-format csv wlan0mon"

 

    # Starts a subprocess to kill the airmon-ng command after 5 seconds

    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    time.sleep(1)

    while True:

        # After some testing, 7 seconds is the perfect number between fast process and most networks collected.

        for x in range(7, 0, -1):

            os.system("clear")

            print("SCANNING FOR WIFIs | FINISH IN: " + str(x) + "s")

            time.sleep(1)

 

        process.kill()

        os.system("clear")

        os.system("reset")

        os.system("clear")

        print("WIFI LIST FILE CREATED!")

        break

 

    time.sleep(1)

    l.close()

    clean_indv()

 

 

# Just to display the saved networks

def display_networks_available():

    os.system("clear")

    # Creates a dir to store all the config files (more organized)

    if not os.path.exists('configs'):

        os.system("mkdir configs")

    # Checks if the file already exists

    if os.path.exists('configs/WiFi__List-01.csv'):

        # Prints a table using the import csv with all the ESSID of the networks discouvered

        print("")

        print("=========================================================")

        print("|		" + "\033[1m" + "List of Available Networks:" + "\033[0m" + "	 	|")        print("=========================================================")

        print(

            "|
