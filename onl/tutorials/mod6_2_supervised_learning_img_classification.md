# Supervised learning and image classification

Here we introduce two important concepts that we have not yet covered in the tutorials. We only scratch the surface, but provide resources for additional reading wich is encouraged!

As Cassie Kozyrkov, Chief Decision Scienist at Google, states <a href="https://kozyrkov.medium.com/machine-learning-is-the-emperor-wearing-clothes-928fe406fe09">(in a very accessible description of machine learning)</a>, "machine learning uses patterns in data to label things." A machine learning algorith is a thing-labeler. The complexity and nuance of "things" to label and the performance of the labeler can get really advanced, but as a basic concept, it's really that simple.

## Supervised learning

<div class="alert alert-info">
**Supervised learning** is an approach that uses an algorithm to learn what label is associated with a given set of attributes for an available dataset such that it can infer what label would be associated with a set of attributes on a dataset where no label is present.
</div>

In other words, we want our machine learning function to learn what the likelihood of a certain label is when it knows both the label and a set of attributes associated with that label so that when it encounters data it has not seen before, it can predict a label given only the set of attributes.

If the labels were continuous (e.g. the amount of rain in a given day) the approach would be regression. If the labels were categorical (e.g. whether it rains in a given day or not), the approach would be classification.

For our exercise, we are predicting if a pixel is "built-up" or not (classification), using the Global Human Settlement Layer (GHSL) data to define this label. GHSL categorizes grid cells as being either "high density" (cities), "low density" (cities and towns), or "rural," so we will simplify this as being "built up" (either high or low density) versus not (rural). We are using VIIRS-DNB and Sentinel-2 image attributes per pixel as our input features. Since we have GHSL data from 2015, we will use data from that year to learn the association of VIIRS-DNB and Sentinel-2 features per pixel and whether it is "built up" or not. Then we can apply this learned association to data that does not have any GHSL label and make a prediction about whether it is built up.

## Classification with image data

Hopefully the concept of "thing-labeling" for land classification task is clear, but it might be confusing how exactly our model will learn the association of input features, like VIIRS-DNB and Sentinal-2 with a label such as "built-up."

Image classification is a useful and popular application of machine learning and computer vision. It most commonly refers to the task of classifying an entire image (or the dominant object in an image, such as a cat) based on the image's pixels as input, as well as the pixels from many, many other images.

It is also possible to classify individual pixels as well, which is the task appropriate to our exercise.

Recall from {doc}`tutorials/mod2_1_data_overview` that data can be stored in raster files, which are like grids of cells (i.e. pixels). All three data sources we are working with: VIIRS-DNB, Sentinel-2, and GHSL will be formatted in raster files. So consider each grid/pixel as an "observation" that contains input feature values (from VIIRS-DNB nighttime Sentinel-2 daytime images). For our 2015 training data, we also have GHSL data that will assign each pixel as "high density," "low density" or "rural" -- that we will further simplify simply as "built-up" or not.

Our classifier will learn what levels of input features are assocated with a given label based on the pixels for each image (i.e. monthly composite) in our 2015 training dataset. When we pass new images (i.e. monthly composites) for the rest of the time period, the classifier will predict the likelihood of a pixel being "built up" based on the available data from VIIRS-DNB and Sentinel-2.

While there are advanced methods of deep learning well-suited to image analysis, such as Convolutional Neural Nets (CNNs), Random Forest (RF) is a good simple classifier to use for this beginner's task.

You may ask whether other information, such as the values of neighboring pixels, is important...yes! Most advanced image classifiers will take advantage of such contextual information as well. Additionally, mathmatical transformations of the raw data can enhance the classifiers ability to distinguish input features. For our exercise, we're sticking with the basics.

## The most important kind of learning: yours
This is a very brief summary of some fairly deep topics but many resources are available for learning more. Two excellent texts cover the fundamentals for the ideas described here: "Pattern Recognition and Machine Learning" {cite}`bishop2006pattern`, and "The Elements of Statistical Learning: Data Mining, and Prediction" {cite}`hastie2009elements`. And of course the internet is awash with free and accessible online courses at many levels.

<div class="alert alert-success">
Python itself provides a useful entry point for these methods via the <a href="https://scikit-learn.org/stable/user_guide.html">documention in the scikit-learn package</a>. And the added benefit is that the packages described contain the very code needed to implement these methods and many examples.
</div>

The good news is that as long as you understand what you are doing and why, the tools for doing this classification are easy to use and require minimal programming experience, as with the previous tutorial exercises. 

Do not let a lack of knowledge prevent you from digging into the data and learning by doing, but rather consider the resources available for understanding applicable theory when something interesting happens with your data and you want to know why. Once you do, you will see what is possible and hopefully be motivated to learn more.

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```