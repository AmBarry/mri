import gzip
import numpy as np
import nibabel.freesurfer.mghformat as fsmgh

mgz_file_handle = gzip.open("brain.mgz")
mgh_header = fsmgh.MGHHeader.from_fileobj(mgz_file_handle)
mgh_image = fsmgh.MGHImage.from_filename("brain.mgz")

np_data = np.asarray(mgh_image.dataobj)




os.mkdir("brain_slices")
for i in range(0, 256):
    np_data_slice = np_data[:,:,i]
    im = PIL.Image.fromarray(np_data_slice)
    im.save("brain_slices/brain{i}.png".format(i=i))


