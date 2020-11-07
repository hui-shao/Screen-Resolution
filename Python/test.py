# -*- coding: UTF-8 -*-
import win32api, win32con


def set_resolution():
    Width = int(input("Width: "))
    Height = int(input("Height: "))
    ResoLutionSet = win32api.EnumDisplaySettings(None, 0)  # 调用win32api接口,获取显示设备信息
    ResoLutionSet.PelsWidth = Width  # 设置分辨率宽
    ResoLutionSet.PelsHeight = Height  # 设置分辨率高
    print("即将设置分辨率为：%d x %d" % (Width, Height))
    ResoLutionSet.BitsPerPel = 32  # 显示设备的颜色分辨率
    ResoLutionSet.DisplayFixedOutput = 2  # 设置分辨率后拉伸画面，否则切换到小分辨率时，屏幕只在中间一小块
    if (input("确认?（y/n）")) == "y":  # DISP_CHANGE_SUCCESSFUL
        win32api.ChangeDisplaySettings(ResoLutionSet, 0)  # 设置生效
    return


def get_resolution():
    screenNum = win32api.GetSystemMetrics(win32con.SM_CMONITORS)
    print("显示设备的总数量为: %d" % screenNum)
    aScreenWidth = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    aScreenHeight = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    print("当前屏幕总的分辨率为：%d × %d " % (aScreenWidth, aScreenHeight))
    WidthGet = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
    HeightGet = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    print("获取的系统分辨率为：%d x %d" % (WidthGet, HeightGet))
    return


if __name__ == "__main__":
    get_resolution()
    set_resolution()