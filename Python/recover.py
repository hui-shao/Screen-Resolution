# -*- coding: UTF-8 -*-
import win32api

if __name__ == '__main__':
    win32api.ChangeDisplaySettings(None, 0)  # 恢复默认