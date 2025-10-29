
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt

# === 參數設定 ===
client = Client("IRIS")                   # IRIS 資料中心
starttime = UTCDateTime("2020-01-01T00:00:00")  # 任意有地震的時間（穩定）
endtime = starttime + 120                 # 取 120 秒波形

network = "IU"                            # 全球 IRIS 網路（穩定）
station = "ANMO"                          # 美國 Albuquerque 測站（示範站）
location = "00"                           # 通道位置代碼
channel = "BHZ"                           # 垂直分量（broadband high-gain）

print(f"使用測站: {station}")

# === 下載波形資料 ===
st = client.get_waveforms(network=network, station=station, location=location,
                          channel=channel, starttime=starttime, endtime=endtime)

# 濾波：去除高頻雜訊
st.filter("bandpass", freqmin=0.5, freqmax=5)

# === 畫圖 ===
fig = plt.figure(figsize=(10, 6))
st.plot(fig=fig, outfile="waveform.png")
print("✅ 已將地震波圖存檔為 waveform.png")
