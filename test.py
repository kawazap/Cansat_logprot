import csv
import pandas as pd
import numpy as np
# 編集したいファイル（元ファイル）を開く
file = open("54.csv","r")
# 書き出し用のファイルを開く
out_file = open("output.csv","w")

# 書き出し用ファイルのヘッダーを記述
#out_file.write("lat,lng,control\n")

# 元ファイルのヘッダーをreadlineメソッドで１行飛ばす
for i in range(9):
    file.readline()
# 元ファイルのレコード部分をreadlinesメソッドで全行を読み取る
lines = file.readlines()

num = 0
# for文で1行ずつ取得
for line in lines:
    if num % 3 == 0: #MPU9250のデータから、 MyYawを取得
        # 改行コードをブランクに置換
        line = line.replace("\n","")
        # カンマ区切りでリストに変換する
        line = line.split(",")
        line = ','.join(line)
    elif num % 3 == 1: #GPUから座標を取得
        # 改行コードをブランクに置換
        line = line.replace("\n","")
        # カンマ区切りでリストに変換する
        line = line.split(",")
        line = ','.join(line)
    out_file.write(line)
    
    num += 1

# ２つのファイルを閉じる
file.close()
out_file.close()
