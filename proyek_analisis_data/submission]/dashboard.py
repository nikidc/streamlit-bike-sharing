import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import calendar
sns.set(style='dark')

# menyiapkan data 
#1
def data_peminjam_berdasarkan_bulan(df):
    data_peminjam_berdasarkan_bulan = df.groupby(['mnth', 'yr']).agg({'cnt': 'sum'}).reset_index()
    data_peminjam_berdasarkan_bulan.month = pd.Categorical(df.mnth, categories=list(calendar.month_abbr)[1:], ordered=True)
    return data_peminjam_berdasarkan_bulan

#2
def data_peminjam_tahun1(df):
    data_peminjam_tahun1 = df[df.yr == 0]
    return data_peminjam_tahun1

#3
def data_peminjam_tahun2(df):
    data_peminjam_tahun2 = df[df.yr == 1]
    return data_peminjam_tahun2

#4
def dfg(df):
    dfg = df.groupby(["mnth", "yr"]).agg({'registered': 'sum', 'casual': 'sum','cnt': 'sum'}).reset_index()
    dfg.month = pd.Categorical(bike_day_df.mnth, categories=list(calendar.month_abbr)[1:], ordered=True)
    return dfg


#menyiapkan dataframe
# load berkas bike_day_df.csv
bike_day_df = pd.read_csv("proyek_analisis_data/submission]/bike_day_df.csv")

# mengurutkan DataFrame berdasarkan order_date serta memastikan kedua kolom tersebut bertipe datetime
datetime_columns = ["dteday"]
# bike_day_df.reset_index(inplace=True)

for column in datetime_columns:
    bike_day_df[column] = pd.to_datetime(bike_day_df[column])

# membuat filter dengan widget date input serta menambahkan logo di sidebar
min_date = bike_day_df["dteday"].min()
max_date = bike_day_df["dteday"].max()

# SIDEBAR sekaligus filter
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# filter data menggunakan
main_df = bike_day_df[(bike_day_df["dteday"] >= str(start_date)) & 
                (bike_day_df["dteday"] <= str(end_date))]

# helper dipanggil
data_peminjam_berdasarkan_bulan = data_peminjam_berdasarkan_bulan(main_df)
dfg = dfg(main_df)
data_peminjam_tahun1 = data_peminjam_tahun1(data_peminjam_berdasarkan_bulan)
data_peminjam_tahun2 = data_peminjam_tahun2(data_peminjam_berdasarkan_bulan)


########## MULAI VIZ ###################
# header 1st
st.header('Bike Sharing :sparkles:')

# informasi mengenai daily_orders
st.subheader('by Niki D')


# col1, col2 = st.columns(2)

# with col1:
#     total_rent = bike_day_df.cnt.sum()
#     st.metric("Total peminjaman", value=total_rent)

# viz
# 2 fig at 1 img
st.subheader("Bulan Peminjaman terbaik dan terburuk")
st.caption("Tahun 2011")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35,15))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="cnt", y="mnth", data=data_peminjam_tahun1.sort_values(by="cnt", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel("Bulan", fontsize=30)
ax[0].set_xlabel(None)
ax[0].set_title("Bulan Peminjaman Terbaik", loc="center", fontsize=59)
ax[0].tick_params(axis='y', labelsize=37)
ax[0].tick_params(axis='x', labelsize=37)

sns.barplot(x="cnt", y="mnth", data=data_peminjam_tahun1.sort_values(by="cnt", ascending=True).head(5), palette=colors,ax=ax[1])
ax[1].set_ylabel("Bulan", fontsize=37)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Bulan Peminjaman Terburuk", loc="center", fontsize=55)
ax[1].tick_params(axis='y', labelsize=37)
ax[1].tick_params(axis='x', labelsize=37)

plt.suptitle("Performa terbaik dan terburuk peminjaman sepeda", fontsize=60)
st.pyplot(fig)
st.write("Dapat dilihat dari grafik yang ditampilkan Bulan peminjaman Terbaik dan Terburuk")


#Viz 2 
st.subheader("Bulan Peminjaman terbaik dan terburuk")
st.caption("Tahun 2012")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35,15))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="cnt", y="mnth", data=data_peminjam_tahun2.sort_values(by="cnt", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel("Bulan", fontsize=30)
ax[0].set_xlabel(None)
ax[0].set_title("Bulan Peminjaman Terbaik", loc="center", fontsize=59)
ax[0].tick_params(axis='y', labelsize=37)
ax[0].tick_params(axis='x', labelsize=37)

sns.barplot(x="cnt", y="mnth", data=data_peminjam_tahun2.sort_values(by="cnt", ascending=True).head(5), palette=colors,ax=ax[1])
ax[1].set_ylabel("Bulan", fontsize=37)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Bulan Peminjaman Terburuk", loc="center", fontsize=55)
ax[1].tick_params(axis='y', labelsize=37)
ax[1].tick_params(axis='x', labelsize=37)

plt.suptitle("Performa terbaik dan terburuk peminjaman sepeda", fontsize=60)
st.pyplot(fig)
st.write("Dapat dilihat dari grafik yang ditampilkan Bulan peminjaman Terbaik dan Terburuk")

st.markdown("""---""")
#viz 3
st.subheader("TREN PEMINJAMAN SEPEDA DARI TAHUN KE TAHUN Berdasarkan jenis membership")

st.caption("Casual")
figure = plt.figure(figsize=(10, 6)) 
plt.title("Total Peminjaman Casual Berdasarkan Tahun")
sns.lineplot(x='mnth', y='casual', data=dfg, hue='yr', marker="o") 
#max value
hfont = {'fontname':'Calibri'} # main font
ann_color = '#c449cc' # annotation color
arrowprops=dict(arrowstyle='-|>', color=ann_color, linewidth=2)
plt.annotate('September 2012', 
            xy=(9, 44500), # arrow position (x, y)
            xytext=(10, 44000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)

plt.annotate('Juli 2011', 
            xy=(7, 37000), # arrow position (x, y)
            xytext=(7.5, 37000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)

# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
orange_patch = mpatches.Patch(color='orange', label='2012')
blue_patch = mpatches.Patch(color='blue', label='2011')
plt.legend(handles=[orange_patch, blue_patch], loc="upper left", bbox_to_anchor=(1.05, 1))

plt.xticks() 
st.pyplot(figure)

#viz 4
st.caption("Terdaftar/Registered")
# viz line chart total peminjam kasual di berdasarkan Tahun
fig = plt.figure(figsize=(10, 6)) 
plt.title("Total Peminjaman Registered Berdasarkan Tahun")
sns.lineplot(x='mnth', y='registered', data=dfg, hue='yr', marker="o") 
#max value
hfont = {'fontname':'Calibri'} # main font
ann_color = '#c449cc' # annotation color
arrowprops=dict(arrowstyle='-|>', color=ann_color, linewidth=2)
plt.annotate('September 2012', 
            xy=(9, 176000), # arrow position (x, y)
            xytext=(10, 175000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)

plt.annotate('Juni 2011', 
            xy=(6, 115000), # arrow position (x, y)
            xytext=(7, 115000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)

# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
orange_patch = mpatches.Patch(color='orange', label='2012')
blue_patch = mpatches.Patch(color='blue', label='2011')
plt.legend(handles=[orange_patch, blue_patch], loc="upper left", bbox_to_anchor=(1.05, 1))
plt.xticks() 
st.pyplot(fig)

# GABUNGAN
st.caption("Gabungan")
#viz line chart total peminjam Gabungan di berdasarkan bulan
fig = plt.figure(figsize=(10, 6)) 
plt.title("Total Peminjaman Gabungan Berdasarkan Tahun")
sns.lineplot(x='mnth', y='cnt', data=dfg, hue='yr', marker="o") 
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
#max value
hfont = {'fontname':'Calibri'} # main font
ann_color = '#c449cc' # annotation color
arrowprops=dict(arrowstyle='-|>', color=ann_color, linewidth=2)
plt.annotate('September 2012', 
            xy=(9, 220000), # arrow position (x, y)
            xytext=(10, 220000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)
plt.annotate('Juni 2011', 
            xy=(6, 147500), # arrow position (x, y)
            xytext=(7, 148000), # text position (x, y)
            color='red',
            arrowprops=arrowprops,
            fontsize=16,
           **hfont)
orange_patch = mpatches.Patch(color='orange', label='2012')
blue_patch = mpatches.Patch(color='blue', label='2011')
plt.legend(handles=[orange_patch, blue_patch], loc="upper left", bbox_to_anchor=(1.05, 1))
plt.xticks() 
st.pyplot(fig)

