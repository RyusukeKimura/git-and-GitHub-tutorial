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

# フッター
st.caption("© 2026 Git & GitHub Study Session")
