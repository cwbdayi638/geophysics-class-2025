# Asia & Taiwan Earthquake Map - PyGMT safe version
# Requirements:
#   pip install obspy pygmt numpy
#   and GMT 6.x installed on system
# --------------------------------------------------

import sys
import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pygmt
import numpy as np

# --- basic checks ---
print("Python:", sys.version.splitlines()[0])
try:
    print("PyGMT version:", pygmt.__version__)
except Exception:
    print("Warning: cannot read pygmt.__version__")

# --------------------------------------------------
# 1) Download earthquake data (near Taiwan, last 5 years)
# --------------------------------------------------
client = Client("IRIS")

region_box = dict(
    minlatitude=20.0,
    maxlatitude=28.0,
    minlongitude=118.0,
    maxlongitude=124.0
)

endtime = UTCDateTime.now()
starttime = endtime - 5 * 365 * 24 * 60 * 60  # 5 years back
minmagnitude = 4.0

try:
    catalog = client.get_events(
        starttime=starttime,
        endtime=endtime,
        **region_box,
        minmagnitude=minmagnitude,
        orderby="time",
    )
    print(f"Downloaded {len(catalog)} events from FDSN.")
except Exception as e:
    print(f"Warning: failed to download from FDSN: {e}")
    catalog = obspy.Catalog()

# --------------------------------------------------
# 2) Parse or use demo data
# --------------------------------------------------
if len(catalog) == 0:
    print("Using demo (synthetic) data.")
    lons = [121.0, 122.5, 120.5]
    lats = [23.5, 24.0, 22.0]
    mags = [5.2, 4.8, 5.5]
    depths = [20.0, 35.0, 10.0]  # km
else:
    lons = [ev.origins[0].longitude for ev in catalog]
    lats = [ev.origins[0].latitude for ev in catalog]
    mags = [ev.magnitudes[0].mag for ev in catalog]
    depths = [ev.origins[0].depth / 1000.0 for ev in catalog]  # convert m->km

# sizes from magnitude (tweak scale if needed)
sizes = [0.06 * m for m in mags]  # in cm units for style string (e.g., c0.3c)

# --------------------------------------------------
# 3) Make CPT and convert depths -> HEX colors (safe path)
# --------------------------------------------------
min_depth = float(np.min(depths))
max_depth = float(np.max(depths))
# create CPT file in current GMT session
pygmt.makecpt(cmap="turbo", series=[min_depth, max_depth, (max_depth - min_depth) / 8.0], continuous=True)

# Try to get color in HEX via pygmt.cpt.get_rgb_color (may exist in your pygmt)
colors = []
use_pygmt_get_rgb = False
try:
    # many pygmt versions provide pygmt.cpt.get_rgb_color(value) -> '#rrggbb'
    for d in depths:
        hexcol = pygmt.cpt.get_rgb_color(d)
        colors.append(hexcol)
    use_pygmt_get_rgb = True
except Exception:
    # fallback: try to use matplotlib (if available) to map depths to colormap
    try:
        import matplotlib.cm as cm
        import matplotlib.colors as mcolors
        cmap = cm.get_cmap("turbo")
        norm = mcolors.Normalize(vmin=min_depth, vmax=max_depth)
        for d in depths:
            rgba = cmap(norm(d))
            # convert rgba (0-1) to hex
            hexcol = mcolors.to_hex(rgba)
            colors.append(hexcol)
        print("Used matplotlib fallback to generate HEX colors from depths.")
    except Exception:
        # last resort: use a single color for all
        print("Warning: cannot map depth to CPT colors (no pygmt.get_rgb and no matplotlib). Using red as default.")
        colors = ["red" for _ in depths]

# --------------------------------------------------
# 4) Plot (Asia base + Taiwan inset), using per-point fill=HEX (no +z, no fill=True)
# --------------------------------------------------
fig = pygmt.Figure()

# Asia basemap
fig.basemap(region=[60, 150, -10, 60], projection="M10i", frame=True)
fig.coast(land="gray90", water="skyblue", borders=1, shorelines=True, resolution="i")

# Plot each quake as separate call with style string sized and fill=hex
for lon, lat, sz, col in zip(lons, lats, sizes, colors):
    # style expects e.g. "c0.36c" where 0.36 is diameter in cm
    style = f"c{sz}c"
    fig.plot(x=lon, y=lat, style=style, fill=col, pen="0.3p,black")

# Add colorbar: create a separate CPT image item for legend.
# Colorbar expects a CPT object; use the CPT file created earlier by makecpt
fig.colorbar(cmap=True, frame=["a10f5", "x+lDepth (km)"], position="JMR+w5c/0.4c+o0.5c/0c+h")

# Taiwan inset: a smaller map at top-right
with fig.inset(position="jTR+w6c/6c+o0.2c", box="+p1p,black", margin=0.2):
    fig.coast(
        region=[region_box["minlongitude"], region_box["maxlongitude"],
                region_box["minlatitude"], region_box["maxlatitude"]],
        projection="M6c",
        land="tan",
        water="skyblue",
        shorelines="1p,black",
        resolution="h",
        frame=["a1f0.5", "+t'Taiwan Region'"]
    )
    for lon, lat, sz, col in zip(lons, lats, sizes, colors):
        fig.plot(x=lon, y=lat, style=f"c{sz}c", fill=col, pen="0.3p,black")
fig.inset(end=True)

# Title
fig.text(x=105, y=55, text=f"Asia & Taiwan Earthquakes (M≥{minmagnitude})", font="14p,Helvetica-Bold,black")

# Save & show
outfile = "Asia_Taiwan_Seismic_Map_safe.png"
fig.savefig(outfile, dpi=300)
print("Saved image:", outfile)
fig.show()
