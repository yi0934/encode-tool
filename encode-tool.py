from tkinter import *
import hashlib
import time
import base64


LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        self.init_window_name.geometry('1068x681+10+10')

        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=12,command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_trans_to_sha1_button = Button(self.init_window_name, text="字符串转sha1", bg="lightblue", width=12,command=self.str_trans_to_sha1) 
        self.str_trans_to_sha1_button.grid(row=2, column=11)
        self.str_trans_to_base64_button = Button(self.init_window_name, text="字符串转base64", bg="lightblue", width=12,command=self.str_trans_to_base64) 
        self.str_trans_to_base64_button.grid(row=3, column=11)
        self.base64_trans_to_str_button = Button(self.init_window_name, text="base64转字符串", bg="lightblue", width=12,command=self.base64_trans_to_str) 
        self.base64_trans_to_str_button.grid(row=4, column=11)
        self.time_trans_button = Button(self.init_window_name, text="time转换", bg="lightblue", width=12,command=self.time_translation) 
        self.time_trans_button.grid(row=5, column=11)			
    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
    def str_trans_to_sha1(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        if src:
            try:
                myMd5 = hashlib.sha1()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_sha1 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转sha1失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_sha1 failed")
    def str_trans_to_base64(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        if src:
            try:
                myMd5_Digest = base64.b64encode(src)
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_base64 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转base64失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_base64 failed")
    def base64_trans_to_str(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5_Digest = base64.b64decode(src)
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:base64_trans_to_str success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"base64转字符串失败")
        else:
            self.write_log_to_Text("ERROR:base64_trans_to_str failed")
    def time_translation(self):
        src = self.init_data_Text.get(1.0,END).encode()
        if src:
            try:
                print (str(src)[2:-3],type(str(src)))
                if re.search(':',str(src)) or re.search('-',str(src)) :
                    timeArray = time.strptime(str(src)[2:-3], "%Y-%m-%d %H:%M:%S")
                    print (timeArray)
                    timestamp = time.mktime(timeArray)
                    print (timestamp)
                    dt =timestamp
                else:
                    a=int(src)
                    time_local = time.localtime(a)
                    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
                myMd5_Digest = dt
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:time_transation success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"time转换失败")
        else:
            self.write_log_to_Text("ERROR:time_translation failed")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          


gui_start()