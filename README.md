# docker-manage 小型编排工具

install：
<pre>
git clone https://github.com/shemic/dm
cd dm
chmod +x install
./install
</pre>

安装时会自动安装docker。如果失败，请自行安装最新版本的docker即可。

基础指令：
<pre>
更新代码：dm up
使用哪个仓库为主(默认aliyun)：dm set private|aliyun|hub
删除某一个软件：dm rm web-php
</pre>

<pre>
可以使用以下命令开启web：
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
2018-01-17更新：增加opencv、dlib库
2018-01-31更新：增加tensorflow、pytorch库，但是没有集成在包里，因为装完比较大，建议自行安装，jupyter里打开命令行，执行以下命令：
cd /shell/install
./tensorflow.sh
./pytorch.sh


使用：
dm run py-note
py-note logs 查看token
访问你的浏览器：ip:10001、ip:10002
dmlearn install * 可以安装你需要的库，如：
dmlearn install seaborn

3、elk：
dm run elk-java（如果之前用了data-java这里就不用再执行了）
dm run elk-es
dm run elk-filebeat（需要到container/conf/elk里定义下抓取的日志目录）
dm run elk-kibana
默认账号密码：elastic/changeme
</pre>

<pre>
2017-12-05更新：
增加个人网盘：
dm run tool-pan
访问：
ip:9030 用户名密码都是superuser
ip:9030/dweb 是离线下载
</pre>

<pre>
2017-12-15更新（重要！）：
删除use功能。以不同的命令替代：

1、使用docker：
dm run web-php

2、安装php扩展：
dp install libevent 安装libevent扩展
dp install swoole 安装swoole扩展
dp install redis
dp install memcached
dp install mongo
dp show 查看当前可以安装的扩展
自带的php5.6和php7已经删除redis、mongo等扩展，请在需要时自行安装。
后续我会按照http://pecl.php.net/packages.php增加一些常用的扩展。
你也可以现在自行实现扩展的安装：
phpInstall swoole-2.0.10 swoole libevent-dev,libaio-dev,libmnl-dev
说明：
phpInstall 为固定指令
swoole-2.0.10 为在pecl.php.net中的扩展名和版本号
swoole 为生成的so名称
libevent-dev,libaio-dev,libmnl-dev 为依赖，多个用逗号隔开



3、使用composer：
dpc install laravel

4、使用dever：
安装plant：
dever是一个php框架，适合开发api、微服务、频繁修改模板、专题等业务，目前是内部测试版本。
plant是dever框架开发的一个小型社区
dever init
dever product plant
例子：http://www.5dev.cn/

5、使用git(方便在任意目录下pull或者push)：
dgit pull /data/
dgit push /data/
</pre>

<pre>
2017-12-18更新：
别名功能优化升级，当多个容器使用同一个别名时，可以使用该别名同时操作这多个容器。
如同时启动了php5、php7时，输入php -v， 可以同时看到这两个php的版本。
使用dp install redis安装扩展时，可以同时安装php5、php7的redis扩展。
该功能将为以后dm-manage多机部署提供支持。
</pre>



<pre>
2018年计划：
分工明确：
1、dm tool：工具包。上述更新都是增加了工具包。
2、dm task：任务器
3、dm manage：后台管理
4、dm cicd：持续集成
5、dm api：对外接口
6、dm shell：命令行工具，可以统一的直接对容器里的软件发布命令，如dp install libevent，将升级成：
dm shell
> php install libevent
> pip install tornado
> exit

7、dm ss：vpn工具

具体计划：
1、增加图形管理界面(dm manage)
2、增加多机使用dm(dm manage -> etcd -> dm1、dm2、dm3)
3、增加任务调度功能(celery、airflow)
4、增加持续集成等功能(从git上自动拉取代码并更新容器：CircleCI)
5、增加测试工具包
6、增加自动代理(能够通过dm直接访问google查资料)
</pre>


<pre>
2018-6-20更新：
1、增加default功能，直接使用dever run web时，只运行里面default定义的进程
2、增加lvs、consul等组件
3、增加集群（简易版本）：
ds init：开启集群，之后将得到集群主机ip
ds join ip：加入到集群中
之后的操作和dm一样
ds run web：启动web服务组集群
ds run web-nginx：启动nginx集群
ds rm web-nginx：删除nginx集群
ds update web-nginx：更新nginx集群（此命令比较复杂，最好参考docker service update）

之后将把consul和daemon加入进去，并实现可视化
</pre>