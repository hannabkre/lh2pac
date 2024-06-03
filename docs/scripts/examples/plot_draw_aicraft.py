"""# Draw an aircraft."""

from lh2pac.gemseo.utils import draw_aircraft
from matplotlib import pyplot as plt

# %%
# First,
# we draw the default aircraft:
draw_aircraft()

# %%
# Then,
# we draw an aircraft with a higher aspect ratio:
draw_aircraft({"aspect_ratio": 12}, "Higher aspect ratio")

# %%
# Lastly,
# we draw an aircraft with a lower aspect ratio:
draw_aircraft({"aspect_ratio": 7}, "Lower aspect ratio")

fig = draw_aircraft(show=False)
plt.show()
