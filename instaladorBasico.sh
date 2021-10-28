sudo apt update
sudo apt upgrade -y

#Instalacion vscode
sudo apt-get install snapd

sudo snap install code --classic

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
sudo apt install -y git

#Instalacion i3
sudo apt install i3 -y

#Instalacion rofi
sudo apt install rofi -y

#Instalacion telegram
sudo apt install telegram-desktop

#Instalacion terminal fish
sudo apt-get install fish

#Usar fish en lugar de bash
chsh -s /usr/bin/fish

#https://cravencode.com/post/essentials/enable-tap-to-click-in-i3wm/

#Descarga scripts github
mkdir bin

cd bin

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/discord

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/Universidad

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/apagar

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/whatsapp

chmod +x discord whatsapp Universidad apagar

#Descarga de las imagenes de whatsapp y discord
mkdir img
cd img

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/img/discord.png

https://raw.githubusercontent.com/alberto-atk/i3Config/main/img/whatsapv1.png
mv whatsapv1.png whatsapp.png

#Agreger /bin al path
PATH=$PATH

PATH=$PATH:/home/alberto/bin

#Hay que reiniciar despues para que se cree el directorio de configuracion de i3 (sudo reboot)

