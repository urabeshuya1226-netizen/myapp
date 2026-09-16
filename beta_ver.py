# お釣りゲーム(ターミナル版)
import random
# タイトル
print("= * 20")
print("お釣りゲーム")
print("= * 20")
# お題のリスト
list = [5, 10, 50, 100, 500]
# お題のランダムチョイス
odai = random.choice(list)
print(f"お題: {odai}円")
# お会計の金額をランダムに生成
kaikei = random.randint(100, 2000)
print(f"お会計: {kaikei}円")
# お支払い金額の入力
pay = int(input("お支払い額: "))
# お釣りの計算
oturi = pay - kaikei
print(f"お釣り: {oturi}円")
# お釣りがお題と一緒かどうかの判定
if oturi == odai:
    print("成功!")
else:
    print("失敗!")
