
# 前言

本向导适用于初学者或者有一点点基础的linux用户。如果有任何问题或者建议请在“焕然一新41吧”发帖询问。或者去别的地方提问。

由于我还没有安装过程的图片，所以本教程可能很少图或者没有图

由于我不是很熟悉uefi，所以本教程对于uefi的用户可能有点危险。

内容有点多，如果你之事想找某个内容请按Ctrl+F搜索。

当然你也可以顺便参考别人写的arch安装向导来修补本向导的不完整。

# 1. 准备

## 1.1 下载Arch Linux安装镜像

下载地址：推荐http://mirrors.ustc.edu.cn/archlinux/iso/ ，选择现在的月份下载，然后选择archlinux-你选择的年月.iso 下载（例如现在是archlinux-2016.07.01-dual.iso）。

你也可以到官网https://www.archlinux.org/ 下载，但是下载的速度特别的慢，请酌情使用。

> 建议：下载完成后验证MD5

## 1.2 刻录u盘

**Windows** :使用“win32diskimage”或者”winsetupfromdisk”刻录。

> 警告：请勿使用软碟通

**Linux** :使用dd刻录.


# 2. 安装Arch Linux

在阅读这一章节的时候，请确保你已经完成了上面的所有步骤，并且确保你有足够的耐心,否则请安装arch的衍生版（manjaro之类的），或者使用本文章最后的一件配置脚本。

## 2.1 选择x86_64 或者i686

建议选择x86_64 ，因为i686可能会停止支持，而且有些软件已经不兼容了，选择完毕后按回车，进入live

## 2.2 检测网络畅通&链接wifi

Ping百度（执行ping baidu.com），如果有数据包返回说明网络联通。

如果你是wifi，输入wifi-menu就可以了。

## 2.3 改源

由于arch默认的是外国的源，速度很慢，所以需要改源
命令nano /etc/pacman.d/mirrorlist 或者 vim /etc/pacman.d/mirrorlist把#后面是china的源弄到最上面，也可以直接删除不是china的源。

## 2.3 分区

> 警告：该步骤可能导致你的硬盘数据丢失，请务必知道自己在做什么。

实体机：输入cfdisk，选择你要安装arch的分区，选中Delete，回车，再按回车，然后选择New，按一下回车，选择write，输入yes，选择quit，回车（你也可以选择分一个swap区）。

然后 mkfs.ext4 /dev/你刚刚分的区。

例如你要安装在第一个分区就mkfs.ext4 /dev/sda1。


虚拟机分区：虚拟机和实体机不一样，必须要一个swap，否则无法引导。

分区方案:cfdisk

* /dev/sda1 1GB~4GB
* /dev/sda2 30%硬盘空间
* /dev/sda3 45%~50%硬盘空间
* /dev/sda4 2*内存

然后执行

1. mkfs.ext4 /dev/sda2
2. mkfs.ext4 /dev/sda3
3. mkswap /dev/sda4
4. swapon /dev/sda4
5.mkfs.ext4 /dev/sda1

注意：请具体参考http://tieba.baidu.com/p/2307324919 来在虚拟机分区

## 2.4 挂载分区

如果你是按照第一个方法分区的话，输入

mount /dev/你的磁盘 /mnt

例如mount /dev/sda1 /mnt

如果你使用的第二种方法分区(虚拟机），请输入

mount /dev/sda2

## 2.5 更新系统源

输入 pacman -Syy ,然后输入y。

等待一下，完成。
## 2.6 安装基本系统

输入pacstrap -i /mnt base base-devel net-tools

按两下回车，输入y，等待十分钟左右。

## 2.7 我也不知道干什么要做这一步

genfstab -p /mnt >> /mnt/etc/fstab

## 2.8 chroot进入新的系统

arch-chroot /mnt

> 提示：可选：安装wifi

先重复上面的改源，然后

pacman -Syy

pacman -S netctl

## 2.9 设置语言，地区什么的
cd /etc
nano locale.gen
将
>en_US.UTF8
zh_CN.GBK
zh_CN.GB2312
zh_CN.GB18030
zh_CN.UTF-8

前的#去掉  
然后输入locale-gen  
再输入
>echo LANG=zh_CN.UTF-8 >> locale.conf  

然后输入nano /etc/vconsole.conf
把下面的内容写进去
>KEYMAP=us
FONT=

保存退出
然后输入
>ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

2.10 创建主机名字
输入nano /etc/hostname
然后在里面输入你要的主机名字，保存退出（ctrl+x)


2.11 设置root密码，创建新用户
输入passwd设置root密码
输入useradd -m -g users -G wheel -s /bin/bash 你要的用户名 创建新用户
passwd 你的用户名
创建密码即可

2.22 安装grub（可能不适用uefi，如果不适用请自行百度）
pacman -S grub-bios 

grub-install /dev/sda 

grub-mkconfig -o /boot/grub/grub.cfg
你也可以参考这个https://wiki.archlinux.org/index.php/GRUB
        EFI和苹果电脑请参考这个
https://wiki.archlinux.org/index.php/GRUB/EFI_examples
2.23取消挂载分区，重启
exit

umount /mnt/{boot,home}

umount /mnt

Reboot








到这里，基本系统安装完毕，接下来就是装桌面环境了

                     安装桌面环境
当你重启进入系统的时候，恭喜你，你的基本系统安装完了，但是你还没有桌面可以用，所以现在我们就要来安装桌面环境.

3.1 接通网络
输入：ip link set 你的网卡名字 up

dhcpcd
当然有的电脑可以直接dhcpcd
链接wifi：wifi-menu
然后ping baidu.com检测网络
3.2 改源&更新系统源列表
遵循上面的改源方法（如果已经是中国的就不用管了），然后pacman -Syy

*安装显卡驱动
pacman -S xf86-video-vesa
pacman -S xf86-video-nouveau
3.3 把用户添加进sudo用户组
输入visudo
在“root  ALL=(ALL)   ALL”这一行下面，再加入一行：
                 xulei  ALL=(ALL)     ALL

3.4 安装桌面环境（列出了2种，请自己选择，如果要状别的，请自行搜索）[记得以root运行！]
1.gnome

pacman -S gnome

pacman -S file-roller evolution gedit gnome-music gnome-photos cheese gnome-mplayer

pacman -S unrar unzip p7zip

pacman -S deepin deepin-extra lightdm
（可选，安装deepin的包美化，增强系统）
pacman -S evince  thunderbird gpicview

pacman -S chromium（可选，安装chromium浏览器）
 然后配置network
pacman -S networkmanager

systemctl enable NetworkManager

systemctl enable gdm

systemctl enable lightdm （可能会失败，不用担心）
然后重启，就能进入gnome了
 
2.安装cinnamon
注意：cinnamon要你配置的很多，小白请勿尝试
22.安装X窗口和桌面环境基础：
pacman -S xorg-server xorg-server-utils    # 安装 Xorg Server
pacman -S xf86-input-synaptics    # 可选，触摸板支持
pacman -S ttf-dejavu wqy-microhei    # 可选，Dejavu 与文泉驿 - 微米黑字体
23.安装cinnamon: pacman -S cinnamon
24.安装startx: pacman -S xorg-xinit
25.安装slim: pacman -S slim
26.配置开机启动slim: systemctl enable slim
27.配置开机启动cinnamon:
echo exec cinnamon-session > ~/.xinitrc

31.安装sudo：pacman -S sudo

33.安装roxterm：pacman -S roxterm
34.安装网络管理：pacman -S networkmanager
35.开机启动网络管理：systemctl enable NetworkManager.service



































        配置系统
经过上面的一系列安装以后，没有出错的话，你现在已经进入了桌面环境,但是这个时候的系统非常不好用（什么软件都没有），所以我们要来安装软件。

4.1切换系统为中文（仅限gnome）
打开终端
输入nano /etc/locale.gen
去掉所有zh_CN前面的#
保存退出
输入locale-gen
  在设置里面打开Langauage，设置语言为中文。 
重启就变成中文了

4.2 安装输入法
1.安装fcitx
注意：按照我的做法，你保证可以安装成功fcitx！
输入sudo pacman -S --needed --noconfirm fcitx-{im,qt5,googlepinyin,configtool}
然后输入sudo pacman -S fcitx-im fcitx-configtool fcitx-cloudpinyin
然后在 nano ~/.xinitrc ，加入：
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
然后输入 nano ～/.profile 
加入
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
重启
            
                2.安装ibus
注意：你可能会遇到双拼或全拼的问题，此问题可能暂时无解
sudo pacman -S ibus
sudo pacman -S ibus-qt 
sudo pacman -S ibus-libpinyin
sudo pacman -S ibus-sunpinyin
ibus-daemon -drx
ibus-setup

但是，如果ibus尚未启动，先将这些
  export GTK_IM_MODULE=ibus
  export XMODIFIERS=@im=ibus
  export QT_IM_MODULE=ibus

代码复制到$HOME/.xprofile，并将这行代码加到该文件：“ibus-daemon -x -d”,再重新登录。


3.安装小小输入法
国人的一个输入法，还不错
下载：http://yongim.ys168.com/
解压，参照这篇文章安装
http://www.mintos.org/skill/xiaoxiao-input.html




4.3 开启yaourt
yaourt源里有很多pacman所没有的软件，包括后面的wineqq，dpkg，chrome都要用到它
在/etc/pacman.conf添加:
[archlinuxfr] 
SigLevel = Never 
Server = http://repo.archlinux.fr/$arch
然后执行:pacman -Sy yaourt

如果上面的方法不可行，这样做
最简单安装Yaourt的方式是添加Yaourt源至您的 /etc/pacman.conf:
[archlinuxcn]
#The Chinese Arch Linux communities packages.
SigLevel = Optional TrustAll
Server   = http://repo.archlinuxcn.org/$arch
同步并安装：
# pacman -Syu yaourt
提示：pacman要root权限，yaourt正好相反，不能加sudo！
注意：完成上面的步骤以后一定要执行sudo /usr/bin/update-ca-trust,否则无法获取aur软件。

4.4 安装google-chrome

确保你安装了yaourt，然后
yaourt -S google-chrome-stable
如果没有yaourt，直接pacman -S google-chrome

4.5 安装dpkg（可选）
yaourt -S dpkg

4.6 安装wineqq
yaourt -S wine-qqintl (安装QQ国际版）
yaourt -S wineqq-longene （安装winee7.8）
如果你想要安装别的deb版qq，确保你安装了dpkg
然后dpkg -i 你的deb
因为arch没有debian上的依赖包，所以你需要安装这两个aur的qq
yaourt -S wine-qqintl 
yaourt -S deepinwine-qq 
这里也推荐一个第三方很好用的wineqq（我现在也用着），按照这里的步骤安装，既可以截图，也可以用键盘输入密码了～https://www.linuxdashen.com/%E4%B8%A4%E4%B8%AA%E7%AE%80%E5%8D%95%E6%AD%A5%E9%AA%A4%E5%9C%A8archlinux%E4%B8%8A%E5%AE%89%E8%A3%85qq
注意，你可能需要开启testing源，请看4.9


4.7 安装vbox
终端执行下面的命令（一条条）
sudo pacman -S virtualbox linux-headers --noconfirm
sudo modprobe vboxdrv
virtualbox



4.8 安装vmware
官网下载vmware12.10(注意，版本必须大于12.1)
你可以到这里下载：http://www.vmware.com/products/workstation/workstation-evaluation.html
下载完成后chmod 777 你下载的文件
然后./你下载的文件
到有一个什么/etc/init.d的时候，点击浏览，选择/etc/init.d这个文件夹，然后下一步，如果没有这个文件夹就创建一个（要用sudo）
然后一直下一步，可能会出现一个错误提示，不要紧，忽略掉。
等图形安装完成以后，执行下面的命令：（不要输入#）
# cd /usr/lib/vmware/modules/source
# tar xf vmmon.tar
# mv vmmon.tar vmmon.old.tar
# sed -i -e 's/get_user_pages/get_user_pages_remote/g' vmmon-only/linux/hostif.c
# tar cf vmmon.tar vmmon-only
# rm -r vmmon-only
# tar xf vmnet.tar
# mv vmnet.tar vmnet.old.tar
# sed -i -e 's/get_user_pages/get_user_pages_remote/g' vmnet-only/userif.c
# tar cf vmnet.tar vmnet-only
# rm -r vmnet-only
输入注册码，大功告成！
ps：第二期启动虚拟机可能会失败，上终端输入sudo /etc/init.d/vmware restart就好了。



4.9 开启testing源
testing源是arch的一个测试源，你可以获取更多地软件和更新的版本



sudo nano /etc/pacman.conf
然后把里面为testing前面的#去掉（所有）
例如说原来是这样的

#[community-testing]
#Include = /etc/pacman.d/mirrorlist
改成

[community-testing]
Include = /etc/pacman.d/mirrorlist
然后保存推出，执行sudo pacman -Syy
警告：不要轻易开testing源，因为可能会导致你的系统滚挂




以上就是安装配置arch的基本内容，文笔不好，多多谅解
需要自动（一体化）配置的请看下面



























       arch一键配置
  当然了，如果你实在是太懒或者根本不会想体验arch，你可以使用@Guanrenfu的快速配置脚本




1.arch快速配置脚本
注意：这只是一个“脚本”帮你快速安装，并不能让你的系统完全像是guanrenfu一样，如果想象他一样，请看2。
警告：虚拟机不适用，如果应要用，不要用fbterm执行（会死机），直接执行就好，但是会乱码，详情请咨询我。
使用方法
按照上面的说明，分区，改源（可以不挂在分区），但是一定要格式化
然后
pacman -Syy
pacman -S git fbterm wqy-microhei 
fbterm(注意：虚拟机就不要进入了）
git clone --depth=1 https://github.com/K-Guan/Arch-quick-install-and-config
./Arch-quick-install-and-config/scripts/Arch-Linux-quick-install.sh
然后按照提示安装

重启以后，安装桌面环境和输入法：
按照上面的说明，改源（如果已经改了就不用了）
然后
pacman -Syy
pacman -S git fbterm wqy-microhei 
fbterm(注意：虚拟机就不要进入了）
git clone --depth=1 https://github.com/K-Guan/Arch-quick-install-and-config
注意：这一步不同，不要以为我打错了。
./Arch-quick-install-and-config/scripts/Arch-Linux-quick-config.sh
然后按照提示安装即可。

2.arch一键完成脚本
本脚本会让你的电脑直接变成像guanrenfu那样
[下载这个](http://keving.pythonanywhere.com/home_folder.tar.gz)。具体步骤是（记得先看完一遍再逐步操作）：

1. 下载上面链接的文件并解压。
2. 启动 Arch Linux Live 。
3. 格式化并挂载硬盘。记得将你要安装系统的分区挂载到 `/mnt`。
3. 在确保能联网或已经的联网的前提下，在 Live 中进入压缩文件中的文件夹内并分别执行以下命令：

  
  bash private/arch_install_and_config/scripts/before.bash
  bash private/arch_install_and_config/scripts/install.fish
  然后先重新挂载mnt（按照2.4的方法）

cp private/arch_install_and_config/scripts/continue_install.bash /mnt/continue_install.bash
chmod 755 /mnt/continue_install.bash
arch-chroot /mnt /continue_install.bash
rm /mnt/continue_install.bash 



  
  并等待结束。快结束时会向你询问机器名 `hostname` 以及 `root` 密码。

4. 重启进入新系统，**在确保能联网或已经的联网的前提下**，进入压缩文件中的文件夹内分别执行以下命令：

   bash private/arch_install_and_config/scripts/before.bash
  fish private/arch_install_and_config/scripts/config.fish
  

  中途会向你询问要新用户的用户名和密码等。

5. 复制压缩文件中的文件夹内所有文件到你的新用户的用户目录下。然后运行 `chown -R <新用户名>:<新用户名> /home/<新用户名>`。

6. 登录你的新用户，并运行：

  
  fish private/arch_install_and_config/scripts/continue_config.fish
  

如果一切没问题的话，应该可以 `startx`了。配置是我直接搬过去的，除了 Chrome 的配置外其他的都和我现在用的完全一样。有什么问题或运行时遇到的错误记得问我。
具体参考
https://github.com/redapple0204/my-boring-python/issues/19





3.以前版本的arch安装向导
感谢@lizongzeshunshun
如果上面有问题的话请参考这个向导（已经实验完全可行）

ArchLinux - Install

1.Download Arch-Linux ISO.
2.Put-Iso-Into-USB
3.Boot USB
4.Choose [x86_64] or [i686]
5.>cfdisk
6.DELETE ALL [SDA]
7.Create [SDA]
******************************
   /dev/sda1    1GB~4GB
   /dev/sda2    30%-Disk-Space
   /dev/sda3    45%~50%-Disk-Space
   /dev/sda4    2*RAM-SPACE
******************************

8.Install-File-System
******************************
>mkfs.ext4 /dev/sda2
>mkfs.ext4 /dev/sda3
>mkswap /dev/sda4
>swapon /dev/sda4
>mkfs.ext4 /dev/sda1
******************************

9.Mount-SDA
******************************
>mount /dev/sda2 /mnt
>mkdir /mnt/{boot,home}
>mount /dev/sda1 /mnt/boot
>mount /dev/sda3 /mnt/home
******************************

10.Change Mirrolist [*IMPORTANT]
******************************
>sed -i "s/^\b/#/g" /etc/pacman.d/mirrorlist
>nano /etc/pacman.d/mirrorlist
ADD TEXT:
Server = http://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
USE [Ctrl+X] And Y And [Enter] to save and quit.
******************************

11.Update source
******************************
>pacman -Syy
******************************

12.Install basic system
******************************
>pacstrap -i /mnt base base-devel net-tools
******************************

13.Fstab
******************************
>genfstab -U -p /mnt >> /mnt/etc/fstab
******************************

14.Basic system setup
******************************
>arch-chroot /mnt /bin/bash
>alias ls='ls --color'
******************************

15.Set Locale
******************************
>nano /etc/locale.gen
>locale-gen
>echo LANG=zh_CN.UTF-8 >> locale.conf
******************************

16.Set Console
******************************
>nano /etc/vconsole.conf
Add text:
KEYMAP=us
FONT=
******************************

17.Set Time Zone
******************************
>ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
******************************

18.Set BIOS time
******************************
nano /etc/adjtime
Add Text:
0.000000 0 0.000000
0
LOCAL
******************************

19.Set LoaclHost-Name
******************************
echo [HostsName] > /etc/hostname
******************************

20.RamDisk
******************************
mkinitcpio -p linux
******************************

21.User setup
******************************
>passwd
>>[Set Password]
>useradd -m -g users -G wheel -s /bin/bash [UserName]
>passwd [UserName]
>>[Set Password]
******************************

20.Install GRUB
******************************
>pacman -S grub-bios 
>grub-install /dev/sda 
>grub-mkconfig -o /boot/grub/grub.cfg
******************************

21.Reboot
******************************
>exit
>umount /mnt/{boot,home}
>umount /mnt
>Reboot
******************************

22.Install Gnome
******************************
>ip link set [NET-CARD-NAME] up
>dhcpcd
>pacman -Syy
>pacman -S gnome
>pacman -S file-roller evolution gedit gnome-music gnome-photos cheese gnome-mplayer
>pacman -S unrar unzip p7zip
>pacman -S deepin deepin-extra lightdm
>pacman -S file-roller evince gedit thunderbird gpicview
>pacman -S chromium
******************************

22.Start Service
******************************
>pacman -S networkmanager
>systemctl enable NetworkManager
>systemctl enable gdm
>systemctl enable lightdm ***[May Error,Doesn't matter]

******************************

23.Reboot and into Gnome
******************************
>reboot
******************************

24.Change to Chinese
******************************
>nano /etc/locale.gen
REMOVE # before "zh_CN*"
>locale-gen
Setting - Langauage - "中文"
>Reboot
>pacman -S wqy-microhei
>Reboot
******************************
























                                                     ------本向导更新于2016.8
                                                              by redapple0204
