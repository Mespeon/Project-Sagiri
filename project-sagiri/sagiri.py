#Project Sagiri - A Personal Exercise on Web Automation using Pyautogui and Selenium
#Coded and button images by Mark Nolledo
#Credits to Marvin Bruno Jr. and John Michael Dharma for their repos, tips, and inspiration.
#THIS IS A WORK IN PROGRESS. BUGS AND INCONSISTENCIES ARE TO BE EXPECTED.

import pyautogui, sys
import xml.etree.ElementTree
from selenium import webdriver
from tkinter import *
from PIL import ImageTk

browser = webdriver.Chrome()

def startDriver(btnName):
    def facebook():
        browser.get('https://www.facebook.com')
        getKey(btnName)
        
    def gmail():
        pyautogui.alert(text='2-step Verification automation is not yet supported.', title='Gmail Login Automation')
        browser.get('https://mail.google.com')
        getKey(btnName)
        
    def twitter():
        browser.get('https://www.twitter.com')
        getKey(btnName)
        
    try:
        browser.maximize_window()
    except:
        pyautogui.alert('Unable to find Chrome driver')
        sys.exit

    autostart = {
        'facebook': facebook,
        'gmail': gmail,
        'twitter': twitter
    }
    autostart.get(btnName)()

def getKey(keyName):
    try:
       readKey = xml.etree.ElementTree.parse('key.xml').getroot()
    except:
        pyautogui.alert('Unable to find key file.')
        
    def getFacebook():
        fbTree = readKey.find(keyName)
        fbUsername = fbTree.findtext('username')
        fbPassword = fbTree.findtext('password')

        usernameInput = browser.find_element_by_id('email')
        passwordInput = browser.find_element_by_id('pass')
        usernameInput.send_keys(fbUsername)
        passwordInput.send_keys(fbPassword)
        browser.find_element_by_id('u_0_r').click()

        if browser.current_url == 'https://web.facebook.com/checkpoint/?next':
            browser.find_element_by_id('u_0_3').click()
            browser.find_element_by_id('u_0_7').click()

        #In case Chrome offers to save password,
        #this will click Never (WIP on auto Never Offer to Save Password)
        #COORDINATES ARE BASED IN 1366 x 768 RESOLUTION
        pyautogui.click(x=1239, y=204)

    def getGmail():
        gmailTree = readKey.find(keyName)
        gmailUsername = gmailTree.findtext('username')
        gmailPassword = gmailTree.findtext('password')

        emailInput = browser.find_element_by_id('identifierId')
        emailInput.send_keys(gmailUsername)
        browser.find_element_by_id('identifierNext').click()
        browser.implicitly_wait(5)
        passwordInput = browser.find_element_by_name('password')
        passwordInput.send_keys(gmailPassword)
        browser.find_element_by_id('passwordNext').click()

    def getTwitter():
        twitterTree = readKey.find(keyName)
        twitterUsername = twitterTree.findtext('username')
        twitterPassword = twitterTree.findtext('password')

        usernameInput = browser.find_element_by_id('signin-email')
        passwordInput = browser.find_element_by_id('signin-password')
        usernameInput.send_keys(twitterUsername)
        passwordInput.send_keys(twitterPassword)
        passwordInput.submit()
 
    getThis = {
        'facebook': getFacebook,
        'gmail': getGmail,
        'twitter': getTwitter
    }
    getThis.get(keyName)()
   
class mainGUI:

    pyautogui.alert(text='Do not close the browser and click on an account option. This will result in an error. \n\nTo prevent this error if the browser is accidentally or intentionally closed, close and restart the program.', title='Webdriver Notice')
                
    def __init__(self, master):
        self.master = master
        master.title('Project Sagiri - Login Assist (Social Automate)')

        #Draw buttons on main window
        #1-1
        self.fbBtn = Button(master, command=lambda: startDriver('facebook'))
        self.fbBtnImage = ImageTk.PhotoImage(file='facebook.png')
        self.fbBtn.config(image=self.fbBtnImage, width='150', height='40')
        self.fbBtn.image = self.fbBtnImage
        self.fbBtn.grid(row=1)

        #1-2
        self.gmailBtn = Button(master, command=lambda: startDriver('gmail'))
        self.gmailBtnImage = ImageTk.PhotoImage(file='gmail.png')
        self.gmailBtn.config(image=self.gmailBtnImage, width='150', height='40')
        self.gmailBtn.image = self.gmailBtnImage
        self.gmailBtn.grid(row=1, column=2)

        #1-3
        self.twitterBtn = Button(master, command=lambda: startDriver('twitter'))
        self.twitterBtnImage = ImageTk.PhotoImage(file='twitter.png')
        self.twitterBtn.config(image=self.twitterBtnImage, width='150', height='40')
        self.twitterBtn.image = self.twitterBtnImage
        self.twitterBtn.grid(row=1, column=3)

        #2-1
        self.closeBtn = Button(master, text='Close Sagiri', command=master.destroy)
        self.closeBtn.grid(row=2, rowspan=2, columnspan=4, sticky=E)
    
root = Tk()
maingui = mainGUI(root)
root.mainloop()
