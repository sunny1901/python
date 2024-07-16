import logging

# fmt

fmt1 = logging.Formatter(fmt=" %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
fmt2 = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s \t [%(module)s]:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
fmt3 = logging.Formatter(fmt="%(asctime)s - %(levelname)s \t [%(module)s]: %(message)s", datefmt='%Y-%m-%d %H:%M:%S')

# 预定义 handler 
console = logging.StreamHandler()
console.setFormatter(fmt1)

file1 = logging.FileHandler(filename='log-1.log', mode='a', encoding='utf-8')
file1.setFormatter(fmt2)

file2 = logging.FileHandler(filename='log-2.log', mode='a', encoding='utf-8')
file2.setFormatter(fmt2)
 
file3 = logging.FileHandler(filename='log-3.log', mode='a', encoding='utf-8')
file3.setFormatter(fmt3)

####################################################################

# 定义日志 , 级别
logger1 = logging.Logger(name='trace.class', level=logging.ERROR)
logger1.addHandler(console)
logger1.addHandler(file1)
logger1.addHandler(file2)
# logger1.removeHandler(file1)
# logger1.removeHandler(file2)

# 定义日志 
logger2 = logging.Logger(name='resutl.class', level=logging.INFO)
logger2.addHandler(file3)

####################################################################
# 写日志
logger1.info (msg='logger1 msg111')
logger1.error(msg='logger1 msg222')
logger1.log  (msg='logger1 msg333 log' , level=50)

# 写日志
logger2.info( 'resut info ')
logger2.error('resut info ')