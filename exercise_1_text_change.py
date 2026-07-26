import streamlit as st


st.set_page_config(
    page_title="課題1：文字を変更する",
    page_icon="✏️",
)

# 課題1：次の2つの文字列を好きな内容に変更してください。
page_title = "✏️ 課題1：はじめての文字変更"
welcome_message = "この文章を、自分の好きなメッセージに変更してみましょう！"

st.title(page_title)
st.write(welcome_message)

st.divider()
st.info("変更できたら、ファイルを保存してアプリ画面を確認しましょう。")
st.caption("次は変更内容をコミットし、Gitの履歴に残してみましょう。")
