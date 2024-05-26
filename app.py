import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('簡易データ分析アプリ')

# サイドバーにデータアップロード
st.sidebar.title('サイドバー')
uploaded_file = st.sidebar.file_uploader('CSVファイルをアップロード', type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write('データフレームの表示')
    st.dataframe(df)
    
    # データ前処理
    st.write('データの基本統計量')
    st.write(df.describe())
    
    # データ可視化
    st.write('データの可視化')
    column = st.selectbox('表示するカラムを選択', df.columns)
    plt.figure(figsize=(10, 4))
    plt.hist(df[column], bins=30)
    st.pyplot(plt)
