#!/bin/bash

#Instalacja Pythona i biblioteki pdfrw
apt install python3
python3 -m pip install pdfrw==0.4

#Stworzenie katalogów
mkdir /opt/pdf-generator
mkdir /var/webpage/public/pdf

#Przeniesienie generatora do odpowiednich folderów
mv public/* /var/webpage/public/pdf/
mv private/* /opt/pdf-generator/

#Stworzenie folderu
mkdir /opt/pdf-generator/logs
chown www-data:www-data /opt/pdf-generator/logs
chmod 775 /opt/pdf-generator/logs
