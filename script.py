from PIL import Image
from matplotlib import image
import os

pack = list(os.scandir('before\\'))

for num in range(len(pack)):
    img = Image.open('before\\' + pack[num].name)
    img.save('afther\\' + pack[num].name + '.webp', format="WEBP")