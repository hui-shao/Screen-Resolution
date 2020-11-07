# -*- coding: UTF-8 -*-
import win32api

if __name__ == '__main__':
    Width = 800
    Height = 600
    ResoLutionSet = win32api.EnumDisplaySettings(None, 0)  # 调用win32api接口,获取显示设备信息
    ResoLutionSet.PelsWidth = Width  # 设置分辨率宽
    ResoLutionSet.PelsHeight = Height  # 设置分辨率高
    print("即将设置分辨率为：%d x %d" % (Width, Height))
    ResoLutionSet.BitsPerPel = 32  # 显示设备的颜色分辨率
    ResoLutionSet.DisplayFixedOutput = 2  # 设置分辨率后拉伸画面，否则切换到小分辨率时，屏幕只在中间一小块
    if (input("确认?（y/n）")) == "y":  # DISP_CHANGE_SUCCESSFUL
        win32api.ChangeDisplaySettings(ResoLutionSet, 0)  # 设置生效
