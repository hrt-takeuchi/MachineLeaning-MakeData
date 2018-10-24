import multiprocessing

#ラベル作成関数

def createLabel(saveDate):

    for j in range(594):
        for k in range(100):
            f = open('/home/spicy/Desktop/jupyter/jupyter_memo/log/'+str(j).zfill(3)+'/'+str(k).zfill(3)+'.log') #ファイル読み込み
            lines =f.readlines()# 1行毎にファイル終端まで全て読む(改行文字も含まれる)
            f.close()
            for line in lines:
                newLine = line.replace('\n','').replace(' ', ',').split(',')
            # lines: リスト。要素は1行の文字列データ

            lastday = int(newLine[0])
            label = [] #答えリスト15人
            finlabel = [] #答えリスト15人＊最終ゲーム日数
            for i in range(15):
                if "WEREWOLF" in lines[i]:
                    label.append(-1)
                else:
                    label.append(1)
            for i in range(int(lastday-1)):
                finlabel = finlabel + label
            file = open(saveDate, 'a')  #追加書き込みモードでオープン
            file.writelines(str(finlabel).replace('[', '').replace(']', '')+",")
            file.writelines(" ")
            file.close()


if __name__ == '__main__':
    jobs = []
    p = multiprocessing.Process(target=createLabel)
    jobs.append(p)
    p.start()
