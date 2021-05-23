import cv2
import os
import sys
import numpy as np
import glob
import datetime

# conda install -c conda-forge tesseract
# conda install -c brianjmcguirk pyocr

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # ファイル名用に時刻取得
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    ymdhms = now.strftime("%Y%m%d%H%M%S")
    test =glob.glob("./images/*.jpg")
    
    # 結果入力の初期化
    result = []
    for i in range(214):
        result.append([0, 0, 0, 0])

    with open("./" + ymdhms + ".csv", "w") as f:
        # 画像読み込み
        for i, t in enumerate(test):
            img = cv2.imread(t, cv2.IMREAD_GRAYSCALE)
            zukanNo = getZukanNo(img)
            f.write(str(zukanNo))
            f.write(", ")
            starNum = getStar(img)
            f.write(str(starNum))
            f.write(", ")
            scoreSum = getScoreSum(img)
            f.write(str(scoreSum))
            if result[zukanNo - 1][starNum - 1] < scoreSum:
                result[zukanNo - 1][starNum - 1] = scoreSum
            for j in range(6):
                f.write(", ")
                f.write(str(getEachScores(img, j)))
            f.write("\n")
            # 進捗
            sys.stdout.write("\r")
            sys.stdout.write("{}/{}".format(i, len(test)))
            sys.stdout.flush()
    with open("./" + ymdhms + "_sum.csv", "w") as f:
        f.write("No, 1-Star, 2-Star, 3-Star, 4-Star\n")
        for i in range(len(result)):
            f.write(str(i + 1))
            for j in range(len(result[0])):
                f.write(", ")
                if(result[i][j] == 0):
                    f.write("")
                else:
                    f.write(str(result[i][j]))
            f.write("\n")

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

def getEachScores(img, row):
    # 特徴点抽出時に、余白がないとだめだから、その余白の大きさ
    yohaku = 10
    # 文字位置
    position = [1005, 1023, 1035, 1047]
    widthNum = 13
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    descriptors = [
        np.load("./Descriptors/ScoreSmall_0.npy"),
        np.load("./Descriptors/ScoreSmall_1.npy"),
        np.load("./Descriptors/ScoreSmall_2.npy"),
        np.load("./Descriptors/ScoreSmall_3.npy"),
        np.load("./Descriptors/ScoreSmall_4.npy"),
        np.load("./Descriptors/ScoreSmall_5.npy"),
        np.load("./Descriptors/ScoreSmall_6.npy"),
        np.load("./Descriptors/ScoreSmall_7.npy"),
        np.load("./Descriptors/ScoreSmall_8.npy"),
        np.load("./Descriptors/ScoreSmall_9.npy"),
    ]

    imgs = []
    for i in range(len(position)):
        img_temp = img[243 + int(row * 31.4) : 243 + int(row * 31.4) + 20, position[i] : position[i] + widthNum ]
        img_temp = cv2.copyMakeBorder(img_temp, yohaku, yohaku, yohaku, yohaku, cv2.BORDER_CONSTANT,value=[255,255,255])
        imgs.append(img_temp)
    return predict(imgs, descriptors)

def getScoreSum(img):
    # 特徴点抽出時に、余白がないとだめだから、その余白の大きさ
    yohaku = 10
    # 文字位置
    position = [968, 999, 1020, 1041]
    widthNum = 21
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    descriptors = [
        np.load("./Descriptors/ScoreLarge_0.npy"),
        np.load("./Descriptors/ScoreLarge_1.npy"),
        np.load("./Descriptors/ScoreLarge_2.npy"),
        np.load("./Descriptors/ScoreLarge_3.npy"),
        np.load("./Descriptors/ScoreLarge_4.npy"),
        np.load("./Descriptors/ScoreLarge_5.npy"),
        np.load("./Descriptors/ScoreLarge_6.npy"),
        np.load("./Descriptors/ScoreLarge_7.npy"),
        np.load("./Descriptors/ScoreLarge_8.npy"),
        np.load("./Descriptors/ScoreLarge_9.npy")
    ]

    imgs = []
    for i in range(len(position)):
        img_temp = img[199 : 233, position[i] : position[i] + widthNum ]
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