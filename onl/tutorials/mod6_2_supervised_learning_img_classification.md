# Supervised learning and image classification

We should introduce two important concepts that we have not yet covered in the tutorials. We only scratch the surface, but encourage you to learn more about these powerful techniques.

<div class="alert alert-info">
As Cassie Kozyrkov, Chief Decision Scientist at Google, states <a href="https://kozyrkov.medium.com/machine-learning-is-the-emperor-wearing-clothes-928fe406fe09">(in a very accessible description of machine learning)</a>, "machine learning uses patterns in data to label things."</div>

A machine learning algorith is a thing-labeler. The complexity and nuance of "things" to label and the performance of the labeler can get really advanced, but as a basic concept, it's really that simple.

## Supervised learning

<div class="alert alert-info">
**Supervised learning** is an approach that uses already-labeled data to learn associations between these labels and a given set of attributes or features, the likelihood of a particular label, such that the algorithm can predict labels on unseen data that are not labeled but have the same features.</div>

If the labels were continuous (e.g. the amount of rain in a given day) the approach would be regression. If the labels were categorical, including binary (e.g. whether it rains in a given day or not), the approach would be classification.

For our exercise, we are predicting if a pixel is "built-up" or not (binary classification), using the Global Human Settlement Layer (GHSL) data to define what "built-up" means. GHSL categorizes grid cells as being either "high density" (cities), "low density" (cities and towns), or "rural," so we will simplify this as being built up (either high or low density) versus not (everything else). 

We are using VIIRS-DNB and Sentinel-2 image attributes as our input features. Since we have GHSL data from 2015, we will use data from that year to learn the association of VIIRS-DNB and Sentinel-2 measurements and built-up land. Then we can apply this learned association to data that does not have any GHSL label (i.e. any year after 2015) and make a prediction about whether it is built up based only on VIIRS-DNB and Sentinel-2 inputs.

## Classification with image data

Hopefully the concept of "thing-labeling" for land classification task is clear, but it might be confusing how exactly our model will learn the association of input features, like VIIRS-DNB and Sentinal-2 with a label such as "built-up."

Image classification is a useful and popular application of machine learning and computer vision. It most commonly refers to the task of classifying an entire image (or the dominant object in an image, such as a cat) based on the image's pixels as input.

It is also possible to classify individual pixels as well, which is the task appropriate to our exercise.

Recall from {doc}`mod2_1_data_overview` that data can be stored in raster files, which are like grids of cells (i.e. pixels). All three data sources we are working with, VIIRS-DNB, Sentinel-2, and GHSL, will be formatted in raster files. So consider each grid cell/pixel in the raster as an observation that contains certain features: the values from corresponding VIIRS-DNB nighttime or Sentinel-2 MSI images. And for our 2015 training data it will also contain a label: the GHSL classification as "built-up" (1) or not (0). For the data that is not in our training set, our inference data, we will only have VIIRS-DNB and Sentinel-2 values and will have to predict the label.

Our classifier's task is to learn what levels of input features are assocated with a given label based on analysis of all the labeled pixels in our training dataset image (from 2015). When we pass new images from 2016-2019, the classifier will predict the likelihood of a pixel being "built up" based on what it sees in terms of VIIRS-DNB and Sentinel-2 data and what it learned from training about the likelihood of those values corresponding to built-up land.

While there are advanced methods of deep learning well-suited to image analysis, such as Convolutional Neural Nets (CNNs), Random Forest (RF) is a simple but often effective classifier to use for this beginner's task.

You may ask whether other information, such as the values of neighboring pixels, is important...yes! Most advanced image classifiers will take advantage of such contextual information as well. Additionally, feature engineering, including mathmatical transformations, and additional data can often improve classifiers a lot. Since we are investigating changes in time, we should also be concerned with the influence of the past on the future (hint: it does) and how that impacts model training and inference...but for our exercise, we're sticking with the basics.

## The most important kind of learning: yours
This is a very brief summary of some fairly deep topics but many resources are available for learning more. Two excellent texts cover the fundamentals for the ideas described here: "Pattern Recognition and Machine Learning" {cite}`bishop2006pattern`, and "The Elements of Statistical Learning: Data Mining, and Prediction" {cite}`hastie2009elements`. And of course the internet is awash with free and accessible online courses at many levels.

<div class="alert alert-success">
Python itself provides a useful entry point for these methods via the <a href="https://scikit-learn.org/stable/user_guide.html">documention in the scikit-learn package</a>. And the added benefit is that the packages described contain the very code needed to implement these methods and many examples.
</div>

The good news is that as long as you stay curious about what you are doing and why, the tools for doing this classification are easy to use and require minimal programming experience, as with the previous tutorial exercises.

Do not let a lack of knowledge prevent you from digging into the data and learning by doing, but rather consider the resources available for understanding applicable theory when something interesting happens with your data and you want to know why. Once you do, you will see what is possible and hopefully be motivated to learn more.

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```