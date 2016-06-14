#!/usr/bin/env python
# coding: utf-8

"""
__doc__
特徴量抽出プログラム for HASC
"""
import csv
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import interp1d

print(__doc__)
__author__ = "Haruyuki Ichino"
__version__ = "0.1"
__date__ = "2016/05/13"

# データ格納ディレクトリ
inputDir = './data/'
# 結果の出力ファイル
out_fileList = './badFileList.txt'
out_personList = './badPersonList.txt'

# Const
th_std = 0.1  # ダメファイルを識別するための標準偏差のしきい値


# ==========================================================
# 関数
# ==========================================================

def checkFiles(file):
    """
    概要: する関数
    @param file:fileオブジェクト
    """

    # csvファイルからデータの読み込み
    data = np.loadtxt(file, delimiter=",")
    print("(行,列) =", data.shape)

    # 最初の0が続く部分を削除
    idx_rm0 = 0
    while data[0, 1] == 0:  # 一番上のx軸の値
        data = np.delete(data, 0, axis=0)
        idx_rm0 += 1
    print("Delete 0 value lines =", idx_rm0)

    # 有効なデータ(行)数のチェック
    dataLines = data.shape[0]  # ファイルデータの最下部のインデックス
    print("Total lines =", dataLines)
    TotalTime = data[dataLines - 1, 0] - data[0, 0]
    print("Total Time[s] = %f" % TotalTime)
    print()

    # # データの長さチェック
    # if TotalTime <= windowSize:
    #     # もしデータ全体が1windowSize分なければreturn
    #     return

    # ファイル名の取得
    fileName = file.split('/')[4]
    print("fileName = " + fileName)

    # 各軸のSTDを取得
    stdX = np.std(data[:, 1])
    stdY = np.std(data[:, 2])
    stdZ = np.std(data[:, 3])
    print("stdX = %f, stdY = %f, stdZ = %f" % (stdX, stdY, stdZ))

    if stdX > th_std or stdY > th_std or stdZ > th_std:
        print("このファイルはおかしい")

        return True


def createDir(dir_path):
    """
    概要: 指定のディレクトリがなければ作成する関数
    """
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


# ==========================================================
# 0. 準備
# ==========================================================

# 行動の種類をactions_lsitに追加し, 行動数をAction_countに入れる
actions = os.listdir(inputDir)

# Counter
accCount = 0
badFileCount = 0

# ファイル出力の準備
f1 = open(out_fileList, "w")
f2 = open(out_personList, "w")

# ==========================================================
# 1.データの読み込み & 特徴量抽出
# ==========================================================

# 行動ディレクトリでの処理
for action in actions:
    # .DS_Storeのチェック
    if action == ".DS_Store":
        continue

    input_action_dir = inputDir + action + '/'

    # ディレクトリじゃない場合はスキップ
    if not os.path.isdir(input_action_dir):
        continue

    # stayディレクトリだけを探索
    if action != "1_stay":
        continue

    print("=================================================")
    print(input_action_dir)
    print("=================================================")

    # 被験者別の処理
    persons = os.listdir(input_action_dir)

    for person in persons:

        # .DS_Storeのチェック
        if person == ".DS_Store":
            continue

        personOut_flag = False

        input_person_dir = input_action_dir + person + '/'

        # ディレクトリじゃない場合はスキップ
        if not os.path.isdir(input_person_dir):
            continue

        # 加速度ファイルリストの作成
        input_acc_files = glob.glob(input_person_dir + '*acc*')
        print("============================================")
        print(person)
        print("============================================")

        # 加速度ファイル別の処理
        for input_acc_file in input_acc_files:

            print("---------------------------------------")
            print(input_acc_file)
            print("---------------------------------------")

            # 各ファイルにアクセス
            if checkFiles(input_acc_file):
                # もし問題のあるファイルなら

                # 出力ファイルに書き込み
                f1.writelines(input_acc_file + "\n")
                if not personOut_flag:
                    f2.writelines(person + "\n")
                    personOut_flag = True

                badFileCount += 1

            accCount += 1
            # 各加速度ファイル処理の終了

            # 各person処理の終了
# 各行動への処理の終了

print()
print("問題のあるファイルの割合: %.2f (%d/%d)" % (badFileCount/accCount, badFileCount, accCount))


# ファイル出力の終了処理
f1.close()
f2.close()
