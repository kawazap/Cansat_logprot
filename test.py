import csv
import pandas as pd
import numpy as np


lat = 0.0
lng = 0.0
yaw = 0.0

# 編集したいファイル（元ファイル）と
# 書き出し用のファイルを開く
with open("54.csv","r") as in_file, \
     open("output.csv","w") as out_file:
    # 書き出し用ファイルのヘッダーを記述
    out_file.write("lat,lng,control\n")

    # for文で1行ずつ取得
    for line in in_file.readlines():
        values = line.strip().split(",")
        if len(values) < 5:
            # カラムが少なすぎる不要なStateとかLogは飛ばす
            continue
        if values[0] == "MPU9250":
            if values[1] == "Yaw":
                # ヘッダーは飛ばす
                continue
            yaw = values[1]
        if values[0] == "GPS":
            if values[1] == "Sats":
                # ヘッダーは飛ばす
                continue
            lat = values[3]
            lng = values[4]
        if values[0] == "State":
            if lat == 0.0 and lng == 0.0 and yaw == 0.0:
                continue
            # 制御ループの最後でStateを吐いているので、このタイミングで吐く
            out_file.write(",".join([str(lat), str(lng), str(yaw)]) + "\n")
