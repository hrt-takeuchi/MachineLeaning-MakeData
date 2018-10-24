import multiprocessing
import pandas as pd

# 特徴量作成関数


def createFeatureValue(saveDate):

    for j in range(594):
            # 778:100
        for k in range(100):
            f = open('/home/spicy/Desktop/jupyter/jupyter_memo/log/' +
                     str(j).zfill(3)+'/'+str(k).zfill(3)+'.log')  # ファイル読み込み
            lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
            f.close()
            # lines: リスト。要素は1行の文字列データ

            # 日にち
            date = 1

            # COしてる占い師
            coSeerCount = 0

            # COしてる霊媒師
            coMediumCount = 0

            # Xの占い師CO順番
            coSeerOrder = 0

            # Xの占い師CO順番
            coMediumOrder = 0

            # Xの人間占い発言数
            talkDivinationHuman = 0

            # Xの人狼占い発言数
            talkDivinationWerewolf = 0

            # Xの被人間占い回数
            DivinationedHuman = 0

            # Xの被人狼占い回数
            DivinationedWerewolf = 0

            # Xの生存状況(生存だと0死亡だと1)
            lifeOrDeath = 0

            # 処刑なら0, 襲撃なら1
            raidedOrNot = [0 for i in range(15)]

            # Xの発言と実際の投票変更数
            ChangeVotingPlace = 0

            # Xがプレイヤ1に肯定発言をした数
            positive1 = 0

            # Xがプレイヤ2に肯定発言をした数
            positive2 = 0

            # Xがプレイヤ3に肯定発言をした数
            positive3 = 0

            # Xがプレイヤ4に肯定発言をした数
            positive4 = 0

            # Xがプレイヤ5に肯定発言をした数
            positive5 = 0

            # Xがプレイヤ6に肯定発言をした数
            positive6 = 0

            # Xがプレイヤ7に肯定発言をした数
            positive7 = 0

            # Xがプレイヤ8に肯定発言をした数
            positive8 = 0

            # Xがプレイヤ9に肯定発言をした数
            positive9 = 0

            # Xがプレイヤ10に肯定発言をした数
            positive10 = 0

            # Xがプレイヤ11に肯定発言をした数
            positive11 = 0

            # Xがプレイヤ12に肯定発言をした数
            positive12 = 0

            # Xがプレイヤ13に肯定発言をした数
            positive13 = 0

            # Xがプレイヤ14に肯定発言をした数
            positive14 = 0

            # Xがプレイヤ15に肯定発言をした数
            positive15 = 0

            # Xがプレイヤ1に否定発言をした数
            denial1 = 0

            # Xがプレイヤ2に否定発言をした数
            denial2 = 0

            # Xがプレイヤ3に否定発言をした数
            denial3 = 0

            # Xがプレイヤ4に否定発言をした数
            denial4 = 0

            # Xがプレイヤ5に否定発言をした数
            denial5 = 0

            # Xがプレイヤ6に否定発言をした数
            denial6 = 0

            # Xがプレイヤ7に否定発言をした数
            denial7 = 0

            # Xがプレイヤ8に否定発言をした数
            denial8 = 0

            # Xがプレイヤ9に否定発言をした数
            denial9 = 0

            # Xがプレイヤ10に否定発言をした数
            denial10 = 0

            # Xがプレイヤ11に否定発言をした数
            denial11 = 0

            # Xがプレイヤ12に否定発言をした数
            denial12 = 0

            # Xがプレイヤ13に否定発言をした数
            denial13 = 0

            # Xがプレイヤ14に否定発言をした数
            denial14 = 0

            # Xがプレイヤ15に否定発言をした数
            denial15 = 0

            # Xがプレイヤ1に投票していなかったら0、投票したら1
            vote1 = 0

            # Xがプレイヤ2に投票していなかったら0、投票したら1
            vote2 = 0

            # Xがプレイヤ3に投票していなかったら0、投票したら1
            vote3 = 0

            # Xがプレイヤ4に投票していなかったら0、投票したら1
            vote4 = 0

            # Xがプレイヤ5に投票していなかったら0、投票したら1
            vote5 = 0

            # Xがプレイヤ6に投票していなかったら0、投票したら1
            vote6 = 0

            # Xがプレイヤ7に投票していなかったら0、投票したら1
            vote7 = 0

            # Xがプレイヤ8に投票していなかったら0、投票したら1
            vote8 = 0

            # Xがプレイヤ9に投票していなかったら0、投票したら1
            vote9 = 0

            # Xがプレイヤ10に投票していなかったら0、投票したら1
            vote10 = 0

            # Xがプレイヤ11に投票していなかったら0、投票したら1
            vote11 = 0

            # Xがプレイヤ12に投票していなかったら0、投票したら1
            vote12 = 0

            # Xがプレイヤ13に投票していなかったら0、投票したら1
            vote13 = 0

            # Xがプレイヤ14に投票していなかったら0、投票したら1
            vote14 = 0

            # Xがプレイヤ15に投票していなかったら0、投票したら1
            vote15 = 0

            

            for line in lines:
                newLine = line.replace('\n', '').replace(' ', ',').split(',')
                if newLine[0] == 0:
                    continue

                # 襲撃
                if newLine[1] == "attack" and newLine[3] == "true":
                    i = int(newLine[2]) - 1
                    raidedOrNot[i] = 2
                elif newLine[1] == "execute":
                    i = int(newLine[2]) - 1
                    raidedOrNot[i] = 1
        # print(str(j) + "フォルダ/" + str(k) + "週目")

    # マルチプロセス処理
    if __name__ == '__main__':
        jobs = []
        p = multiprocessing.Process(target=createFeatureValue)
        jobs.append(p)
        p.start()
