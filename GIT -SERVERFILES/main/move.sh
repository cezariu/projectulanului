cd /usr/home/main/srv1/share/bin
rm -rf game
rm -rf db
cp -iprv /usr/src/jailsrc/SERVER/Server/db/db /usr/home/main/srv1/share/bin/db
cp -iprv /usr/src/jailsrc/SERVER/Server/game/game /usr/home/main/srv1/share/bin/game
chmod 777 game
chmod 777 db
echo -e "gata le-am mutat"