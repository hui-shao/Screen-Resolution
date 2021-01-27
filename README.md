# 分支说明

**该分支保留了原来的Python版本 (目前已弃用)**

------



# Screen-Resolution / 屏幕分辨率设置

A program based on C++/Python to customize screen resolution. 

一个基于C++/Python的用于调整Windows系统分辨率的小程序
<p align="left">
    <img src="https://img.shields.io/badge/platform-Windows-orange.svg?longCache=true&style=flat-square">
    <img src="https://img.shields.io/github/license/hui-shao/Screen-Resolution?style=flat-square">
    <a href="https://github.com/hui-shao/Screen-Resolution/releases"><img src="https://img.shields.io/github/v/release/hui-shao/Screen-Resolution?include_prereleases&style=flat-square"></a>
    <a href="https://github.com/hui-shao/Screen-Resolution/releases"><img src="https://img.shields.io/github/downloads/hui-shao/Screen-Resolution/total?color=blueviolet&style=flat-square"></a>
</p>

### 主要功能

接受传入参数，并将传入的参数值设置为分辨率。要求传入参数在“当前系统所支持的分辨率”列表内

```
Usage: [Width] [Height]
```

示例: 

```powershell
Screen-Resolution.exe 1920 1080
```

### 使用实例

- 可以设置为快捷方式放置在桌面
- 可以加入开机自启，实现自动调整分辨率

操作步骤如下：

1. `右键-新建快捷方式`，填写程序路径, 并在结尾加上传入参数，例如：`F:\Screen-Resolution.exe 1920 1080`
2. 设置开机自启。按下 `Win + R` 打开“运行”，输入 `shell:startup` 并执行，这将会打开 “启动” 文件夹。将快捷方式复制进刚才打开的目录里即可。