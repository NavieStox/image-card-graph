from PIL import Image, ImageDraw
import numpy as np

IMG_DIR = '/web/data/img/'
DEFAULT_RATIO = np.array([0.3, 0,6, 0.1])
X_INDICE = 10
Y_INDICE = 10
GRADE = 10
BRIGHT_RANGE = 256 / GRADE

def trim(img, x, y, width, height):
  return img[y:y+width, x:x+height]

def trimSquare(img, x, y, size):
  return trim(img, x, y, size, size)

def cellSplit(img, x_indice, y_indice):
  row_split_img = np.array(np.array_split(img, x_indice)).flatten()
  return np.array([np.array_split(buf, y_indice, 1) for buf in row_split_img]).flatten()

if __name__=='__main__':
  gray_image = Image.open(IMG_DIR + 'Lenna.png').convert('L')
  gray_image.save(IMG_DIR + 'gray.png')
  img = np.array(gray_image)

  min_bright = np.min(img)
  max_bright = np.max(img)

  palette = Image.new('RGB', img.shape, (255, 255, 255))
  draw = ImageDraw.Draw(palette)

  y = 0
  for row in np.array_split(img, X_INDICE):
    x = 0
    for cell in np.array_split(np.array(row), Y_INDICE, 1):
      shape = np.array(cell).shape
      bright = int(np.round(np.average(cell)))
      bright = int(np.round(bright / BRIGHT_RANGE) * BRIGHT_RANGE)
      draw.rectangle(((x, y), (x + shape[1], y + shape[0])), fill=(bright, bright, bright))
      x = x + shape[1]
    y = y + shape[0]
  print(x, y)
  palette.save(IMG_DIR + 'gray.png')




  # Image.fromarray(trim_img).save(IMG_DIR + 'test.png')
