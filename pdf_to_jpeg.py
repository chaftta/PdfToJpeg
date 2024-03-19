import os
import argparse
from pdf2image import convert_from_path
from pathlib import Path
from PIL import Image

def convert_pdf_to_images(pdf_path, base_name, digits, image_width, quality):
    print(f"PDFのパス:{pdf_path}")
    print(f"ベースファイル名:{base_name}")
    print(f"ページの桁数:{digits}")
    print(f"画像の横幅:{image_width}")
    print(f"品質:{quality}")
    # poppler/binのパスを取得
    poppler_path = Path(__file__).parent.absolute() / "poppler/bin"
    # ベースファイル名の指定が無い場合は、PDFのベースファイル名を使用する
    if base_name is None:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # PDFの画像化
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    # 画像を加工して保存
    for i, image in enumerate(images):
        page_number = str(i + 1).zfill(digits)
        output_file = f"{base_name}_{page_number}.jpg"

        # アスペクト比を維持しつつ横幅を1600ピクセルに固定
        width, height = image.size
        image_height = int(height * (image_width / width))
        resized_image = image.resize((image_width, image_height), Image.LANCZOS)
        resized_image.save(output_file, 'JPEG', quality=quality)

if __name__ == "__main__":
    # パラメータを取得
    parser = argparse.ArgumentParser(description="このスクリプトは、PDFをJPEG化するコマンドラインツールです")
    parser.add_argument("pdf_path", help="PDFのパス")
    parser.add_argument("--name", nargs='?', help="出力画像のベースファイル名")
    parser.add_argument("--digits", nargs='?', type=int, default=2, help="ページの桁数 (default: 2)")
    parser.add_argument("--quality", nargs='?', type=int, default=90, help="品質 (default: 90)")
    parser.add_argument("--width", nargs='?', type=int, default=1600, help="出力画像の横幅 (default: 1600)")
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        print(f"'{args.pdf_path}'のファイルがありません")
    else:
        convert_pdf_to_images(args.pdf_path, args.name, args.digits, args.width, args.quality)
        print("PDFの画像化が完了しました")
