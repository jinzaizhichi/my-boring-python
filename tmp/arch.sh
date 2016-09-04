# create `continue_install.bash`
cp private/arch_install_and_config/scripts/continue_install.bash /mnt/continue_install.bash
chmod 755 /mnt/continue_install.bash

# run 'continue_install.bash' via `arch-chroot`
arch-chroot /mnt /continue_install.bash
rm /mnt/continue_install.bash   
