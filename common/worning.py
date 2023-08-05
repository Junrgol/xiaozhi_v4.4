import tkinter
import tkinter.messagebox
import tkinter as tk
from PIL import Image, ImageTk
import sys

class worning:
    def message_worning(self,title='提示', message='一些提醒'):
        top = tkinter.Tk()
        top.withdraw()  # 实现主窗口隐藏(即隐藏带tk标题的空白窗口)
        top.update()  # 需要update一下
        if title == '提示':
            tkinter.messagebox.showinfo(title=title, message=message)  # 不管如何点击提示框（确定/关闭），返回值都是“ok”
        elif title == '警告':
            tkinter.messagebox.showwarning(title=title, message=message)
        elif title == '错误':
            tkinter.messagebox.showerror(title=title, message=message)
        else:
            tkinter.messagebox.showwarning(title=title, message=message)
        top.destroy()  # 销毁控件，释放内存

    def tishi(self,msg=""):
        root = tk.Tk()
        root.title("info")
        root.overrideredirect(True)
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        scale=width/1463
        t_w = int(250*scale)
        t_h = int(50*scale)
        root.attributes("-alpha", 1)
        color = "RoyalBlue"
        if 'main' in sys.argv[0]:
            path = '/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1]) + '/common/'
        else:
            path='/'.join(sys.argv[0].replace("\\", '/').split('/')[:-3])+'/common/'
        image = Image.open(path+'bggg.png').resize((t_w, t_h))
        image = ImageTk.PhotoImage(image)
        lbImage = tk.Label(root, image=image, text=msg, compound="center", fg="white",
                           font=("微软雅黑", int(10*scale), "bold"),wraplength=t_w)
        lbImage.pack(fill=tk.BOTH, expand=tk.YES)
        # tk.Label(root, text="This is a pop-up message",bg=color,fg="white",font=("微软雅黑", 10, "bold")).pack(side='bottom', fill='both', expand=True)
        x = int(width / 2 - t_w / 2)
        y = int(height * 0.9 - t_h / 2)
        root.configure(bg=color)
        root.geometry("%sx%s+%s+%s" % (str(t_w), str(t_h), str(x), str(y)))
        root.after(2000, lambda: root.destroy())  # time in ms
        root.mainloop()
