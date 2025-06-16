import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import time

st.title('伝票・請求書OCR検証アプリ（POC）')

folder = "scanned_images"  # スキャナーの画像保存フォルダ

if not os.path.exists(folder):
    os.makedirs(folder)

uploaded_files = os.listdir(folder)

if st.button("最新ファイルをOCR処理"):
    if uploaded_files:
        latest_file = max([os.path.join(folder, f) for f in uploaded_files], key=os.path.getctime)
        
        img = cv2.imread(latest_file)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        st.image(img_rgb, caption='読み込み画像', use_column_width=True)
        
        # OCR処理
        text = pytesseract.image_to_string(img_rgb, lang='jpn')
        
        st.subheader('OCR結果')
        st.text_area("抽出されたテキスト", text, height=300)
        
        # サンプルチェック（POC向け単純例）
        if "合計" in text:
            st.success("「合計」のキーワードを検出しました。確認してください。")
        else:
            st.warning("「合計」のキーワードが見つかりません。要確認。")
    else:
        st.error("画像がまだありません。スキャンしてください。")
