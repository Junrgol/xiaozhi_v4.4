import os
import winreg
import winshell

"""
这里调用了winshell的CreateShortcut函数。
传入4个参数，分别为：快捷方式的路径，exe文件的路径，图标路径，还有描述信息。
"""
class startup:

    def __init__(self):
        self.startupPath = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' % os.getlogin()
        print(self.startupPath)
        #self.startupPath=r'D:\\Desktop'
    def create_shortcut(self,bin_path: str, name: str, desc: str):
        '''
        :param bin_path: exe路径
        :param name: 需要创建快捷方式的路径
        :param desc: 描述，鼠标放在图标上面会有提示
        :return:
        '''
        try:
            shortcut = name + ".lnk"
            winshell.CreateShortcut(
                Path=shortcut,
                Target=bin_path,
                Icon=(bin_path, 0),
                Description=desc
            )
            return True
        except ImportError as err:
            print("Well, do nothing as 'winshell' lib may not available on current os")
            print("error detail %s" % str(err))
        return False
    def Create_StartUp(self,bin_path,link_name,desc):
        '''
        :param bin_path: exe路径
        :param link_path: 快捷方式地址、名称
        :param desc: 描述，鼠标放在图标上面会有提示
        :return:
        '''
        return self.create_shortcut(bin_path,self.startupPath +link_name, desc)

    def Destory_StartUp(self,link_name):
        if os.path.exists(self.startupPath +link_name+".lnk"):
            os.remove(self.startupPath +link_name+".lnk")
            return True
        else:
            return False

