# Future Lightroom Lr using Augmentation [Computer Vision]
We have developed an Image processing and enhancing python app using konia in pytorch framework for the Daisi Hackathon (via Hackerearth)
### Team Details:
#### Team Leader: NANDHAKUMAR S 
#### Members: SUJITH V, MOHAMED RAFEEK S
#### Designation: Student at BANNARI AMMAN INSTITUTE OF TECHNOLOGY, SATHYAMANGALAM.
#### Contact: +919488393947
#### Mail: nandhakumarshanmugam.udt.4757@gmail.com

## What we used......
• Daisi


• Streamlit UI


• Pytorch


• Kornia


#### We have done our project in the daisi platform (https://app.daisi.io/) using Streamlit UI. We used Kornia Pytorch to process and enhance the image. 
## Features
• Geometric Operations - Image Affine Transformation

• Random Erase - Randomly selects a rectangular region in an input image and erases its pixels.

• Random Resized Crop - A crop of the original image is made: the crop has a random area (H * W) and a random aspect ratio. This crop is finally resized to the given size.

## Screenshots of our App

![1](https://user-images.githubusercontent.com/113059991/189355954-d33ced30-6c74-4c1d-b5ee-41accc19a90a.JPG)



![2](https://user-images.githubusercontent.com/113059991/189355991-103a8497-2714-498b-b926-e0f6d1032515.JPG)



### Processed Image 

![Lr](https://user-images.githubusercontent.com/113059991/189353828-799dd5f7-6380-4e9d-8cf3-16a2128f0b0b.JPG)


## Usage of Daisi

It is recommended to use this application on the daisi platform itself using the link https://app.daisi.io/daisies/nandhakumar/Future_Lightroom_LR_using_Augmentation/app
However, you can still use your own editor using the below method:

### First, load the Packages:

```
import pydaisi as pyd
future_lightroom_lr_using_augmentation = pyd.Daisi("nandhakumar/Future_Lightroom_LR_using_Augmentation")
```
### Now, connect to Daisi and access the functions using:

```
future_lightroom_lr_using_augmentation.set_transform(content).value
```

