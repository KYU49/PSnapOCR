import cv2
import os
import sys
import numpy as np
import glob
import datetime

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

    # ハイスコア画像のファイル名保存
    highImg = []
    for i in range(214):
        highImg.append(["", "", "", ""])

    with open("./" + ymdhms + "_detail.csv", "w") as f:
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
                highImg[zukanNo - 1][starNum - 1] = os.path.split(t)[1]
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
    
    # cs書き出し用
    with open("./" + ymdhms + "_cs-script.txt", "w", encoding="utf-8") as f:
        f.write("* Score upload tool\n")
        f.write("Open Cyberscore by Chrome or Firefox of PC (Not IE or Safari)\n")
        f.write("https://cyberscore.me.uk/game/2785\n")
        f.write("Click \"+ Submit records\"\n")
        f.write("Check \"1★ Photos\" and click \"Edit selected records\"\n")
        f.write("Set \"Plat form:\" to \"Switch\".\n")
        f.write("Open Developer Tools (If enabled, F12) -> Open \"Console\" tab.\n")
        f.write("Copy the below codes and paste the console (Attention is shown if Firefox).\n")
        f.write("Click \"Save changes\"\n")
        f.write("Repeat  for \"2★ Photos\", \"3★ Photos\", \"4★ Photos\"\n\n")

        f.write("a=[")
        for i in range(len(result[0])):
            f.write("[")
            for j in range(len(result)):
                f.write(str(result[j][i]))
                f.write(",")
            f.write("0],")   # 面倒なので、,が残らないように0を入れておく
        f.write("[]")   # 面倒なので、,が残らないように空配列を入れておく

        f.write("];for(p=0;p<214;p++){for(s=0;s<4;s++){e=document.getElementsByName((464550+p+s*214)+'-input1')[0];if(e){e.value=a[s][p];}}}\n\n")
        f.write("* Proofs upload tool\n")
        f.write("Use FireFox or Chrome\n")
        f.write("Open \"Submit proofs\" -> \"Upload proofs from your device\"\n")
        f.write("-> Open \"Developer tool\" in your browser (F12 key)\n")
        f.write("-> Open \"Console\" tab -> Copy & paste the below codes\n")
        f.write("-> File button is shown below the navigation bar (Home, Games, Scoreboards, The site, Forum, Search[])\n")
        f.write("-> Upload all of images in \"images\" directory\n")
        f.write("-> Appropriate files are input into each row.\n")
        f.write("-> Click each \"Upload proof\" button manually\n\n")
        f.write("let arr = {")
        for i in range(len(highImg)):
            for j in range(len(highImg[0])):
                if(highImg[i][j] != ""):
                    f.write(str(464550 + i + j * 214))
                    f.write(":\"")
                    f.write(str(highImg[i][j]))
                    f.write("\",")
        f.write("0:\"\"};fileInput = document.createElement(\"input\");fileInput.type = \"file\";fileInput.multiple = true;fileInput.addEventListener(\"change\", e => {const {files} = e.target;for(let i = 0; i < document.forms.length; i++){let tempForm = document.forms[i];if(!tempForm.chart_id){continue;}const id = tempForm.chart_id.value;if(id in arr){const input = tempForm.proof_file;const fileName = arr[id];for(let j = 0; j < files.length; j++){let file = files[j];if(file.name == fileName){const dt = new DataTransfer();dt.items.add(file);input.files = dt.files;break;}}}}}, false);const pageRoot = document.getElementById(\"pagefull\");pageRoot.insertBefore(fileInput, pageRoot.firstChild);\n")
        #TODO 自動でUpload proof押してくれるツール欲しいよね
        
def getStar(img):
    ## 星の数を検出
    # 切り出し img[top : bottom, left : right]
    img_stars = img[64 : 64 + 30, 199 : 199 + 122]

    # 中埋め
    cv2.floodFill(img_stars, None, (0, 0), (0, 0, 0), loDiff=(50, 50, 50), upDiff=(50, 50, 50), flags=(4 | cv2.FLOODFILL_FIXED_RANGE))

    ## 2値化
    threshold = 0
    _, img_binary = cv2.threshold(img_stars, threshold, 255, cv2.THRESH_BINARY)

    # 星の数を算出
    contours, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
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