##  update
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import openpyxl
from openpyxl import load_workbook

def intro():
    

    st.write("# Welcome to Risk Map Monitoring")
    st.sidebar.success("Pilih unitnya dulu yuk")
    st.markdown(
        "Selamat Datang! Silahkan Pilih Unit Dipojok Kiri "
        
    )

def ta():
    st.title("Risk Management Matrix Unit TA")
    wb = load_workbook(filename='data.xlsx', read_only=True)
    ##df = pd.read_excel('data.xlsx')
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')

    #data 1
    df_new = df.loc[ (df['Risiko'] == 'Adanya aktivitas tambahan yang berasal dari manajemen request yang belum dibudgetkan di awal tahun serta Adanya realokasi budget anggaran yang tidak sesuai') & (df['Unit'] == 'TA')]
    df_new2 = df.loc[ (df['Risiko'] == 'Adanya aktivitas tambahan yang berasal dari manajemen request yang belum dibudgetkan di awal tahun serta Adanya realokasi budget anggaran yang tidak sesuai') & (df['Unit'] == 'TA')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Risiko pembuatan invoice untuk project dan retail tidak sesuai dengan lead time') & (df['Unit'] == 'TA')]
    df_new4 = df.loc[ (df['Risiko'] == 'Risiko pembuatan invoice untuk project dan retail tidak sesuai dengan lead time') & (df['Unit'] == 'TA')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Keterlambatan pencatatan AP AR') & (df['Unit'] == 'TA')]
    df_new6 = df.loc[ (df['Risiko'] == 'Keterlambatan pencatatan AP AR') & (df['Unit'] == 'TA')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Penurunan Revenue karena perusahaan menanggung biaya selisih perubahan tarif PPN Serta Dilakukan audit pajak setiap tahun') & (df['Unit'] == 'TA')]
    df_new8 = df.loc[ (df['Risiko'] == 'Penurunan Revenue karena perusahaan menanggung biaya selisih perubahan tarif PPN Serta Dilakukan audit pajak setiap tahun') & (df['Unit'] == 'TA')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Terdapat PPh Badan yang harus dibayar walaupun sesuai Laporan Keuangan GMF mengalami kerugian Serta Kenaikan staff expense akibat dari naiknya employee tax expense') & (df['Unit'] == 'TA')]
    df_new10 = df.loc[ (df['Risiko'] == 'Terdapat PPh Badan yang harus dibayar walaupun sesuai Laporan Keuangan GMF mengalami kerugian Serta Kenaikan staff expense akibat dari naiknya employee tax expense') & (df['Unit'] == 'TA')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Adanya aktivitas tambahan yang berasal dari manajemen request yang belum dibudgetkan di awal tahun serta Adanya realokasi budget anggaran yang tidak sesuai'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Risiko pembuatan invoice untuk project dan retail tidak sesuai dengan lead time'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Keterlambatan pencatatan AP AR'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Penurunan Revenue karena perusahaan menanggung biaya selisih perubahan tarif PPN Serta Dilakukan audit pajak setiap tahun'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Terdapat PPh Badan yang harus dibayar walaupun sesuai Laporan Keuangan GMF mengalami kerugian Serta Kenaikan staff expense akibat dari naiknya employee tax expense'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "lower center", bbox_to_anchor=(1, 1))
    plt.title('TA Risk Map')
    st.pyplot(fig)
    

def tb():
    
    st.title("Risk Management Matrix Unit TB")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Risiko'] == 'Pencapaian revenue belum bisa mengkompensasi kebutuhan biaya operasional') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Risiko'] == 'Pencapaian revenue belum bisa mengkompensasi kebutuhan biaya operasional') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'auditee tidak memprioritaskan penyelesaian tindak lanjut audit') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Risiko'] == 'auditee tidak memprioritaskan penyelesaian tindak lanjut audit') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Adanya aktivitas tambahan yang berasal dari manajemen request yang belum dibudgetkan di awal tahun serta Adanya realokasi budget anggaran yang tidak sesuai') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Risiko'] == 'Adanya aktivitas tambahan yang berasal dari manajemen request yang belum dibudgetkan di awal tahun serta Adanya realokasi budget anggaran yang tidak sesuai') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Risiko'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Risiko'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Pencapaian revenue belum bisa mengkompensasi kebutuhan biaya operasional '), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='auditee tidak memprioritaskan penyelesaian tindak lanjut audit'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TB Risk Map')
    st.pyplot(fig)

def tc():
    st.title("Risk Management Matrix Unit TC")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    

    #data 1
    df_new = df.loc[ (df['Risiko'] == 'Operating profit tidak mencapai target atau minus') & (df['Unit'] == 'TC')]
    df_new2 = df.loc[ (df['Risiko'] == 'Operating profit tidak mencapai target atau minus') & (df['Unit'] == 'TC')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Nilai inventory yang tinggi') & (df['Unit'] == 'TC')]
    df_new4 = df.loc[ (df['Risiko'] == 'Nilai inventory yang tinggi') & (df['Unit'] == 'TC')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Pelayanan yang tidak sesuai dengan ekspektasi customer') & (df['Unit'] == 'TC')]
    df_new6 = df.loc[ (df['Risiko'] == 'Pelayanan yang tidak sesuai dengan ekspektasi customer') & (df['Unit'] == 'TC')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Personel produksi yang kurang baik secara kualitas atau kuantitas') & (df['Unit'] == 'TC')]
    df_new8 = df.loc[ (df['Risiko'] == 'Personel produksi yang kurang baik secara kualitas atau kuantitas') & (df['Unit'] == 'TC')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Operating profit tidak mencapai target atau minus'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Nilai inventory yang tinggi'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Pelayanan yang tidak sesuai dengan ekspektasi customer'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Personel produksi yang kurang baik secara kualitas atau kuantitas'), df_new8.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TC Risk Map')
    st.pyplot(fig)



def td():
    
    st.title("Risk Management Matrix Unit TD")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    

    #data 1
    df_new = df.loc[ (df['Risiko'] == 'Realisasi budget dinas TD mengalami over budget') & (df['Unit'] == 'TD')]
    df_new2 = df.loc[ (df['Risiko'] == 'Realisasi budget dinas TD mengalami over budget') & (df['Unit'] == 'TD')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Customer tidak puas atas layanan IT GMF') & (df['Unit'] == 'TD')]
    df_new4 = df.loc[ (df['Risiko'] == 'Customer tidak puas atas layanan IT GMF') & (df['Unit'] == 'TD')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Tidak tercapainya kesepakatan dengan partner pada rencana pengembangan inorganic') & (df['Unit'] == 'TD')]
    df_new6 = df.loc[ (df['Risiko'] == 'Tidak tercapainya kesepakatan dengan partner pada rencana pengembangan inorganic') & (df['Unit'] == 'TD')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Asset investasi dinas TD tidak terutilisasi dengan maksimal') & (df['Unit'] == 'TD')]
    df_new8 = df.loc[ (df['Risiko'] == 'Asset investasi dinas TD tidak terutilisasi dengan maksimal') & (df['Unit'] == 'TD')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Realisasi budget dinas TD mengalami over budget'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Customer tidak puas atas layanan IT GMF'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Tidak tercapainya kesepakatan dengan partner pada rencana pengembangan inorganic'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Asset investasi dinas TD tidak terutilisasi dengan maksimal'), df_new8.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TD Risk Map')
    st.pyplot(fig)
    
def te():
    st.title("Risk Management Matrix Unit TE")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Target pencapaian KPI Dinas tidak tercapai') & (df['Unit'] == 'TE')]
    df_new2 = df.loc[ (df['Risiko'] == 'Target pencapaian KPI Dinas tidak tercapai') & (df['Unit'] == 'TE')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Konfigurasi pesawat antara sistem dan aktual tidak sesuai setelah proses maintenance pesawat (RTS)') & (df['Unit'] == 'TE')]
    df_new4 = df.loc[ (df['Risiko'] == 'Konfigurasi pesawat antara sistem dan aktual tidak sesuai setelah proses maintenance pesawat (RTS)') & (df['Unit'] == 'TE')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Ketidakakuratan dokumen perintah kerja (Job Card) dalam menentukan kebutuhan material dan referensi kerja') & (df['Unit'] == 'TE')]
    df_new6 = df.loc[ (df['Risiko'] == 'Ketidakakuratan dokumen perintah kerja (Job Card) dalam menentukan kebutuhan material dan referensi kerja') & (df['Unit'] == 'TE')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'SLA tidak terpenuhi terkait produk pelayanan dan jasa dengan customer') & (df['Unit'] == 'TE')]
    df_new8 = df.loc[ (df['Risiko'] == 'SLA tidak terpenuhi terkait produk pelayanan dan jasa dengan customer') & (df['Unit'] == 'TE')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Pelanggan tidak puas dengan kinerja engineer dalam mendeliver pekerjaan') & (df['Unit'] == 'TE')]
    df_new10 = df.loc[ (df['Risiko'] == 'Pelanggan tidak puas dengan kinerja engineer dalam mendeliver pekerjaan') & (df['Unit'] == 'TE')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Target pencapaian KPI Dinas tidak tercapai'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Konfigurasi pesawat antara sistem dan aktual tidak sesuai setelah proses maintenance pesawat (RTS)'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Ketidakakuratan dokumen perintah kerja (Job Card) dalam menentukan kebutuhan material dan referensi kerja'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='SLA tidak terpenuhi terkait produk pelayanan dan jasa dengan customer'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Pelanggan tidak puas dengan kinerja engineer dalam mendeliver pekerjaan'), df_new10.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TE Risk Map')
    st.pyplot(fig)
    
def tf():
    st.title("Risk Management Matrix Unit TF")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Budget PBTH yang tidak sesuai dengan keadaan operasional aktual') & (df['Unit'] == 'TF')]
    df_new2 = df.loc[ (df['Risiko'] == 'Budget PBTH yang tidak sesuai dengan keadaan operasional aktual') & (df['Unit'] == 'TF')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Unserviceable material yang diturunkan dari pesawat keberadaannya tidak diketahui / hilang') & (df['Unit'] == 'TF')]
    df_new4 = df.loc[ (df['Risiko'] == 'Unserviceable material yang diturunkan dari pesawat keberadaannya tidak diketahui / hilang') & (df['Unit'] == 'TF')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Structure gap material consume muncul setelah maintenance selesai dilaksanakan') & (df['Unit'] == 'TF')]
    df_new6 = df.loc[ (df['Risiko'] == 'Structure gap material consume muncul setelah maintenance selesai dilaksanakan') & (df['Unit'] == 'TF')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Notifikasi dengan status SOD meningkat drastis') & (df['Unit'] == 'TF')]
    df_new8 = df.loc[ (df['Risiko'] == 'Notifikasi dengan status SOD meningkat drastis') & (df['Unit'] == 'TF')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Rencana kerja yang tidak tercapai') & (df['Unit'] == 'TF')]
    df_new10 = df.loc[ (df['Risiko'] == 'Rencana kerja yang tidak tercapai') & (df['Unit'] == 'TF')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Budget PBTH yang tidak sesuai dengan keadaan operasional aktual'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Unserviceable material yang diturunkan dari pesawat keberadaannya tidak diketahui / hilang'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Structure gap material consume muncul setelah maintenance selesai dilaksanakan'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Notifikasi dengan status SOD meningkat drastis'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Rencana kerja yang tidak tercapai'), df_new10.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TF Risk Map')
    st.pyplot(fig)

    
def th():
    st.title("Risk Management Matrix Unit TH")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Attractive & Competitive C&B untuk memotivasi Pegawai belum maksimal') & (df['Unit'] == 'TH')]
    df_new2 = df.loc[ (df['Risiko'] == 'Attractive & Competitive C&B untuk memotivasi Pegawai belum maksimal') & (df['Unit'] == 'TH')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Target Revenue Perusahaan tidak tercapai sedangkan Staff Expense tidak berkurang') & (df['Unit'] == 'TH')]
    df_new4 = df.loc[ (df['Risiko'] == 'Target Revenue Perusahaan tidak tercapai sedangkan Staff Expense tidak berkurang') & (df['Unit'] == 'TH')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Requirement jumlah & kualifikasi pegawai dalam suatu dinas tidak terpenuhi') & (df['Unit'] == 'TH')]
    df_new6 = df.loc[ (df['Risiko'] == 'Requirement jumlah & kualifikasi pegawai dalam suatu dinas tidak terpenuhi') & (df['Unit'] == 'TH')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Program pengembangan (IDAP) tidak berjalan') & (df['Unit'] == 'TH')]
    df_new8 = df.loc[ (df['Risiko'] == 'Program pengembangan (IDAP) tidak berjalan') & (df['Unit'] == 'TH')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['Risiko'] == 'System baru kurang maksimal penggunaannya') & (df['Unit'] == 'TH')]
    df_new10 = df.loc[ (df['Risiko'] == 'System baru kurang maksimal penggunaannya') & (df['Unit'] == 'TH')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5
    
     #data6
    df_new11 = df.loc[ (df['Risiko'] == 'System baru tidak terimplementasikan') & (df['Unit'] == 'TH')]
    df_new12 = df.loc[ (df['Risiko'] == 'System baru tidak terimplementasikan') & (df['Unit'] == 'TH')]
    df_new12 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new11['Nilai Likelihood Risiko Inheren'] = df_new11['Nilai Likelihood Risiko Inheren'] - 0.7
    df_new11['Nilai Consequence Risiko Inheren'] = df_new11['Nilai Consequence Risiko Inheren'] - 0.7
    df_new12['Nilai Consequence Risiko Inheren'] = df_new12['Nilai Consequence (Risiko Residu)'] - 0.7
    df_new12['Nilai Likelihood Risiko Inheren'] = df_new12['Nilai Likelihood (Risiko Residu)'] - 0.7

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Attractive & Competitive C&B untuk memotivasi Pegawai belum maksimal'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Target Revenue Perusahaan tidak tercapai sedangkan Staff Expense tidak berkurang'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Requirement jumlah & kualifikasi pegawai dalam suatu dinas tidak terpenuhi'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Program pengembangan (IDAP) tidak berjalan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='System baru kurang maksimal penggunaannya'), df_new10.assign(Risk='')])
    con6 = pd.concat([df_new11.assign(Risk='System baru tidak terimplementasikan'), df_new12.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con6,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C2", "C2"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TH Risk Map')
    st.pyplot(fig)
    
    
def ti():


    st.title("Risk Management Matrix Unit TI")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    

    #data 1
    df_new = df.loc[ (df['Risiko'] == 'Kurangnya value added yang dirasakan oleh auditee terhadap rekomendasi internal audit ') & (df['Unit'] == 'TI')]
    df_new2 = df.loc[ (df['Risiko'] == 'Kurangnya value added yang dirasakan oleh auditee terhadap rekomendasi internal audit ') & (df['Unit'] == 'TI')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'auditee tidak memprioritaskan penyelesaian tindak lanjut audit') & (df['Unit'] == 'TI')]
    df_new4 = df.loc[ (df['Risiko'] == 'auditee tidak memprioritaskan penyelesaian tindak lanjut audit') & (df['Unit'] == 'TI')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == '1. Terbatasnya budget pengembangan tools audit 2. Keterbatasan kemampuan dalam pengembangan tools audit 3. Tidak adanya spare waktu untuk melakukan pengembangan tools audit 4. Perbaikan proses tidak efisien dan efektif') & (df['Unit'] == 'TI')]
    df_new6 = df.loc[ (df['Risiko'] == '1. Terbatasnya budget pengembangan tools audit 2. Keterbatasan kemampuan dalam pengembangan tools audit 3. Tidak adanya spare waktu untuk melakukan pengembangan tools audit 4. Perbaikan proses tidak efisien dan efektif') & (df['Unit'] == 'TI')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == ' Belum dialokasikan keseluruhan pelaksanaan sertifikasi QIA- budget personil baru ') & (df['Unit'] == 'TI')]
    df_new8 = df.loc[ (df['Risiko'] == ' Belum dialokasikan keseluruhan pelaksanaan sertifikasi QIA- budget personil baru ') & (df['Unit'] == 'TI')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya value added yang dirasakan oleh auditee terhadap rekomendasi internal audit '), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='auditee tidak memprioritaskan penyelesaian tindak lanjut audit'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='1. Terbatasnya budget pengembangan tools audit 2. Keterbatasan kemampuan dalam pengembangan tools audit 3. Tidak adanya spare waktu untuk melakukan pengembangan tools audit 4. Perbaikan proses tidak efisien dan efektif'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Asset investasi dinas TD tidak terutilisasi dengan maksimal'), df_new8.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])


    sns.move_legend(ax, "lower center", bbox_to_anchor=(1, 1))
    plt.title('TI Risk Map')
    st.pyplot(fig)

def tj():
    st.title("Risk Management Matrix Unit TJ")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Adanya pekerjaan ter-TECO di sistem yang tidak sesuai dengan aktual (manhours dan material consumed)') & (df['Unit'] == 'TJ')]
    df_new2 = df.loc[ (df['Risiko'] == 'Adanya pekerjaan ter-TECO di sistem yang tidak sesuai dengan aktual (manhours dan material consumed)') & (df['Unit'] == 'TJ')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Pengerjaan task yg tertunda karena kurangnya keakuratan informasi ketersediaan part dan/atau aktivitas inspeksi/temuan yang terlambat') & (df['Unit'] == 'TJ')]
    df_new4 = df.loc[ (df['Risiko'] == 'Pengerjaan task yg tertunda karena kurangnya keakuratan informasi ketersediaan part dan/atau aktivitas inspeksi/temuan yang terlambat') & (df['Unit'] == 'TJ')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai procedure sehingga menyebabkan accident/incident') & (df['Unit'] == 'TJ')]
    df_new6 = df.loc[ (df['Risiko'] == 'Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai procedure sehingga menyebabkan accident/incident') & (df['Unit'] == 'TJ')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Tidak dapat memberikan feedback kepada permintaan/komplain customer dengan baik melalui pemenuhan kriteria keberhasilan proyek') & (df['Unit'] == 'TJ')]
    df_new8 = df.loc[ (df['Risiko'] == 'Tidak dapat memberikan feedback kepada permintaan/komplain customer dengan baik melalui pemenuhan kriteria keberhasilan proyek') & (df['Unit'] == 'TJ')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai prosedur') & (df['Unit'] == 'TJ')]
    df_new10 = df.loc[ (df['Risiko'] == 'Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai prosedur') & (df['Unit'] == 'TJ')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5
    
     #data6
    df_new11 = df.loc[ (df['Risiko'] == 'Adanya accident/incident & rework yang berdampak pada project') & (df['Unit'] == 'TJ')]
    df_new12 = df.loc[ (df['Risiko'] == 'Adanya accident/incident & rework yang berdampak pada project') & (df['Unit'] == 'TJ')]
    df_new12 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new11['Nilai Likelihood Risiko Inheren'] = df_new11['Nilai Likelihood Risiko Inheren'] - 0.7
    df_new11['Nilai Consequence Risiko Inheren'] = df_new11['Nilai Consequence Risiko Inheren'] - 0.7
    df_new12['Nilai Consequence Risiko Inheren'] = df_new12['Nilai Consequence (Risiko Residu)'] - 0.7
    df_new12['Nilai Likelihood Risiko Inheren'] = df_new12['Nilai Likelihood (Risiko Residu)'] - 0.7
    
     #data7
    df_new13 = df.loc[ (df['Risiko'] == 'TAT melebihi target') & (df['Unit'] == 'TJ')]
    df_new14 = df.loc[ (df['Risiko'] == 'TAT melebihi target') & (df['Unit'] == 'TJ')]
    df_new14 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new13['Nilai Likelihood Risiko Inheren'] = df_new13['Nilai Likelihood Risiko Inheren'] - 0.1
    df_new13['Nilai Consequence Risiko Inheren'] = df_new13['Nilai Consequence Risiko Inheren'] - 0.1
    df_new14['Nilai Consequence Risiko Inheren'] = df_new14['Nilai Consequence (Risiko Residu)'] - 0.1
    df_new14['Nilai Likelihood Risiko Inheren'] = df_new14['Nilai Likelihood (Risiko Residu)'] - 0.1

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Adanya pekerjaan ter-TECO di sistem yang tidak sesuai dengan aktual (manhours dan material consumed)'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Pengerjaan task yg tertunda karena kurangnya keakuratan informasi ketersediaan part dan/atau aktivitas inspeksi/temuan yang terlambat'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai procedure sehingga menyebabkan accident/incident'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Tidak dapat memberikan feedback kepada permintaan/komplain customer dengan baik melalui pemenuhan kriteria keberhasilan proyek'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Kelalaian dalam pelaksanaan jobcard/MDR yang tidak sesuai prosedur'), df_new10.assign(Risk='')])
    con6 = pd.concat([df_new11.assign(Risk='Adanya accident/incident & rework yang berdampak pada project'), df_new12.assign(Risk='')])
    con7 = pd.concat([df_new13.assign(Risk='TAT melebihi target'), df_new14.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con6,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C2", "C2"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con7,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C1", "C1"])


    sns.move_legend(ax, "lower center", bbox_to_anchor=(1, 1))
    plt.title('TJ Risk Map')
    st.pyplot(fig)
    
def tl():
    st.title("Risk Management Matrix Unit TL")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Keterlambatan pengiriman material U/S ke shop') & (df['Unit'] == 'TL')]
    df_new2 = df.loc[ (df['Risiko'] == 'Keterlambatan pengiriman material U/S ke shop') & (df['Unit'] == 'TL')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Adanya accident incident yang terjadi akibat kualitas maintenance') & (df['Unit'] == 'TL')]
    df_new4 = df.loc[ (df['Risiko'] == 'Adanya accident incident yang terjadi akibat kualitas maintenance') & (df['Unit'] == 'TL')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Target yang tidak tercapai sesuai dengan SLA') & (df['Unit'] == 'TL')]
    df_new6 = df.loc[ (df['Risiko'] == 'Target yang tidak tercapai sesuai dengan SLA') & (df['Unit'] == 'TL')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Adanya aktivitas maintenance serta manhours yang tidak tercapture') & (df['Unit'] == 'TL')]
    df_new8 = df.loc[ (df['Risiko'] == 'Adanya aktivitas maintenance serta manhours yang tidak tercapture') & (df['Unit'] == 'TL')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Potensi revenue tidak terbilling karena keterlambatan tagihan atau ketidaklengkapan dokumen') & (df['Unit'] == 'TL')]
    df_new10 = df.loc[ (df['Risiko'] == 'Potensi revenue tidak terbilling karena keterlambatan tagihan atau ketidaklengkapan dokumen') & (df['Unit'] == 'TL')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5
  
  

    ##concat
    con = pd.concat([df_new.assign(Risk='Keterlambatan pengiriman material U/S ke shop'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya accident incident yang terjadi akibat kualitas maintenance'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Target yang tidak tercapai sesuai dengan SLA'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Adanya aktivitas maintenance serta manhours yang tidak tercapture'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Potensi revenue tidak terbilling karena keterlambatan tagihan atau ketidaklengkapan dokumen'), df_new10.assign(Risk='')])
   
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TL Risk Map')
    st.pyplot(fig)   
    
    
def tm():
    st.title("Risk Management Matrix Unit TM")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Operating profit tidak mencapai target atau minus') & (df['Unit'] == 'TM')]
    df_new2 = df.loc[ (df['Risiko'] == 'Operating profit tidak mencapai target atau minus') & (df['Unit'] == 'TM')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Terjadi keterlambatan update informasi ke stakeholder') & (df['Unit'] == 'TM')]
    df_new4 = df.loc[ (df['Risiko'] == 'Terjadi keterlambatan update informasi ke stakeholder') & (df['Unit'] == 'TM')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Ketidaksesuaian dalam audit ekternal & Legal action dari vendor') & (df['Unit'] == 'TM')]
    df_new6 = df.loc[ (df['Risiko'] == 'Ketidaksesuaian dalam audit ekternal & Legal action dari vendor') & (df['Unit'] == 'TM')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'SLA pemenuhan material tidak tercapai') & (df['Unit'] == 'TM')]
    df_new8 = df.loc[ (df['Risiko'] == 'SLA pemenuhan material tidak tercapai') & (df['Unit'] == 'TM')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
   #data5
    df_new9 = df.loc[ (df['Risiko'] == 'Tidak tercapainya target HCR yang berdampak pada bisnis dan operasional') & (df['Unit'] == 'TM')]
    df_new10 = df.loc[ (df['Risiko'] == 'Tidak tercapainya target HCR yang berdampak pada bisnis dan operasional') & (df['Unit'] == 'TM')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5
  

    ##concat
    con = pd.concat([df_new.assign(Risk='Operating profit tidak mencapai target atau minus'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Terjadi keterlambatan update informasi ke stakeholder'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Ketidaksesuaian dalam audit ekternal & Legal action dari vendor'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='SLA pemenuhan material tidak tercapai'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Tidak tercapainya target HCR yang berdampak pada bisnis dan operasional'), df_new10.assign(Risk='')])
   
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])
  


    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TM Risk Map')
    st.pyplot(fig)   
    
    
def tp():
    st.title("Risk Management Matrix Unit TP")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['Risiko'] == 'Penurunan performa utilisasi pesawat terhadap RKAP (PBTH GA)') & (df['Unit'] == 'TP')]
    df_new2 = df.loc[ (df['Risiko'] == 'Penurunan performa utilisasi pesawat terhadap RKAP (PBTH GA)') & (df['Unit'] == 'TP')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['Risiko'] == 'Pembatalan/ pengurangan atau perubahan jadwal maintenance GA & NGA') & (df['Unit'] == 'TP')]
    df_new4 = df.loc[ (df['Risiko'] == 'Pembatalan/ pengurangan atau perubahan jadwal maintenance GA & NGA') & (df['Unit'] == 'TP')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Risiko'] == 'Cash in kurang dari monthly plan') & (df['Unit'] == 'TP')]
    df_new6 = df.loc[ (df['Risiko'] == 'Cash in kurang dari monthly plan') & (df['Unit'] == 'TP')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Risiko'] == 'Customer tidak kembali melakukan perawatan pesawat di GMF') & (df['Unit'] == 'TP')]
    df_new8 = df.loc[ (df['Risiko'] == 'Customer tidak kembali melakukan perawatan pesawat di GMF') & (df['Unit'] == 'TP')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['KPI'] == 'Progress Billing') & (df['Unit'] == 'TP')]
    df_new10 = df.loc[ (df['KPI'] == 'Progress Billing') & (df['Unit'] == 'TP')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.1
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.1
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.1
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.1
    
     #data6
    df_new11 = df.loc[ (df['KPI'] == 'Information Capital readiness') & (df['Unit'] == 'TP')]
    df_new11 = df.loc[ (df['KPI'] == 'Information Capital readiness') & (df['Unit'] == 'TP')]
    df_new12 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new11['Nilai Likelihood Risiko Inheren'] = df_new11['Nilai Likelihood Risiko Inheren'] - 0.47
    df_new11['Nilai Consequence Risiko Inheren'] = df_new11['Nilai Consequence Risiko Inheren'] - 0.47
    df_new12['Nilai Consequence Risiko Inheren'] = df_new12['Nilai Consequence (Risiko Residu)'] - 0.47
    df_new12['Nilai Likelihood Risiko Inheren'] = df_new12['Nilai Likelihood (Risiko Residu)'] - 0.47
    

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Penurunan performa utilisasi pesawat terhadap RKAP (PBTH GA)'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Pembatalan/ pengurangan atau perubahan jadwal maintenance GA & NGA'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Cash in kurang dari monthly plan'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Customer tidak kembali melakukan perawatan pesawat di GMF'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Keterlambatan pembayaran oleh pelanggan dan Cash in yang tertunda'), df_new10.assign(Risk='')])
    con6 = pd.concat([df_new11.assign(Risk='Target Go-live program inisiatif digital Korporat tidak tercapai'), df_new12.assign(Risk='')])
   
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con6,
                     style='Risk', hue='Risk', ax=ax, s=160, palette=["C1", "C1"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TP Risk Map')
    st.pyplot(fig)
    
def tq():
    st.title("Risk Management Matrix Unit TQ")
    df = pd.read_excel(open('data.xlsx', 'rb'), sheet_name='RR2023')
    
     #data 1
    df_new = df.loc[ (df['ID'] == '160') & (df['Unit'] == 'TQ')]
    df_new2 = df.loc[ (df['ID'] == '160') & (df['Unit'] == 'TQ')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6


    #data2
    df_new3 = df.loc[ (df['ID'] == '163') & (df['Unit'] == 'TQ')]
    df_new4 = df.loc[ (df['ID'] == '163') & (df['Unit'] == 'TQ')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['ID'] == '164') & (df['Unit'] == 'TQ')]
    df_new6 = df.loc[ (df['ID'] == '164') & (df['Unit'] == 'TQ')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['ID'] == '166') & (df['Unit'] == 'TQ')]
    df_new8 = df.loc[ (df['ID'] == '166') & (df['Unit'] == 'TQ')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3
    
     #data5
    df_new9 = df.loc[ (df['ID'] == '173') & (df['Unit'] == 'TQ')]
    df_new10 = df.loc[ (df['ID'] == '173') & (df['Unit'] == 'TQ')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5
    
     #data6
    df_new11 = df.loc[ (df['ID'] == '174') & (df['Unit'] == 'TQ')]
    df_new12 = df.loc[ (df['ID'] == '174') & (df['Unit'] == 'TQ')]
    df_new12 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new11['Nilai Likelihood Risiko Inheren'] = df_new11['Nilai Likelihood Risiko Inheren'] - 0.7
    df_new11['Nilai Consequence Risiko Inheren'] = df_new11['Nilai Consequence Risiko Inheren'] - 0.7
    df_new12['Nilai Consequence Risiko Inheren'] = df_new12['Nilai Consequence (Risiko Residu)'] - 0.7
    df_new12['Nilai Likelihood Risiko Inheren'] = df_new12['Nilai Likelihood (Risiko Residu)'] - 0.7
    
     #data7
    df_new13 = df.loc[ (df['ID'] == '193') & (df['Unit'] == 'TQ')]
    df_new14 = df.loc[ (df['ID'] == '193') & (df['Unit'] == 'TQ')]
    df_new14 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new13['Nilai Likelihood Risiko Inheren'] = df_new13['Nilai Likelihood Risiko Inheren'] - 0.1
    df_new13['Nilai Consequence Risiko Inheren'] = df_new13['Nilai Consequence Risiko Inheren'] - 0.1
    df_new14['Nilai Consequence Risiko Inheren'] = df_new14['Nilai Consequence (Risiko Residu)'] - 0.1
    df_new14['Nilai Likelihood Risiko Inheren'] = df_new14['Nilai Likelihood (Risiko Residu)'] - 0.1

  

    ##concat
    con = pd.concat([df_new.assign(Risk='Perjalanan dinas mengalami hambatan/tidak terlaksana'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Kualitas produk yang direlease oleh Certifying Staff GMF tidak bagus dan mendapatkan komplain dari customer'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Turn Around Time suatu project melebihi batas yang sudah di rencanakan'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Masih ditemukannya finding yang sama dari audit internal maupun external'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Kurangnya kompetensi personnel'), df_new10.assign(Risk='')])
    con6 = pd.concat([df_new11.assign(Risk='Tidak terlaksananya program terkait Organization Capital Readiness'), df_new12.assign(Risk='')])
    con7 = pd.concat([df_new13.assign(Risk='Evaluasi pengajuan penambahan capability Aircraft, Engine, APU dan Component yang melebihi waktu target'), df_new14.assign(Risk='')])
   
    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con6,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C2", "C2"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con7,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C1", "C1"])


    sns.move_legend(ax, "lower center", bbox_to_anchor=(1, 1))
    plt.title('TQ Risk Map')
    st.pyplot(fig)
    

def tr():
    


    st.title("Risk Management Matrix Unit TR")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya akurat dalam mengelola proyek'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya pekerjaan yang tidak ter-record dengan baik'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TR Risk Map')
    st.pyplot(fig)

def tu():
    


    st.title("Risk Management Matrix Unit TU")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya akurat dalam mengelola proyek'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya pekerjaan yang tidak ter-record dengan baik'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TU Risk Map')
    st.pyplot(fig)

def tv():
    


    st.title("Risk Management Matrix Unit TV")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya akurat dalam mengelola proyek'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya pekerjaan yang tidak ter-record dengan baik'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TV Risk Map')
    st.pyplot(fig)

def tx():
    


    st.title("Risk Management Matrix Unit TX")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya akurat dalam mengelola proyek'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya pekerjaan yang tidak ter-record dengan baik'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TX Risk Map')
    st.pyplot(fig)

def tz():
    


    st.title("Risk Management Matrix Unit TZ")
    df = pd.read_excel('data.xlsx')
    df2 = pd.read_excel('data.xlsx')

    #data 1
    df_new = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df.loc[ (df['Title'] == 'Kurang akurat dalam mengelola proyek') & (df['Unit'] == 'TB')]
    df_new2 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new['Nilai Likelihood Risiko Inheren'] = df_new['Nilai Likelihood Risiko Inheren'] - 0.6
    df_new['Nilai Consequence Risiko Inheren'] = df_new['Nilai Consequence Risiko Inheren'] - 0.6
    df_new2['Nilai Consequence Risiko Inheren'] = df_new2['Nilai Consequence (Risiko Residu)'] - 0.6
    df_new2['Nilai Likelihood Risiko Inheren'] = df_new2['Nilai Likelihood (Risiko Residu)'] - 0.6

    #data2
    df_new3 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df.loc[ (df['Title'] == 'Adanya pekerjaan yang tidak ter-record dengan baik') & (df['Unit'] == 'TB')]
    df_new4 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new3['Nilai Likelihood Risiko Inheren'] = df_new3['Nilai Likelihood Risiko Inheren'] - 0.2
    df_new3['Nilai Consequence Risiko Inheren'] = df_new3['Nilai Consequence Risiko Inheren'] - 0.2
    df_new4['Nilai Consequence Risiko Inheren'] = df_new4['Nilai Consequence (Risiko Residu)'] - 0.2
    df_new4['Nilai Likelihood Risiko Inheren'] = df_new4['Nilai Likelihood (Risiko Residu)'] - 0.2

    #data3
    df_new5 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df.loc[ (df['Title'] == 'Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik') & (df['Unit'] == 'TB')]
    df_new6 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new5['Nilai Likelihood Risiko Inheren'] = df_new5['Nilai Likelihood Risiko Inheren'] - 0.8
    df_new5['Nilai Consequence Risiko Inheren'] = df_new5['Nilai Consequence Risiko Inheren'] - 0.8
    df_new6['Nilai Consequence Risiko Inheren'] = df_new6['Nilai Consequence (Risiko Residu)'] - 0.8
    df_new6['Nilai Likelihood Risiko Inheren'] = df_new6['Nilai Likelihood (Risiko Residu)'] - 0.8

    #data4
    df_new7 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df.loc[ (df['Title'] == 'Kesalahan dalam menentukan material yang dibutuhkan') & (df['Unit'] == 'TB')]
    df_new8 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new7['Nilai Likelihood Risiko Inheren'] = df_new7['Nilai Likelihood Risiko Inheren'] - 0.3
    df_new7['Nilai Consequence Risiko Inheren'] = df_new7['Nilai Consequence Risiko Inheren'] - 0.3
    df_new8['Nilai Consequence Risiko Inheren'] = df_new8['Nilai Consequence (Risiko Residu)'] - 0.3
    df_new8['Nilai Likelihood Risiko Inheren'] = df_new8['Nilai Likelihood (Risiko Residu)'] - 0.3

    #data5
    df_new9 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df.loc[ (df['Title'] == 'Remove install component tidak sesuai antara sistem dan actual') & (df['Unit'] == 'TB')]
    df_new10 = df_new2.drop(['Nilai Consequence Risiko Inheren', 'Nilai Likelihood Risiko Inheren'], axis='columns')
    df_new9['Nilai Likelihood Risiko Inheren'] = df_new9['Nilai Likelihood Risiko Inheren'] - 0.5
    df_new9['Nilai Consequence Risiko Inheren'] = df_new9['Nilai Consequence Risiko Inheren'] - 0.5
    df_new10['Nilai Consequence Risiko Inheren'] = df_new10['Nilai Consequence (Risiko Residu)'] - 0.5
    df_new10['Nilai Likelihood Risiko Inheren'] = df_new10['Nilai Likelihood (Risiko Residu)'] - 0.5


    ##concat
    con = pd.concat([df_new.assign(Risk='Kurangnya akurat dalam mengelola proyek'), df_new2.assign(Risk='')])
    con2 = pd.concat([df_new3.assign(Risk='Adanya pekerjaan yang tidak ter-record dengan baik'), df_new4.assign(Risk='')])
    con3 = pd.concat([df_new5.assign(Risk='Implementasi dan aplikasi manhours dan material plan yang belum berjalan dengan baik'), df_new6.assign(Risk='')])
    con4 = pd.concat([df_new7.assign(Risk='Kesalahan dalam menentukan material yang dibutuhkan'), df_new8.assign(Risk='')])
    con5 = pd.concat([df_new9.assign(Risk='Remove install component tidak sesuai antara sistem dan actual'), df_new10.assign(Risk='')])

    ##design
    img = plt.imread('backgroundrisk.png')
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C0", "C0"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con2,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C6", "C6"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con3,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C5", "C5"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con4,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C3", "C3"])
    sns.scatterplot(x='Nilai Consequence Risiko Inheren' , y='Nilai Likelihood Risiko Inheren', data=con5,
                    style='Risk', hue='Risk', ax=ax, s=160, palette=["C4", "C4"])

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title('TZ Risk Map')
    st.pyplot(fig)
    

page_names_to_funcs = {
    "Belum ada Unit": intro,
    "TA": ta,
    "TB": tb,
    "TC" : tc,
    "TD" : td,
    "TE" : te,
    "TF" : tf,
    "TH" : th,
    "TI" : ti,
    "TJ" : tj,
    "TL" : tl,
    "TM" : tm,
    "TP" : tp,
    "TQ" : tq,
    "TR" : tr,
    "TU" :tu,
    "TV" : tv,
    "TX" :tx,
    "TZ" : tz
}

demo_name = st.sidebar.selectbox("Silahkan Pilih Unit", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()