import sys
import os

class Drivers():
    virtual_env_path = sys.prefix
    win_chrome_32 = os.path.join(virtual_env_path, '\Lib\site-packages\chromedriver_py\chromedriver_win32.exe')
    win_chrome_64 = os.path.join(virtual_env_path, 'Lib\\site-packages\\chromedriver_py\\chromedriver_win64.exe')
    mac_chrome_arm64 = os.path.join(virtual_env_path, '\Lib\site-packages\chromedriver_py\chromedriver_mac-arm64')
    mac_chrome_x64 = os.path.join(virtual_env_path, '\Lib\site-packages\chromedriver_py\chromedriver_mac-x64')
    linux_64 = os.path.join(virtual_env_path, '\Lib\site-packages\chromedriver_py\chromedriver_linux64')

