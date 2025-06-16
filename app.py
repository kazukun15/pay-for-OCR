import streamlit as st
import os
import cv2
from PIL import Image

# アプリ設定
st.set_page_config(page_title="伝票OCRアプリ（POC）", layout="wide")

# サイドバー操作エリア
st.sidebar.title("操作メニュー")
# スキャン画像保存フォルダの指定
folder = st.sidebar.text_input("スキャン画像保存フォルダ", value="scanned_images")
# フォルダがなければ作成
if not os.path.exists(folder):
    os.makedirs(folder)

# スキャンボタン
if st.sidebar.button("スキャン実行"):
    # フォルダ内の最新ファイルを取得
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if files:
        latest_file = max(
            [os.path.join(folder, f) for f in files],
            key=os.path.getctime
        )
        # 画像読み込み
        img = cv2.imread(latest_file)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # プレビュー表示
        st.subheader("スキャン画像 プレビュー")
        st.image(img_rgb, caption=os.path.basename(latest_file), use_column_width=True)
    else:
        st.sidebar.error("フォルダに画像がありません。スキャンしてください。")

# メインエリアにチュートリアル表示
st.title("伝票・請求書OCR検証アプリ（POC）")
st.write("サイドバーの『スキャン実行』ボタンを押して、スキャン画像のプレビューを表示します。")

# ここにOCR処理などの追加機能を実装可能
