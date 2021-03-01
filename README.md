# Doppler White Paper
Leon Yin
<br>
Published: 2019-04-06<br>
Last Updated: 2021-02-28

Note:<br>
This project is no longer maintained. Please refer to the forked project: [Meme Observatory](https://github.com/memeticinfluence/meme-observatory).

## Intro
The Doppler is an open source computer vision toolkit used to trace and measure image-based activity online. 

The Doppler has two main functions:
1. Reverse Image Search 
2. Mosaic Analysis. 

In this article we'll display these features using Reddit data collected by our friends at [pushshift](https://PushShift.io). However, the methods and backend are generalizable to any source of images. By standardizing how we study images we get closer to cross-platform analysis.

## Table of Contents
This article is broken up into several Jupyter Notebooks.
1. Data Collection <br>
    <i>How to build an image dataset from Reddit?</i> <br>
    [GitHub](https://github.com/yinleon/doppler_tutorials/blob/master/1-download-data.ipynb) | [NBViewer](https://nbviewer.jupyter.org/github/yinleon/doppler_tutorials/blob/master/1-download-data.ipynb)  
2. Feature Extraction <br>
    <i>How to transform images into searchable features using a pre-trained neural net?</i> <br>
    [GitHub](lhttps://github.com/yinleon/doppler_tutorials/blob/master/2-feature-extraction.ipynb) | [NBViewer](https://nbviewer.jupyter.org/github/yinleon/doppler_tutorials/blob/master/2-feature-extraction.ipynb)
3. Mosaic Analysis <br>
    <i>How to sort images by visual similarity?</i> <br>
    [GitHub](https://github.com/yinleon/doppler_tutorials/blob/master/3-mosaic-analysis.ipynb) | [NBViewer](https://nbviewer.jupyter.org/github/yinleon/doppler_tutorials/blob/master/3-mosaic-analysis.ipynb)
4. Reverse Image Search <br>
    <i>How to find similar images and provenance?</i> <br>
    [GitHub](https://github.com/yinleon/doppler_tutorials/blob/master/4-reverse-image-search.ipynb) | [NBViewer](https://nbviewer.jupyter.org/github/yinleon/doppler_tutorials/blob/master/4-reverse-image-search.ipynb)

The repository is also hosted in the [Binder](https://mybinder.org/v2/gh/yinleon/doppler_tutorials/master
) interactive environment.

## How does it work?
In order to use the two functions of the Doppler, images need to be transformed into differential features. To do this we use two computer vision techniques, d-hashing and feature extraction using a pre-trained neural network.

### D-Hashing
D-Hashing creates a fingerprint for an image (regardless of size or minor color variations). With this technique it is easy to check for duplicate images. This method (outlined [here](http://www.hackerfactor.com/blog/?/archives/529-Kind-of-Like-That.html)) is also quick and not intense for a computer. We use the imagehash Python library to do this.

### Feature Extraction
Neural networks are able to learn numeric attributes used to differentiate between images. These numbers are continuous which allows us to calculate similarity. These features are what allow us to cluster images for the mosaic and rank similarity for the reverse image search. Thanks for the decidcation of open source developers and researchers implementation is relatively easy. However, it requires a lot of matrix math which is a lot of work for a regular computer. This process is greatly accelerated using a computer with a graphics processing unit (GPU). We use PyTorch to do this.

These two techniques serve somewhat different purposes. The Doppler architecture intends to take advantage of both techniques when appropriate.


## Why We're Building this?
We seek to empower newsrooms, researchers and members of civil society groups to easily research and debunk coordinated hoaxes, harassment campaigns, and racist propaganda that originate from unindexed online commuities.

Specifically, the Disinfo Doppler will help evidence-based reporting and research into content that is ephemeral, unindexed and toxic in nature. The Disinfo Doppler would allow a greater variety of users the ability to navigate and investigate these spaces in a more secure and systematic way than is currently available. Formalizing how we observse this content is of utmost importance, as extended contact with these spaces is unnecessary and can lead to vicarious trauma, and in some rare cases radicalization. The Disinfo Doppler allows users to distance themselves from tertiary material not relevant to their investigation, while providing context vertically and horizontally.
