import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('./ilder/ha.jpg')

plt.imshow(img)
plt.axis('off')  # Entfernt die Achsen
plt.show()