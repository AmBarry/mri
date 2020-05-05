import umap
import numpy as np
import os
import nibabel.freesurfer.mghformat as fsmgh

# load data

def load_brain(path):
    mgh_image = fsmgh.MGHImage.from_filename(path)
    np_data = np.asarray(mgh_image.dataobj)
    return np.reshape(np_data, (1, 256 * 256 * 256))

root = "/home/cgroza/projects/rpp-aevans-ab/nikhil/data/fs60"

i = 0
mri_data = []
mri_label = []
for subject in os.listdir(root):
    if i % 100 == 0:
        print("Loading brain", i)
    brain_path = os.path.join(root, subject, "mri", "brain.mgz")
    if os.path.exists(brain_path):
        mri_data.append(load_brain(brain_path))
        mri_label.append(subject)
        i = i + 1
mri_data = np.reshape(np.array(mri_data), (len(mri_data), 256**3))
reducer = umap.UMAP()
embedding = reducer.fit_transform(mri_data)

np.savetxt("umap_embedding.csv", embedding, delimiter = ",")
with open("umap_labels.txt", "w") as labf:
    labf.write(str(mri_label))

