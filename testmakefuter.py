import multiprocessing
import pandas as pd

# 特徴量作成関数
def createFeatureValue():
    for j in range(1):
            # 778:100
        for k in range(1):
            f = open('/home/spicy/Desktop/jupyter/jupyter_memo/log/' +
                     str(j).zfill(3)+'/'+str(k).zfill(3)+'.log')  # ファイル読み込み
            lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
            f.close()
            # lines: リスト。要素は1行の文字列データ

            # 日にち
            date = 0

            # COしてる占い師
            coSeerCount = 0

            # COしてる霊媒師
            coMediumCount = 0

            # Xの占い師CO順番
            coSeerOrder = 0

            # プレイヤ1〜15の特徴量配列
            num = i
            agentNum = 'agent' + str(i)
            agentNum = [dataFrame[if 3= 'estimate'][1][1:date], ]
            agent2 = []
            agent3 = []
            agent4 = []
            agent5 = []
            agent6 = []
            agent7 = []
            agent8 = []
            agent9 = []
            agent10 = []
            agent11 = []
            agent12 = []
            agent13 = []
            agent14 = []
            agent15 = []

            for line in lines:
                newLine = line.replace('\n', '').replace(' ', ',').split(',')

                if int(newLine[0]) !=  date:
                    date = int(newLine[0])

                if 
                



# マルチプロセス処理
if __name__ == '__main__':
    createFeatureValue()

    # プレイヤごとの特徴量を求める関数
    def agentList(agentId):

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

        # Xがプレイヤ1〜15に肯定発言をした数
        positive1 = 0
        positive2 = 0
        positive3 = 0
        positive4 = 0
        positive5 = 0
        positive6 = 0
        positive7 = 0
        positive8 = 0
        positive9 = 0
        positive10 = 0
        positive11 = 0
        positive12 = 0
        positive13 = 0
        positive14 = 0
        positive15 = 0

        # Xがプレイヤ1〜15に否定発言をした数
        denial1 = 0
        denial2 = 0
        denial3 = 0
        denial4 = 0
        denial5 = 0
        denial6 = 0
        denial7 = 0
        denial8 = 0
        denial9 = 0
        denial10 = 0
        denial11 = 0
        denial12 = 0
        denial13 = 0
        denial14 = 0
        denial15 = 0

        # Xがプレイヤ1〜15に投票していなかったら0、投票したら1
        vote1 = 0
        vote2 = 0
        vote3 = 0
        vote4 = 0
        vote5 = 0
        vote6 = 0
        vote7 = 0
        vote8 = 0
        vote9 = 0
        vote10 = 0
        vote11 = 0
        vote12 = 0
        vote13 = 0
        vote14 = 0
        vote15 = 0

        # 特徴量リスト
        FeatureValue = []

        return FeatureValue
