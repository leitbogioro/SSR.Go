# -酸酸仁乳（ShadowsocksRR）一键安装包饮用指南-
这是一个我魔改的酸酸乳一键安装包，原脚本来自秋水逸冰大神，原版本有一些旧了，底包最高只能支持到auth_chain_b协议，该一键安装包目前ShadowsocksR（ShadowsocksRR）随时和@Akarrin接盘后的https://github.com/shadowsocksrr 的新版本保持同步。
### 使用方法：
if 已安装过秋水逸冰大神的一键包，请先卸载：
<pre><code> ./shadowsocksR.sh uninstall </code></pre>
then 重新安装：
<pre><code>wget --no-check-certificate -O shadowsocksRR.sh https://git.io/vdMUr</code></pre>
<pre><code>chmod +x shadowsocksRR.sh</code></pre>
<pre><code>./shadowsocksRR.sh 2>&1 | tee shadowsocksR.log</code></pre>
安装完成后，推荐重启一下SSRR服务：
<pre><code>/etc/init.d/shadowsocks restart</code></pre>
