#! /bin/bash

# $1 nombre del .desktop
# $2 direccion imagen
# $3 direccion del exec

texto=$"[Desktop Entry] \n
Encoding=UTF-8 \n
Version=1.0 \n
Type=Application \n
Terminal=false \n
Exec=$3 \n
Name=$1 \n
Icon=$2 \n"


nombreArchivo="$1.desktop"

touch $nombreArchivo
chmod +x $nombreArchivo
echo -e $texto > $nombreArchivo