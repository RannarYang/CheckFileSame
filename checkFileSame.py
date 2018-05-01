import os  
import hashlib  
import logging  
import sys  
  
def logger():  
    """ 获取logger"""  
    logger = logging.getLogger()  
    if not logger.handlers:  
        # 指定logger输出格式  
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')  
        # 文件日志  
        file_handler = logging.FileHandler("test.log")  
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式  
        # 控制台日志  
        console_handler = logging.StreamHandler(sys.stdout)  
        console_handler.formatter = formatter  # 也可以直接给formatter赋值  
        # 为logger添加的日志处理器  
        logger.addHandler(file_handler)  
        logger.addHandler(console_handler)  
        # 指定日志的最低输出级别，默认为WARN级别  
        logger.setLevel(logging.INFO)  
    return logger  
  
def get_md5(filename):  
    m = hashlib.md5()  
    mfile = open(filename, "rb")  
    m.update(mfile.read())  
    mfile.close()  
    md5_value = m.hexdigest()  
    return md5_value  
  
def get_urllist():  
    urlList=[]  
    
    for parent,dirnames,filenames in os.walk('.'):
        for i in filenames:  
            path = os.path.join(parent, i)
            urlList.append(path)
    return  urlList  
  
if __name__ == '__main__':  
    log = logger()  
    md5List =[]  
    urlList =get_urllist()  
    md52Path = {}
    for a in urlList:  
        md5 =get_md5(a)  
        if (md5 in md5List):  
            # os.remove(a)  
            log.info("repeat: " + md52Path[md5] + '   ' +  a)  
        else:  
            md5List.append(md5)  
            md52Path[md5] = a