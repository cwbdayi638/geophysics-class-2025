from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client

import matplotlib.pyplot as plt

# 設定 IRIS FDSN client
client = Client("IRIS")

# 設定時間與持續秒數
starttime = UTCDateTime("2025-10-07T23:52:12")
duration = 120
endtime = starttime + duration

# 台灣常用測站 (例如: TW.TWGB)
network = "TW"
station = "NACB"  # 可改成其他台灣測站
location = ""
channel = "BHZ"   # 可改成其他通道

# 抓取地震波資料
st = client.get_waveforms(network, station, location, channel, starttime, endtime)

# 畫圖並存檔
fig = plt.figure()
st.plot(outfile="/workspaces/geophysics-class-2025/notebooks/HW01_U11310029_waveform.png", fig=fig)
plt.close(fig)