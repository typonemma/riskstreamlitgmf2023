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

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
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
    plt.title('TD Risk Map')
    st.pyplot(fig)

def td():
    


    st.title("Risk Management Matrix Unit TD")
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
    plt.title('TB Risk Map')
    st.pyplot(fig)

def td():
    


    st.title("Risk Management Matrix Unit TD")
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
    plt.title('TB Risk Map')
    st.pyplot(fig)
    
def ti():
    


    st.title("Risk Management Matrix Unit TI")
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
    plt.title('TI Risk Map')
    st.pyplot(fig)

def tj():
    


    st.title("Risk Management Matrix Unit TJ")
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
    plt.title('TJ Risk Map')
    st.pyplot(fig)
    
def tm():
    


    st.title("Risk Management Matrix Unit TM")
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
    plt.title('TM Risk Map')
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
    "TI" : ti,
    "TJ" : tj,
    "TM" : tm,
    "TR" : tr,
    "TU" :tu,
    "TV" : tv,
    "TX" :tx,
    "TZ" : tz
}

demo_name = st.sidebar.selectbox("Silahkan Pilih Unit", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()