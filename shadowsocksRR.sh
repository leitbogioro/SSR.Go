#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
#=================================================================#
#   System Required:  CentOS 6,7, Debian, Ubuntu                  #
#   Description: One click Install ShadowsocksRR Server           #
#   Author: MollyLau                                              #
#   Thanks: @breakwa11 <https://twitter.com/breakwa11> & TeddySun #
#   Intro:  https://goo.gl/SjXFKi                                 #
#=================================================================#

clear
echo
echo "#############################################################"
echo "# One click Install ShadowsocksRR Server                    #"
echo "# Intro: https://goo.gl/SjXFKi                              #"
echo "# Author: MollyLau                                          #"
echo "# Github: https://github.com/shadowsocksrr                  #"
echo "#############################################################"
echo

# 关闭 selinux
disable_selinux(){
    if [ -s /etc/selinux/config ] && grep 'SELINUX=enforcing' /etc/selinux/config; then
        sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
        setenforce 0
    fi
}

# 判断系统分支
check_sys(){
    local checkType=$1
    local value=$2

    local release=''
    local systemPackage=''

    if [[ -f /etc/redhat-release ]]; then
        release="centos"
        systemPackage="yum"
    elif grep -Eqi "centos|red hat|redhat" /etc/issue -o /proc/version; then
        release="centos"
        systemPackage="yum"
    elif grep -Eqi "debian" /etc/issue -o /proc/version; then
        release="debian"
        systemPackage="apt"
    elif grep -Eqi "ubuntu" /etc/issue -o /proc/version; then
        release="ubuntu"
        systemPackage="apt"
    fi
# check_sys()函数内部，需要声明局部变量
# grep -Eqi中，E用于扩展的正则，q用于逻辑判断，i不区分大小写，后面跟上关键字条件
# cat 与 grep 命令配合使用，cat 用于读取 /cat/issue 文件，该文件里包含了当前操作系统的名称、版本号
# /proc/version 文件中，包含了系统的详细内核信息

    if [[ ${checkType} == "sysRelease" ]]; then
        if [ "$value" == "$release" ]; then
            return 0
        else
            return 1
        fi
    elif [[ ${checkType} == "packageManager" ]]; then
        if [ "$value" == "$systemPackage" ]; then
            return 0
        else
            return 1
        fi
    fi
}

# 预安装检测
pre_install(){
    if check_sys packageManager yum || check_sys packageManager apt; then
        # 不支持 CentOS 5
        if centosversion 5; then
            echo -e "Not supported CentOS 5, please change to CentOS 6+/Debian 7+/Ubuntu 12+ and try again."
            exit 1
        fi
    else
        echo -e "Your OS is not supported. please change OS to CentOS/Debian/Ubuntu and try again."
        exit 1
    fi
	
	# 设置 ShadowsocksRR 密码
    while true
    do
    dpwd=`cat /dev/urandom | tr -dc "a-zA-Z0-9_+\~\!\@\#\$\%\^\&\*" | fold -w 16 | head -n 1` # 获取系统UUID
    echo -e "Please enter a password for ShadowsocksRR(Default will generate a new random password):"
    read -p "(Default password: ${dpwd}):" shadowsockspwd
    [ -z "${shadowsockspwd}" ] && shadowsockspwd=${dpwd}
    dpwdleng=`expr length ${shadowsockspwd}` # 获取密码长度
    dpwlow=`echo ${shadowsockspwd} | grep -E '^(.*[a-z]+).*$'` # 获取密码中的所有小写字母
    dpwnum=`echo ${shadowsockspwd} | grep -E '^(.*[0-9]).*$'` # 获取密码中的所有数字
    if [ ${dpwdleng} -ge 6 ] && [ ${dpwdleng} -le 36 ] && [ -n "${dpwlow}" ] && [ -n "${dpwnum}" ]; then
        echo
        echo "---------------------------"
        echo "password = ${shadowsockspwd}"
        echo "---------------------------"
        echo
        break
    else
    echo -e "[${red}Error${plain}] Your password is too weak, please re-enter a stronger one(at least 18 characters, include letters and numbers)."
    fi
    done
	
    # 设置 ShadowsocksRR 端口
    while true
    do
    dport=$(shuf -i 10000-59999 -n 1) # 若不手动设置则随机选取
    echo -e "Please input port for ShadowsocksRR [1-65535] (Default between 10000-59999):"
    read -p "(Default port: ${dport}):" shadowsocksport
    [ -z "${shadowsocksport}" ] && shadowsocksport=${dport}
    expr ${shadowsocksport} + 1 &>/dev/null
    if [ $? -eq 0 ]; then
        if [ ${shadowsocksport} -ge 1 ] && [ ${shadowsocksport} -le 65535 ] && [ ${shadowsocksport:0:1} != 0 ]; then
            echo
            echo "---------------------------"
            echo "port = ${shadowsocksport}"
            echo "---------------------------"
            echo
            break
        fi
    fi
    echo -e "[${red}Error${plain}] Please enter a correct number [1-65535]"
    done
	
	
    
    char=`get_char`
    # 安装必要运行环境
    if check_sys packageManager yum; then
        yum install -y python python-devel python-setuptools git openssl openssl-devel curl wget unzip gcc automake autoconf make libtool
    elif check_sys packageManager apt; then
        apt-get -y update
        apt-get -y install python python-dev python-setuptools git openssl libssl-dev curl wget unzip gcc automake autoconf make libtool
    fi
    cd ${cur_dir}
}

# 下载必要运行组件

download_files(){
    # 下载 libsodium
    if ! wget --no-check-certificate -O libsodium-1.0.16.tar.gz https://github.com/jedisct1/libsodium/releases/download/1.0.16/libsodium-1.0.16.tar.gz; then
        echo -e "[${red}Error${plain}] Failed to download libsodium-1.0.16.tar.gz!"
        exit 1
    fi
    # 下载 ShadowsocksRR
    if ! wget --no-check-certificate -O manyuser.zip https://github.com/leitbogioro/ShadowsocksRR-Install/releases/download/archive/manyuser.zip; then
        echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR file!"
        exit 1
    fi
    # 下载 ShadowsocksRR 运行脚本
    if check_sys packageManager yum; then
        if ! wget --no-check-certificate https://raw.githubusercontent.com/leitbogioro/shadowsocks_install/master/shadowsocksR -O /etc/init.d/shadowsocks; then
            echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR chkconfig file!"
            exit 1
        fi
    elif check_sys packageManager apt; then
        if ! wget --no-check-certificate https://raw.githubusercontent.com/leitbogioro/shadowsocks_install/master/shadowsocksR-debian -O /etc/init.d/shadowsocks; then
            echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR chkconfig file!"
            exit 1
        fi
    fi
}

# 下载必要运行组件
download_files(){
    # 下载 libsodium
    if ! wget --no-check-certificate -O libsodium-1.0.16.tar.gz https://github.com/jedisct1/libsodium/releases/download/1.0.16/libsodium-1.0.16.tar.gz; then
        echo -e "[${red}Error${plain}] Failed to download libsodium-1.0.16.tar.gz!"
        exit 1
    fi
    # 下载 ShadowsocksRR
    if ! wget --no-check-certificate -O manyuser.zip https://github.com/leitbogioro/ShadowsocksRR-Install/releases/download/archive/manyuser.zip; then
        echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR file!"
        exit 1
    fi
    # 下载 ShadowsocksRR 运行脚本
    if check_sys packageManager yum; then
        if ! wget --no-check-certificate https://raw.githubusercontent.com/leitbogioro/ShadowsocksRR-Install/Dev/shadowsocksR -O /etc/init.d/shadowsocksr; then
            echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR chkconfig file!"
            exit 1
        fi
    elif check_sys packageManager apt; then
        if ! wget --no-check-certificate https://raw.githubusercontent.com/leitbogioro/ShadowsocksRR-Install/Dev/shadowsocksR-debian -O /etc/init.d/shadowsocksr; then
            echo -e "[${red}Error${plain}] Failed to download ShadowsocksRR chkconfig file!"
            exit 1
        fi
    fi
}

# 防火墙设置
firewall_set(){
    echo -e "[${green}Info${plain}] firewall set start..."
    if centosversion 6; then
        /etc/init.d/iptables status > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            iptables -L -n | grep -i ${shadowsocksport} > /dev/null 2>&1
            if [ $? -ne 0 ]; then
                iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport ${shadowsocksport} -j ACCEPT
                iptables -I INPUT -m state --state NEW -m udp -p udp --dport ${shadowsocksport} -j ACCEPT
                /etc/init.d/iptables save
                /etc/init.d/iptables restart
            else
                echo -e "[${green}Info${plain}] port ${shadowsocksport} has been set up."
            fi
        else
            echo -e "[${yellow}Warning${plain}] iptables looks like shutdown or not installed, please manually set it if necessary."
        fi
    elif centosversion 7; then
        systemctl status firewalld > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            firewall-cmd --permanent --zone=public --add-port=${shadowsocksport}/tcp
            firewall-cmd --permanent --zone=public --add-port=${shadowsocksport}/udp
            firewall-cmd --reload
        else
            echo -e "[${yellow}Warning${plain}] firewalld looks like not running or not installed, please enable port ${shadowsocksport} manually if necessary."
        fi
    fi
    echo -e "[${green}Info${plain}] firewall set completed..."
}

config_shadowsocks(){
    cat > /etc/shadowsocksr.json<<-EOF
{
    "server":"0.0.0.0",
    "server_ipv6":"[::]",
    "server_port":${shadowsocksport},
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"${shadowsockspwd}",
    "timeout":300,
    "method":"chacha20-ietf",
    "protocol":"auth_akarin_rand",
    "protocol_param":"",
    "obfs":"tls1.2_ticket_auth",
    "obfs_param":"",
    "redirect":"",
    "dns_ipv6":false,
    "fast_open":false,
    "workers":1
}
EOF
}

# 安装 ShadowsocksRR
install(){
    # 安装 libsodium
    if [ ! -f /usr/lib/libsodium.a ]; then
        cd ${cur_dir}
        tar zxf libsodium-1.0.16.tar.gz
        cd libsodium-1.0.16
        ./configure --prefix=/usr && make && make install
        if [ $? -ne 0 ]; then
            echo -e "[${red}Error${plain}] libsodium install failed!"
            install_cleanup
            exit 1
        fi
    fi

    ldconfig
    # 安装 ShadowsocksRR
    cd ${cur_dir}
    unzip -q manyuser.zip
    mv shadowsocksr-manyuser/shadowsocks /usr/local/
    if [ -f /usr/local/shadowsocks/server.py ]; then
        chmod 777 /usr/local/shadowsocks/server.py
        chmod +x /etc/init.d/shadowsocksr
        if check_sys packageManager yum; then
            chkconfig --add shadowsocksr
            chkconfig shadowsocksr on
        elif check_sys packageManager apt; then
            update-rc.d -f shadowsocksr defaults
        fi
        /etc/init.d/shadowsocksr start

        clear
        echo "Welcome to visit:https://git.io/vdMTQ"
        echo "Just access to a wide world!"
        echo
    else
        echo "ShadowsocksRR install failed, please send private messages to <https://goo.gl/SjXFKi> and contact me"
        install_cleanup
        exit 1
    fi
}

# 安装完成后清理
install_cleanup(){
    cd ${cur_dir}
    rm -rf manyuser.zip shadowsocksr-manyuser libsodium-1.0.16.tar.gz libsodium-1.0.16
}

# 安装 ShadowsocksRR
install_shadowsocksr(){
    disable_selinux
    pre_install
    download_files
    config_shadowsocks
    if check_sys packageManager yum; then
        firewall_set
    fi
    install
    install_cleanup
}

# 初始化步骤
action=$1
[ -z $1 ] && action=install
case "$action" in
    install|uninstall)
        ${action}_shadowsocksr
        ;;
    *)
        echo "Arguments error! [${action}]"
        echo "Usage: `basename $0` [install|uninstall]"
        ;;
esac
