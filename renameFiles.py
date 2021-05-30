import glob
import os
import sys
import cv2
import numpy as np
     
def main():
    # 拡張子.jpgのファイルを取得する
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = "./images/rename/"
     
    # ファイルを取得する
    flist = glob.glob(path + "*.jpg")
     
    # ファイル名を一括で変更する
    for i, file in enumerate(flist):
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        os.rename(file, path + str(getZukanNo(img)).zfill(3) + "-" + str(getStar(img)) + ".jpg")
        # 進捗
        sys.stdout.write("\r")
        sys.stdout.write("{}/{}".format(i, len(flist)))
        sys.stdout.flush()


def getStar(img):
    ## 2値化
    threshold = 150
    _, img_binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    ## 星の数を検出
    # 切り出し img[top : bottom, left : right]
    img_stars = img_binary[64 : 64 + 30, 199 : 199 + 122]
    # 中埋め
    cv2.floodFill(img_stars, None, (0,0), (0,0,0),flags=4)

    # 星の数を算出
    contours, _ = cv2.findContours(img_stars, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return len(contours)


def getZukanNo(img):
    # 特徴点抽出時に、余白がないとだめだから、その余白の大きさ
    yohaku = 10
    # 文字位置
    position = [725, 734, 743]
    widthNum = 10
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    descriptors = [
        np.load("./Descriptors/ZukanNo_0.npy"),
        np.load("./Descriptors/ZukanNo_1.npy"),
        np.load("./Descriptors/ZukanNo_2.npy"),
        np.load("./Descriptors/ZukanNo_3.npy"),
        np.load("./Descriptors/ZukanNo_4.npy"),
        np.load("./Descriptors/ZukanNo_5.npy"),
        np.load("./Descriptors/ZukanNo_6.npy"),
        np.load("./Descriptors/ZukanNo_7.npy"),
        np.load("./Descriptors/ZukanNo_8.npy"),
        np.load("./Descriptors/ZukanNo_9.npy")
    ]
    img = cv2.bitwise_not(img)

    imgs = []
    for i in range(len(position)):
        img_temp = img[144 : 161, position[i] : position[i] + widthNum ]
        img_temp = cv2.copyMakeBorder(img_temp, yohaku, yohaku, yohaku, yohaku, cv2.BORDER_CONSTANT,value=[255,255,255])
        imgs.append(img_temp)
    return predict(imgs, descriptors)
    
    
def predict(img, img_temp):
    result = 0
    threshold = 150
    for i, target in enumerate(img):
        predict = 0
        # 文字が存在するかの判定用に2値化
        _, isBlank = cv2.threshold(target, threshold, 255, cv2.THRESH_BINARY)
        if(np.any(cv2.bitwise_not(isBlank))):    # 文字があるかの判定
            score = 0
            for j, template in enumerate(img_temp):
                _, maxVal, _, _ = cv2.minMaxLoc(cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED))
                if(score < maxVal):
                    score = maxVal
                    predict = j
        result = result + predict * pow(10, len(img) - i - 1)
    return result


if __name__ == "__main__":
    main()