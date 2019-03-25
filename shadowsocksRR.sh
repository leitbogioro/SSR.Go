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

echo
echo "本项目已改版为SSR.Go，不再更新，新项目地址请移步 https://git.io/fNpR5 特此声明！"
read -n1 -p  "你是决定安装新版SSR.Go（按y），还是继续安装此脚本？（按n），按 Ctrl + C 取消" ans
if [[ ${ans} =~ [yY] ]]; then
    bash -c "$(curl -fsSL https://git.io/fNpuL)"
else
    echo -e "\n"

libsodium_file="libsodium-1.0.17"
libsodium_url="https://github.com/jedisct1/libsodium/releases/download/1.0.17/libsodium-1.0.17.tar.gz"

# Current folder
cur_dir=`pwd`

# 加密方式
ciphers=(
none
aes-256-cfb
aes-256-cfb8
aes-256-ctr
bf-cfb
camellia-256-cfb
cast5-cfb
chacha20-ietf
chacha20
xchacha20
salsa20
xsalsa20
idea-cfb
seed-cfb
rc4-md5
rc4-md5-6
table
)

# 参见:
# https://github.com/shadowsocksrr/shadowsocks-rss/blob/master/readme.md
# https://github.com/shadowsocksrr/shadowsocks-rss/wiki/config.json

# 协议
protocols=(
origin
verify_deflate
auth_sha1_v4
auth_sha1_v4_compatible
auth_aes128_md5
auth_aes128_sha1
auth_chain_a
auth_chain_b
auth_chain_c
auth_chain_d
auth_chain_e
auth_chain_f
auth_akarin_rand
auth_akarin_spec_a
)

# 混淆
obfs=(
plain
http_simple
http_simple_compatible
http_post
http_post_compatible
tls1.2_ticket_auth
tls1.2_ticket_auth_compatible
tls1.2_ticket_fastauth
tls1.2_ticket_fastauth_compatible
random_head
)

# 脚本字体颜色
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
plain='\033[0m'

# 必须以 root 用户运行该脚本
[[ $EUID -ne 0 ]] && echo -e "[${red}Error${plain}] This script must be run as root!" && exit 1

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

# 获得 redhat 系统版本
getversion(){
    if [[ -s /etc/redhat-release ]]; then
        grep -oE  "[0-9.]+" /etc/redhat-release
    else
        grep -oE  "[0-9.]+" /etc/issue
    fi
}

# CentOS 系统版本
centosversion(){
    if check_sys sysRelease centos; then
        local code=$1
        local version="$(getversion)"
        local main_ver=${version%%.*}
        if [ "$main_ver" == "$code" ]; then
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

# 获得公共 IP 地址
get_ip(){
    local IP=$( ip addr | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | egrep -v "^192\.168|^172\.1[6-9]\.|^172\.2[0-9]\.|^172\.3[0-2]\.|^10\.|^127\.|^255\.|^0\." | head -n 1 )
    [ -z ${IP} ] && IP=$( wget -qO- -t1 -T2 ipv4.icanhazip.com )
    [ -z ${IP} ] && IP=$( wget -qO- -t1 -T2 ipinfo.io/ip )
    [ ! -z ${IP} ] && echo ${IP} || echo
}

get_char(){
    SAVEDSTTY=`stty -g`
    stty -echo
    stty cbreak
    dd if=/dev/tty bs=1 count=1 2> /dev/null
    stty -raw
    stty echo
    stty $SAVEDSTTY
}

# 预安装检测
pre_install(){
    if check_sys packageManager yum || check_sys packageManager apt; then
        # 不支持 CentOS 5
        if centosversion 5; then
            echo -e "$[{red}Error${plain}] Not supported CentOS 5, please change to CentOS 6+/Debian 7+/Ubuntu 12+ and try again."
            exit 1
        fi
    else
        echo -e "[${red}Error${plain}] Your OS is not supported. please change OS to CentOS/Debian/Ubuntu and try again."
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
    if [ ${dpwdleng} -ge 6 ] && [ ${dpwdleng} -le 36 ] && [ -n "${dpwlow}" ] || [ -n "${dpwnum}" ]; then
        echo
        echo "---------------------------"
        echo "password = ${shadowsockspwd}"
        echo "---------------------------"
        echo
        break
    else
    echo -e "[${red}Error${plain}] Your password is too weak, please re-enter a stronger one(at least 6 characters, include letters and numbers)."
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

    # 设置 shadowsocksRR 加密方式
    while true
    do
    echo -e "Please select stream cipher for ShadowsocksRR:"
    for ((i=1;i<=${#ciphers[@]};i++ )); do
        hint="${ciphers[$i-1]}"
        echo -e "${green}${i}${plain}) ${hint}"
    done
    read -p "Which cipher you'd select(Default: ${ciphers[7]}):" pick
    [ -z "$pick" ] && pick=8
    expr ${pick} + 1 &>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "[${red}Error${plain}] Input error, please input a number"
        continue
    fi
    if [[ "$pick" -lt 1 || "$pick" -gt ${#ciphers[@]} ]]; then
        echo -e "[${red}Error${plain}] Input error, please input a number between 1 and ${#ciphers[@]}"
        continue
    fi
    shadowsockscipher=${ciphers[$pick-1]}
    echo
    echo "---------------------------"
    echo "cipher = ${shadowsockscipher}"
    echo "---------------------------"
    echo
    break
    done

    # 设置 shadowsocksRR 协议
    while true
    do
    echo -e "Please select protocol for ShadowsocksRR:"
    for ((i=1;i<=${#protocols[@]};i++ )); do
        hint="${protocols[$i-1]}"
        echo -e "${green}${i}${plain}) ${hint}"
    done
    read -p "Which protocol you'd select(Default: ${protocols[12]}):" protocol
    [ -z "$protocol" ] && protocol=13
    expr ${protocol} + 1 &>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "[${red}Error${plain}] Input error, please input a number"
        continue
    fi
    if [[ "$protocol" -lt 1 || "$protocol" -gt ${#protocols[@]} ]]; then
        echo -e "[${red}Error${plain}] Input error, please input a number between 1 and ${#protocols[@]}"
        continue
    fi
    shadowsockprotocol=${protocols[$protocol-1]}
    echo
    echo "---------------------------"
    echo "protocol = ${shadowsockprotocol}"
    echo "---------------------------"
    echo
    break
    done

    # 设置 shadowsocksRR 混淆
    while true
    do
    echo -e "Please select obfs for ShadowsocksRR:"
    for ((i=1;i<=${#obfs[@]};i++ )); do
        hint="${obfs[$i-1]}"
        echo -e "${green}${i}${plain}) ${hint}"
    done
    read -p "Which obfs you'd select(Default: ${obfs[5]}):" r_obfs
    [ -z "$r_obfs" ] && r_obfs=6
    expr ${r_obfs} + 1 &>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "[${red}Error${plain}] Input error, please input a number"
        continue
    fi
    if [[ "$r_obfs" -lt 1 || "$r_obfs" -gt ${#obfs[@]} ]]; then
        echo -e "[${red}Error${plain}] Input error, please input a number between 1 and ${#obfs[@]}"
        continue
    fi
    shadowsockobfs=${obfs[$r_obfs-1]}
    echo
    echo "---------------------------"
    echo "obfs = ${shadowsockobfs}"
    echo "---------------------------"
    echo
    break
    done

    echo
    echo "Press any key to start...or Press Ctrl+C to cancel"
    char=`get_char`
    # 安装必要运行环境
    if check_sys packageManager yum; then
        yum install -y python python-devel python-setuptools openssl openssl-devel curl wget unzip gcc automake autoconf make libtool
    elif check_sys packageManager apt; then
        apt-get -y update
        apt-get -y install python python-dev python-setuptools openssl libssl-dev curl wget unzip gcc automake autoconf make libtool
    fi
    cd ${cur_dir}
}
# 下载必要运行组件
download_files(){
    # 下载 libsodium
    if ! wget --no-check-certificate -O ${libsodium_file}.tar.gz ${libsodium_url}; then
        echo -e "[${red}Error${plain}] Failed to download ${libsodium_file}.tar.gz!"
        exit 1
    fi
    # 下载 ShadowsocksRR
    if ! wget --no-check-certificate -O manyuser.zip https://github.com/leitbogioro/SSRGo/raw/master/manyuser.zip; then
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

# 配置 ShadowsocksRR
config_shadowsocks(){
    cat > /etc/shadowsocks.json<<-EOF
{
    "server":"0.0.0.0",
    "server_ipv6":"[::]",
    "server_port":${shadowsocksport},
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"${shadowsockspwd}",
    "timeout":300,
    "udp_timeout":150,
    "method":"${shadowsockscipher}",
    "protocol":"${shadowsockprotocol}",
    "protocol_param":"",
    "obfs":"${shadowsockobfs}",
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
        tar zxf ${libsodium_file}.tar.gz
        cd ${libsodium_file}
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
        chmod +x /etc/init.d/shadowsocks
        if check_sys packageManager yum; then
            chkconfig --add shadowsocks
            chkconfig shadowsocks on
        elif check_sys packageManager apt; then
            update-rc.d -f shadowsocks defaults
        fi
        /etc/init.d/shadowsocks start

        clear
        echo
        echo -e "Congratulations, ShadowsocksRR server install completed!"
        echo -e "Your Server IP        : \033[41;37m $(get_ip) \033[0m"
        echo -e "Your Server Port      : \033[41;37m ${shadowsocksport} \033[0m"
        echo -e "Your Password         : \033[41;37m ${shadowsockspwd} \033[0m"
        echo -e "Your Protocol         : \033[41;37m ${shadowsockprotocol} \033[0m"
        echo -e "Your obfs             : \033[41;37m ${shadowsockobfs} \033[0m"
        echo -e "Your Encryption Method: \033[41;37m ${shadowsockscipher} \033[0m"
        echo
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
    rm -rf manyuser.zip shadowsocksr-manyuser ${libsodium_file}.tar.gz ${libsodium_file}
}


# 卸载 ShadowsocksRR
uninstall_shadowsocksr(){
    printf "Are you sure uninstall ShadowsocksRR? (y/n)"
    printf "\n"
    read -p "(Default: n):" answer
    [ -z ${answer} ] && answer="n"
    if [ "${answer}" == "y" ] || [ "${answer}" == "Y" ]; then
        /etc/init.d/shadowsocks status > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            /etc/init.d/shadowsocks stop
        fi
        if check_sys packageManager yum; then
            chkconfig --del shadowsocks
        elif check_sys packageManager apt; then
            update-rc.d -f shadowsocks remove
        fi
        rm -f /etc/shadowsocks.json
        rm -f /etc/init.d/shadowsocks
        rm -f /var/log/shadowsocks.log
        rm -rf /usr/local/shadowsocks
        echo "ShadowsocksRR uninstall success!"
    else
        echo
        echo "uninstall cancelled, nothing to do..."
        echo
    fi
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

fi
