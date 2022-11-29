import csv
import json
import os
# with open('./assets/data/dataset_list.csv', 'r') as f:
#      reader = csv.reader(f)
#      for row in reader:
#          print((row[4:]))

# txt to csv

def txt2csv(filename,csvfilename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            res=line.strip('\n').split("\t")
            with open(csvfilename, 'w', newline='') as csvfile:
                writer  = csv.writer(csvfile,delimiter='\t')
                writer.writerow(res)
            csvfile.close()
    f.close()

def change_pic_name():
    """
    图片的第一张删除了，因此其他的需要更改文件名，顺序依次前移一位
    """
    path='./assets/image/dataset_img/'
    for i in range(1,362):
        newname = str(i-1)+".jpg"
        os.rename(path+str(i)+".jpg", path+newname) 
def process_new_pic():
    """
    从361开始重新命名新的160张图片
    """
    path='./assets/image/new_160_pic/ori_160_pic/'
    start_num=361
    for filename in os.listdir(path):
        newname = str(start_num)+".png"
        os.rename(path+filename, path+newname)
        start_num+=1
# process_new_pic()
# change_pic_name()           
# --------------------------------------------------------------------
def create_new_dataset_json(ori_json,new_json):
    """
    由于删除了第一张图片，因此所有json中的id字段应该减去1
    """
    f = open(ori_json,'r',encoding='utf-8')
    web_cards = json.load(f)
    newlist=[]
    for item in web_cards:
        tempjson=item
        tempjson["id"]=item["id"]-1
        newlist.append(tempjson)
    with open(new_json,'w',encoding='utf-8') as file_obj:
        json.dump(newlist,file_obj,indent=4)
        
    return web_cards

def write_160_pic_json(ori_json,new_json):
    """
    将新添加的160张图片的json信息添加到.json文件，拼接之前的360张图片
    """
    f = open(ori_json,'r',encoding='utf-8')
    web_cards = json.load(f)
    newlist=[]
    for item in web_cards:
        tempjson=item
        newlist.append(tempjson)
    for i in range(361,521):
        tempjson={"id":i,"eg_title":"","eg_source":"massvis","eg_link":"http://massvis.mit.edu/"}
        newlist.append(tempjson)
    with open(new_json,'w',encoding='utf-8') as file_obj:
        json.dump(newlist,file_obj,indent=4)

# write_160_pic_json("./assets/json/video_dataset1.json","./assets/json/video_dataset2.json")
# cards=create_new_dataset_json('./assets/json/video_dataset.json','./assets/json/video_dataset1.json')
# --------------------------------------------------------------------
def write_dataset_to_csv():
    """
    把360+160的json格式数据写入到dataset_list.csv（网页上的下载页面的第二个文件）
    """
    read_path="./assets/json/website_dataset.json"
    write_path="./assets/data/dataset_list222.csv"
    f = open(read_path,'r',encoding='utf-8')
    web_cards = json.load(f)
    
    file_csv = open(write_path, 'w', encoding='utf-8',newline='')
    csv_writer=csv.writer(file_csv)
    csv_writer.writerow(["id","eg_source","eg_title","eg_link"])
    for item in web_cards:
         csv_writer.writerow([item["id"]+40,item["eg_source"],item["eg_title"],item["eg_link"]])
    f.close()
    file_csv.close()



write_dataset_to_csv()