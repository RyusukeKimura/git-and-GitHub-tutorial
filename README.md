# 🚀 はじめての Streamlit アプリ

このリポジトリは、「GitHub Desktop から触って学ぶ Git & GitHub」勉強会用のサンプルプロジェクトです。

シンプルな Streamlit アプリを題材に、ファイルの編集、コミット、プッシュ、Pull Request、コンフリクト解消を体験できます。

## 🛠️ 事前準備

### Windows

1. [Python 公式サイトのダウンロードページ](https://www.python.org/downloads/windows/)から、Windows用のPythonインストーラーをダウンロードする
2. インストーラーを起動し、最初の画面で **Add python.exe to PATH** にチェックを入れてからインストールする
3. PowerShell またはコマンドプロンプトを開き、Pythonが使えることを確認する

```powershell
py --version
```

4. GitHub Desktopでこのリポジトリをクローンし、リポジトリのフォルダをPowerShellまたはコマンドプロンプトで開く
5. 依存ライブラリをインストールする

```powershell
py -m pip install -r requirements.txt
```

6. アプリを起動する

```powershell
py -m streamlit run app.py
```

> `py` コマンドが見つからない場合は、ターミナルを開き直してください。それでも動かない場合は `python` に読み替えて試してください。

### Mac

1. [Python 公式サイトのダウンロードページ](https://www.python.org/downloads/macos/)から、macOS用のPythonインストーラーをダウンロードする
2. ダウンロードした `.pkg` ファイルを開き、画面の案内に従ってインストールする
3. ターミナルを開き、Pythonが使えることを確認する

```bash
python3 --version
```

4. GitHub Desktopでこのリポジトリをクローンし、リポジトリのフォルダをターミナルで開く
5. 依存ライブラリをインストールする

```bash
python3 -m pip install -r requirements.txt
```

6. アプリを起動する

```bash
python3 -m streamlit run app.py
```

ブラウザが自動的に開かない場合は、ターミナルに表示される URL へアクセスしてください。

## 📚 ワークショップ課題

### 課題 1：文字を変更する

練習用の `exercise_1_text_change.py` を開き、`page_title` と `welcome_message` を好きな内容へ変更してコミットしてみましょう。

次のコマンドで練習用アプリを起動できます。

```bash
streamlit run exercise_1_text_change.py
```

### 課題 2：機能を追加して Pull Request を作る

新しいブランチを作り、ボタン、チェックボックス、セレクトボックスなどを追加して Pull Request を作成してみましょう。

実装例は `exercise_2_feature_example.py` で確認できます。次のコマンドで起動できます。

```bash
streamlit run exercise_2_feature_example.py
```

### 課題 3：コンフリクトを体験する

練習用の `exercise_3_conflict_practice.py` を使います。

1. 1つ目のブランチを作り、`conflict_message` の文字を変更してコミットする
2. 元のブランチから2つ目のブランチを作り、同じ `conflict_message` を別の文字へ変更してコミットする
3. 一方のブランチをマージした後、もう一方をマージしてコンフリクトを発生させる
4. 残したい内容へ修正し、コンフリクトを解消してコミットする

次のコマンドで練習用アプリを起動できます。

```bash
streamlit run exercise_3_conflict_practice.py
```

> コンフリクト練習は、講師の案内に従い、練習用ブランチで行ってください。

## 📁 ファイル構成

```text
.
├── .gitignore
├── README.md
├── app.py
├── exercise_1_text_change.py
├── exercise_2_feature_example.py
├── exercise_3_conflict_practice.py
└── requirements.txt
```

## 💡 困ったとき

- アプリを停止するには、ターミナルで `Ctrl + C` を押します。
- 変更前に現在のブランチを確認しましょう。
- コミット前に変更内容とコミット対象のファイルを確認しましょう。
