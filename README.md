#code-manage-sublime

##简介
code-manage-sublime是一个sublime2插件，用来管理一些常用的代码模板。通过该插件可以很方便的将Sublime中的代码添加到管理文件中，同时也能很方便的将管理的代码插入到当前文件指定位置。

##如何安装
由于并未申请sublime官方的认证，因此想要安装该插件只能先从github下载zip包，在sublime的Packages文件加下新建CodeManage文件夹，将zip解压到该目录下，重启sublime即可。

##快捷键
```json
  [{
      "command": "code_tpl_add",
      "keys": [
      "ctrl+alt+]"
      ]
      }, {
      "command": "code_tpl_insert",
      "keys": [
        "ctrl+alt+["  
      ]
  }]
```
##如何使用
###1.添加新代码
选中要添加的代码，然后按ctrl+alt+]后填写该段代码的模板名称即可。
###2.插入代码
将光标定位到要插入代码位置，按ctrl+alt+[后选择要插入的模板名即可。
###3.使用替代符
我们可以在代码模板里边定义一些变量，然后通过配置文件var-map.conf来设置变量。var-map.conf格式如下（每行都是key=value,不能有空格）：
```
username=awayy1432
```
在模板文件里对应变量格式为{{xxxx}}，下边是一个文件注释头的模板：
```
/**
* {{username}}
* created {{date}}
**/
```
此外，date无需在var-map.conf里设置，会直接替换成当前时间

