import time
import shutil
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import sys,os
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtWidgets import (QApplication, QMessageBox,
                             QMenu, QAction, QSystemTrayIcon,QToolButton)
from subprocess import run,Popen
import subprocess
import psutil
import yaml
from system_hotkey import SystemHotkey
import pyautogui
import tkinter as tk
sys.path.append('/'.join(sys.argv[0].replace("\\", '/').split('/')[:-2]))
from common.Startup import startup
from common.worning import worning
from concurrent.futures import ThreadPoolExecutor
import datetime
from PyQt5.QtCore import pyqtProperty
import win32ui
import win32gui



#@colorful("blueDeep")
class MainWindow(Ui_MainWindow,QMainWindow,QApplication):
    sigkeyhot = pyqtSignal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        root = tk.Tk() #获取屏幕尺寸
        pc_screenheight = root.winfo_screenheight()
        root.destroy()
        scale=pc_screenheight/900
        new_width,new_height=int(scale*self.size().width()),int(scale*self.size().height())
        #self.resize(new_width,new_height)

        self.subprocess_PID={}
        self.program_setting_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/setting.yaml'
        with open(self.program_setting_dir, 'r', encoding='UTF-8') as stream:
            self.program_setting_data = yaml.safe_load(stream)
        # 绑定按钮点击事件
        self.common_button = [self.toolButton_0_1, self.toolButton_0_2, self.toolButton_0_3, self.toolButton_0_4,
                         self.toolButton_0_5, self.toolButton_0_6, self.toolButton_0_7, self.toolButton_0_8,
                         self.toolButton_0_9, self.toolButton_0_10, self.toolButton_0_11, self.toolButton_0_12,self.toolButton_1_1, self.toolButton_1_2, self.toolButton_1_3, self.toolButton_1_4,
                         self.toolButton_1_5, self.toolButton_1_6, self.toolButton_1_7, self.toolButton_1_8,
                         self.toolButton_1_9, self.toolButton_1_10, self.toolButton_1_11, self.toolButton_1_12]
        self.program_path=self.get_program()
        #创造自启字段，放置在common文件夹的auto_start.yaml中
        auto_start_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(auto_start_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        if setting_data == None:
            setting_data = {}
        for program_path in self.program_path:
            program_name=program_path.split('/')[-2]
            if program_name not in setting_data.keys():
                setting_data[program_name] ={'auto_run':False,'year':'0','month':'0','day':'0','week':'0','day_of_week':'0','hour':'0','minute':'0','second':'0'}
        with open(auto_start_dir, 'w', encoding='UTF-8') as stream:
            yaml.dump(setting_data, stream)
        public_i=0
        personal_i=12
        self.FileSubsystem={}
        for i in range(len(self.program_path)):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.program_path[i]+'/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #self.common_button[i].setIconSize(QtCore.QSize(int(60*scale),int(60*scale)))
            if "Public" in self.program_path[i]:
                #self.common_button[public_i]=add_color(self.common_button[public_i])
                self.FileSubsystem[self.common_button[public_i]]=self.program_path[i]
                self.common_button[public_i].setIcon(icon)
                self.common_button[public_i].clicked.connect(self.program_run)
                self.common_button[public_i].setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                self.common_button[public_i].customContextMenuRequested.connect(self.create_rightmenu)
                public_i+=1
            else:
                #self.common_button[personal_i]=add_color(self.common_button[personal_i])
                self.FileSubsystem[self.common_button[personal_i]] = self.program_path[i]
                self.common_button[personal_i].setIcon(icon)
                self.common_button[personal_i].clicked.connect(self.program_run)
                self.common_button[personal_i].setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                self.common_button[personal_i].customContextMenuRequested.connect(self.create_rightmenu)
                personal_i += 1
        for m in list(range(public_i,12))+list(range(personal_i,24)):
            self.common_button[m].setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.common_button[m].customContextMenuRequested.connect(self.create_rightmenu_none)

        self.path = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/'
        self.sysIcon = QIcon(self.path+'xiaozhi.ico')
        self.setWindowIcon(self.sysIcon)
        self.initUi()

        #此处设置程序快捷键
        # 2. 设置我们的自定义热键响应函数
        self.sigkeyhot.connect(self.KeypressEvent)
        # 3. 初始化两个热键
        self.hk_start, self.hk_stop = SystemHotkey(), SystemHotkey()
        # 4. 绑定快捷键和对应的信号发送函数
        self.hk_start.register(('control', 'q'), callback=lambda x: self.sendkeyevent("control+q"))
        self.hk_stop.register(('control', '8'), callback=lambda x: self.sendkeyevent("control+8"))

        self.python_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/Python38/'
        #此处写自动启动的程序，采用不阻塞的多线程管理
        #self.program_auto_run()
        #self.auto_run=Auto_Thread()
        #self.auto_run.start()
        self.tttrun()

        #整个软件的自启程序
        self.startupPath = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' % os.getlogin()
        if os.path.exists(self.startupPath +"xiaozhi.lnk"):
            self.startup.setText("取消自启")
        self.startup.triggered.connect(lambda:self.startup_pro())
        self.setting.triggered.connect(lambda: Sub_System_setting(self.path+'common/'))




        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去边框
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.focusWindowChanged.connect(self.tryy)
        #self.setWindowFlag(QtCore.Qt.Popup)    #Qt.FramelessWindowHint隐藏边框


    def tryy(self):
        print(1111111111)
    def startup_pro(self):
        # 整个软件自启程序
        su = startup()
        wn=worning()
        if self.startup.text()=="设置自启":
            bin_path = sys.argv[0].replace("\\", '/')
            link_path = "xiaozhi"
            desc = "小智助手"
            msg = su.Create_StartUp(bin_path, link_path, desc)
            if msg==True:
                self.startup.setText("取消自启")
                wn.message_worning("提示","软件已设置自启，将在下次开机自动启动！")

        elif self.startup.text()=="取消自启":
            msg = su.Destory_StartUp("xiaozhi")
            if msg==True:
                self.startup.setText("设置自启")
                wn.message_worning("提示", "软件已取消自启！")
        else:
            pass

     # 热键处理函数
    def KeypressEvent(self, i_str):
        if not self.program_setting_data['pause']:
            if self.isActiveWindow():
                self.hide()
            else:
                self.showNormal()
                self.activateWindow()
            # print("按下的按键是%s" % (i_str,))


    # 热键信号发送函数(将外部信号，转化成qt信号)
    def sendkeyevent(self, i_str):
        self.sigkeyhot.emit(i_str)


    def create_rightmenu(self):
        sender=self.sender()
        for i in range(len(self.common_button)):
            if sender==self.common_button[i]:
                print(i)
                # 菜单对象
                self.groupBox_menu = QMenu(self)
                self.actionC = QAction(QIcon('image/设置.png'), u'参数设置', self)
                self.groupBox_menu.addAction(self.actionC)
                # 获取自动启动设置，改变自启动状态
                setting_text = u'设置自启'
                self.actionA = QAction(QIcon('image/保存.png'), setting_text,
                                       self)  # self.actionA = self.contextMenu.addAction(QIcon("images/0.png"),u'|  动作A')
                self.actionA.setShortcut('Ctrl+S')  # 设置快捷键
                self.groupBox_menu.addAction(self.actionA)  # 把动作A选项添加到菜单
                self.actionD = QAction(QIcon('image/停止运行.png'), u'停止运行', self)
                self.groupBox_menu.addAction(self.actionD)
                if sender.styleSheet() == self.program_setting_data['StyleSheet_error']:
                    self.actionE = QAction(QIcon('image/停止运行.png'), u'打开错误日志', self)
                    self.groupBox_menu.addAction(self.actionE)
                    self.actionE.triggered.connect(lambda: self.Open_log(self.FileSubsystem[sender]))
                self.actionF = QAction(QIcon('image/停止运行.png'), u'打开程序所在位置', self)
                self.groupBox_menu.addAction(self.actionF)
                self.actionB = QAction(QIcon('image/删除.png'), u'删除', self)
                self.groupBox_menu.addAction(self.actionB)

                self.actionA.triggered.connect(
                    lambda: Sub_System_auto_run_setting(self.FileSubsystem[sender].split('/')[-2]))  # 将动作A触发时连接到槽函数 button
                self.actionB.triggered.connect(lambda: self.delete_program(self.FileSubsystem[sender]))
                self.actionC.triggered.connect(lambda: Sub_System_setting(self.FileSubsystem[sender]))
                self.actionF.triggered.connect(lambda: self.Open_dir(self.FileSubsystem[sender]))
                self.actionD.triggered.connect(
                    lambda: self.Sub_System_stop(self.FileSubsystem[sender].split('/')[-2]))
                self.groupBox_menu.popup(QCursor.pos())  # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以，

                break
    def create_rightmenu_none(self):
        sender=self.sender()
        for i in range(len(self.common_button)):
            if sender==self.common_button[i]:
                # 菜单对象
                self.groupBox_menu = QMenu(self)
                self.actionE = QAction(QIcon('image/设置.png'), u'添加应用', self)
                self.groupBox_menu.addAction(self.actionE)
                self.actionE.triggered.connect(lambda: self.add_new_pro(i))
                self.groupBox_menu.popup(QCursor.pos())  # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以，
                break
    def add_new_pro(self,num):
        try:
            dir=QtWidgets.QFileDialog.getOpenFileName(self,  "选取文件",'/'.join(sys.argv[0].replace("\\",'/').split('/')[:-1]) + '/', "All Files (*);;Text Files (*.txt)")
            pro=dir[0]
        except Exception as ex:
            print(ex)
        print(pro)
        type="Public" if num<12 else "Personal"
        pro_dir="/".join(pro.replace("\\","/").split('/')[:-1])+"/"
        pro_name=pro.replace("\\","/").split('/')[-1].split(".")[0]
        wn = worning()
        if ".py" in pro:
            if os.path.exists(pro_dir+"icon.png"):
                if not os.path.exists(self.path + type + "/" + pro_name):
                    os.mkdir(self.path + type + "/" + pro_name)
                shutil.copyfile(pro_dir+"icon.png",self.path+type+"/"+pro_name+"/icon.png")
                shutil.copyfile(pro.replace("\\","/"),self.path + type + "/" + pro_name + "/run.py")
                wn.tishi(f"应用【{pro_name}】已添加，重启小智后生效！")
            else:
                wn.tishi(f"该应用无图标，请设计一个图标以后再试！")
        elif ".exe" in pro:
            if not os.path.exists(self.path + type + "/" + pro_name):
                os.mkdir(self.path + type + "/" + pro_name)
            with open(self.path+type+"/"+pro_name+"/run.py","w+") as f:
                f.write("from subprocess import run\nrun(\""+pro+"\")")
            be=bulid_exe(pro,self.path+type+"/"+pro_name+"/icon.png")
            be.create_pro()
            wn.tishi(f"应用【{pro_name}】已添加，重启小智后生效！")
        else:
            wn.tishi(f"请选择正确的文件！")
    def set_auto_start(self,name):#设置程序自启动的文件
        print("yishezhizijqi",name)
        auto_start_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(auto_start_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        setting_data[name]=not setting_data[name]
        with open(auto_start_dir, 'w', encoding='UTF-8') as stream:
            yaml.dump(setting_data, stream)

    def Sub_System_stop(self,ss):
        print(self.subprocess_PID)
        try:
            pid = self.subprocess_PID[ss]
            process = psutil.Process(pid)
            for proc in process.children(recursive=True):
                proc.kill()
                process.kill()
        except:
            print(f"{ss}未启动")
    def Open_dir(self,path):
        os.startfile(path)

    def Open_log(self,path):
        run(r"C:\Windows\system32\notepad.exe "+path+"log_error.log")


    def delete_program(self,path):
        icon__path=path+'icon.png'
        os.rename(icon__path,path+'icon_delete.png')
        wn=worning()
        wn.tishi("应用已移除，重启小智后生效！")



    def program_run(self):
        self.hide()
        try:
            pyautogui.hotkey('ctrl', 'c')
        except KeyboardInterrupt:
            pass
        sender=self.sender()
        #index=self.common_button.index(sender)
        #print(index)

        if sender.styleSheet()==self.program_setting_data['StyleSheet_running']:
            wn=worning()
            wn.tishi("该应用正在运行，请勿重复启动！")
        else:
            ss = self.FileSubsystem[sender].split('/')[-2]
            try:
                scheduler = BackgroundScheduler()
                print(f"{ss}已启动")
                scheduler.add_job(self.job, args=(ss,'run',), id=ss, trigger='date', next_run_time=datetime.datetime.now())
                scheduler.start()
                # os.system('pythonw '+self.program_path[index]+'/run.pyw')
                # print(self.python_dir+'pythonw.exe '+self.FileSubsystem[sender]+'run.py')
                # run(self.python_dir+'pythonw.exe '+self.FileSubsystem[sender]+'run.py', shell=True)
            except Exception as ex:
                with open('except.txt', 'a+') as f:
                    f.write("主程序:" + str(ex))
                print(ex)




    def program_auto_run(self):
        auto_start_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(auto_start_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        with ThreadPoolExecutor(max_workers=1) as t:
            obj_list=[]
            for path in setting_data.keys():
                if setting_data[path]:
                    obj = t.submit(self.cmd_run_program, path)
                    print(11111111111111111111)
                    obj_list.append(obj)
            print(2222222)
        print(3)

    def cmd_run_program(self,path):
        dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/'
        python_dir = dir + 'Python38/'
        try:
            # os.system('pythonw '+self.program_path[index]+'/run.pyw')
            run(python_dir + 'pythonw.exe ' + dir + path + '/auto_run.py', shell=True)
        except Exception as ex:
            print(ex)


    def get_program(self):
        program_path = []
        public_file_dir = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1]) + '/Public/'
        for root, dirs, files in os.walk(public_file_dir):
            for dir in dirs:
                # print(dir)
                if os.path.exists(root + dir + '/icon.png'):
                    program_path.append(root + dir + '/')
        personal_file_dir = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1]) + '/Personal/'
        for root, dirs, files in os.walk(personal_file_dir):
            for dir in dirs:
                # print(dir)
                if os.path.exists(root + dir + '/icon.png'):
                    program_path.append(root + dir + '/')
        return program_path

    def tttrun(self):
        print("自启程序正在运行")
        auto_start_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(auto_start_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        scheduler = BackgroundScheduler()
        tishi_msg1 = "开机自启"
        tishi_msg2 = "定时启动"
        for ss in setting_data.keys():
            auto_run_setting = {}
            if setting_data[ss]['auto_run']:
                for x in setting_data[ss].keys():
                    if setting_data[ss][x] != '0' and type(setting_data[ss][x]) != bool:
                        auto_run_setting[x] = setting_data[ss][x]
                if auto_run_setting == {}:
                    tishi_msg1 = ss + '、' + tishi_msg1
                    scheduler.add_job(self.job, args=(ss,'auto_run',), id=ss, trigger='date',
                                      run_date=datetime.datetime.now() + datetime.timedelta(seconds=3))
                    #scheduler.add_listener()
                else:
                    print(f'开启定时任务【{ss}】')
                    tishi_msg2 = ss + '、' + tishi_msg2
                    scheduler.add_job(self.job, args=(ss,'auto_run',), id=ss, trigger='cron', **auto_run_setting)
        scheduler.start()
        wn = worning()
        wn.tishi(tishi_msg1 + '__' + tishi_msg2)

    def ChangeStyle(self,ss,code=None):
        for x in self.FileSubsystem.keys():
            if self.FileSubsystem[x].split('/')[-2]==ss:
                commonbutton=x
                break
        if code==None:
            commonbutton.setStyleSheet(self.program_setting_data['StyleSheet_running'])
            '''self.animation = QPropertyAnimation(commonbutton, b'color')
            self.animation.setDuration(2000)
            self.animation.setLoopCount(10)
            self.animation.setStartValue(255)
            self.animation.setKeyValueAt(0.5, 0)
            self.animation.setEndValue(255)
            self.animation.start()'''
        elif code==1:
            commonbutton.setStyleSheet(self.program_setting_data['StyleSheet_error'])
        else:
            commonbutton.setStyleSheet(self.program_setting_data['StyleSheet_end'])
        #commonbutton.setStyleSheet(self.program_setting['StyleSheet'])


    def job(self, ss,type):
        try:
            # os.system('pythonw '+self.program_path[index]+'/run.pyw')
            msg="未找到自启文件！"
            run_list1=['Public/' + ss + '/auto_run.py','Personal/' + ss + '/auto_run.py','Public/' + ss + '/run.py','Personal/' + ss + '/run.py']
            run_list2 = [ 'Public/' + ss + '/run.py','Personal/' + ss + '/run.py', 'Personal/' + ss + '/auto_run.py','Public/' + ss + '/auto_run.py']
            run_list=run_list1 if type=='auto_run' else run_list2
            for run_file in run_list:
                if os.path.exists(self.path + run_file):
                    print('运行 ', self.python_dir + 'pythonw.exe ' + self.path +run_file)
                    self.ChangeStyle(ss)
                    start_up=subprocess.STARTUPINFO()
                    start_up.dwFlags=subprocess.CREATE_NEW_CONSOLE|subprocess.STARTF_USESHOWWINDOW
                    start_up.wShowWindow=subprocess.SW_HIDE
                    #False,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE
                    model = {"stdout": subprocess.PIPE, "stdin": subprocess.PIPE, "stderr": subprocess.PIPE}
                    #print(ss)
                    #if ss in self.program_setting_data["super_model"]:
                        #model = {}
                    msg = Popen(self.python_dir.replace(" ",'\" \"') + 'pythonw.exe ' + self.path.replace(" ",'\" \"') + run_file.replace(" ",'\" \"'),shell=True,startupinfo=start_up,creationflags=subprocess.CREATE_NO_WINDOW,**model)
                    self.subprocess_PID[ss]=msg.pid
                    stdout, stderr = msg.communicate()
                    # print('abcd',stderr)
                    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    pro_dir = self.path + run_file
                    with open('/'.join(pro_dir.split('/')[:-1]) + '/log_error.log', 'a+') as f:
                        f.write(now_time + ' ' + str(stderr) + '\n')
                    msg.wait()
                    self.ChangeStyle(ss, int(msg.returncode))
                    break
                else:
                    pass
        except Exception as ex:
            print(ex)
        self.showNormal()




    def initUi(self):

        #self.createMessageGroupBox()
        self.createTrayIcon()

        #mainLayout = QVBoxLayout()
        #mainLayout.addWidget(self.grpMessageBox)
        #self.setLayout(mainLayout)

        # 让托盘图标显示在系统托盘上
        self.trayIcon.show()
    # 创建托盘图标
    def createTrayIcon(self):
        text='启用小智(&P)' if self.program_setting_data['pause'] else '禁用小智(&P)'
        aRestore = QAction('恢复(&R)', self, triggered=self.showNormal)
        aRerun = QAction('重启小智(&S)', self, triggered=self.Rerun)
        self.aPause = QAction(text, self, triggered=self.Pause)
        aQuit = QAction('退出(&Q)', self, triggered=self.exit_pro)

        menu = QMenu(self)
        menu.addAction(aRestore)
        menu.addAction(aRerun)
        menu.addAction(self.aPause)
        menu.addAction(aQuit)


        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(self.sysIcon)

        self.trayIcon.setContextMenu(menu)
        self.trayIcon.messageClicked.connect(self.messageClicked)
        self.trayIcon.activated.connect(self.iconActivated)

    # 应用退出
    def exit_pro(self):
        QApplication.instance().quit()
        #sys.exit()
        self.trayIcon.hide()
        sys.exit()
        print('a'+1)

    def Rerun(self):
        QApplication.instance().quit()
        # sys.exit()
        self.trayIcon.hide()
        #sys.exit()
        # print('a'+1)
        print("正在重启")
        pro_dir = sys.argv[0].replace("\\", '/')
        run(self.python_dir + 'pythonw.exe ' + pro_dir, shell=True)

    def Pause(self):
        with open(self.program_setting_dir, 'r', encoding='UTF-8') as stream:
            self.program_setting_data = yaml.safe_load(stream)
        self.program_setting_data['pause']= not self.program_setting_data['pause']
        with open(self.program_setting_dir, 'w', encoding='UTF-8') as stream:
            yaml.dump(self.program_setting_data, stream)
        text='启用小智(&P)' if self.program_setting_data['pause'] else '禁用小智(&P)'
        self.aPause.setText(text)
        wn=worning()
        if self.program_setting_data['pause']:
            wn.tishi("小智已禁用！")
        else:
            wn.tishi("小智已启用！")

    # 关闭事件处理, 不关闭，只是隐藏，真正的关闭操作在托盘图标菜单里
    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            #QMessageBox.information(self, '系统托盘',
                                    #'程序将继续在系统托盘中运行，要终止本程序，\n''请在系统托盘入口的上下文菜单中选择"退出"')
            self.hide()
            event.ignore()

    def messageClicked(self):
        QMessageBox.information(None, '系统托盘',
                                '对不起，我已经尽力了。'
                                '也许你应该试着问一个人?')

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.DoubleClick, QSystemTrayIcon.MiddleClick):
            self.showNormal()

class add_color(QToolButton):
    def __init__(self, parent=None):
        super(add_color, self).__init__(parent)

    def _set_color(self, value):
        color = 'border: 1px solid rgba(255, 0, 0, %s);' % value
        self.setStyleSheet(color)

    color = pyqtProperty(int, fset=_set_color)


from apscheduler.schedulers.background import BackgroundScheduler
#定义一个线程类
class Auto_Thread(QThread):
    #自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    #finishSignal = pyqtSignal(str)

    # 带一个参数t
    def __init__(self,parent=None):
        super(Auto_Thread, self).__init__(parent)
        self.dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/'
        self.python_dir = self.dir + 'Python38/'
    #run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        print("自启程序正在运行")
        auto_start_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(auto_start_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        scheduler=BackgroundScheduler()
        tishi_msg1="开机自启"
        tishi_msg2="定时启动"
        for ss in setting_data.keys():
            auto_run_setting= {}
            if setting_data[ss]['auto_run']:
                for x in setting_data[ss].keys():
                    if setting_data[ss][x] != '0' and type(setting_data[ss][x])!=bool:
                        auto_run_setting[x]=setting_data[ss][x]
                if auto_run_setting== {}:
                    tishi_msg1 = ss+'、'+tishi_msg1
                    scheduler.add_job(self.job,args=(ss,),id=ss,trigger='date',run_date=datetime.datetime.now()+datetime.timedelta(seconds=10))
                    #scheduler.add_listener()
                else:
                    print(f'开启定时任务【{ss}】')
                    tishi_msg2 = ss + '、' + tishi_msg2
                    print(auto_run_setting)
                    scheduler.add_job(self.job,args=(ss,),id=ss,trigger='cron',**auto_run_setting)
        scheduler.start()
        wn=worning()
        wn.tishi(tishi_msg1+'__'+tishi_msg2)

    def job(self,ss):
        try:
            # os.system('pythonw '+self.program_path[index]+'/run.pyw')
            if os.path.exists(self.dir +'Public/'+ ss + '/auto_run.py'):
                print('自启运行 ', self.python_dir + 'pythonw.exe ' + self.dir +'Public/'+ ss + '/auto_run.py')
                run(self.python_dir + 'pythonw.exe ' + self.dir +'Public/'+ ss + '/auto_run.py', shell=True)
            elif os.path.exists(self.dir +'Personal/'+ ss + '/auto_run.py'):
                print('自启运行 ', self.python_dir + 'pythonw.exe ' + self.dir + 'Personal/' + ss + '/auto_run.py')
                run(self.python_dir + 'pythonw.exe ' + self.dir +'Personal/'+ ss + '/auto_run.py', shell=True)
                
            else:
                print("未找到自启文件！")
                pass
        except Exception as ex:
            print(ex)




from tkinter import *
class Sub_System_setting:
    def __init__(self,dir):
        self.dir = dir
        print(self.dir)
        #pro_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/' + self.dir
        if os.path.exists(self.dir + 'setting.yaml'):
            self.root = Tk()
            self.root.title('设置参数')
            with open(self.dir + 'setting.yaml', 'r', encoding='UTF-8') as stream:
                setting_data = yaml.safe_load(stream)
            i = 0
            self.keys = setting_data.keys()
            self.data = {}
            for x in self.keys:
                la1 = Label(self.root, text=x)
                la1.grid(row=i, column=0, padx=(10, 0), pady=10)  # 0行0列
                en1 = Entry(self.root)  # 用户名文本框
                en1.insert(0, setting_data[x])
                en1.grid(row=i, column=1, columnspan=2, padx=(0, 10), ipadx=60)
                # 0行1列，跨2列
                self.data[x] = {'label': la1, 'entry': en1, 'type': type(setting_data[x])}
                i += 1

            but1 = Button(self.root, text="确定", command=self.setting)
            but1.grid(row=len(setting_data.keys()), column=1, padx=(30, 0), pady=10, ipadx=30)
            but2 = Button(self.root, text="取消", command=self.root.destroy)
            but2.grid(row=len(setting_data.keys()), column=2, padx=(0, 30), ipadx=30)
            self.root.resizable(False, False)
            screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
            screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
            width = 422  # 设定窗口宽度
            height = 45*(i+2) # 设定窗口高度
            left = (screenWidth - width) / 2
            top = (screenHeight - height) / 2

            # 宽度x高度+x偏移+y偏移
            # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
            self.root.geometry(f"+{int(left)}+{int(top)}")
            self.root.mainloop()
        else:
            wn = worning()
            wn.message_worning("提示", "此应用无设置文件！")


    def setting(self):
        #pro_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/'+self.dir
        with open(self.dir+'setting.yaml', 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)

        new_satting_data={}
        for x in self.data.keys():
            if self.data[x]['type']==bool:
                new_satting_data[x]=False if int(self.data[x]['entry'].get())==0 else True
            elif self.data[x]['type']==int:
                new_satting_data[x] = int(self.data[x]['entry'].get())
            elif self.data[x]['type']==float:
                new_satting_data[x] = float(self.data[x]['entry'].get())
            else:
                new_satting_data[x] = self.data[x]['entry'].get()

        if new_satting_data != setting_data:
            with open(self.dir+'setting.yaml', 'w', encoding='UTF-8') as stream:
                yaml.dump(new_satting_data, stream)

            wn = worning()
            wn.message_worning("提示", "配置已修改！")
        self.root.destroy()



    def exit_sys(self):
        self.root.quit()

class Sub_System_auto_run_setting:
    def __init__(self,dir):
        self.dir = dir
        print(self.dir)
        pro_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(pro_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        if self.dir in setting_data.keys():
            self.root = Tk()
            self.root.title('设置参数')
            auto_run=setting_data[self.dir]
            i = 0
            keys = auto_run.keys()
            self.data = {}
            for x in keys:
                la1 = Label(self.root, text=x)
                la1.grid(row=i, column=0, padx=(10, 0), pady=10)  # 0行0列
                en1 = Entry(self.root)  # 用户名文本框
                en1.insert(0, auto_run[x])
                en1.grid(row=i, column=1, columnspan=2, padx=(0, 10), ipadx=60)
                # 0行1列，跨2列
                self.data[x] = {'label': la1, 'entry': en1, 'type': type(auto_run[x])}
                i += 1

            but1 = Button(self.root, text="确定", command=self.setting)
            but1.grid(row=len(setting_data.keys()), column=1, padx=(30, 0), pady=10, ipadx=30)
            but2 = Button(self.root, text="取消", command=self.root.destroy)
            but2.grid(row=len(setting_data.keys()), column=2, padx=(0, 30), ipadx=30)
            self.root.resizable(False, False)
            screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
            screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
            width = 422  # 设定窗口宽度
            height = 45 * (i + 2)  # 设定窗口高度
            left = (screenWidth - width) / 2
            top = (screenHeight - height) / 2

            # 宽度x高度+x偏移+y偏移
            # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
            self.root.geometry(f"+{int(left)}+{int(top)}")
            self.root.mainloop()
        else:
            new_setting_data={'auto_run':False,'year':'0','month':'0','day':'0','week':'0','day_of_week':'0','hour':'0','minute':'0','second':'0'}
            setting_data[self.dir]=new_setting_data
            with open(pro_dir, 'w', encoding='UTF-8') as stream:
                yaml.dump(setting_data, stream)
            wn = worning()
            wn.message_worning("提示", "此应用无设置文件！再次点击重新设置")
            self.__init__(self.dir)


    def setting(self):
        pro_dir = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/auto_start.yaml'
        with open(pro_dir, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        new_satting_data={}
        for x in self.data.keys():
            if self.data[x]['type']==bool:
                new_satting_data[x]=False if int(self.data[x]['entry'].get())==0 else True
            elif self.data[x]['type']==int:
                new_satting_data[x] = int(self.data[x]['entry'].get())
            elif self.data[x]['type']==float:
                new_satting_data[x] = float(self.data[x]['entry'].get())
            else:
                new_satting_data[x] = self.data[x]['entry'].get()

        if new_satting_data != setting_data[self.dir]:
            setting_data[self.dir]=new_satting_data
            with open(pro_dir, 'w', encoding='UTF-8') as stream:
                yaml.dump(setting_data, stream)

            wn = worning()
            wn.message_worning("提示","自启配置已修改！")
        self.root.destroy()



    def exit_sys(self):
        self.root.quit()
from PIL import ImageDraw,Image,ImageFont
class bulid_exe():
    def __init__(self,path,save_icon):
        self.path=path.replace("\\","/")
        self.save_icon=save_icon
    def Get_exe_icon(self):
        large, small = win32gui.ExtractIconEx(self.path, 0)
        win32gui.DestroyIcon(small[0])
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), large[0])
        hbmp.SaveBitmapFile(hdc, '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1])+"/common/pic/save.png")
        # ============1.打开图片============
        img = Image.open('/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1])+"/common/pic/save.png")
        # ============2.处理图片============
        # 将图片分成小方块
        img_array = img.load()
        # 遍历每一个像素块，并处理颜色
        width, height = img.size  # 获取宽度和高度
        for x in range(0, width):
            for y in range(0, height):
                rgb = img_array[x, y]  # 获取一个像素块的rgb
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                tt = 10
                if r < tt and g < tt and b < tt:  # 判断规则
                    img_array[x, y] = (255, 255, 255)

        # ============3.保存图片============
        return img

    # 图片背景透明化
    def transPNG(self,img):
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = list()
        for item in datas:
            if item[0] > 220 and item[1] > 220 and item[2] > 220:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        print(222, img.size)
        img = img.resize((150, 150))
        print(111, img.size)
        return img

    # 图片融合
    def mix(self,img1, img2, coordinator):
        im = img1
        mark = img2
        layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        layer.paste(mark, coordinator)
        out = Image.composite(layer, im, layer)
        return out
    def create_pro(self):
        img=self.Get_exe_icon()
        verse = self.transPNG(img)
        file = Image.open('/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1])+'/common/pic/icon.png')
        draw = ImageDraw.Draw(file)
        font = ImageFont.truetype('/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1])+"/common/pic/msyh.ttc", 50)
        name = self.path.split("/")[-1].split(".")[0]
        w = font.getlength(name)
        draw.text((int(147 - w / 2), 200), name, (0, 0, 0), font=font)
        file.resize((100, 100))
        x1 = verse.size[0]
        x2 = file.size[0]
        co = (int((x2 - x1) / 2), int((x2 - x1) / 2 * 0.7))
        file = self.mix(file, verse, co)
        file.save(self.save_icon)