#原程式碼
#import pygmt
#fig = pygmt.Figure()
#fig.coast(region=[119, 123, 21.5, 25.5], projection="M12c", shorelines=True, frame=True)
#fig.plot(x=[121.6], y=[24.0], style="c0.3c", color="green")
#fig.plot(x=[120.6], y=[24.2], style="c0.3c", color="red")
#fig.show()

import pygmt

fig = pygmt.Figure()

# 亞洲地圖
fig.coast(
    region=[90, 150, -15, 55], 
    projection="M18c",
    land="lightgray",
    water="lightblue",
    shorelines=True,
    frame=["af", "+tAsian Volcanic Arcs"],
)

# 火山座標
volcanoes = {
    # Japan Arc
    "Fuji": [138.73, 35.36],
    "Aso": [131.1, 32.88],
    "Tarumae": [141.37, 42.7],
    # Ryukyu Arc
    "Sakurajima": [130.67, 31.58],
    "Kuchinoerabu": [130.22, 30.45],
    # Philippine Arc
    "Mayon": [123.68, 13.26],
    "Pinatubo": [120.35, 15.13],
    "Taal": [121.0, 14.0],
    # Indonesian Arc
    "Krakatoa": [105.42, -6.1],
    "Tambora": [118.0, -8.25],
    "Merapi": [110.44, -7.54],
    "Agung": [115.51, -8.34],
    # Kurile Arc
    "Klyuchevskoy": [160.63, 56.06],
    "Ebeku": [156.0, 50.7],
}

for name, (lon, lat) in volcanoes.items():
    fig.plot(x=lon, y=lat, style="t0.4c", fill="red")
    fig.text(x=lon, y=lat, text=name, font="8p,black", justify="LM", offset="0.5c/0c")

fig.show()
