# dever-manage 小型编排工具
<pre>
git clone https://github.com/shemic/dm
cd dm
chmod +x install
./install
</pre>

无需关注是否安装了docker，本工具会自动安装docker。(本工具直接使用阿里云提供的sh来安装docker，经过测试，ubuntu16无法安装成功，请直接用apt install docker.io安装。)

基础指令：
<pre>
更新代码：dm up
使用docker工具包(默认已经使用该工具包)：dm use docker
使用哪个仓库为主(默认aliyun)：dm set private|aliyun|hub
删除某一个软件：dm rm web-php
</pre>

<pre>
当前使用的工具包为docker时，可以使用以下命令开启web：
启动全部：dm run web
启动某一个软件：dm run web-mysql
删除全部：dm rm web
删除某一个软件：dm rm web-php
</pre>

执行完之后，请用浏览器访问你的ip即可。修改nginx配置可到container/conf/web/nginx下。

<pre>
目录说明：
1、container：容器内的文件
2、data：生成的数据目录，可以用作备份
3、src：源码
</pre>

<pre>
指令传参说明：

-h 查看帮助 
-a or --action 方法名
-n or --name 配置文件名或行为名
-p or --param 执行参数，一般要根据name判断

docker方法列表：
1、show：显示当前启动的docker容器
2、showi：显示当前的docker镜像
3、rm：删除出现异常或者没有启动的docker容器
4、rmi：删除过期的docker镜像
5、package：显示可用的docker镜像(2017-07-25)

方法列表（带有name参数）：
1、run：运行容器
2、stop：停止容器
3、restart：重启容器
4、crate：创建容器
5、call：运行容器，仅运行一次，用于执行一些特殊指令
6、up：运行容器并更新docker镜像
7、rm：删除正在运行的docker容器
8、save：保存或备份正在运行的docker容器
9、load：将保存或备份的docker容器恢复并重新运行
10、show：显示当前启动的docker容器(2017-07-25)

例子：
1、dm -a run -n web-php：根据src/docker/conf/web.conf里的php配置，来持续运行php容器
2、dm -a run -n tool-apidoc -p input=demo^out=output：根据src/docker/conf/tool.conf里的apidoc配置，来运行apidoc容器，这个配置里设置了run参数，指令中加入run，则apidoc容器将作为工具使用，无需持续运行apidoc容器，仅执行一次。input=demo将替换{$input}为demo，out=output将替换{$out}为output，冒号“:”为默认值
容器的配置请修改src/docker/conf/*.conf

也可以使用无参数名的方式来传入参数：
1、dm run web-php
2、dm call tool-apidoc input=demo^out=output

2017-07-25更新：
当使用dm run之后，会自动生成这个容器的基本指令，比如执行了上述的dm run web-php

之后可以这样使用：
1、web-php: 进入该容器的sh命令行
2、web-php logs：查看该容器启动日志
3、web-php inspect：查看该容器的基本信息
4、web-php stop：停止该容器
5、web-php rm：停止并删除该容器，等同于dever rm web php
6、web-php show：显示该容器的状态
7、web-php run：运行或者重新启动改容器
8、web-php restart：重新启动容器

</pre>
<pre>
2017-11-14更新：
当前工具包：docker、dever、php、git
1、使用dever来安装plant：
dever是一个php框架，适合开发api、微服务、频繁修改模板等业务
plant是dever框架开发的一个小型社区
dm use dever
dm init
dm product plant
例子：http://www.5dev.cn/

2、使用git(方便在任意目录下pull或者push)：
dm use git
dm pull /data/
dm push /data/

3、使用php(暂时不能使用)：
dm use php
dm install redis 安装插件
dm composer laravel 安装composer里的软件包

</pre>

<pre>
2017-11-15更新：
接下来要更新的功能：
1、增加图形管理界面(dm manage)
2、增加多机使用dm(dm manage -> etcd -> dm1、dm2、dm3)
</pre>

<pre>
2017-11-22更新：
增加一些比较有用的docker工具包：
1、大数据套件：
dm run data-java
dm run data-hadoop
dm run data-spark
dm run data-zeppelin
需要先等待data-java安装完成之后再安装之后的。可以到container/share/lib下看一下是否有jdk
访问：
ip:9991 
ip:40099
ip:9999

2、机器学习：
dm run py-note（jupyter+numpy、scipy、matplotlib、pandas、scikit-learn、scrapy、gevent、pymysql、psycopg2）

3、elk：
dm run elk-java（如果之前用了data-java这里就不用再执行了）
dm run elk-es
dm run elk-filebeat（需要到src/docker/conf/elk里定义下抓取的日志目录）
dm run elk-kibana
默认账号密码：elastic/changeme
</pre>

<pre>
2017-12-05更新：
增加个人网盘：
dm run tool-pan
访问：
ip:9090 用户名密码都是superuser
ip:9090/dweb 是离线下载
</pre>