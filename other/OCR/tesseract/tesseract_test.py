import pytesseract
from PIL import Image

# Tesseract OCRの言語データのパスを指定します
tesseract_lang_data = '--tessdata-dir "/usr/local/share/tessdata"'
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"


image_path = "../img/Screenshot 2023-05-20 at 7.40.54.png"  # ローカルの画像パス

# 画像を開く
image = Image.open(image_path)

# 画像から文字を抽出
text = pytesseract.image_to_string(image, lang="jpn")

# テキストファイルに出力
output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(text)

print(f"テキストを {output_file} に出力しました。")
