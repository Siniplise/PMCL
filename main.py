# import LogHandler


from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import LoggingHandler as LGH

# import PyqtGui


LGH.Log_Main.info("PyQt5调用")

# import Main


import minecraft_launcher_lib as mclib
import subprocess
import sys
import uuid

LGH.Log_Main.info("主模块调用")

# Define Path

from res.MainWindowGui import Ui_MainWindow
import res.res_rc

user_name = "None"
user_uuid = "None"
user_password = "None"
f_skin = "None"
selected_version = "None"
java_dir = "None"
minecraft_dir = "None"
j_xms = 0
j_xmx = 0
installed_versions = mclib.utils.get_installed_versions("C:\\Users\\zam\\AppData\\Roaming\\.minecraft")

# Check File

# try:
#     if os.access(resPath,mode=os.R_OK):
#         LGH.Log_Main.info(f"找到:{resPath}")
#     else:
#         LGH.Log_Main.critical(f"文件未找到: \"{resPath}\"!")
#         sys.exit(1)
#     if os.access(guiPath,mode=os.R_OK):
#         LGH.Log_Main.info(f"找到文件:{guiPath}")
#     else:
#         LGH.Log_Main.critical(f"文件未找到: \"{guiPath}\"!")
#         sys.exit(1)
#     if os.access(userpatch,mode=os.R_OK):
#         LGH.Log_Main.info(f"找到文件:{userpatch}")
#     else:
#         LGH.Log_Main.critical(f"文件未找到: \"{userpatch}\"!")
#         sys.exit(1)
#     if os.access(database,mode=os.R_OK):
#         LGH.Log_Main.info(f"找到文件:{database}")
#     else:
#         LGH.Log_Main.warning(f"文件未找到: \"{database}\"!正在创建...")
#         try:
#             with open("res\\user.json", "w") as FileEv:
#                 with open("res/database.json", "r") as MainFileEv:
#                     MainFileDic = json.load(MainFileEv)
#                     FileEv_Data = MainFileDic["user"]
#                     json.dump(FileEv_Data, FileEv)
#                     LGH.Log_Main.info(f"创建成功!{database}")
#         except Exception:
#             LGH.Log_Main.critical(f"创建失败!:{database}")
#             sys.exit(1)
# except Exception:
#     pass

# def LoadProfile(filename):
#     global uid
#     global mcdir
#     global jdir
#     global xms
#     global xmx
#     global username
#     with open(filename, "r") as usercfg:
#         userload = json.load(usercfg)
#         uid = userload["uuid"]
#         mcdir = userload["mcdir"]
#         xmx = userload["xmx"]
#         xms = userload["xms"]
#         username = userload["name"]
#         jdir = userload["javadir"]
#     return userload
#
#
# def SaveProfile(filename):
#     with open(database) as mainfile:
#         with open(userpatch) as userfile:
#             mainev = json.load(mainfile)
#             maindat = mainev["user"]
#             maindat["javadir"] = jdir
#             maindat["mcdir"] = mcdir
#             maindat["name"] = username
#             maindat["uuid"] = uid
#             maindat["xms"] = xms
#             maindat["xmx"] = xmx
#             json.dump(maindat, userfile)
#     return maindat

class Main:
    def __init__(self, version):
        self.version = version

    def set_versions(self):
        global selected_version
        if selected_version == "1.12.2":
            selected_version = self.version
            LGH.Log_Main.info(f"启动版本设置为{selected_version}")
            return selected_version
        else:
            LGH.Log_Main.critical("版本切换失败!")
            print(Exception)
            sys.exit(1)

    def GetCommand(self):
        global Command
        try:
            uid = str(uuid.uuid4())
            option = {
                "username": user_name,
                "uuid": uid,
                "token": uid,
                "-Dminecraft.launcher.brand": "PMCL",
                "-Dminecraft.launcher.version": "1.0.0",
            }

            Command = mclib.command.get_minecraft_command(version=str(self.version),
                                                          minecraft_directory="C:\\Users\\zam\\AppData\\Roaming\\.minecraft",
                                                          options=option)
            LGH.Log_Main.info("命令已传递.")
        except Exception:
            pass
        return Command

    def Run(self):
        try:
            result = self.GetCommand()
            subprocess.Popen(result)
            LGH.Log_Main.info("已启动,请等待...")
        except Exception:
            return False

MainClass = Main(version="1.12.2")

try:
    class GUI(QMainWindow,Ui_MainWindow):
        def __init__(self,Parent=None):
            super(GUI,self).__init__(Parent)
            self.setupUi(self)
            global user_name
            global user_password
            global java_dir
            global minecraft_dir
            global j_xmx
            global j_xms
            global f_skin

            self.Main_Close.clicked.connect(self.MainWindow.close)
            self.Main_Mix.clicked.connect(self.MainWindow.showMinimized)
            self.Launch_Button.clicked.connect(lambda: MainClass.Run())
            user_name = self.Acount_Edit.text()
            user_password = self.Password_Edit.text()
            minecraft_dir = self.McDir_Edit.text()
            java_dir = self.JavaDir_Edit.text()
            j_xmx = self.Xmx_Edit.text()
            j_xms = self.Xms_Edit.text()

except Exception:
    LGH.Log_Main.critical("GUI构建失败!")
    print(Exception)
    sys.exit(1)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(mainWindow)
    mainWindow.show()

    LGH.Log_Main.info("GUI调用")

    sys.exit(app.exec_())
