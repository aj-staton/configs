#!/usr/bin/python
# This script will automate the building of a github repo.
# Written by: Austin Staton 
# Date; March 31, 2020

import sys, os
import time
import stdiomask # Hides password on user input.
from selenium import webdriver

username = os.popen('git config --global user.name').read().strip()
password = "" # Fill in your own passoword.

'''
This function handles the opening of the browser, navigation to the new repo 
page, and creation of the new repository. If GitHub updates the HTML on their
website, this WILL break.
'''
def web_nav(repo, visibility):
  browser = webdriver.Firefox()
  browser.set_window_size(400,400)
  # Login Screen
  browser.get('https://github.com/login')
  try:
    item = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    item.send_keys(username)
  except:
    print("Issues in filling the username field.\nExiting...")
    sys.exit()
  try:
    item = browser.find_elements_by_xpath("//*[@id='password']")[0]
    item.send_keys(password)
  except:
    print("Could not fill in the password.\nExiting...")
    sys.exit()
  try:
    item = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")[0]
    item.click()
  except:
    print("Issue clicking Sign in\nExiting...")
    sys.exit()
  
  #######################################################
  # If you're an MFA user this delay needs to be present.
  raw_input("Have you entered your MFA code?")
  
  #######################################################

  # New Repo Screen -- only availible after login.
  browser.get('https://github.com/new')
  try:
    item = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    item.send_keys(repo)
  except:
    print("Could not fill in the Repository name.\nExiting...")
    sys.exit()
  try:
    if (visibility.lower().strip() == "private"):
      item = browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0]
      item.click()
  except:
    print("Could not select repository visibility\nExiting...")
    sys.exit()
  try:
    item = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
    item.click()
  except:
    print("Could not fill in README checkbox.\nExiting...")
    sys.exit()
  try:
    item = browser.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[3]/button")[0]
    item.submit()
    print("\nRepository Created!")
  except:
    print("Could not click 'Create repository' button.\nExiting...")
    sys.exit()

  browser.close()

def main(argv):
   
  if (len(argv) > 3 or len(argv) <= 1):
    print("usage: python builder <directory to build> <public/private>")
    sys.exit()
    
  repo = str(argv[1])
  visibility = ""
  if (len(argv) == 3):
    if (argv[2].lower().strip() == "private" or argv[2].lower().strip() == "public"):
      visibility = argv[2]
  else:
    visibility = "private"
  

  path = os.popen('pwd').read()

  # Ensure github is installed. If not, install it.
  version = os.popen('git --version').read()
  if ("not found" in version):
    print("git is not installed.")
    try:
      os.system('sudo apt-get install git')
    except:
      print("Please install git with your package manager.")
  else:
    print("Creating the " + visibility + " git repo at: \n" + path)
  
  web_nav(repo, visibility)
  os.system('git clone https://github.com/'+ username + '/' + repo)


if __name__ == "__main__":
  main(sys.argv)
