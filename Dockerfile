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
CMD ['streamlit', 'run', 'app.py', '--server.port=8501', '--server.enableCORS=false']
