# Snippet

#!/bin/bash
#Tested on Debian (Ubuntu 16.04 LTS)

# Issue: 
#		EXT4 filesystem becomes read-only due to bad blocks.
#		Indicated by machine booting into grub command line
#		with the following message:

# grub$  efi: requested map not found.
# grub$  esrt: ESRT header is not in the memory map.

# Solution:
#		Run the following in the root terminal after booting in
#		recovery mode.
# To get into recovery mode at boot (Ubuntu): 
# 		Select "Advanced options for Ubuntu" then "Recovery mode". 
#		At the menu, select "root" to drop down to a root terminal.

sudo umount /
sudo umount /dev/mmcblk0p2
sudo fsck.ext4 /dev/mmcblk0p2 -y
sudo dpkg --configure -a
sudo apt-get dist-upgrade

# If the above solution does not work, a BIOS re-flash or full re-format may be necessary.

# End snippet