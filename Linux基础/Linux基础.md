**1** Linux没有像Windows里面的盘符的概念，简单来说就是所有的文件啊全都放在一个盘里面这个盘叫```/```，只是分成不同文件夹当中，不同文件夹也有不同的权限，以下详细介绍Linux下面的文件夹

```
Linux 主要目录速查表
• /：根目录，一般根目录下只存放目录，在 linux 下有且只有一个根目录，所有的东西都是从这里开始
	• 当在终端里输入  /home ，其实是在告诉电脑，先从 /（根目录）开始，再进入到 home 目录

• /bin、/usr/bin：可执行二进制文件的目录，如常用的命令 ls、tar、mv、cat 等

• /boot：放置 linux 系统启动时用到的一些文件，如 linux 的内核文件：/boot/vmlinuz，系统引导管理器：/boot/grub

• /dev：存放linux系统下的设备文件，访问该目录下某个文件，相当于访问某个设备，常用的是挂载光驱mount /dev/cdrom /mnt

• /etc：系统配置文件存放的目录，不建议在此目录下存放可执行文件，重要的配置文件有
	• /etc/inittab
	• /etc/fstab
	• /etc/init.d
	• /etc/X11
	• /etc/sysconfig
	• /etc/xinetd.d

• /home：系统默认的用户家目录，新增用户账号时，用户的家目录都存放在此目录下
	• ~ 表示当前用户的家目录
	• ~edu 表示用户 edu 的家目录
• /lib、/usr/lib、/usr/local/lib：系统使用的函数库的目录，程序在执行过程中，需要调用一些额外的参数时需要函数库的协助
• /lost+fount：系统异常产生错误时，会将一些遗失的片段放置于此目录下
• /mnt: /media：光盘默认挂载点，通常光盘挂载于 /mnt/cdrom 下，也不一定，可以选择任意位置进行挂载
• /opt：给主机额外安装软件所摆放的目录
• /proc：此目录的数据都在内存中，如系统核心，外部设备，网络状态，由于数据都存放于内存中，所以不占用磁盘空间，比较重要的文件有：/proc/cpuinfo、/proc/interrupts、/proc/dma、/proc/ioports、/proc/net/* 等
• /root：系统管理员root的家目录
• /sbin、/usr/sbin、/usr/local/sbin：放置系统管理员使用的可执行命令，如 fdisk、shutdown、mount 等。与 /bin 不同的是，这几个目录是给系统管理员 root 使用的命令，一般用户只能"查看"而不能设置和使用
• /tmp：一般用户或正在执行的程序临时存放文件的目录，任何人都可以访问，重要数据不可放置在此目录下

• /srv：服务启动之后需要访问的数据目录，如 www 服务需要访问的网页数据存放在 /srv/www 内
	• /usr：应用程序存放目录
	• /usr/bin：存放应用程序
	• /usr/share：存放共享数据
	• /usr/lib：存放不能直接运行的，却是许多程序运行所必需的一些函数库文件
	• /usr/local：存放软件升级包
	• /usr/share/doc：系统说明文件存放目录
	• /usr/share/man：程序说明文件存放目录
• /var：放置系统执行过程中经常变化的文件
	• /var/log：随时更改的日志文件
	• /var/spool/mail：邮件存放的目录
	• /var/run：程序或服务启动后，其 PID 存放在该目录下

```

**2** Linux也有图形界面，如Ubuntu，centOS等等，但作为服务器系统，它的操作几乎都是通过指令去完成的，所以，学习Linux指令是操作Linux的一个入门，有关服务器的知识可以上百度先看一看服务器的图片

![服务器图片 alt][./timg.jpg]

那么通过SSH远程管理服务器，之后讲

> 最常用的指令有10条左右，后面更多的指令在用到就百度就可以了

指令的格式就是  ```指令名 [-选项] [操作对象]	```

*****

现在你是小王，在这个目录下，先查看一下这个目录下面有点什么东西  输入```ls```查看当前目录下的内容，如果在详细一点查看在后面就是 ```ls -l ```  再显示隐藏文件和文件夹就是```ls -la```或者```ls -l -a```

上面就是第一个指令```ls``` 对应的单词就是**list** -----查看当前文件夹下的内容

有时候你还不知道现在所在文件夹的位置的时候，指令```pwd``` 一个非常实用的查看当前文件夹所在位置，对应的英文就是**print work directory**

*****

看也看了，下一步就是对文件进行操作了，这就像在Windows里面一样，一个文件或者文件夹，增删
**增**：touch \[文件名]  记得带上文件的后缀，虽然不带也能打开，但还是给个面子；mkdir \[文件夹名] 对应的就是make directory的意思
**删**：rm \[文件或者文件夹名字]  对应remove



#####Linux的命令从来都不是用来背的，常用的不过十来个命令已经可以胜任大部分工作，而在对大部分工作之外去提升效率等等也只是在需要的时候再去查就可以了