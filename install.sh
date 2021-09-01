#!/usr/bin/env bash
if [[ "$(id -u)" -ne 0 ]];
then
 echo "Please, Run This Programm as Root!"
 echo "
Usage: 
     sudo install.sh
    "
 exit 1
fi
function main() {
    printf '\033]2;Google-Translator/Installing'
    clear
    echo "
MMMMMMMMMMMMWNXK000OO00KKXNWMMMMMMMMMMMM
MMMMMMMMWNKOxdllcccccccclldxOKNWMMMMMMMM
MMMMMMWKkolccccccccccccccccccldONMMMMMMM
MMMMWKxlcccccccccccccccccccccld0NMMMMMMM
MMMNOocccccccloxkO0000OkxolldONWMMMMMMMM
MMNOlccccccokKNWMMMMMMMMWNK0NWMMMMMMMMMM
MWKOxolcclxKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MN0OOOkdokNWMMMMMMMWWWWWNNNNNNNNNWNWWWMM
WXOOOOOO0NMMMMMMMMWKxxdddddddddddddddONM
WKOOOOOOKWMMMMMMMMWOoolllllllllllllllxXM
WKOOOOOOKWMMMMMMMMWOoolllllllllllllllxXM
WX0OOOOkkKWMMMMMMMWXOOkkOOkOkkollllllkNM
MNKOOkdoldKWMMMMMMMMMMMMMMMMW0dlllllo0WM
MMXkdlllllokXWMMMMMMMMMMMMWNOdllllloONMM
MMWKdlllllllox0KNNWWWWNNX0kdllllllokNMMM
MMMWXkolllllllllodxxxxdoolllllllld0NMMMM
MMMMMWKkolllllllllllllllllllllldOXWMMMMM
MMMMMMMWX0kdlllllllllllllllldk0NWMMMMMMM
MMMMMMMMMMWNK0OkxxddddxxkO0KNWMMMMMMMMMM
MMMMMMMMMMMMMMMWWNNNNNNWWMMMMMMMMMMMMMMM
"
    echo "Installing..."
    apt install python
    apt install python3
    apt install python-pip
    pip install --upgrade pip
    echo "Ok, Finish...!"
    echo "
Usage:
      python3 translate.py
    "
    exit 1
}
main