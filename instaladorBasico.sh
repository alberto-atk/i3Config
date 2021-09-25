sudo apt update
sudo apt upgrade -y

#Instalacion vscode
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

sudo apt install code

#Instalacion chrome
wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo apt-get update

sudo apt-get install libappindicator1

sudo dpkg -i google-chrome-stable_current_amd64.deb

#Instalacion Github Desktop
sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.9.3-linux1/GitHubDesktop-linux-2.9.3-linux1.deb

sudo dpkg -i GitHubDesktop-linux-2.9.3-linux1.deb

#Instalacion flameshot
sudo apt-get install -y flameshot

#Instalacion git
sudo apt install git -y

