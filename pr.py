import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime as dt


st.set_page_config(
    page_title="ジャンボウサイト"
)

#精度向上ボタンで役立つ関数1
def time_check(x):
    return (x-21.84)

#精度向上ボタンで役立つ関数2
def point_check(y):
    return (-y+1000)/100

#種目選択を可能にする調整
def reshape_recode(z):
    if z < 60:
        return z
    elif z > 60:
        m = int(z // 60)
        s = round((z % 60),2)
        return m,s
    
def shape_rest(r):
    if r < 60:
        return r
    elif r >= 60:
        R = dt.timedelta(seconds = r)
        return R

st.title("個人記録表(ジャンボウポイント)")
st.write("日本記録表(短水路)")
df = pd.DataFrame({'Fr':['9.83','21.84','49.21','108.95','236.47','498.16','951.03'],
                   'Ba':['11.44','23.95','51.63','116.01','','',''],
                   'Br':['12.01','26.58','58.13','1288.28','','',''],
                   'Fly':['10.52','23.33','52.42','113.72','','',''],
                   'IM':['','','53.93','118.91','254.51','',''],
                   'FR':['40.29','88.02','201.83','438.39','','',''],
                   'XFR':['44.95','100.16','221.04','476.85','','',''],
                   'MR':['44.10','100.22','217.66','','','',''],
                   'XMR':['48.39','105.63','238.78','','','','']},
    index = ['25m','50m','100m','200m','400m','800m','1500m']
    )
st.dataframe(df)

#50m自由形　日本記録からきれいな数字0.5秒刻みのポイント対応表
df2 = pd.DataFrame({
    'time':[21.84,22.00,22.25,22.50,22.75,23.00,23.50,24.00,24.50,25.00,25.50,26.00,26.50,27.00,27.50,28.00,28.50,29.00,29.50,30.00,30.50,31.00,31.25,31.50,31.75,32.00],
    'point':[1000,978,945,914,884,856,802,753,708,666,628,592,559,529,500,474,450,427,405,385,367,349,341,333,325,317]
})
st.write(len(df2))
#どうやら二次関数のようなので式を導出する
time_ex = df2[['time']].apply(time_check)
point_ex = df2[['point']].apply(point_check)

X = pd.DataFrame(time_ex,index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
Y = pd.DataFrame(point_ex,index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
Z = pd.concat([X,Y],axis=1)



#対応表の散布図
st.scatter_chart(df2,x = "time",y = "point")
#数字を整えたデータフレームとその散布図
st.scatter_chart(Z,x = 'point',y = 'time')



#比較する日本記録を選択
distance = st.selectbox("距離は？：",('25m','50m','100m','200m','400m','800m','1500m'))
style = st.selectbox("種目は？：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))

#選択日本記録を抽出
select_recode = float(df.at[distance,style])

if select_recode < 60:
    shape_recode = reshape_recode(select_recode)
    st.write(distance,style,"の日本記録は",shape_recode,"秒です")
    #自分の記録を入力
    time = st.number_input("貴方のタイムは？:")
    rest = round((select_recode - time)*(-1),2)
    Rest = shape_rest(rest)
    st.write('日本記録：',shape_recode,'秒,貴方の記録：',time,'秒、日本記録まであと',Rest)
elif select_recode >= 60:
    shape_recode_m,shape_recode_s = reshape_recode(select_recode)
    st.write(distance,style,"の日本記録は",shape_recode_m,'分',shape_recode_s,"秒です")
    #自分の記録を入力
    time = st.number_input("貴方のタイムは？:")
    rest = round((select_recode - time)*(-1),2)
    Rest = shape_rest(rest)
    st.write('日本記録：',shape_recode_m,'分',shape_recode_s,'秒,貴方の記録：',time,' 日本記録まであと',Rest)


#二次関数の係数を導出　y = a ** x a:の導出
#反比例　y = a/x a:の導出
for i in range(0,26):
    a = round(float(X.iloc[i,0] / pow(Y.iloc[i,0],2)),3)
    a_round = round(a,2)
    st.write(a,a_round,round(X.iloc[i,0],2),round(Y.iloc[i,0],2))


x2 = st.number_input("pointを入力してください(50m自由形のタイムを返します)")
y2 = (0.22*pow((-x2+1000)/100,2))
#Y1 = (y2*100)+21.84
Y1 = round((y2+21.84),2)
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

