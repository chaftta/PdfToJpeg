# pdf_to_jpeg

このツールは、PDFファイルをページ毎にJPEGにして保存するツールです。

使用には、以下の準備が必要です
- python3のインストール
- pdf2imageのインストール
	pip install pdf2image
- popplerのダウンロードしてこのディレクトリに配置する


## popplerのダウンロードと配置

githubからpopplerをダウンロードして、pdf_to_jpeg.pyのディレクトリから相対でpoppler/binにpopplerのexe達を配置します。

## 使い方

1. スクリプトの引数にPDFのファイルパスと出力ファイルのベースファイル名とページの桁数を指定します。  
	```
	python pdf_to_jpeg.py path/to/target.pdf [--name ベースファイル名] [--digits ページの桁数] [--width 出力画像の横幅] [--quality 品質]
	```
	ベースファイル名とページの桁数は省略が可能です。  

	省略すると以下の値が使用されます。  
	ベースファイル名：PDFのベースファイル名(上のコマンド例の場合"target"になります)  
	ページの桁数：2  
	出力画像の横幅：1600  
	品質：90  

