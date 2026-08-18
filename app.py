import streamlit as st


st.set_page_config(
    page_title="はじめての Streamlit アプリ",
    page_icon="🎉",
)

# タイトルと説明
st.title("🎉 はじめての Streamlit アプリ")
st.write("GitHub Desktop と Git の基本を学ぶためのサンプルアプリです。")

st.divider()

# セクション 1: ユーザーからの入力インタラクション
st.header("1. あなたの名前を教えてください")
user_name = st.text_input("お名前（ニックネーム可）:", "ゲスト")

if user_name:
    st.success(f"こんにちは、{user_name}さん！ Git の世界へようこそ！")

st.divider()

# セクション 2: ちょっとしたおまけ機能（スライダー）
st.header("2. 今日の気分を教えてください")
mood_level = st.slider("モチベーション度（1〜10）", 1, 10, 5)

if mood_level >= 8:
    st.balloons()
    st.write("🔥 絶好調ですね！この調子で進めましょう！")
elif mood_level >= 4:
    st.write("👍 いい感じです！楽しく学んでいきましょう。")
else:
    st.write("☕ 自分のペースでのんびりいきましょう〜。")

st.divider()

st.title("🛠️ 課題2：機能追加の実装例")
st.write("ボタン、チェックボックス、セレクトボックスを追加した例です。")

favorite_tool = st.selectbox(
    "使ってみたいGitツールを選んでください",
    ["GitHub Desktop", "コマンドライン", "両方"],
)

show_tip = st.checkbox("学習のヒントを表示する")
if show_tip:
    st.info("小さな変更ごとにコミットすると、変更履歴を確認しやすくなります。")

if st.button("選択内容を表示"):
    st.success(f"「{favorite_tool}」を使って練習してみましょう！")

st.divider()
st.caption("このファイルを参考に、自分のブランチで新しい機能を追加してみましょう。")

# フッター
st.caption("© 2026 Git & GitHub Study Session")
