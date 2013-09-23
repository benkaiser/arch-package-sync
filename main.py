#!/usr/bin/python

# globals
website = "http://xpressen.com/arch-sync/"
get_pacman_packages = 'pacman -Qqe | grep -vx "$(pacman -Qqm)"'
get_aur_packages = 'pacman -Qqm'

# main program
def main():
    # setup arguements
    parser = argparse.ArgumentParser(description='Sync arch packages between computers.')
    parser.add_argument("-i", "--id", dest="id", help="Download id found in the url " + website + "/ID")
    args = parser.parse_args()
    if args.id == None:
        # get pacman package list
        pacman = subprocess.Popen(get_pacman_packages, stdout=subprocess.PIPE, shell=True).communicate()[0].decode("utf-8").strip()
        # get aur package list
        aur = subprocess.Popen(get_aur_packages, stdout=subprocess.PIPE, shell=True).communicate()[0].decode("utf-8").strip()
        resp = input("Packages lists ready for uploading... Upload them? [Y/n]: ");
        if(resp == "" or resp == "Y" or resp == "y"):
            # start the upload
            print("Uploading....")
            values = {'pacman': pacman, 'aur': aur}
            data = urllib.parse.urlencode(values)
            binary_data = data.encode('utf-8')
            req = urllib.request.Request(website, binary_data)
            res = urllib.request.urlopen(req)
            page = res.read().decode('utf-8')
            print(page)
        else:
            print("Okay. Now attempting to wipe your home dir, Just kidding!")
    else:
        # downoad from the specified args.id
        print("Download!")

if __name__ == '__main__':
    try:
        # imports
        import subprocess # calling pacman
        import argparse # parameter parsing
        import urllib # url utility
        from urllib.request import urlopen # url utility

        # did not faile on imports, run program
        main()
    except ImportError as error:
        print("Missing python module: " + str(error)[16:])