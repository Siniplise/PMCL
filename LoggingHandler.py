import logging

import colorlog

# COLOR CONFIG
Color_MainConfig = {
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
# GET LOGGER

Log_LoggingHandler = logging.getLogger("LOGGER")
Log_LoggingHandler.setLevel(logging.DEBUG)

Log_Main = logging.getLogger("Main")
Log_Main.setLevel(logging.DEBUG)

# SET HANDLER

Log_LoggingHandler_Handler = logging.StreamHandler()
Log_LoggingHandler_Handler.setLevel(logging.DEBUG)

Log_Main_Handler = logging.StreamHandler()
Log_Main_Handler.setLevel(logging.DEBUG)


# CREATE FORMATTER

Log_Formatter = logging.Formatter(
    fmt='[%(asctime)s][%(filename)s][%(name)s][%(levelname)s] : %(message)s'
)

# GET COLOR

Log_Formatter_Color = colorlog.ColoredFormatter(
    fmt='%(log_color)s[%(asctime)s][%(filename)s][%(name)s][%(levelname)s] : %(message)s',
    log_colors=Color_MainConfig
)

# SET FORMATTER

Log_Main_Handler.setFormatter(Log_Formatter_Color)
Log_LoggingHandler_Handler.setFormatter(Log_Formatter_Color)


# PATCHES HANDLER

Log_Main.addHandler(Log_Main_Handler)
Log_LoggingHandler.addHandler(Log_LoggingHandler_Handler)


Log_LoggingHandler.info(msg="日志处理器构建完成")
