#!/data/data/com.termux/files/home/../usr/bin/sh
termux-wake-lock
sleep 15
nohup mysqld_safe > /dev/null 2>&1 &
nohup python ~/watchdog_tunnels.py > ~/watchdog.log 2>&1 &