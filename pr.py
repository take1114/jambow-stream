import streamlit as st
import pandas as pd
import math


st.set_page_config(
    page_title="ジャンボウサイト",
    page_icon=":bear:"
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

#比較する日本記録を選択
def Select_jrecode_style():
    col1,col2 = st.columns(2)
    with col1:
        distance = st.selectbox("距離：",('50m','100m','200m','400m','800m','1500m'))
    with col2:
        style1 = st.selectbox("種目：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
    return distance,style1

#比較するマスターズ記録を選択
def Select_mrecode_style():
    col1,col2 = st.columns(2)
    with col1:
        distance = st.selectbox("distance：",('25m','50m','100m','200m','400m','800m','1500m'))
    with col2:
        style2 = st.selectbox("style：",('Fr','Ba','Br','Fly','IM','FR','XFR','MR','XMR'))
    return distance,style2

#比較するチーム記録を選択
def Select_trecode_style():
    col1,col2 = st.columns(2)
    with col1:
        distance = st.selectbox("距離：",('25m','50m','100m','200m','400m','800m','1500m'))
    with col2:
        style3 = st.selectbox("種目：",('Fr','Ba','Br','Fly','IM'))
    return distance,style3

#自分の記録・ポイント、日本記録・ポイント表示
def real(sr,t,d,s):
        if sr < 60:
            #タイム表示調整
            shape_recode = reshape_recode(sr)
            #ポイントを取得
            myPoint = point_get(t,sr)
            Maxpoint = point_get(sr,sr)
            st.write(d,s)
            st.write("トップ記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録:',t,'秒',myPoint,'ポイント')
        elif sr >= 60:
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(sr)
            time_m,time_s = reshape_recode(t)
            #ポイントを取得
            myPoint = point_get(t,sr)
            Maxpoint = point_get(sr,sr)
            st.write(d,s)
            st.write("トップ記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')

#自分の記録・ポイント、目標記録・ポイント表示、日本記録・ポイント表示
def target(Sr,T,d1,s1,ud_t):
        if Sr < 60:
            #タイム表示調整
            shape_recode = reshape_recode(Sr)
            #ポイントを取得
            myPoint = point_get(T,Sr)
            Maxpoint = point_get(Sr,Sr)
            #入力ポイントから当該タイムを取得
            #Z = time_get(mypoint,Sr)
            ud_p = point_get(ud_t,Sr)
            st.write(d1,s1)
            st.write("top記録　:",shape_recode,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",ud_t,"秒",ud_p,"ポイント")
            st.write('貴方の記録:',T,'秒',myPoint,'ポイント')
        elif Sr >= 60:
            #ポイントを取得
            myPoint = point_get(T,Sr)
            Maxpoint = point_get(Sr,Sr)
            #入力ポイントから当該タイムを取得
            ud_p = point_get(ud_t,Sr)
            #タイム表示調整
            shape_recode_m,shape_recode_s = reshape_recode(Sr)
            YM,YS = reshape_recode(ud_t)
            time_m,time_s = reshape_recode(T)
            #結果を表示
            st.write(d1,s1)
            st.write("top記録　:",shape_recode_m,'分',shape_recode_s,"秒",Maxpoint,"ポイント")
            st.write("目標記録　:",YM,"分",YS,"秒",ud_p,"ポイント")
            st.write('貴方の記録：',time_m,"分",time_s,'秒',myPoint,'ポイント')

#記録の入力
def input_time():
    col1,col2 = st.columns(2)
    with col1:
        t_m = st.number_input("分",min_value=0,step = 1)
    with col2:
        t_s = st.number_input("秒",min_value=0.0,step = 0.01)

    total = t_m*60+t_s
    return total

tab1,tab2,tab3,tab4 = st.tabs(["日本記録へ至る道","マスターズの頂","チームトップ","記録更新(現在作成中)"])

#フィナポイント
with tab1:
    st.title("フィナポイント")
    st.write("日本記録表(短水路)(単位：秒)")

    #記録表示
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
    distance,style = Select_jrecode_style()

    #選択日本記録を抽出
    select_recode = float(df1.at[distance,style])

    #持ちタイムを入力
    #time = st.number_input("貴方のタイムは？:(例：6分42秒19→402.19と入力すること)")
    time = input_time()
    result_btn = st.button("現実")
    if result_btn:
        #自分の記録・ポイント、日本記録・ポイント表示
        real(select_recode,time,distance,style)
    
    #目標ポイント入力によりタイムを算出する
    update_time = st.number_input("目標timeを入力してください")
    display_btn = st.button("目標")
    if display_btn:
        #自分の記録・ポイント、目標記録・ポイント表示、日本記録・ポイント表示
        target(select_recode,time,distance,style,update_time)

#ジャンボウポイント
with tab2:
    st.title("ジャンボウポイント")
    st.write("マスターズ日本記録表(短水路)(単位：秒)")

    #記録表示
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

    #比較するマスターズ記録を選択
    distance1,style1 = Select_mrecode_style()
    
    #選択日本記録を抽出
    select_recode = float(df.at[distance1,style1])
    
    #持ちタイムを入力
    time = st.number_input("貴方のタイムは？:(例：1分40秒32→100.32と入力すること)")
    result_btn = st.button("結果")
    if result_btn:
        #自分の記録・ポイント、日本記録・ポイント表示
        real(select_recode,time,distance1,style1)
    
    #目標ポイント入力によりタイムを算出する
    update_time1 = st.number_input("目標タイムを入力してください")
    display_btn = st.button("表示")
    if display_btn:
        #自分の記録・ポイント、目標記録・ポイント表示、日本記録・ポイント表示
        target(select_recode,time,distance1,style1,update_time1)

#ツキノワグマポイント
with tab3:
    st.title("ツキノワグマポイント")
    st.write("ツキノワグマ記録表(短水路)(単位：秒)")

    #記録表示
    df3 = pd.DataFrame({'Fr':['11.18','23.61','51.75','139.62','','',''],
                        'Ba':['13.08','26.68','62.29','164.59','','',''],
                        'Br':['14.19','30.62','67.47','','','',''],
                        'Fly':['11.02','25.97','61.13','','','',''],
                        'IM':['','','62.06','145.45','','','']},
        index = ['25m','50m','100m','200m','400m','800m','1500m'])
    st.dataframe(df3)

    #比較するteam記録を選択
    distance2,style2 = Select_trecode_style()
    
    #選択日本記録を抽出
    select_recode = float(df3.at[distance2,style2])
    
    #持ちタイムを入力
    time = st.number_input("現在の貴方のタイムは？:(例：6分42秒19→402.19と入力すること)")
    result_btn = st.button("差")
    if result_btn:
        #自分の記録・ポイント、日本記録・ポイント表示
        real(select_recode,time,distance2,style2)
    
    #目標ポイント入力によりタイムを算出する
    update_time2 = st.number_input("目標timeを入力")
    display_btn = st.button("道標")
    if display_btn:
        #自分の記録・ポイント、目標記録・ポイント表示、日本記録・ポイント表示
        target(select_recode,time,distance2,style2,update_time2)

#記録更新タブ(現在作成中)
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





