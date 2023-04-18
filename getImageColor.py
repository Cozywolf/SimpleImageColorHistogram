# %%
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [15, 10]
plt.rcParams["figure.autolayout"] = True

# %%
imgPath = './Lenna.png'
img = Image.open(imgPath)
colorCounts = set()
colors = []

# %%
for x in range(img.size[0]):
    for y in range(img.size[1]):
        colorCounts.add(img.getpixel((x, y)))
        colors.append(img.getpixel((x, y)))

# print("Total colors:", len(colorCounts))

# Create plot grid
figure, axis = plt.subplots(2, 2)

axis[0, 0].hist([color[0] for color in colors], range=(0, 255), bins=256, color='red')
axis[0, 0].set_title("Red Channel")

axis[0, 1].hist([color[1] for color in colors], range=(0, 255), bins=256, color='green')
axis[0, 1].set_title("Green Channel")

axis[1, 0].hist([color[2] for color in colors],range=(0, 255), bins=256, color='blue')
axis[1, 0].set_title("Blue Channel")

axis[1, 1].hist([round((color[0]+color[1]+color[2])/3) for color in colors],
                range=(0, 255), bins=256, color='black', alpha=0.5)
axis[1, 1].set_title("Luminance level")

plt.savefig(f'{imgPath[2:-4]}_histogram.png')

# %%
