# --------------------------------------------------
# 引入所需的套件
# ObsPy, numpy, matplotlib.pyplot 是繪圖的必要依賴
# 確保你的環境中已安裝： pip install obspy numpy matplotlib
# --------------------------------------------------
import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt
import numpy as np # 雖然本例可能不直接用到 numpy，但它是 ObsPy 的常見依賴

# --------------------------------------------------
# Part 1: ObsPy 應用 - 下載地震目錄並繪製地圖
# --------------------------------------------------
print("--- ObsPy 地震目錄下載與繪圖 ---")

# (1) 設定 FDSN 客戶端，我們使用 USGS/IRIS 作為範例
# client = Client("IRIS") # 國際地震資料中心
client = Client("NCEDC") # 區域資料中心，有時速度更快

# (2) 設定查詢參數 (台灣周邊地區)
# 亞洲地圖的範圍太大，我們會將地圖範圍聚焦在台灣附近（地震帶）
# 經度 (min/max): 118°E - 124°E
# 緯度 (min/max): 20°N - 28°N
minlatitude = 20.0
maxlatitude = 28.0
minlongitude = 118.0
maxlongitude = 124.0

# 時間範圍：查詢最近五年的地震
endtime = UTCDateTime.now()
starttime = endtime - 5 * 365 * 24 * 60 * 60 # 五年前

# 最小震級 (M): 為了避免下載太多小地震點
minmagnitude = 5.0 

# (3) 查詢地震目錄 (Catalog)
try:
    print(f"正在查詢 {starttime.year} 年至今，範圍 M{minmagnitude}+ 的地震...")
    catalog = client.get_events(
        starttime=starttime, 
        endtime=endtime,
        minlatitude=minlatitude,
        maxlatitude=maxlatitude,
        minlongitude=minlongitude,
        maxlongitude=maxlongitude,
        minmagnitude=minmagnitude,
        orderby='time', # 依時間排序
    )
    
    # 檢查是否下載到資料
    if len(catalog) == 0:
        print("警告：未在設定範圍內找到符合條件的地震事件。")
        # 為了能畫出圖，可以嘗試放寬查詢條件或使用預設的 Catalog
    
    print(f"成功下載 {len(catalog)} 個地震事件。")

except Exception as e:
    print(f"查詢 FDSN 失敗: {e}")
    print("使用一個空的 Catalog 來避免程式崩潰。")
    catalog = obspy.Catalog()


# (4) 繪製地圖 (ObsPy 內建功能)
# ObsPy 的 plot_map() 函數依賴 matplotlib/cartopy/basemap 來繪圖。
# 由於您可能未安裝 Cartopy 或 Basemap (常見於環境錯誤)，
# ObsPy 會盡可能使用 Matplotlib 繪製最基礎的地圖。

print("正在繪製台灣周邊地震帶地圖...")

# 設定圖形大小
fig = plt.figure(figsize=(10, 8)) 

# 使用 ObsPy Catalog 物件的 plot_map 方法
catalog.plot(
    projection='local', # 局部投影 (ObsPy 預設)
    fig=fig,
    title=f"台灣周邊 M{minmagnitude}+ 地震分佈 ({starttime.year}-{endtime.year})",
    color="depth",      # 根據深度著色
    continent_fill_color='lightgray', # 陸地顏色
    water_fill_color='skyblue',      # 海洋顏色
    entry_width=0.5,
)

# 為了確保圖上有軸線標註，我們手動設定地圖的顯示範圍
ax = plt.gca()
ax.set_xlim(minlongitude, maxlongitude)
ax.set_ylim(minlatitude, maxlatitude)
ax.set_xlabel("經度")
ax.set_ylabel("緯度")


# (5) 存檔並顯示圖形
filename = "Taiwan_Seismic_Map.png"
fig.savefig(filename, dpi=300) 
print(f"圖形已存檔為: {filename}")
plt.show()

# -----------------------------------------------
