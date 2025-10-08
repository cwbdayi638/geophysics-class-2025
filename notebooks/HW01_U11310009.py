from obspy import UTCDateTime, read_inventory
from obspy.clients.fdsn import Client

import matplotlib.pyplot as plt

# 參數設定
client = Client("IRIS")
starttime = UTCDateTime("2025-10-07T23:52:12")
endtime = starttime + 120

# 取得台灣地區的測站清單
inventory = client.get_stations(network="*", station="*", location="*", channel="BH?", 
                               starttime=starttime, endtime=endtime,
                               minlatitude=21.8, maxlatitude=25.4, minlongitude=119.3, maxlongitude=122.1,
                               level="response")

# 選擇第一個可用測站
net = inventory[0].code
sta = inventory[0][0].code
loc = inventory[0][0][0].location_code
cha = inventory[0][0][0].code

# 下載波形資料
st = client.get_waveforms(network=net, station=sta, location=loc, channel=cha,
                         starttime=starttime, endtime=endtime)

# 畫圖並存檔
fig = plt.figure(figsize=(10, 4))
st.plot(fig=fig, outfile="waveform.png", size=(1000, 300), dpi=150, title=f"{net}.{sta}.{loc}.{cha}")
plt.close(fig)
print(f"已儲存波形圖於 waveform.png，測站: {net}.{sta}.{loc}.{cha}")