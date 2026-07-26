import streamlit as st


st.set_page_config(
    page_title="課題3：コンフリクト練習",
    page_icon="⚡",
)

st.title("⚡ 課題3：コンフリクト練習")
st.write("異なるブランチで、下の conflict_message の行を別々に変更してください。")

# コンフリクト練習では、両方のブランチで次の1行を編集します。
conflict_message = "このメッセージを自分の好きな言葉に変更してください。"

st.info(conflict_message)
st.caption("同じ行を別々の内容に変更すると、マージ時にコンフリクトを体験できます。")
