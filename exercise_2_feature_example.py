import streamlit as st


st.set_page_config(
    page_title="課題2：機能追加の実装例",
    page_icon="🛠️",
)

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
