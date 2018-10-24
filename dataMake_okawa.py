import multiprocessing
import time
import datetime

#ラベル作成モジュール、特徴量作成モジュールをそれぞれ読み込み
import logToFeatureValue_okawa as LFV
import logToLabel_okawa as LL


def dataMake():
    # 日付を各ファイル名に追加
    now = datetime.datetime.now()
    today = "{0:%m%d}".format(now)
    saveLabelFile = './loglabel{0}.json'.format(today)
    saveFeatureValueFile ='./logfeaturevalue{0}.json'.format(today)

    # データの作成
    start = time.time()
    LFV.createFeatureValue(saveFeatureValueFile)
    dend = time.time()
    print ("特徴量作成時間:{0}".format(round(dend - start, 3)) + "[sec]")

    # ラベルデータの作成
    LL.createLabel(saveLabelFile)
    lend = time.time()
    print ("ラベル作成時間:{0}".format(round(lend - dend, 3)) + "[sec]")

    # 生成ファイルの要素数の比較
    proof(saveLabelFile, saveFeatureValueFile)
    end = time.time()
    print("処理合計：{0}".format(round(end-start,3))+ "[sec]")


#ラベル数と特徴量データ数の一致を確認する関数
def proof(saveLabelFile, saveFeatureValueFile):
    kyoshidata = open(saveLabelFile)
    kyoshidata2 = kyoshidata.readlines()
    kyoshidata.close()
    # print(kyoshidata2[0])
    kData = kyoshidata2[0].replace('\n','').split(', ')
    gakusyudata = open(saveFeatureValueFile)
    gakusyudata2 = gakusyudata.readlines()
    gakusyudata.close()
    gData = gakusyudata2[0].replace('[','').split('],')
    if len(gData) == len(kData):
        print("label:"+str(len(kData)) + "\nデータ:"+ str(len(gData)) + "\n合ってる")
    else:
        print("label:"+str(len(kData)) + "\nデータ:"+ str(len(gData)) +"\n行数が違うよ")

if __name__ == '__main__':
    jobs = []
    p = multiprocessing.Process(target=dataMake)
    jobs.append(p)
    p.start()
