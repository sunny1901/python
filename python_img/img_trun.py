from PIL import Image

path = "F:\\sunny\\照片\\1.webp"
# path = "F:\\sunny\\face.jpg"
path2 = "F:\\sunny\\照片\\2.jpg"
def webp_to_jpg(input_path, output_path):
    try:
        # 打开WebP图像
        image = Image.open(input_path)

        # 保存为JPEG格式
        image.convert('RGB').save(output_path, 'JPEG')

        print('Conversion successful.')
    except Exception as e:
        print('Conversion failed:', str(e))


def turn1():


    # 输入的WebP图像路径
    webp_path = path  # 替换为你的WebP图像路径

    # 输出的JPEG图像路径
    jpeg_path = path2  # 输出的JPEG图像路径

    # 将WebP转换为JPEG
    webp_to_jpg(webp_path, jpeg_path)


def turn2():

    im = Image.open(path)
    if im.mode == "RGBA":
        im.load()  # required for png.split()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
    save_name = path.replace('webp', 'jpg')
    im.save('{}'.format(save_name), 'JPEG')

turn1()