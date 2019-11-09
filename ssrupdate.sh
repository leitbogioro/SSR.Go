#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# 如果检查到运行环境中存在阿里云服务，安装将立即终止
agentwatch=`ps aux | grep 'agentwatch'`
aliyunsrv=`ps aux | grep 'aliyun'`
AliYunDun=`ps aux | grep 'AliYunDun'`
AliHids=`ps aux | grep 'AliHids'`
AliYunDunUpdate=`ps aux | grep 'AliYunDunUpdate'`
if [ -d /usr/local/aegis ] || [[ -f /etc/init.d/aegis ]] || [[ ! -n $agentwatch ]] || [[ ! -n $aliyunsrv ]] || [[ ! -n $AliYunDun ]] || [[ ! -n $AliHids ]] || [[ ! -n $AliYunDunUpdate ]]; then
    echo -e "[${red}Error${plain}] 检测到您的系统中存在阿里云的相关监控服务进程，如继续使用，你会尝到被社会主义铁拳捅进菊花里的滋味！！！"
    echo "安装程序立即终止"
    echo "可行的解决办法（以下采用一种即可）："
    echo "1. 使用我的脚本，卸载阿里云的监控服务：https://github.com/leitbogioro/Fuck_Aliyun"
    echo "2. 使用我的脚本，重新安装纯净的 Linux 系统：https://github.com/leitbogioro/Tools"
    rm -rf ssrinstall
    exit 1
fi

#检查是否为Root
[ $(id -u) != "0" ] && { echo "发生错误，你必须以 root 用户执行此安装程序"; exit 1; }

/etc/init.d/shadowsocks stop

#如果检测到已有配置，则将改配置转换成备份文件
SSR_config="/etc/shadowsocks.json"
SSR_backup="/etc/shadowsocks.backup"
if [ ! -d ${SSR_config} ]; then
    mv ${SSR_config} ${SSR_backup}
fi

#克隆ssr.go项目
cd /usr/local/
rm -R SSR.Go
git clone https://github.com/leitbogioro/SSR.Go

#安装shadowsocksRR主程序
bash <(curl -L -s https://git.io/fNpEa)

#如果检测到配置备份文件，则将该备份的配置文件替换成正式配置文件
if [ ! -d ${SSR_backup} ]; then
    rm -rf ${SSR_config}
    mv ${SSR_backup} ${SSR_config}
fi

# 删除旧的维护策略并写入新的
if [[ `grep -i "/etc/init.d/shadowsocks restart" /etc/crontab` ]]; then
    sed -i '/shadowsocks/d' /etc/crontab
fi
if [[ ! `grep -i "SSR.Go/maintain.sh" /etc/crontab` ]]; then
    sed -i '$i 30 4    * * 0   root    bash /usr/local/SSR.Go/maintain.sh' /etc/crontab
fi
/etc/init.d/cron restart

#配置ssr初始环境
rm -rf /usr/local/bin/ssr
ln -sf /usr/local/SSR.Go/ssr /usr/local/bin
chmod +x /usr/local/bin/ssr
chmod +x /etc/init.d/shadowsocks
chmod +x /usr/local/shadowsocks/
/etc/init.d/shadowsocks restart

clear

echo "SSR.Go 和 ShadowSocksR 更新成功！"
echo "输入 ssr 并回车即可使用"
