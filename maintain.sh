#!/bin/bash
SSR_start="/etc/init.d/shadowsocks start"
SSR_stop="/etc/init.d/shadowsocks stop"
SSR_log="/var/log/shadowsocksr.log"

${SSR_stop}

if [ ! -d ${SSR_log} ]; then
    rm -rf ${SSR_log}
    touch ${SSR_log}
fi

${SSR_start}
