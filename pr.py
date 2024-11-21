import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="ジャンボウサイト"
)
st.snow()
#col1,col2 = st.columns(2)
#精度向上ボタンで役立つ関数1
def time_check(x):
    return x-21.84#+0.34

#精度向上ボタンで役立つ関数2
def point_check(y):
    return (-y+1000)/100

st.title("個人記録表(ジャンボウポイント)")
st.write("日本記録表(短水路)")
df = pd.DataFrame({'Fr':['9.83','21.84','49.21','1:48.95','3:56.47','8:18.16','15:51.03'],
                   'Ba':['11.44','23.95','51.63','1:56.01','','',''],
                   'Br':['12.01','26.58','58.13','2:08.28','','',''],
                   'Fly':['10.52','23.33','52.42','1:53.72','','',''],
                   'IM':['','','53.93','1:58.91','4:14.51','',''],
                   'FR':['40.29','1:28.02','3:21.83','7:18.39','','',''],
                   'XFR':['44.95','1:40.16','3:41.04','7:56.85','','',''],
                   'MR':['44.10','1:40.22','3:37.66','','','',''],
                   'XMR':['48.39','1:45.63','3:58.78','','','','']},
    index = ['25m','50m','100m','200m','400m','800m','1500m']
    )
st.dataframe(df)

#50m自由形　日本記録からきれいな数字0.5秒刻みのポイント対応表
df2 = pd.DataFrame({
    'time':[21.84,22.00,22.25,22.50,22.75,23.00,23.50,24.00,24.50,25.00,25.50,26.00,26.50,27.00,27.50,28.00,28.50,29.00,29.50,30.00,30.50,31.00,31.25,31.50,31.75,32.00],
    'point':[1000,978,945,914,884,856,802,753,708,666,628,592,559,529,500,474,450,427,405,385,367,349,341,333,325,317]
})

#どうやら二次関数のようなので式を導出する
time_ex = df2[['time']].apply(time_check)
point_ex = df2[['point']].apply(point_check)

X = pd.DataFrame(time_ex,index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
Y = pd.DataFrame(point_ex,index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
Z = pd.concat([X,Y],axis=1)

#with col1:
#比較する日本記録を選択
distance = st.selectbox("距離は？：",('25m','50m','100m','200m','400m','800m','1500m'))
#対応表の散布図
st.scatter_chart(df2,x = "time",y = "point")
#with col2:
style = st.selectbox("種目は？：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
#数字を整えたデータフレームとその散布図
st.scatter_chart(Z,x = 'point',y = 'time')
select_recode = float(df.at[distance,style])
st.write(distance,style,"の日本記録は",select_recode,"秒です")

#自分の記録を入力
time = st.number_input("貴方のタイムは？:")

rest = round((select_recode - time)*(-1),2)

st.write('日本記録：',select_recode,'秒,貴方の記録：',time,'秒、日本記録まであと',rest,'秒')
st.write(df2)







#二次関数の係数を導出　y = a ** x a:の導出
for i in range(0,26):
    a = round(float(X.iloc[i,0] / pow(Y.iloc[i,0],2)),3)
    a_round = round(a,2)
    st.write(a,a_round,round(X.iloc[i,0],2),round(Y.iloc[i,0],2))

x2 = st.number_input("pointを入力してください")
y2 = (0.26*pow((-x2+1000)/100,2))
Y1 = (y2+21.84)
st.write(Y1,"秒")

#単回帰分析結果－情報の精度か足りずいまいち
model_lr = LinearRegression()
model_lr.fit(Y,X)
#
st.write("モデル関数の回帰変数w1:%.3f"%model_lr.coef_)
st.write("モデル関数の切片w2:%.3f"%model_lr.intercept_)
st.write("y = %.3fx+%.3f"%(model_lr.coef_,model_lr.intercept_))

x3 = st.number_input("point値を入力してください")
Y2 = model_lr.coef_*((-x3+1000)/100)+model_lr.intercept_
st.write(Y2+21.84)

