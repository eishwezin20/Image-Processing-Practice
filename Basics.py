from skimage import io
img = io.imread('????.jpg')   # img file name
io.imshow(img)

#Getting Image Resolution
img.shape

#Getting Pixel Values
import pandas as pd
df = pd.DataFrame(img.flatten())
filepath = 'pixel_values1.xlsx'
df.to_excel(filepath, index=False)

#Convert to YPbPr
img_ypbpr= color.rgb2ypbpr(img)
#Convert back to RGB
img_rgb= color.ypbpr2rgb(img_ypbpr)

#Saving an Image
io.imsave("??????.jpg", img_ypbpr)
