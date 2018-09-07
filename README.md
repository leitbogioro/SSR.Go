# 本分支的一些最新说明
# Something latest explanations about this branch.

<ul>
<li>这个分支原来是用来存储 ShadowSocksR 单用户版（以下简称“shadowsocksRR”）的一键安装包，文件名是：<a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksRR.sh">shadowsocksRR.sh</a>，它的安装过程中，会提示用户半自动化设置详细参数；
<p>This branch used to storage single user of ShadowSocksR onekey install and file name is <a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksRR.sh">shadowsocksRR.sh</a>(hereinafter referred to as "shadowsocksRR").During configuration, it will reminds users to set-up detailed specs by semi-automatic.</p></li>
<br />
<li>并且，添加了用来管理 shadowsocksRR 程序进程的 “<a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksR-debian">shadowsocksR-debian</a>” 和 “<a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksR-redhat">shadowsocksR-redhat</a>” shell 文件，进程管理文件可以控制 shadowsocksRR 进行启动、停止、重启、查询运行状态的操作，shadowsocksR-debian 可供 apt 包管理方式的 Linux 发行版使用，如 Ubuntu、Debian 等；shadowsocksR-redhat 可供 yum 包管理方式的 Linux 发行版使用，如 CentOS、Red-Hat 等；
<p>And add a shell to provide 4 operations about "start", "stop", "restart", "status" to control shadowsocksRR's main program's running which if used apt package as management such as Ubuntu, Debian(for <a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksR-debian">shadowsocksR-debian</a>) or CentOS, RedHat(for <a href="https://github.com/leitbogioro/SSR.Go/blob/master/shadowsocksR-redhat">shadowsocksR-redhat</a>) linux release etc.</p></li>
<br />
<li>后来，我编写出 SSR.Go，<a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrmain.sh">ssrmain.sh</a>是一个不带参数设置提示的 shadowsocksR 安装程序（<a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrinstallEn.sh">ssrinstallEn.sh</a>是对应的英文版）、<a href="https://github.com/leitbogioro/SSR.Go/blob/master/python_for_centos6.sh">python_for_centos6.sh</a> 是一个用来给 CentOS 6 做 python 版本更新和兼容性适配的外挂脚本文件。它们隶属于部署 SSR.Go 的预运行环境文件——“<a href="https://github.com/leitbogioro/SSR.Go/blob/Dev/ssrinstall">ssrinstall</a>”。
<p>And then, I developed SSR.Go, <a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrmain.sh">ssrmain.sh</a> is an none-pre-configurated shadowsocksR install program(<a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrinstallEn.sh">ssrinstallEn.sh</a> is a corresponding English version), <a href="https://github.com/leitbogioro/SSR.Go/blob/master/python_for_centos6.sh">python_for_centos6.sh</a> is a shell file which is used to update default python version about CentOS 6 to adapt compatibility. These 2 files are all belong to pre-deploy-environment for SSR.Go——<a href="https://github.com/leitbogioro/SSR.Go/blob/Dev/ssrinstall">ssrinstall</a>。</p></li>
<br />
<li>现在，多用户版的 shadowsocksR 管理工具正在开发中，<a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrmainmulti.sh"> ssrmainmulti.sh </a>是用来安装 shadowsocksR 多用户版预运行环境的 shell 脚本。<a href="https://github.com/leitbogioro/SSR.Go/blob/master/SSRMulti-Debian"> SSRMulti-Debian </a> 和 <a href="https://github.com/leitbogioro/SSR.Go/blob/master/SSRMulti-Redhat"> SSRMulti-Redhat </a>分别可供 apt 包管理方式的 Ubuntu、Debian 等和 yum 包管理方式的 CentOS、Red-Hat Linux 发行版使用，用来控制 shadowsocksR 多用户版主程序运行状态。
<p>Now, ShadowsocksR management tools for multi user edition is developing. <a href="https://github.com/leitbogioro/SSR.Go/blob/master/ssrmainmulti.sh"> ssrmainmulti.sh </a>is a shell about install shadowsocksR multi user pre-running-environment. <a href="https://github.com/leitbogioro/SSR.Go/blob/master/SSRMulti-Debian"> SSRMulti-Debian </a> and <a href="https://github.com/leitbogioro/SSR.Go/blob/master/SSRMulti-Redhat"> SSRMulti-Redhat </a> are provided separately to which if used apt package as management such as Ubuntu, Debian or CentOS, RedHat linux release etc.</p></li>
</ul>
<br />

# 大新闻
# Big News
本脚本项目已不再更新，请移步我的新分支项目————SSR.Go：https://git.io/fNpR5
</br>
</br>
I decide to begin a new project which belong to another branch————SSR.Go: https://git.io/fNpR5
</br>
</br>

# 简介
# Introduce
一个可以突破中国互联网审查的强力代理工具。
<br />
ShadowSocksRR is a robust proxy which can breakthrough Chinese internet censorship.
<br />

使用本工具，可方便调整ShadowSocksRR的配置和运行：
<br />
You can use it easily to configurate ShadowSocksRR program and keep it running. 
<br />
<br />

# 以下内容已永久进入历史的垃圾堆，不再维护和更新
# The following content is still available:
### 真香！
### Oh ♂ that's ♂ good~~
<br />
<br />

# 酸酸仁乳（ShadowsocksRR）一键安装包饮用指南
# ShadowSocksRR onkey installer user guide:
<br />
这是一个我魔改的酸酸乳一键安装包，原脚本来自秋水逸冰（Teddysun）大佬https://git.io/vdMTK ，原脚本里的ShadowsocksR服务端版本有一些旧了，底包最高只能支持到auth_chain_b协议，我的一键安装包目前可以随时和@Akkariiin接盘后的ShadowsocksR（ShadowsocksRR）https://git.io/vdMTB 的最新版本保持同步。
<br />
<br />
This installer is modified by TeddySun's works（https://git.io/vdMTK） because I find that source code in TeddySun's works does't update to this new branch（BreakWa11's ShadowSocksR project has permanent suspended）. If I have free time, it will always update. 


### 使用方法：
### Instructions:
<br />
1. 如果已安装过TeddySun的一键包，请先卸载：
<br />
<br />
Please unintall which installer made by TeddySun if you have been installed:
<br />
<br />
<pre><code> ./shadowsocksR.sh uninstall </code></pre>
<br />
2. 然后重新安装：
<br />
<br />
Then reinstall:
<br />
<br />
<pre><code>wget --no-check-certificate -O shadowsocksRR.sh https://git.io/vdMUr && chmod +x shadowsocksRR.sh && ./shadowsocksRR.sh 2>&1 | tee shadowsocksR.log</code></pre>
<br />
3. 安装完成后，推荐重启一下SSRR服务：
<br />
<br />
It's recommend for you to restart SSRR service after installation.
<br />
<br />
<pre><code>/etc/init.d/shadowsocks restart</code></pre>
<br />
4. 修改配置文件。
<br />
<br />
How to modify SSRR configuration file?
<br />
<br />
<pre><code>vi /etc/shadowsocks.json</code></pre>
<br />

### 重新安装/更新：
### Reinstall/Update:
<br />
1. 如果安装过这个脚本，请先卸载：
<br />
<br />
If you have installed this shell, please unintall first.
<br />
<br />
<pre><code> ./shadowsocksRR.sh uninstall </code></pre>
<br />
2. 删除原脚本：
<br />
<br />
Delete former shell.
<br />
<br />
<pre><code> find . -name shadowsocksRR.sh -delete </code></pre>
<br />
3. 重复上一节“使用方法”中的第2、3步。
<br />
<br />
Repeat second and third step in previous section.
<br />
<br />

### History:
- Use UUID for default password may cause shadowsocksRR don't work so I change strategy of password generation length to 16 characters, include numbers、uppercase and lowercase letters、special characters.
- UUID generator is only pre-installed by Ubuntu, when I run this shell on Debian, variable $dpwd could not obtain UUID correctly, so I changed a general way to get it instead of transform uuidgen component to make sure it works on different environment. 
- Add an UUID generator as new password for SSRR installer（recommend）, at least 18 characteres, include letters and numbers.（2018.7.28）
- Add English description for readme.md（2018.7.26）
- A guy told me once following default opions, the configurations of congratulate interface are different from promptions of installtion process when shell executed finally so I fixed it.（2018.7.26）
- Cancel default port 443, use rand ports between 10000 to 59999 during install.（2018.7.21）
- Give main program a permission of 777.（2018.7.21）
- Optimized linux OS determine logic.（2018.7.16）

### 更新历史：
- 部分UUID类型可能会导致shadowsocksRR不能正常连接网络，故重新修改了密码生成策略，16位随机字符、包括数字、大小写字母特殊字符。
- 由于获取UUID的方法只适用于Ubuntu，故换了一种调用方式，确保脚本的兼容性。
- 采用系统自带的UUID生成功能，替代每次需要手动输入密码，要求至少18位数字，然后用正则来检查长度字母数字是否符合要求，推荐使用脚本里自带的UUID生成功能，作为你的SSRR服务端密码（2018.7.28）
- readme.md 增加了英文说明（2018.7.26）
- 修复了按回车键一路采取默认配置，实际配置和脚本提示配置并不一致的问题（2018.7.26）
- 修复了采用默认443端口，防火长城会瞬间封杀目标实例IP（取10000~59999之间的随机数）；（2018.7.21）
- 修复了主程序server.py由于没有赋予足够的权限，导致安装完成后并不能正常运行的问题（chmod 777）；（2018.7.21）
- 优化系统判断逻辑（2018.7.16）
- ShadowSocksRR 的开发人手不足，核心 Python 项目更新后，其他客户端版本的跟进并不快，导致客户端用户不能及时使用最新的协议和特性，本次新增的auth_akarin_rand / auth_akarin_spec_a 协议只放出了 Python / Windows 的源代码。其中，Windows 版本只有源代码文件，并未进行编译，我拜托群里的小伙伴，将最新版本的 Windows 客户端给编译了出来并提供下载，谢谢泥萌，比心 ~~ （2018.6.22）
- 加入auth_akarin_rand / auth_akarin_spec_a 协议，新协议的改动非常大，协议详情参见：https://github.com/shadowsocksrr/shadowsocksr/commit/08b88026e884eac456b0d7dee1d5dbcbf30cebe3 （2018.6.22）
- auth_chain_c/e/f 这三种协议均存在问题，客户端设置后无法和服务端连接，不建议在配置的时候使用，auth_chain_d协议主要针对数据包的长度分布归属到模式中，让包分布看起来更规整，并在一定程度上增加了各种密码生成的模式的最大适用长度，这样就不需要在极端情况下再临时生成随机数，降低大包传输时的计算量，提高下载极限速度，推荐使用。文档说明：https://github.com/shadowsocksrr/shadowsocks-rss/blob/master/ssr.md （2018.2.28）；
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

# 郑重声明
# Statement
自2018年2月25日起，ShadowSocksR经历了极其严重的干扰、屏蔽和封锁，有大量用户表示，自己凡是搭建了的ShadowSocksR的VPS，IP已经被防火长城给屏蔽，本人也有不少机器不幸遇难，ShadowSocksR目前遭遇破娃酱撒手不干和后继无人的状况，不再推荐个人使用。
为此，我特意做了一番测试，在CloudGarage的VPS后面板尝试新建一台机器，并被分配到了新的IP，然后部署ShadowSocksR服务，运用的是auth_chain_d + TLS ticket auth + chacha20的配置参数，并使用强密码和日本地区未被防火长城过滤掉的日本网站混淆参数，试图躲避防火长城的攻击，很可惜的是，这个IP仅仅存活了不到半天，就被防火长城给屏蔽，很明显，过年后国家进一步增强了封锁手段，<b>使用ShadowSocksR简直就是自寻死路，为了你手中有限的IP地址资源考虑，我建议大家立马暂时停止使用</b>。
<br />

### 防火长城有了哪些进步？大规模的封锁意味着什么？以后突破封锁该怎么做？
### How many progress does GFW have been archived? How to fight with it?
- 理论上来说，只要防火长城愿意，目前主流的ShadowSocksR、ShadowSocks with OBFS、v2ray、蓝灯、自由门、等主流应用都是完全有能力将其封锁的，其本质是因为开发突破封锁工具的开发者的个人力量，相比国家级别的软 + 硬一体化封锁手段，显得脆弱且无力，请尽可能使用那些小众、部署难度大、抗封锁手段丰富有效、不易被商家大规模应用并出售代理生意的工具/手段。显然，目前突破封锁工具脆弱程度的大致排名是：<a href="https://github.com/shadowsocksrr">ShadowSocksRR</a> > <a href="https://github.com/shadowsocks">Shadowsocks + OBFS</a> > <a href="https://github.com/v2ray">v2ray</a> > <a href="https://github.com/coyove/goflyway">GoFlyWay</a>/<a href="https://github.com/txthinking/brook">Brook</a>，目前我已转向v2ray，各位好自为之；
- 这次防火长城主要针对的，是ShadowSocksR，如果你是小白，非要尝试去用，我建议你选择支持自由更换IP的商家，比如Vultr、DigitalOcean、Linode、搬瓦工（好吧，这几个商家的屁眼已经被国人给操烂了，它们日本、美西等地的IP大批量地被GFW blocked，有的时候开日本的机器，换十次IP能有一个可以用的就不错了，前人糟践完了，只会让后来者更没有车上），了解更多内容，请参见冯硕大佬的这篇文章：《<a href="https://zhuanlan.zhihu.com/p/33841302">可以免费换IP的VPS商家盘点</a>》；
- 不再建议购买搬瓦工的VPS做梯子使用，搬瓦工有大量IP被列入重点监测的对象，且这个商家设置了一个官方ping服务监测点，只要探测到自己机器的IP被国内屏蔽，即使你购买了可以自由切换机房的套餐，无论怎样操作，都会出现“Migration backend is currently not available for this VPS. Please try again in 10-15 minutes. (734152)”这样的错误提示。年付20刀，换个IP就要8刀，要是又被ban了还要继续加钱换，按防火长城的屏蔽神速，你换IP估计得换到破产。
- 随着举国之力建设的防火长城的技术进步，大规模被封锁IP的情况只会愈演愈烈，请<b>不要把自己正常业务网站（比如博客、应用服务等）的服务和搭建翻墙服务的放在同一个境外服务器上！阿里云国际、腾讯云国际之类的照样不能免俗</b>，因为你要随时做好自己手上的梯子被防火长城发现，IP被ban的事实，正常业务更换IP的代价是极大的，这个利害关系一定要搞清楚。
- 极少情况下，你的机器即使没有搭建梯子，IP也会被ban，当然这种情况是极其偶然的，一般认为防火长城会拦截到你的数据包，进行深度包分析，在“带有SSR/SS流量特征”的概率大到一定程度（只要特征符合即可，无需截获你和服务器之间通信的具体信息）的时候，才会做出整治行动，不会做出“宁可错杀千人，绝不放过一个”的赖皮行径。
- 大部分飞机场的热门区域，比如日本、美西、香港、新加坡等地的IP段，可能会被防火长城拉进重点监控对象，还是上面那一点的意思，防火长城不会随意屏蔽整个C类IP段，但因为加大了监控力度，这部分被特殊照顾的IP段里的IP一旦出现了敏感特征流量，那么防火长城在获得了足够多的证据的前提下，会毫不留情地封禁对应的IP，因为特意加大了监控力度，所以从建立机器到被屏蔽IP的过程会快到令你恐惧的地步，以后会变得越来越快，越来越精准。解决办法也不是没有，选择更偏僻地区的冷门VPS商家，问题或许可以迎刃而解。
- 少数情况下，你的机器如果立马禁止代理服务，并不再有相应的客户端与其通信，过一段时间，防火长城会解封你的IP，但是这个IP就已经默认被加入重点监测的对象，至于敢不敢再搭建梯子，你自己看着办吧（如果你购买的是搬瓦工的可切换机房套餐，建议立马切换机房，不要再保有这个IP）。
- 如果你愿意用一台被屏蔽的IP做测试，可以发现一个很有意思的现象，就是我们在本机（中国大陆境内）试图向远程机器做一个Traceroute，是可以完全走通的，走出了正确的路径，并返回了途经的各个路由节点名称；但是，我们尝试用Xshell连接这台远程服务器（走新搭建的v2ray代理），并在这台远程服务器里做连接到我们本机IP Traceroute的时候（或者Traceroute to 你在国内拥有的某家IDC服务商下面的机器IP也可以），走向国内出海处节点的那一程被阻断。简单来讲，就是去向的连接没有被拦截，防火长城拦截的是回程连接，如果是有防止国内机密泄露的考虑，那么拦截应当是双向的。而仅仅拦截的是数据包传回国内，说明防火长城此次的举动，就是为了大规模阻止境外服务器被用来做代理，单向拦截需要花费的成本比双向拦截要低一些，搭建代理翻墙的核心原理就是客户端向服务端发出请求，服务端应答客户端的请求，把相关内容回传到客户端上。回传的数据丢失了，无论是ping，还是http、ssh请求等，自然就失效了。
- 我始终相信，<b>自由地获取、发布不受任何政体审查的信息，是一项天赋基本人权</b>，随着国内一些众所周知的政治剧变，保障这份人权将变成一种奢望，但是，既然来到了这个世界，我们不能违背作为人类的本性，自愿接受被砍去手足、挖去双眸、刺破耳膜、缝上口鼻的命运，而且我也相信，这个国家会慢慢变得更好，现有的手段和压迫都只是暂时的苟且，总有一天，我们有自信，向全世界输出、接受所有批评、褒美我们的各种不同的声音，这是作为一个负责任、政治/文化/统治有自信的大国所应当具备的风度。治水之道，堵不如疏，水能载舟，亦能覆舟，当他们足够富足、聪明、独立、知礼之后，简单粗暴地封堵信息的流动，只会让黑白颠倒，事实不分，公信力逐步恶化，最终固步自封，停止进步，自食其果。
- 从“斯德哥尔摩症”的角度，墙被推倒只是时间问题，为此我一个文科生，掌握了从选购VPS，到Linux系统命令行、运营维护等各种奇奇怪怪的技能，多年以后，回首年轻的时候，这段经历也许是我这一生最不可思议的各种经历之一（~~另外一个美妙的经历，是认识了<a href="https://github.com/kirioxiangmeow"></a>~~ 发生了一些不快，她不值得）。
- 有关v2ray，没什么好讲的了，总之就是难用，当然更加便于使用的服务端部署/调整配置的一键包和GUI客户端之类的也是有的，我列举出来供大家参考一番，能摸索清楚的就用，弄不明白的，还是老老实实呆在墙里吧：
1. <a href="https://v2ray.com/ui_client/">GUI客户端（含Windows、Mac、Android、iOS等）</a>；
2. <a href="https://github.com/tracyone/v2ray.fun">服务端一键部署/调试配置脚本（推荐Cent OS7/Debian 8/Ubuntu 16.04 +，CentOS 6不可使用）</a>；
3. <a href="https://toutyrater.github.io/">v2ray白话文教程</a>。
- 脑子和搜索能力是个好东西，希望在座的各位和我一样拥有。
- 感谢每一个爱我的，以及在这条道路上提供工具和路径的，无私奉献的人，我们有着不同的性别、出身、工作、思维观念，但是，有一个共同的追求，让我们在这特别的时空里相遇，并努力为这14亿人口中的极小一部分，提供看世界的机会，这份相识就足够了。
<br />
<br />
