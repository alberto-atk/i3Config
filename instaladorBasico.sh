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
sudo apt install i3blocks -y

#Instalacion rofi
sudo apt install rofi -y

#Instalacion telegram
sudo apt install telegram-desktop

#Instalacion pavucontrol(pulseaudio manager)
sudo apt install pavucontrol -y

#Instalacion terminal fish
sudo apt-get install fish

#Usar fish en lugar de bash
chsh -s /usr/bin/fish

#https://cravencode.com/post/essentials/enable-tap-to-click-in-i3wm/

#Descarga scripts github
mkdir bin

cd bin

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/discord

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/whatsapp

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/youtube-music

chmod +x discord whatsapp Universidad apagar

#Descarga de las imagenes de whatsapp y discord
mkdir img
cd img

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/img/discord.png

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/img/whatsapv1.png
mv whatsapv1.png whatsapp.png

wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/img/youtube-music1.png
mv youtube-music1.png youtube-music.png

#Agreger /bin al path
PATH=$PATH

PATH=$PATH:/home/alberto/bin


#Descarga de los .desktop
cd /usr/share/applications/
sudo wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/whatsapp.desktop
sudo wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/discord.desktop
sudo wget https://raw.githubusercontent.com/alberto-atk/i3Config/main/youtube-music.desktop
#Hay que reiniciar despues para que se cree el directorio de configuracion de i3 (sudo reboot)

