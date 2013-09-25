#!/usr/bin/python

# globals
website = "http://xpressen.com/arch-sync/"
website = "http://localhost:3000/arch-sync/"
get_pacman_packages = 'pacman -Qqe | grep -vx "$(pacman -Qqm)"'
get_aur_packages = 'pacman -Qqm'

# main program
def main():
    # setup arguements
    parser = argparse.ArgumentParser(description='Sync arch packages between computers.')
    parser.add_argument("-d", "--download", dest="id", help="Download package list found in the url " + website + "/USERNAME")
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
            values = {'pacman': pacman, 'aur': aur, 'username':  os.getlogin()}
            data = urllib.parse.urlencode(values)
            binary_data = data.encode('utf-8')
            req = urllib.request.Request(website, binary_data)
            res = urllib.request.urlopen(req)
            page = res.read().decode('utf-8')
            print(page)
        else:
            print("Exiting...")
    else:
        # downoad from the specified args.id
        new_url = website + args.id
        print("Downloading packages from " + new_url)
        req = urllib.request.Request(new_url)
        res = urllib.request.urlopen(req)
        page = json.loads(res.read().decode('utf-8'))
        loc = input("Save files to (default current directory): ")
        if len(loc) > 0:
          # save to current directory
          path = os.path.normpath(loc)
        else:
          # save to specified directory
          path = os.getcwd()
        path += os.sep
        save_to_file(path + "/Pacman_Packages", page["pacman"])
        save_to_file(path + "/AUR_Packages", page["aur"])


def save_to_file(location, data):
  print("Saving data to file: " + location)
  fp = open(location, "w")
  fp.write(data)
  fp.close()


if __name__ == '__main__':
    try:
        # imports
        import subprocess # calling pacman
        import argparse # parameter parsing
        import urllib # url utility
        from urllib.request import urlopen # url utility
        import os # get username
        import json # decode recieved data

        # did not fail on imports, run program
        main()
    except ImportError as error:
        print("Missing python module: " + str(error)[16:])