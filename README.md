# 酸酸仁乳（ShadowsocksRR）一键安装包饮用指南
这是一个我魔改的酸酸乳一键安装包，原脚本来自秋水逸冰（Teddysun）大神https://git.io/vdMTK ，原脚本里的ShadowsocksR服务端版本有一些旧了，底包最高只能支持到auth_chain_b协议，我的一键安装包目前可以随时和@Akkariiin接盘后的ShadowsocksR（ShadowsocksRR）https://git.io/vdMTB 的最新版本保持同步。
### 使用方法：
if 已安装过秋水逸冰大神的一键包，请先卸载：
<pre><code> ./shadowsocksR.sh uninstall </code></pre>
then 重新安装：
<pre><code>wget --no-check-certificate -O shadowsocksRR.sh https://git.io/vdMUr && chmod +x shadowsocksRR.sh && ./shadowsocksRR.sh 2>&1 | tee shadowsocksR.log</code></pre>
安装完成后，推荐重启一下SSRR服务：
<pre><code>/etc/init.d/shadowsocks restart</code></pre>
<br />

### 更新历史：
- 来自https://github.com/AkaneAkaza 的dev通道底包更新说明：https://github.com/shadowsocksrr/shadowsocksr/commits/akkariiin/dev （长期置顶）
- 底包切换至https://github.com/shadowsocksrr/shadowsocksr/tree/akkariiin/dev 通道https://github.com/shadowsocksrr/shadowsocksr/archive/akkariiin/dev.zip 并重新解压打包至上传（2018.1.27）；
- 更新加密插件libsodium版本至1.0.16；（2018.1.27）
- 恢复对auth_chain_C协议的支持（2018.1.27）；
- 因auth_chain_X系列协议继承了auth_aes128_md5/sha1协议中将数据传输包的头部引入Encrypt-then-MAC模式，以对抗防火长城（GreatFireWall）CCA攻击、探测攻击和重放攻击的特性，并支持单端口设置多用户，每次客户端与服务器建立连接的时候，均生成新的不同的密钥，且不同用户之间无法解密对方传输的数据，要求服务端的UTC时区与客户端的相差不超过24小时，强烈推荐使用。auth_chain_X系列协议自带RC4加密，故删除安装脚本中对RC4加密方式的支持；（2018.1.27）
- 添加对idea-cfb、seed-cfb、table加密方式的支持（2018.1.27）；
- 因Windows版ShadowSocksR不支持xchacha20、xsalsa20加密方式，故删除（2018.1.27）；
- 因安全问题，删除aes-192-cfb、aes-128-cfb、aes-192-cfb8、aes-128-cfb8、aes-192-ctr、aes-128-ctr加密方式（2018.1.27）；
- 将命令合并，优化安装流程（2017.11.16）；
- 修改“推荐/默认”端口为443 （2017.11.8）；
- 默认超时（timeout）设置从原来的120更改成300，该项设置的数值越大，连接保持的时间也越长，使并发的tcp连接数也保持得更多，个人使用tcp并发高是多多益善的，如果你给超过10个人分享了你的公共代理（飞机场），请酌情调低该值，推荐设置为60，来自@clowwindy，原链接：[shadowsocks 公共代理的必要设置](https://gist.github.com/fqrouter/95c037f9a3ba196fd4dd) （2017.11.8）；
- 添加对 random_head 混淆模式的支持，然而并不推荐使用（2017.11.8）；
- 补全对 rc4 加密方式的支持（2017.11.8）；
- auth_chain_c 协议在配合20端口使用下，在一段时间正常连接后，突然失去响应，切换到别的节点再切换回来，即立马恢复正常，配合80、443等端口使用，未发现明显的问题，目前还是不推荐使用，不在一键脚本里添加该选项（2017.10.17）；
- 经测试，移除对 auth_chain_c 协议的支持，我用了一点事儿都没，然后就…………（2017.10.16）;
- 替换安装提示中的关键词ShadowsocksR为ShadowsocksRR（2017.10.16）；
- 更新加密插件libsodium版本至1.0.15；（2017.10.16）；
- 添加对 salsa20、xchacha20、xsalsa20 加密方式的支持（2017.10.15）；
- 添加对 auth_chain_e和add auth_chain_f 协议的支持（2017.10.15）；
- 添加对 auth_chain_c和add auth_chain_d 协议的支持（2017.10.15）。
