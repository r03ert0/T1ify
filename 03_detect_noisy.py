from skimage import io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt
import numpy as np
import sys
from skimage.measure import label, regionprops
import glob
from skimage.filters.rank import entropy
from skimage.morphology import disk

def detect(path):
    # good="jpgs/t1w_OAS30001_MR_d0757_3.jpg"
    # good="jpgs/t1w_OAS30001_MR_d0129_9.jpg"
    # good="jpgs/t1w_OAS30002_MR_d0653_3.jpg"
    # bad="jpgs/t1w_OAS30672_MR_d0966_7.jpg"

    img = io.imread(path)

    if np.mean(entropy(img,disk(5))) > 4:
        labels1 = segmentation.slic(img, compactness=1, n_segments=2000)
        g = graph.rag_mean_color(img, labels1, mode='similarity')
        labels2 = graph.cut_normalized(labels1, g)
        out = color.label2rgb(labels2, img, kind='avg')

        # plt.imshow(out)
        # plt.show()

        if regionprops(labels2):
            print(path, regionprops(labels2)[0].area)
        else:
            print(path, "no regions")

def main(argv):
    files = glob.glob("jpgs/*.jpg")
    for f in files:
        detect(f)

if __name__ == "__main__":
    main(sys.argv)