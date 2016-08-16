# install other packages
pacman -S --needed --noconfirm xf86-input-synaptics
pacman -S --needed --noconfirm guake
pacman -S --needed --noconfirm gnome-terminal
pacman -S --needed --noconfirm scrot
pacman -S --needed --noconfirm fcitx-{im,qt5,googlepinyin,configtool}
pacman -S --needed --noconfirm p7zip
pacman -S --needed --noconfirm mpv
pacman -S --needed --noconfirm easytag
pacman -S --needed --noconfirm alsa-utils
pacman -S --needed --noconfirm nodejs
pacman -S --needed --noconfirm phantomjs
pacman -S --needed --noconfirm pavucontrol
pacman -S --needed --noconfirm simplescreenrecorder
pacman -S --needed --noconfirm progress
pacman -S --needed --noconfirm btrfs-progs
pacman -S --needed --noconfirm vim-python3 bpython python-pip

pacman -S --needed --noconfirm mdk3
pacman -S --needed --noconfirm nmap
pacman -S --needed --noconfirm ettercap
pacman -S --needed --noconfirm aircrack-ng

# install and enable Network Manager
pacman -S --needed --noconfirm networkmanager
systemctl enable NetworkManager
systemctl start NetworkManager
