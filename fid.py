# example of calculating the frechet inception distance in Keras for cifar10
import numpy
from numpy import cov
from numpy import trace
from numpy import iscomplexobj
from numpy import asarray
from numpy.random import shuffle
from scipy.linalg import sqrtm
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.datasets.mnist import load_data
from skimage.transform import resize
# from keras.datasets import cifar10
import glob
from PIL import Image, ImageFilter
 
 
# calculate frechet inception distance
def calculate_fid(model, images1, images2):
	# calculate activations
	act1 = model.predict(images1)
	act2 = model.predict(images2)
	# calculate mean and covariance statistics
	mu1, sigma1 = act1.mean(axis=0), cov(act1, rowvar=False)
	mu2, sigma2 = act2.mean(axis=0), cov(act2, rowvar=False)
	# calculate sum squared difference between means
	ssdiff = numpy.sum((mu1 - mu2)**2.0)
	# calculate sqrt of product between cov
	covmean = sqrtm(sigma1.dot(sigma2))
	# check and correct imaginary numbers from sqrt
	if iscomplexobj(covmean):
		covmean = covmean.real
	# calculate score
	fid = ssdiff + trace(sigma1 + sigma2 - 2.0 * covmean)
	return fid
 
# prepare the inception v3 model
model = InceptionV3(include_top=False, pooling='avg', input_shape=(299,299,3))
# # load cifar10 images
# (images1, _), (images2, _) = cifar10.load_data()
# shuffle(images1)
# images1 = images1[:10000]
images1_names = glob.glob("target\\*.png")
#images2_names = glob.glob("..\\ezdxf\\145\\*A.png")#534.342
#images2_names = glob.glob("..\\ezdxf\\145\\*blur.png")#509.581
#images2_names = glob.glob("./pix2pix_results/*.png")#603.823
images2_names = glob.glob("./stylegan_results/*.jpg")#824.923
images1 = numpy.array([numpy.array(Image.open(i).convert("RGB").resize((299, 299), Image.BICUBIC)) for i in images1_names])
images2 = numpy.array([numpy.array(Image.open(i).convert("RGB").resize((299, 299), Image.BICUBIC)) for i in images2_names])

print('Loaded', len(images1), len(images2))

# pre-process images
images1 = preprocess_input(images1)
images2 = preprocess_input(images2)
# calculate fid
fid = calculate_fid(model, images1, images2)
print('FID: %.3f' % fid)