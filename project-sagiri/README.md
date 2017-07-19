PROJECT SAGIRI: A Web Login Automation Program
- This project is coded using Python 3. Use or install idle3 in order to run this.
- pip3 install pyautogui selenium and PIL; otherwise GUI may not work.
- Developed in a Linux environment and tested once on Windows. It will work on Windows provided that
all needed modules/libraries are pip3 installed. Expect bugs.
- For best result, run this in a Linux-based OS.


THIS IS A WORK IN PROGRESS.                  
BUGS AND INCONSISTENCIES ARE TO BE EXPECTED.

Github repository will be updated if changes
are ready to be committed.                  
Find me as Mespeon and check repo.

IMPORTANT NOTES:
A. Edit key.xml before using the program. This is an XML file that will be read by the program in order
to automate credential typing and submission. Currently, this file only supports Facebook, GMail, and
Twitter. DO NOT EDIT ANY OF THE TAGS AS THIS WILL BREAK THE PROGRAM. Leaving tags empty will make the
program do nothing.
    EDITING THE key.xml FILE
    1. Open with Notepad, Notepad++, Scratch, or any text editor.
    2. Find the account you'd use.
    3. Between the <username> tags, type your username. (ex. <username>XXYYZZ</username>)
    4. Between the <password> tags, type your password. (ex. <password>AABBCC</password>)
    5. Save the file and then run the program to see if it could properly read and type your credentials.

B. This may be an automated login program but it will never send any sensitive information via a backdoor.
The program uses an external key file and it will simply read whatever information you put in that file.
Check the source code if you want to be sure. 

CREDITS:
Marvin Bruno (brunomarvss @ Github) - original source code (and for the inspiration!)
JM Dharma - for the inspiration and talks and debugging and everything
