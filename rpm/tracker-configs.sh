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
# Include Android user data directories
gsettings set org.freedesktop.Tracker.Miner.Files index-recursive-directories "['&DESKTOP', '&DOCUMENTS', '&DOWNLOAD', '&MUSIC', '&PICTURES', '&VIDEOS', '$HOME/android_storage']"
# Our custom ignore flags are 'backup.metadata' and '.nomedia'
gsettings set org.freedesktop.Tracker.Miner.Files ignored-directories-with-content "[ '.trackerignore', 'backup.metadata', '.nomedia' ]"
# Ignore .git metadata, but not git repos
gsettings set org.freedesktop.Tracker.Miner.Files ignored-directories "[ '.git', 'po', 'CVS', 'core-dumps', 'lost+found' ]"
# Ignore common album art image names that might occur on the SD card
gsettings set org.freedesktop.Tracker.Miner.Files ignored-files "[ '*~', '*.o', '*.la', '*.lo' , '*.loT', '*.in', '*.csproj', '*.m4', '*.rej', '*.gmo', '*.orig', '*.pc', '*.omf', '*.aux', '*.tmp', '*.po', '*.vmdk', '*.vm*', '*.nvram', '*.part', '*.rcore', '*.lzo', 'autom4te', 'conftest', 'confstat', 'Makefile', 'SCCS', 'ltmain.sh', 'libtool', 'config.status', 'confdefs.h', 'configure', '#*#', '~$*.doc?', '~$*.dot?', '~$*.xls?', '~$*.xlt?', '~$*.xlam', '~$*.ppt?', '~$*.pot?', '~$*.ppam', '~$*.ppsm', '~$*.ppsx', '~$*.vsd?', '~$*.vss?', '~$*.vst?', '*.desktop', '*.directory', 'Folder.jp*', 'Folder.png', 'Folder.gif', 'cover.jp*', 'cover.png', 'cover.gif', 'AlbumArt*.*' ]"
tracker reset -ey

