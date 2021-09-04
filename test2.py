import csv
import sys
import pandas as pd
import numpy as np


lat = 0.0
lng = 0.0
yaw = 0.0

# 編集したいファイル（元ファイル）と
# 書き出し用のファイルを開く
with open("59.csv","r") as in_file, \
     open("output.csv","w") as out_file:
    # 書き出し用ファイルのヘッダーを記述
    out_file.write("lat,lng,control\n")

    i = 0
    # for文で1行ずつ取得
    for line in in_file.readlines():
        values = line.strip().split(",")
        if len(values) < 5:
            # カラムが少なすぎる不要なStateとかLogは飛ばす
            continue
        if values[0] == "State":
            if values[1] == "VehicleMode":
                continue
            lat += float(values[7])
            lng += float(values[8])
            yaw += float(values[9])
            i += 1
            if lat == 0.0 and lng == 0.0 and yaw == 0.0:
                continue
            if values[1] == 'Completed':
                break
            # 制御ループの最後でStateを吐いているので、このタイミングで吐く
            if i >= 10:
                out_file.write(",".join([str(lat/i), str(lng/i), str(yaw/i)]) + "\n")
                i = 0
                lat = 0.0
                lng = 0.0
                yaw = 0.0
