import streamlit as st
import pandas as pd
import datetime as dt
import math


st.set_page_config(
    page_title="ジャンボウサイト"
)

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
    
def point_get(t,nr):
    p = ((nr/t)**3)*1000
    P = math.floor(p)
    return P

st.title("個人記録表(ジャンボウポイント)")
st.write("日本記録表(短水路)(単位：秒)")
df = pd.DataFrame({'Fr':['9.83','21.84','49.21','108.95','236.47','498.16','951.03'],
                   'Ba':['11.44','23.95','51.63','116.01','','',''],
                   'Br':['12.01','26.58','58.13','128.28','','',''],
                   'Fly':['10.52','23.33','52.42','113.72','','',''],
                   'IM':['','','53.93','118.91','254.51','',''],
                   'FR':['40.29','88.02','201.83','438.39','','',''],
                   'XFR':['44.95','100.16','221.04','476.85','','',''],
                   'MR':['44.10','100.22','217.66','','','',''],
                   'XMR':['48.39','105.63','238.78','','','','']},
    index = ['25m','50m','100m','200m','400m','800m','1500m']
    )
st.dataframe(df)

#比較する日本記録を選択
distance = st.selectbox("距離は？：",('25m','50m','100m','200m','400m','800m','1500m'))
style = st.selectbox("種目は？：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
#選択日本記録を抽出
select_recode = float(df.at[distance,style])
#持ちタイムを入力
time = st.number_input("貴方のタイムは？:(例：1分40秒32→100.32と入力すること)")

result_btn = st.button("結果")
if result_btn:
    if select_recode < 60:
        shape_recode = reshape_recode(select_recode)
        #自分の記録を入力
        myPoint = point_get(time,select_recode)
        Maxpoint = point_get(select_recode,select_recode)
        st.write(distance,style)
        st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
        st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
    elif select_recode >= 60:
        shape_recode_m,shape_recode_s = reshape_recode(select_recode)
        #自分の記録を入力
        myPoint = point_get(time,select_recode)
        Maxpoint = point_get(select_recode,select_recode)
        st.write(distance,style)
        st.write("日本記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
        st.write('貴方の記録：',time,'秒',myPoint,'ポイント')


mypoint = st.number_input("目標pointを入力してください")

display_btn = st.button("表示")
if display_btn:
    shape_recode = reshape_recode(select_recode)
    myPoint = point_get(time,select_recode)
    Maxpoint = point_get(select_recode,select_recode)
    rtp = math.pow(mypoint/1000,1/3)
    mytime = select_recode/rtp
    Y1 = (math.floor(mytime*100))/100
    st.write(distance,style)
    st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
    st.write("目標記録　:",Y1,"秒",mypoint,"ポイント")
    st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
    #rest = round((select_recode - time)*(-1),2)
    #Rest = shape_rest(rest)
    #st.write('日本記録まであと',Rest,'秒')


