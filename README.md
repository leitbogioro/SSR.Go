<!-- anchor area -->
<p><a href="#Introduce">简介（Introduce）</a></h1></p>
     <ul>
     <li><a href="#Preface">前言（Preface）</a></li>
     <li><a href="#Install">安装（Install）</a></li>
     <li><a href="#Spec">特性（Specs）</a></li>
     <li><a href="#Sample">使用示例（Sample）</a></li>
     <li><a href="#Request">外部要求（Request）</a></li>
     <li><a href="#Updates">更新日志（Updates）</a></li>
     <li><a href="#THX">致谢（Thanks）</a></li>
     </ul>
<!-- anchor area -->

<h1><a id="Introduce">简介（Introduce）</a></h1>
<p>全新面貌的SSR.Go，现已启航！她是一款可突破中国互联网审查的强力代理工具。使用本工具，你可方便地调整、管理 ShadowSocksRR 的配置和运行。以下是本工具的说明，你可以点击相应的跳转链接，寻找你感兴趣或对你而言感觉重要的部分。</p>
<p>ShadowSocksRR powered by SSR.Go is a robust proxy which can breakthrough Chinese internet censorship. You can use it easily to configurate and manage ShadowSocksRR program and keep it running. Just click urls which interested or important for you and they construct to descriptions of this tool.</p>
<br />

<h2><a id="Preface">前言（Preface）</a></h2>
<p>面对威权压迫，你是甘为一辈子懦夫，还是坚定勇气，试着改变这个污浊不堪的世界？于此，虽千万人吾往矣。全新的shadowsocksR管理助手——SSR.Go，现已问世。长夜漫漫，父说，擦亮双眸的你，需要一道光明，使者便从了他的意，把光明给带来了。</p>
<p>I'm not only hate GFW, but also fighting with it. No matter from where, human has natural rights to access to uncensored information to escape from authoritarianism and oppression.</p>
<br />

<h2><a id="Install">安装（Install）</a></h2>
<p>如果你的 VPS 刚刚新装过系统，<b>强烈建议你输入以下命令，重启并再次连接</b>，否则安装的过程中，会出现各种各样未知的问题。</p>
<p>I really recommend you to restart your VPS when your installed system just now and you need to reconnect it manual in order to avoid lots of unknown mistakes.</p>
<pre><code>reboot</code></pre>
<p>然后开始安装此工具（简体中文版）。</p>
<pre><code>bash -c "$(curl -fsSL https://git.io/fNpuL)"</code></pre>
<p>And then you can install it ( An English version ).</p>
<pre><code>bash -c "$(curl -fsSL https://git.io/fAUCt)"</code></pre>
<p>需要注意的是，<b>简体中文版 SSR.Go 和英文版 SSR.Go 只能同时使用其中的一个，不可共存。</b></p>
<p>You need to consider that <b>only one version of simplified Chinese or English version of SSR.Go can run on your environment</b>.</p>
<br />

<h2><a id="Spec">特性（Specs）</a></h2>
<p>1. 一键部署 ShadowSocksR 和 SSR.Go，无需额外设置运行环境</p>
<p>Once bash command, ShadowSocksR with it's manager————SSR.Go and included operating environment will be installed. </p>
<br />
<p>2. 在你的vps里的任意位置，输入 ssr 即可启动，对话框式操作界面，方便快捷</p>
<p>It's so convince that you just need input "ssr" to run it everywhere in your linux system then dialog operation will lead you to config with ShadowSocksR.</p>
<br />
<p>3. <b>默认采用最新版实验型协议————akarrin 系列</b>，抗封锁能力较强，<b>目前只有 Windows 客户端支持，手机/路由器均不能用，但仍然强烈建议使用</b>，下载链接：<a href="https://github.com/leitbogioro/ShadowsocksRR-Install/files/2127044/ShadowsocksR-win-4.9.0.zip-dev.zip">ShadowsocksR-win-4.9.0.zip-dev</a>。</p>
<p>Use akarrin series protocol as ShadowSocksR's config, <b>I recommend this protocol because it has strong anti-blocking ability but it can only supported on Windows and doesn't work on smartphone or wireless-router.</b>Press it to download: <a href="https://github.com/leitbogioro/ShadowsocksRR-Install/files/2127044/ShadowsocksR-win-4.9.0.zip-dev.zip">ShadowsocksR-win-4.9.0.zip-dev</a>.</p>
<p>4. 可快速生成、查看客户端配置信息，无需费劲巴拉地修改 config.json 文件。</p>
<p>You can quickly generate, look up client configurate information instead of modifiy a "config.json" which you don't have any fuckin patient to deal with!</p>
<p>5. 专为 CentOS 6/7 解决了复杂的二维码生成组件配置环境（你知道我 TM 花了多大劲吗！），你可以在 CentOS 系统上愉快地使用它们。</p>
<p>Especially complained a complex compatibility problem about qrcode generation library on CentOS 6/7（do you know how much fuckin difficult I had suffered!）, now you can have a perfect experience on CentOS.</p>
<br />

<h2><a id="Sample">使用示例（Sample）</a></h2>

![1](1.jpg)

![2](2.jpg)

![3](3.jpg)

![4](4.jpg)
<br />
<br />

<h2><a id="Request">外部要求（Request）</a></h2>
<p>1. 一台运行以下任意Linux系统的VPS：</p>
<p>A linux virtual private server which run the following system:</p>
<ul>
<li>Debian 7</li> 
<li>Debian 8</li>
<li>Ubuntu 14</li>
<li><b>Ubuntu 16（推荐 Recommend）</b></li>
<li>CentOS 7</li>
</ul>
<br />
<p>2. ssh连接工具（推荐：<a href="https://www.netsarang.com/products/xsh_overview.html">Xshell</a> 或 <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">Putty</a>）</p>
<p>A ssh connect tool（Recommend <a href="https://www.netsarang.com/products/xsh_overview.html">Xshell</a> or <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">Putty</a>）</p>
<br />
<p>3. 部分系统在执行安装命令前，需要安装curl组件，对应命令如下：
<p>Some environment need to install curl before download and install SSR.Go, you should do:</p>
<p>Cent OS</p>
<pre><code>yum -y install curl</code></pre>
<p>Debian/Ubuntu</p>
<pre><code>apt-get install curl -y</code></pre>
<br />

<h2><a id="Updates">更新日志（Updates）：</a></h2>
<ul>
<li>使 CentOS 6/7 上的二维码生成功能可用。（2018.8.26）</li>
<p>Make a perfect availability about generate qrcode on CentOS 6/7.</p>
<li>增加生成二维码功能，因 Cent OS 6 自带的 python 版本与 qrcode 组件的运行环境不兼容，故暂时功能异常，正在修复中。（2018.8.24）</li>
<p>Add a function about generate client qrcode, but it depends on qrcode pip kit for python2.7 and it doesn't complain with python2.6 in Cent OS 6 so I'm fixing it.</p>
<li>修复了阿里云、腾讯云、Azure、Amazon、Google Cloud Platform等自带安全组规则的vps获取 IP 地址会变成内网地址的问题。（2018.8.24）</li>
<p>Fix a problem about getting external network IP address but it causes to local IP address in vps from AlibabaCloud, TencentCloud, Azure, Amazon, Google Cloud Platform etc which has it's own security group rule.(2018.8.24)</p>
<li>更新获取服务端 IP 地址逻辑。（2018.8.23）</li>
<p>Update get server IP address logic.(2018.8.23)</p>
<li>修正更新 ssr 和 SSR.Go 功能无效的问题。（2018.8.22）</li>
<p>Fix an invalid mistake about updating ssr and SSR.Go.(2018.8.22)</p>
<li>优化安装流程（2018.8.22）</li>
<p>Optimize installation process.(2018.8.22)</p>
<li>修复在 CentOS 6/7 上运行错误的<a href="https://github.com/leitbogioro/SSR.Go/issues/9#issue-352075641">问题</a>，详情请<a href="https://github.com/leitbogioro/SSR.Go/issues/9#issuecomment-415026731">参见</a>。（2018.8.22）</li>
<p>Fix an error about running with <a href="https://github.com/leitbogioro/SSR.Go/issues/9#issue-352075641">mistakes</a> on CentOS 6/7, for more details, please <a href="https://github.com/leitbogioro/SSR.Go/issues/9#issuecomment-415026731">view</a>.(2018.8.22)</p>
<li>新增中英文切换功能（2018.8.21）</li>
<p>Add a function about switch a version between simplified Chinese and English each other.(2018.8.21)</p>
<li>正式推出英文版。（2018.8.21）</li>
<p>An English version of SSR.Go is released.(2018.8.21)</p>
<li>添加“首次进入后需要重启才能顺利安装”的描述。（2018.8.20）</li>
<p>Add notice about "You need to reboot your system after installed system before install SSR.Go."(2018.8.20)</p>
<li>修复了加密依赖“libsodium”的安装策略。（2018.8.19）</li>
<p>Fix install strategy about "libsodim" encryption component.(2018.8.19)</p>
<li>修复了安装过程中，ShadowSocksR主程序————“manyuser.zip”文件下载错误的问题（2018.8.19）</li>
<p>Fix a problem about during install, main ShadowSocksR source code————"manyuser.zip" can't download.(2018.8.19)</p>
<li>修改增添端口策略，如果 iptables 里已经有了 SSR 运行的端口，则不重复添加，以免添加大量冗余规则。（2018.8.19）</li>
<p>Change add ports tactics, if there are same ports which SSR running need in iptables it won't add rules indeed to avoid mass redundancy.(2018.8.19)</p>
<li>新增将 SSR 运行端口添加到系统防火墙功能。（2018.8.19）</li>
<p>Expand a new function for add iptables port rules about port of SSR used.(2018.8.19)</p>
<li>修改安装后提示“输入 srr 并回车使用即可使用”的错误描述（2018.8.18）</li>
<p>Change wrong prompt after installed(2018.8.18)</p>
<li>初版完成。（2018.8.17）</li>
<p>First release is completed.(2018.8.17)</p>
<li>增添文档描述。（2018.8.17）</li>
<p>Add documents and describes.(2018.8.17)</p>
</ul>
<br />

<h2><a id="THX">致谢（Thanks）：</a></h2>
<p>tracyone：<a href="https://github.com/tracyone/v2ray.fun">v2ray.fun</a></p>
<p>v2ray.fun 原作者：<a href="https://github.com/YLWS-4617">雨落无声</a></p>
<p>ShadowSocksR 原作者：<a href="https://github.com/breakwa11">破娃酱</a></p>
<p>ShadowSocksRR 现维护者<a href="https://github.com/Akkariiin"> Akarrin </a>和其项目主页：<a href="https://github.com/shadowsocksrr">ShadowSocksRR</a></p>
<p>ShadowsocksR 一键安装包作者：<a href="https://teddysun.com">TeddySun</a></p>
<br />

<h2>喜欢就请我吃顿煎饼果子呗</h2>

![5](5.jpg)
