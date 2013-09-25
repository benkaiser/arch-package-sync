WARNING
-------
This needs a server-side script which I am not hosting. To host it yourself the code is in the node_server_script (used on a hosted nodejs app).

Arch Package Sync
=================
Used to move a list of installed packages between computers. Typically this is used when installing on a new computer, to mirror the same package installation.

Steps
------
ON SOURCE COMPUTER

- Download the main.py script
- Make it executable
- Run it with no parameters to upload you package lists
- A url including your username will be given to you. You will need this for the destination computer

ON DESTINATION COMPUTER

- Same as above, but download the package lists using the -i parameter and your id. e.g: `./main.py -i <username>` where <username> is your username from before. 
- This will save two files to your current directory, Pacman_Packages and AUR_Packages. You can then use them to install through pacman and yaort (or your prefered AUR helper).
