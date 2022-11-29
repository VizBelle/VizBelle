# 处理图片尾缀
import os
def re_name_s():
    path="./assets/image/back_carouse/"
    src_files = os.listdir(path)
    for single_chart in src_files:
        chart_files = os.listdir(os.path.join(path,single_chart))
        for file in chart_files:
            if file.split(".")[0]=="chart-marks":
                full_file_name = os.path.join(path, single_chart, file)
                end_file_name=os.path.join(path, single_chart,"chart-mark."+file.split(".")[1])
                os.rename(full_file_name,end_file_name)
            if file.split(".")[0]=="chart-legends":    
                full_file_name = os.path.join(path, single_chart, file)
                end_file_name=os.path.join(path, single_chart,"chart-legend."+file.split(".")[1])
                os.rename(full_file_name,end_file_name)

re_name_s()