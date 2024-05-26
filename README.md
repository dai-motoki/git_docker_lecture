
## 要件定義書：stlamlit 簡易データ分析アプリ



### 開発時の課題

- バージョンがよくわからなくなる
- 環境の問題でエラーが起こりよくわからなくなる

### 1. 概要
stlamlit簡易データ分析アプリは、データのアップロード、前処理、解析、可視化を行うためのWebアプリケーションです。このアプリケーションは、PythonのStreamlitフレームワークを使用して構築され、Dockerを利用して容易にデプロイできるようにします。

### 2. 目的
本要件定義書は、stlamlit簡易データ分析アプリのディレクトリ構成およびDocker環境の構築に関する詳細を定義するものです。

### 3. ディレクトリ構成
以下に、アプリケーションのディレクトリ構成を示します。

```
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

### 4. ファイルの詳細

#### app.py
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("簡易データ分析アプリ")

# データアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("データフレームの表示")
    st.dataframe(df)

    # データ前処理
    st.write("データの基本統計量")
    st.write(df.describe())

    # データ解析
    st.write("データの相関行列")
    st.write(df.corr())

    # データ可視化
    st.write("データの可視化")
    column = st.selectbox("表示するカラムを選択", df.columns)
    plt.figure(figsize=(10, 4))
    plt.hist(df[column], bins=30)
    st.pyplot(plt)
```

#### Dockerfile
```Dockerfile
# ベースイメージ
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY app.py .

# Streamlitの実行コマンド
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```

#### requirements.txt
```
streamlit
pandas
matplotlib
```

#### .dockerignore
```
__pycache__
*.pyc
*.pyo
*.pyd
```

### 5. 環境構築手順

1. リポジトリをクローン
    ```bash
    git clone <repository_url>
    cd stlamlit_app
    ```

2. Dockerイメージをビルド
    ```bash
    docker build -t stlamlit_app .
    ```

3. Dockerコンテナを実行
    ```bash
    docker run -p 8501:8501 stlamlit_app
    ```

4. ブラウザで`http://localhost:8501`にアクセスしてアプリを使用

以上で、stlamlit簡易データ分析アプリの要件定義書となります。