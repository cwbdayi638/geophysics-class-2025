from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy import Stream
import matplotlib.pyplot as plt

# === 1. 建立 IRIS 客戶端 ===
client = Client("IRIS")

# === 2. 設定時間區段 ===
starttime = UTCDateTime("2025-10-07T23:52:12")
endtime = starttime + 120  # 120 秒

# === 3. 台灣 TW 網路測站清單 ===
stations = ["KMNB", "NACB", "SSLB", "TPUB", "TWGB", "YHNB", "YULB"]

# === 4. 嘗試逐一下載測站資料 ===
st = Stream()
for sta in stations:
    try:
        tr = client.get_waveforms(
            network="TW", 
            station=sta, 
            location="*", 
            channel="BH?", 
            starttime=starttime, 
            endtime=endtime
        )
        st += tr
        print(f"✅ 成功下載 {sta} 測站的地震波")
    except Exception as e:
        print(f"⚠️ {sta} 下載失敗：{e}")

# === 5. 檢查是否有成功的資料 ===
if len(st) == 0:
    print("❌ 沒有成功下載到任何地震波。")
else:
    # 去均值與濾波
    st.detrend("demean")
    st.filter("bandpass", freqmin=1, freqmax=10)

    # === 6. 畫波形圖 ===
    fig = plt.figure(figsize=(10, 6))
    st.plot(equal_scale=False, show=False, fig=fig)
    plt.title("TW Network Seismic Waveforms - 2025/10/07 23:52:12 UTC")
    plt.savefig("waveform.png", dpi=150)
    print("📈 圖檔已儲存為 waveform.png")
