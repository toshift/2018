# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    # サンプル数
    N = 100

    # 整数乱数配列を生成 0 ~ 100
    rx = np.random.rand(N) * 100

    # ヒストグラム
    _, bins = np.histogram(rx, N -1, [0,100])

    # グラフ表示
    plt.xlim(0, 100) # x軸
    plt.ylim(0, 100) # y軸
    plt.scatter(bins, rx)
    plt.xlabel("size", fontsize=20)
    plt.ylabel("RandomValue", fontsize=20)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()