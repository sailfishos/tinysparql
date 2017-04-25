#!/bin/bash
set -e
if [ "$MIC_RUN" != "" ]; then
	echo "tracker-configs.sh - returning FAIL to postpone oneshot to first boot"
	exit 1
fi

gsettings set org.freedesktop.Tracker.Miner.Files index-removable-devices true
gsettings set org.freedesktop.Tracker.Miner.Files crawling-interval 0
gsettings set org.freedesktop.Tracker.Miner.Files initial-sleep 30
gsettings set org.freedesktop.Tracker.Miner.Files throttle 10
gsettings set org.freedesktop.Tracker.Miner.Files enable-writeback false
gsettings set org.freedesktop.Tracker.Miner.Files removable-days-threshold 30
gsettings set org.freedesktop.Tracker.Miner.Files index-single-directories "['$HOME']"
gsettings set org.freedesktop.Tracker.Miner.Files index-recursive-directories "['&DESKTOP', '&DOCUMENTS', '&DOWNLOAD', '&MUSIC', '&PICTURES', '&VIDEOS', '$HOME/android_storage']"
gsettings set org.freedesktop.Tracker.Miner.Files ignored-directories-with-content "[ 'backup.metadata', '.nomedia' ]"
gsettings set org.freedesktop.Tracker.Miner.Files ignored-directories "[ 'po', 'CVS', 'core-dumps', 'lost+found', '$HOME/android_storage/Android' ]"
tracker reset --soft
