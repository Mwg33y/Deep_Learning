# Deep_Learning

Deep learning is a type of Artificial Intelligence that uses mathematical algorithms to process data with minimal 
human interference (supervised/unsupervised). The data is extracted from an observed system or set of circumstances. 
The elements that generate or create data in a system are the parameters of the system. Deep learning uses mathematical 
algorithms. It also uses a set of processes and steps to model each parameters significance in the observed system. The result
is an algorithm model that imitates/mimics the system. This modeled can be used to make predictions and identify patterns 
in a system. A Deep Leaning algorithm is first trained with a portion of the data available from the system. It is then tested
using another portion of the same data to verify if the model represents the system. 

Between the input of data and the output of a representative model, Deep Learning algorithms use many steps to determine a 
model's behaviour. This steps form networks and process information similar to the way that neurons in the human brain do. This 
also means that Deep Learning requires significant computer processing power when creating a model using large amounts of 
data, and many intermittent steps.


The types of Deep Learning Algorithms (Different ways that I have implemented each one):


1. Artificial Neural Networks (Which customers are the most likely to leave a hypothetical bank)

Artificial Neural Networks are based on brain function and are used to simulate connections between neurons in the brain. This
is achieved by placing nodes between the input and output stages. These nodes process the input parameters and 
adjust the significance of each parameter through many iterations and comparing how close the output of the 
the algorithm is to the testing data set. Adjustments are made to the algorithm until the difference between
the output value is extremely close to the actual value. This acceptable error range gives us an optimal algorithm.

2. Convolutional Neural Networks (Algorithm Image recognition using 8000 images of cats and dogs)

Convolutional Neural Networks are a deep learning algorithm that is used for object or image recognition. The algorithm goes through the 
data set containing the images, reduces the size of each image for easier computation, analyzes the pixel data, and tries to identify
the subsequent images using the data it collects along the way. The algorithm improves with every iteration.

3. Recurrent Neural Networks (Time series analysis: Loblaws stock prices prediction)

Recurrent Neural Networks are used to analyse sequential data and time-series data. It uses internal feed back loops located at it's nodes to 
retain the recent information that it consumed. It uses the new information and the retained information to 
build an alorithm that can make predictions of highly probable future data points.


4. Self Organizing Maps (Predict banking fraud for a hypothetical bank using their client information)

Self Organizing Maps reduce the number of parameters in a large dataset. It keeps the most impactful parameters
and groups the different row elements (e.g. customers, voters, clients, etc.) into categories. 
The same set of rows can be observed with more significance given to different or new parameters. 
Several iterations with occasional parameter changes can help
identify certain patterns/behaviours and allow for prediction of highly probable future patterns (e.g. 
certain reactions or decisions voters might make given a new ballot issue). The different categories help
identify the reaction or lack there of to a given parameter by that members of that category. An example of an SOM
is a heat-map.


