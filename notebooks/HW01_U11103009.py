from obspy import UTCDateTime, read_inventory
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
# 參數設定
client = Client("IRIS")
starttime = UTCDateTime("2025-10-07T23:52:12")
duration = 120  # 秒
endtime = starttime + duration
# 選擇一個常見的台站 (可根據需求更改)
network = "TW"
station = "NACB"
location = ""
channel = "BHZ"
# 下載地震波資料
st = client.get_waveforms(network, station, location, channel, starttime, endtime)
# 下載台站資訊 (用於繪圖)
inv = client.get_stations(network=network, station=station, location=location, channel=channel, level="response")
# 畫圖
fig = plt.figure(figsize=(10, 4))
st.plot(outfile="waveform.png", fig=fig, title=f"{network}.{station}.{location}.{channel} {starttime} ~ {endtime}")
print("地震波圖已儲存為 waveform.png")