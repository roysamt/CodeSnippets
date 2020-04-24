# Snippet

#!/bin/bash
#Tested on Debian (Ubuntu 16.04 LTS)

# Issue: 
#		Serial port (/dev/ttyS*) does not show up in kernel ring message buffer
#		and is not openable in software.
# i.e.
dmesg | grep ttyS
# does not return an entry for the problematic serial port.

# Solution:
# For example, we will use /dev/ttyS0.

# Step 1: Disable port as active console (if applicable)
# To check applicablity:
cat /sys/class/tty/console/active
# If /dev/ttyS0 is listed, we edit the grub config to remove it:
sudo sudo
vim /etc/default/grub.d/platform.cfg
# Edit the file to remove the `console` assignment for the serial port
# e.g. remove "console=ttyS0,115200"
# Now update grub and reboot
sudo update-grub
sudo reboot

# Step 2: Disabble geTTY service on the port
# Run the following in sequence, replacing "ttyS2" with the appropriate serial port
systemctl start serial-getty@ttyS0.service
systemctl stop serial-getty@ttyS0.service
systemctl disable serial-getty@ttyS0.service
systemctl mask serial-getty@ttyS0.service
# This starts, stops, disables bootstrapping, and masks out the auto enable for bootstrapping the service.
sudo reboot
# The ageTTY service will now no longer appear on the serial port

# End snippet