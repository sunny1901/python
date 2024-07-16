import exifread
import re
import sys
import os
from os import stat
from PIL import Image
path = "F:\\sunny\\照片\\1.webp"
# path = "F:\\sunny\\face.jpg"
path = "F:\\sunny\\照片\\1.jpg"
path = "F:\\sunny\\照片\\2.jpg"

def read():
    GPS = {}
    date = ''
    f = open(path,'rb')
    contents = exifread.process_file(f)
    print(1)
    for key in contents:
        if key == "GPS GPSLongitude":
            print("经度: ", contents[key],contents['GPS GPSLatitudeRef'])
            print("纬度: ",contents['GPS GPSLatitude'],contents['GPS GPSLongitudeRef'])
            print("高度基准: ",contents['GPS GPSAltitudeRef'])
            print("海拔高度: ",contents['GPS GPSAltitude'])
        if re.match('Image Make', key):
            print('品牌信息: ' , contents[key])
        if re.match('Image Model', key):
            print('具体型号: ' , contents[key])
        if re.match('Image DateTime', key):
            print('拍摄时间: ' , contents[key])
        if re.match('EXIF ExifImageWidth', key):
            print('照片尺寸: ' , contents[key],'*',contents['EXIF ExifImageLength'])
        if re.match('Image ImageDescription',key):
            print('图像描述: ' , contents[key])

def read2():
    # # 读取彩色图片
    # img = cv2.imread(r'./t1.jpg')
    # # 获取图像形状
    # print(img.shape)

    from PIL import Image

    img = Image.open(path)
    imgSize = img.size  # 图片的长和宽
    print(imgSize)
    maxSize = max(imgSize)  # 图片的长边

    minSize = min(imgSize)  # 图片的短边
    print(maxSize, minSize)


def read3():
    from PIL import Image

    image_path = path
    try:
        # 打开图片
        with Image.open(image_path) as img:
            # 获取dpi
            dpi = img.info.get('dpi')
            print('dpi-A',dpi)

        img = Image.open(image_path)
        dpi = img.info['dpi']
        print('dpi', dpi[0])
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def read4():

    statinfo = stat(path)
    print(statinfo)  # 属性
    print(statinfo.st_size)  # 大小字节
    print('%.3f' % (statinfo.st_size / 1024 / 1024))  # 大小M


def getFileProperties(fname):
    import win32api
    """
    读取给定文件的所有属性, 返回一个字典.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
                 'CompanyName', 'LegalCopyright', 'ProductVersion',
                 'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                 'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                                                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                                                fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            ## print str_info
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except Exception as e:
        print("无法打开图像:", str(e))


def read5():
    getFileProperties(path)



def get_image_properties(image_path):
        if not os.path.isfile(image_path):
            print("文件不存在")
            return

        try:
            image = Image.open(image_path)
            properties = {
                "文件路径": image_path,
                "图像格式": image.format,
                "图像模式": image.mode,
                "图像大小": image.size,
                "图像信息": image.info
            }
            return properties
        except Exception as e:
            print("无法打开图像:", str(e))

def read6():

    image_path = path
    image_properties = get_image_properties(image_path)

    if image_properties:
        print("图像属性:")
        for key, value in image_properties.items():
            print(f"{key}: {value}")

def read7():
    from PIL import Image

    # 图像文件路径
    image_path = path

    # 打开图像文件
    img = Image.open(image_path)

    # 获取图像尺寸
    width, height = img.size

    # 获取图像格式
    image_format = img.format

    # 获取其他属性，例如dpi和颜色模式
    dpi = img.info.get('dpi')
    color_mode = img.mode

    # 关闭图像文件
    img.close()

    # 打印属性信息
    print(f"图像尺寸: {width} x {height} 像素")
    print(f"图像格式: {image_format}")
    print(f"DPI: {dpi}")
    print(f"颜色模式: {color_mode}")

def read8():
    import os
    import win32file
    import win32con

    def get_file_properties(file_path):
        try:
            # 获取文件属性
            file_info = win32file.GetFileAttributes(file_path)

            # 获取文件大小
            file_size = os.path.getsize(file_path)

            # 获取文件分辨率
            # 这里只是演示，实际获取分辨率需要使用专门的图像处理库
            resolution = "Not available"

            # 获取文件修改时间
            modification_time = os.path.getmtime(file_path)

            # 将文件修改时间转换为可读格式
            modification_time_readable = str(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time)))

            # 返回文件属性
            return {
                'File Path': file_path,
                'File Size (bytes)': file_size,
                'Resolution': resolution,
                'Modification Time': modification_time_readable,
                'Attributes': file_info
            }
        except Exception as e:
            return str(e)

    # 图片路径
    image_path = path  # 替换为你的图片路径

    # 获取图片属性
    image_properties = get_file_properties(image_path)

    # 打印图片属性
    for key, value in image_properties.items():
        print(f'{key}: {value}')


# read()
#
# read2()
#
read3()
#
# read4()
#
# read5()
#
# read6()

# read7()
# read8()