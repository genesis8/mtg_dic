
'''

[説明]

in_file には以下のようなデータが格納されている。

築地毅,つきじつよし
阿部裕司,あべゆうじ

out_file には in_file に格納されているヨミの部分文字列から
漢字に変換するための辞書登録データが出力される。

＠つ,築地毅
＠つき,築地毅
＠つきじ,築地毅
＠つきじつ,築地毅
＠つきじつよ,築地毅
＠つきじつよし,築地毅
＠あ,阿部裕司
＠あべ,阿部裕司
＠あべゆ,阿部裕司
＠あべゆう,阿部裕司
＠あべゆうじ,阿部裕司

WINDOWSのIME辞書登録ツールはtsvしか受け付けないので
サクラエディタで上記csvをtsv化してから使う事

'''

in_file = open("sample_in2.txt")

for line in in_file:
	[kanji,yomi] = line.strip().split(",")
	
	for i in range( 1 , len(yomi) + 1 ):
		print ( "＠" + yomi[0:i] + "," +"《"+ kanji + "》" + ",名詞" )
		
in_file.close()
