#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin

# 脚本字体颜色
green='\033[0;32m'
red='\033[0;31m'
plain='\033[0m'

# 必须以 root 用户运行该脚本
[[ $EUID -ne 0 ]] && echo -e "[${red}错误${plain}] 你必须以管理员身份运行该脚本！" && exit 1

# 安装 python-2.7.15
python_url="https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz"
python_file="Python-2.7.15"

install_python(){
    # 安装所有的开发工具包
    yum groupinstall -y "Development tools"

    # 安装其它的必需包
    yum install -y update zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel wget

    # 下载、编译和安装 Python 2.7
    wget ${python_url}
    # 下载 python 主程序失败后的操作
    if ! wget ${python_url}; then
        echo -e "[${red}错误${plain}] ${python_file} 主程序下载失败，请检测你的网络！"
        exit 1
    fi
    tar zxf ${python_file}.tgz
    cd ${python_file}
    ./configure
    make && make install

    # 将 Python 安装在 /usr/local/bin 目录下
    ll -tr /usr/local/bin/python*

    # 系统自带的 Python 是在 /usr/bin 目录下
    ll -tr /usr/bin/python*

    # 更新系统默认 Python 版本
    # 把系统默认的旧版 Python 重命名
    mv /usr/bin/python /usr/bin/python.old

    # 删除系统默认的 python-config 软链接
    rm -f /usr/bin/python-config

    # 创建新版本的 Python 软链接
    ln -s /usr/local/bin/python /usr/bin/python
    ln -s /usr/local/bin/python-config /usr/bin/python-config
    ln -s /usr/local/include/python2.7/ /usr/include/python2.7

    # 目录 /usr/bin 下的 Python 应该是
    ll -tr /usr/bin/python*

    # 为新版 Python 安装 setuptools
    wget https://bootstrap.pypa.io/ez_setup.py -O - | python
    # setuptools 正确安装完成后，easy_install 命令就会被安装在 /usr/local/bin 目录下了

    # 为新版 Python 安装 pip
    easy_install pip
    # 正确安装完成后，pip 命令就会被安装在 /usr/local/bin 目录下了
    # 为新版 Python 安装 distribute 包（可选） 
    pip install distribute

    # 清理 python 安装包
    rm -rf /root/$python_file /root/$python_file.tgz
}

prevent_yum(){
    sed -i '1s/python/python2.6/1' /usr/bin/yum
    # 将旧版本python路径复制到新版本 Python 的路径 /usr/local/lib/python2.7/site-packages/ 下
    cp -r /usr/lib/python2.6/site-packages/yum /usr/local/lib/python2.7/site-packages/
    cp -r /usr/lib/python2.6/site-packages/rpmUtils /usr/local/lib/python2.7/site-packages/
    cp -r /usr/lib/python2.6/site-packages/iniparse /usr/local/lib/python2.7/site-packages/
    cp -r /usr/lib/python2.6/site-packages/urlgrabber /usr/local/lib/python2.7/site-packages/
    cp -r /usr/lib64/python2.6/site-packages/rpm /usr/local/lib/python2.7/site-packages/
    cp -r /usr/lib64/python2.6/site-packages/curl /usr/local/lib/python2.7/site-packages/
    cp -p /usr/lib64/python2.6/site-packages/pycurl.so /usr/local/lib/python2.7/site-packages/
    cp -p /usr/lib64/python2.6/site-packages/_sqlitecache.so /usr/local/lib/python2.7/site-packages/
    cp -p /usr/lib64/python2.6/site-packages/sqlitecachec.py /usr/local/lib/python2.7/site-packages/
    cp -p /usr/lib64/python2.6/site-packages/sqlitecachec.pyc /usr/local/lib/python2.7/site-packages/
    cp -p /usr/lib64/python2.6/site-packages/sqlitecachec.pyo /usr/local/lib/python2.7/site-packages/
}

# 判断是否需要安装 python 2.7

# 输出版本号 centos 字段
System_CentOS=`rpm -q centos-release|cut -d- -f1`
Linux_System=`cat /etc/issue 2>&1|awk 'NR==1{print $1}'`
# 输出 centos 系统大版本号
CentOS_Version=`cat /etc/redhat-release|sed -r 's/.* ([0-9]+)\..*/\1/'`
# python 版本号
Python_Version=`python -V 2>&1|awk '{print $2}'|awk -F '.' '{print $0}'`
# 输出 python 大版本号
Python_Version1=`python -V 2>&1|awk '{print $2}'|awk -F '.' '{print $1}'`
# 输出 python 小版本号
Python_Version2=`python -V 2>&1|awk '{print $2}'|awk -F '.' '{print $2}'`
# 输出 python 修订号
Python_Version3=`python -V 2>&1|awk '{print $2}'|awk -F '.' '{print $3}'`

# 只允许 centos 6 且自带低于 python 2.7 的版本安装
if [[ ! `expr match ${Linux_System} "[C|c][E|e][N|n][T|t][O|o][S|s]"` -eq "6" ]]; then
    echo -e "[${red}错误${plain}] 您的系统版本（${Linux_System}）和此程序不兼容，程序已退出！"
    exit 1
elif [[ ${CentOS_Version} != "6" ]]; then
    echo -e "[${red}错误${plain}] 您的系统版本（${System_CentOS} ${CentOS_Version}）和此程序安装要求不符，程序已退出！"
    exit 1
elif [[ ${Python_Version1} != "2" ]]; then
    echo -e "[${red}错误${plain}] 您系统内已安装的 python 版本（${Python_Version}）和本脚本要求的不符，程序已退出！"
    exit 1
elif [[ ${Python_Version1} == "2" ]] && [[ ${Python_Version2} -ge "7" ]]; then
    echo -e "[${green}完成${plain}] 您系统内已安装的 python 版本（${Python_Version}）已满足需要，程序已退出！"
    exit 1
elif [[ -f /etc/redhat-release ]] && [[ ${System_CentOS} == "centos" ]] && [[ ${CentOS_Version} == "6" ]] && [[ ${Python_Version1} == "2" ]] && [[ "${Python_Version2}" -lt 7 ]] && [[ ${Python_Version3} -lt "15" ]]; then
    install_python
    if ! grep '/usr/bin/python2.6' /usr/bin/yum; then
        prevent_yum
        echo -e "${green}[完成]${plain} ${python_file} 已安装到你的系统中！"
        exit 1
    else
        echo -e "${green}[完成]${plain} ${python_file} 已安装到你的系统中！"
    fi
fi
