import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
a1=pd.read_csv("D:/Downloads file/archive.zip")
print(a1) 
text=" ".join(titl.split()[0] for titl in a1.title)
word_cloud=WordCloud(collocations=True,background_color='white').generate(text)
plt.imshow(word_cloud, interpolation='gaussian')
plt.show()
