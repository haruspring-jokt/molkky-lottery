import os
import random

def __main__(l_count):

    box = []
    # ファイルを読み込む
    with open("./entry.txt") as f:
        for s_line in f:
            # 抽選ボックスに入れる
            box.append(s_line.replace("\n", ""))

    # 確認用（本番ではコメントアウト）
    print(box)

    # 抽選ボックスの順番をシャッフルする
    random.shuffle(box)

    # print(box)
    
    # 指定回数分抽選ボックスを引く
    for i in range(l_count):
        print(box[i])



if __name__ == "__main__":
    __main__(7)
