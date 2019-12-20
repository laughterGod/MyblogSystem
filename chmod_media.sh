#!/bin/bash
chmod -R 777 ./media/

# 1. crontab -e
# 2. */1 * * * * cd /home/MyProject/MyblogSystem/ && sh ./chmod_media.sh
# 3. /sbin/service crond restart

