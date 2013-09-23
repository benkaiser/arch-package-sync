Arch Package Sync
=================
Used to move a list of installed packages between computers. Typically this is used when installing on a new computer, to mirror the same package installation.

Steps
------
ON SOURCE COMPUTER

- Download the main.py script.
- Make it executable
- Run it with no parameters to upload you package lists
- An ID number will be given to you. Write this down.

ON DESTINATION COMPUTER

- Same as above, but download the package lists using the -i parameter and your id. e.g: `./main.py -i 123456`
- This will save two files to your current directory, Packages and AUR_Packages

#TODO: Give instructions for installing the package list on the new computer.