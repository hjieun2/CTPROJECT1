import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
#import matplotlib.pyplot as plt 이 모듈은 데이터 시각화할 때 쓰이지만.. (정적임 즉 상호작용 안 됨)

st.set_page_config(layout='wide',page_title="My App")


html = '''
<html>
    <haed>
        <title>This HTML App</title>
    </head>
    <body>
        <h1> This Long Text!!!</h1>
        <br>
        <br>
        <h3>This a small text</h3>
    </body>
</html>    
'''

with open('./com_html.html','r', encoding='utf-8') as f:
    filehtml=f.read()
    f.close()

url="https://www.youtube.com/watch?v=XyEOEBsa8I4"

df=pd.read_csv('./data/data.csv')
df.columns = df.columns.str.strip()
 

st.title('This is my first webapp!')
col1, col2=st.columns((2,2))
with col1:
    with st.expander('동영상...'):
        st.subheader('AI 보이스피싱....')
        st.video(url)
        
    with st.expander('Content2_image'):
        st.subheader('Content2_image....')
        st.image('./images/catdog.jpeg')
        st.markdown(html, unsafe_allow_html=True)
        st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
        
with col2:
    with st.expander('성적표...'):
        st.subheader('성적표....')
        st.table(df) 
        subject=st.selectbox("과목을 선택하세요:", ['kor', 'math', 'eng', 'info'])
        # plotly 그래프 생성
        fig = px.bar(df, x='name', y=subject, color='name', title=f'{subject.upper()}점수')
        
        st.plotly_chart(fig)
        #dff=df.groupby(by='name').sum()
        #st.cahrt(df)
    
    with st.expander('페이지 만들기'):
        st.subheader('페이지 만들기....')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)