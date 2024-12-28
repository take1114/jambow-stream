import streamlit as st
import pandas as pd
import math


st.set_page_config(
    page_title="ジャンボウサイト"
)

#タイム表示調整
def reshape_recode(z):
    if z < 60:
        return z
    elif z > 60:
        m = int(z // 60)
        s = round((z % 60),2)
        return m,s

#タイムからポイントの計算式
def point_get(t,nr):
    p = ((nr/t)**3)*1000
    P = math.floor(p)
    return P

#ポイントからタイム算出式
def time_get(mp,sr):
    rtp = math.pow(mp/1000,1/3)
    mytime = sr/rtp
    Y1 = (math.floor(mytime*100))/100
    return Y1

##タイム更新関数
#def time_upgrade(DF,d,s,TM):
#    DF[d,s] = TM
#    return DF


tab1,tab2,tab3,tab4 = st.tabs(["日本記録へいたる道","マスターズの頂","ツキノワグマポイント","記録更新(現在作成中)"])
with tab1:
    st.title("個人記録表(フィナポイント)")
    st.write("日本記録表(短水路)(単位：秒)")
    df1 = pd.DataFrame({'Fr':['20.95','46.22','101.29','216.87','453.78','865.95'],
                        'Ba':['22.81','49.65','108.25','','',''],
                        'Br':['25.91','55.77','120.35','','',''],
                        'Fly':['22.19','49.54','106.85','','',''],
                        'IM':['','51.29','110.47','234.81','',''],
                        'FR':['83.80','187.79','412.04','','',''],
                        'XFR':['89.51','','','','',''],
                        'MR':['91.28','201.07','','','',''],
                        'XMR':['97.29','','','','','']},
        index = ['50m','100m','200m','400m','800m','1500m'])
    st.dataframe(df1)
    #比較する日本記録を選択
    distance = st.selectbox("距離：",('50m','100m','200m','400m','800m','1500m'))
    style = st.selectbox("種目：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
    #選択日本記録を抽出
    select_recode = float(df1.at[distance,style])
    #持ちタイムを入力
    time = st.number_input("貴方のタイムは？:(例：6分42秒19→402.19と入力すること)")
    result_btn = st.button("現実")
    if result_btn:
        if select_recode < 60:
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            time_m,time_s = reshape_recode(time)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')
    mypoint = st.number_input("目標ポイントを入力してください")
    display_btn = st.button("目標")
    if display_btn:
        if select_recode < 60:
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",Z,"秒",mypoint,"ポイント")
            st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            YM,YS = reshape_recode(Z)
            time_m,time_s = reshape_recode(time)
            #結果を表示
            st.write(distance,style)
            st.write("日本記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",YM,"分",YS,"秒",mypoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')

with tab2:
    st.title("個人記録表(ジャンボウポイント)")
    st.write("マスターズ日本記録表(短水路)(単位：秒)")
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
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            time_m,time_s = reshape_recode(time)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')
    mypoint = st.number_input("目標pointを入力してください")
    display_btn = st.button("表示")
    if display_btn:
        if select_recode < 60:
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",Z,"秒",mypoint,"ポイント")
            st.write('貴方の記録:',time,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #ポイントを取得
            myPoint = point_get(time,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            YM,YS = reshape_recode(Z)
            time_m,time_s = reshape_recode(time)
            #結果を表示
            st.write(distance,style)
            st.write("日本記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",YM,"分",YS,"秒",mypoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')

with tab3:
    st.title("個人記録表(ツキノワグマポイント)")
    st.write("日本記録表(短水路)(単位：秒)")
    df3 = pd.DataFrame({'Fr':['11.27','23.61','51.75','139.62','','',''],
                        'Ba':['','26.68','','164.59','','',''],
                        'Br':['','30.62','67.47','','','',''],
                        'Fly':['11.02','25.97','61.13','','','',''],
                        'IM':['','','62.06','145.45','','','']
                        },
        index = ['25m','50m','100m','200m','400m','800m','1500m'])
    st.dataframe(df3)
    #比較する日本記録を選択
    distance = st.selectbox("距離：",('25m','50m','100m','200m','400m','800m','1500m'))
    style = st.selectbox("種目：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
    #選択日本記録を抽出
    select_recode = float(df3.at[distance,style])
    #持ちタイムを入力
    time_tuki = st.number_input("貴方のタイムは？:(例：6分42秒19→402.19と入力すること)")
    result_btn = st.button("差")
    if result_btn:
        if select_recode < 60:
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time_tuki,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("トップ記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録:',time_tuki,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            time_m,time_s = reshape_recode(time_tuki)
            #ポイントを取得
            myPoint = point_get(time_tuki,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            st.write(distance,style)
            st.write("トップ記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')
    mypoint = st.number_input("目標ポイントを入力してください")
    display_btn = st.button("目標")
    if display_btn:
        if select_recode < 60:
            #タイム表示調整
            shape_recode = reshape_recode(select_recode)
            #ポイントを取得
            myPoint = point_get(time_tuki,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            st.write(distance,style)
            st.write("日本記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",Z,"秒",mypoint,"ポイント")
            st.write('貴方の記録:',time_tuki,'秒',myPoint,'ポイント')
        elif select_recode >= 60:
            #ポイントを取得
            myPoint = point_get(time_tuki,select_recode)
            Maxpoint = point_get(select_recode,select_recode)
            #入力ポイントから当該タイムを取得
            Z = time_get(mypoint,select_recode)
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(select_recode)
            YM,YS = reshape_recode(Z)
            time_m,time_s = reshape_recode(time)
            #結果を表示
            st.write(distance,style)
            st.write("トップ記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",YM,"分",YS,"秒",mypoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')
with tab4:
    distance = st.selectbox("距離？：",('25m','50m','100m','200m','400m','800m','1500m'))
    style = st.selectbox("種目？：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
    #持ちタイムを入力
    Time = st.number_input("更新タイムは？:(例：1分40秒32→100.32と入力すること)")
    japan_recode_btn = st.button("日本記録さらなる高みへ")
    masters_recode_btn = st.button("マスターズさらなる高みへ")
    
    if masters_recode_btn:
        #選択日本記録を抽出
        df.at[distance,style] = Time
        st.write(df)
    elif japan_recode_btn:
        df1.at[distance,style] = Time
        st.write(df1)





