# Password Locker

## Description

An application that allows users to generate, store and manage their passwords offline

## Features
1. Save Passwords
2. Generate new passwords
3. View saved passwords
4. Delete saved passwords
5. Copy passwords on clipboard if required



## BDD
| BEHAVIOUR                            | INPUT EXAMPLE                           | OUTPUT EXAMPLES       |
|--------------------------------------|:------------------------------------:|--------------------------|
|Start the application | User runs $./run.py in terminal|User is prompted to enter their userName and password to create an account|
|Login to existing account | Tyoe username and password | User is logged into the app and menu is displayed |
|Create new credentials | Select add new credentials options | User is prompted to either generate their own password or let the system generate one for them |
|View saved credentials |Select search credentials | A list of saved credential(s) is displayed |
|Delete a saved credentials | Select remeove credential | saved credentials are displayed for user to chose the one they desire to delete |

## Github Pages
    The UI templates can be tested on [github pages](https://tgalvinjr.github.io/password-locker-IP/)
    
## Setup instructions
1. Open your terminal 
2. From Github, clone/download this repository 
3. Run the command $ git clone https://github.com/tgalvinjr/password-locker-IP.git
4. Change directory by running $ cd password-locker-IP
5. Run $ chmod +x run.py to make the program executable
6. Run $ ./run.py

## Prerequisties 
Install required libraries by running $ pip install -r requirements.txt



## Technologies Used
`Python 3.6`

## Known Bugs
None at the moment

### Author(s) information
Alvin Michoma
[Github](https://github.com/tgalvinjr)

## License and Copyright information
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tgalvinjr/password-locker-IP/blob/master/LICENSE) file for details

## Acknowledgments
- Hat tip to everyone who unblocked me in class
- Special thanks to Moringa TMs Peter, Edgar and Newton for the guidance 
