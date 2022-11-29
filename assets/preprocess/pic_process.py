import cv2

from PIL import Image
 

def process_width_600():
    """
    先将所有图片的宽处理成600
    """
    img_path="./assets/image/40pic/"
    out_path="./assets/image/new_40pic/"
    for i in range(-29,1):
        img = Image.open(img_path+str(i)+'.png')
        # img.convert('RGB')
        out = img.resize((600,int(600*img.size[1]/img.size[0])))
        # img=img.convert('RGB')
        out.save(out_path+str(i)+'.png')
        # crop_img = img[0:y1,0:x1]      #x0,y0为裁剪区域左上坐标；x1,y1为裁剪区域右下坐标
        # cv2.imwrite(save_path,crop_img)  #save_path为保存路径

def splic_pic():
    """
    再将所有图片处理成600*338
    截取最上半部分的图片
    """
    num=0
    img_path="./assets/image/new_40pic/"
    out_path="./assets/image/new2_40pic/"
    for i in range(-29,1):
        img = Image.open(img_path+str(i)+'.png')
        if img.size[1]>338:
            cropped = img.crop((0, 0, 600, 338))
        else:
            cropped = img.crop((0, 0, 600, 338))
            num=num+1
        cropped.save(out_path+str(i)+'.png')
    print(num)


def convert_pngtojpg():
    img_path="./assets/image/new2_40pic/"
    out_path="./assets/image/new3_40pic/"
    for i in range(-29,1):
        img = Image.open(img_path+str(i)+'.png')
        img = img.convert('RGB')
        img.save(out_path+str(i)+'.jpg')
# convert_pngtojpg()
# 427 444
# process_width_600()
# splic_pic()