import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mypro import MainWindow
import threading
from pynput import mouse
import time
from pynput.keyboard import Controller
import yaml

class MouseMonitor():
    # 定义一个鼠标监控的类
    def __init__(self,MainWindow):
        # 初始化一个鼠标右键按下的时间变量
        self.right_press_time = 0
        self.keyboard = Controller()
        self.MainWindow=MainWindow
        self.program_setting_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/setting.yaml'

    def threads_js(self):

        '''mm = js()
        mm.start()
        mm.join()'''
        print("开始计时")
        global mouse_right_press
        now = time.mktime(time.localtime())
        while mouse_right_press:
            time.sleep(0.1)
            fu = time.mktime(time.localtime())
            press_time=0.4
            if fu - now > press_time:
                print(fu,now)
                #self.MainWindow.move(self.x,self.y)
                self.MainWindow.showNormal()
                self.MainWindow.activateWindow()

                # with mouse.Listener(on_click=on_click, suppress=True) as lis:
                # lis.join()
                break

    def on_click(self, x, y, button, pressed):
        global mouse_right_press
        # 定义鼠标点击事件的处理函数
        #print(55555,self.MainWindow.minimumSize())
        mx,my=self.MainWindow.x(),self.MainWindow.y()
        if x>mx and x<mx+self.MainWindow.size().width() and y>my and y<my+self.MainWindow.size().height():
            pass
        else:
            if self.MainWindow.isActiveWindow():
                #hld = win32gui.FindWindow(None, u"小智助手")
                #win32gui.SetWindowPos(hld, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
                self.MainWindow.hide()
        '''if button == mouse.Button.middle:
            if pressed:
                self.MainWindow.move(int(x-self.MainWindow.size().width()/2),int(y-self.MainWindow.size().height()/2))
                self.MainWindow.showNormal()
                self.MainWindow.activateWindow()'''

        with open(self.program_setting_dir, 'r', encoding='UTF-8') as stream:
            self.program_setting_data = yaml.safe_load(stream)
        #print("按下的按键是%s" % (i_str,))
        if  button == mouse.Button.middle and not self.program_setting_data['pause']:
            # 如果是鼠标右键
            if pressed:
                mouse_right_press=True
                # 如果按下，记录当前时间
                '''self.right_press_time = time.time()
                self.x=int(x-self.MainWindow.size().width()/2)
                self.y=int(y-self.MainWindow.size().height()/2)
                self.MainWindow.move(self.x, self.y)
                self.MainWindow.showNormal()
                self.MainWindow.activateWindow()'''
                #thread_js = threading.Thread(target=self.threads_js)
                #thread_js.start()

            else:
                mouse_right_press=False
                # 如果松开，计算按下的时间间隔
                duration = time.time() - self.right_press_time
                self.x = int(x - self.MainWindow.size().width() / 2)
                self.y = int(y - self.MainWindow.size().height() / 2)
                self.MainWindow.move(self.x, self.y)
                self.MainWindow.showNormal()
                self.MainWindow.activateWindow()
                #hld = win32gui.FindWindow(None, u"小智助手")
                #win32gui.SetWindowPos(hld, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)

                '''if duration > 0.8:
                    # 如果超过1秒，打印输出
                    self.MainWindow.move(x-130,y-130)
                    self.MainWindow.showNormal()
                    self.MainWindow.activateWindow()
                    self.keyboard.press(pynput.keyboard.Key.esc)
                    self.keyboard.release(pynput.keyboard.Key.esc)'''
        '''else:
            print(self.MainWindow.isActiveWindow())
            if not self.MainWindow.isActiveWindow():
                self.MainWindow.hide()'''




    def start(self):
        # 定义一个启动监听器的方法
        self.listener.join()

    def mouse_listener_thread(self):
        # 定义一个鼠标监听器线程函数
        #mouse.Listener(on_click=self.on_click)
        with mouse.Listener(on_click=self.on_click) as listener:
            # 启动监听器
            listener.join()

    def stop(self):
        # 定义一个停止监听器的方法
        self.listener.stop()





if __name__ == '__main__':
    path = '/'.join(sys.argv[0].replace("\\", "/").split("/")[-1]) + '/'
    try:
        global mouse_right_press
        mouse_right_press = False
        app = QApplication(sys.argv)
        # apply_stylesheet(app,theme="light_blue.xml")
        # app.setStyleSheet(qdarkstyle.load_stylesheet())
        main_window = MainWindow()
        # 创建一个鼠标监控类的对象
        mm = MouseMonitor(main_window)
        # 创建一个线程对象，调用鼠标监控类的start方法
        t = threading.Thread(target=mm.mouse_listener_thread)
        # 启动线程
        t.start()

        # 等待线程结束
        main_window.show()
        # main_window.hide()
        sys.exit(app.exec_())

        t.join()

        # apply_stylesheet(app,theme="light_blue.xml")
        # app.setStyleSheet(qdarkstyle.load_stylesheet())
        # main_window=CandyWindow.createWindow(main_window,"blueDeep",title="小智助手",ico_path=path+"pic/robot.png")
    except Exception as ex:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pro_dir = self.path + run_file
        with open(path + '/log_error.log', 'a+') as f:
            f.write(now_time + ' ' + ex + '\n')

