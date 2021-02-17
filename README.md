# 名字DAI語逆変換器
<strike>TDN表記逆変換器</strike>

ysd→吉田等、名字の平仮名一字に対してアルファベットを当てる表記の逆変換器

## 使い方

1. webscraping.pyを実行し、名字ファイルを抜き出したnames.csvを取得。(アクセス負荷が予想されるため、使用は最小限でお願いします)

2. main.pyを調べたい名字とともに実行。

```
$ python main.py [検索する名字(小文字でも大文字でも可)]
```
(例)
```
$ python main.py ysd
吉田: よしだ
安田: やすだ
```

## 注意点
・名字ランキング1~1000位までの名字を登録しているため、実在する名字でも見つからない場合があります。

・酒井、境など、読みの一致している漢字は片方のみを採用しています。

・名字一覧は<a href = "https://namaeranking.com/?search=ランキング&tdfk=全国&namae=姓名">こちらのサイト</a>より引用しています。
