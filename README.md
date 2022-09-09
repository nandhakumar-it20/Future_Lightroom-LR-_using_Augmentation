# Future_Lightroom_Lr_using_Augmentation [Computer Vision]
We have developed a Image processing and enhancing python app using konia in pytorch framework for the Daisi Hackathon (via Hackerearth)
### Team Details:
#### Team Leader: NANDHAKUMAR S 
#### MEMBERS: SUJITH V, MOHAMED RAFEEK S
#### Designation: Student at BANNARI AMMAN INSTITUTE OF TECHNOLOGY, SATHYAMANGALAM.
#### Contact: +919488393947
## Features
• Geometric Operations - Image Affine Transformation

• Random Erase - Randomly selects a rectangular region in an input image and erases its pixels.

• Random Resized Crop - A crop of the original image is made: the crop has a random area (H * W) and a random aspect ratio. This crop is finally resized to the given size.


![1](https://user-images.githubusercontent.com/113059991/189335729-9efb0d38-eede-4506-88f5-da16698076b0.JPG)


![2](https://user-images.githubusercontent.com/113059991/189335759-5a736351-c5fa-4deb-94bc-e0dc49a25b29.JPG)



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

