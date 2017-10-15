# -酸酸乳饮用指南-
这是一个我魔改的酸酸乳一键安装包，原脚本来自秋水逸冰大神，原版本有一些旧了，底包最高只能支持到auth_chain_b协议，该一键安装包目前ShadowsocksR（ShadowsocksRR）随时和@Akarrin接盘后的https://github.com/shadowsocksrr 的新版本保持同步。
### 使用方法：
if 已安装过秋水逸冰大神的一键包，请先卸载：
<pre><code> ./shadowsocksR.sh uninstall </code></pre>
then 重新安装：
     wget --no-check-certificate -O shadowsocksRR.sh https://git.io/vdMUr
     chmod +x shadowsocksRR.sh
     ./shadowsocksRR.sh 2>&1 | tee shadowsocksR.log
安装完成后，推荐重启一下SSRR服务：
    /etc/init.d/shadowsocks restart
