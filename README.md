# CloudI
## CloudI: A classification tool for cloud images
### Goal of This Project
The idea came into my mind sometime this May, when I was strolling round my home. I was taking photos of the sky and there were some clouds in the images. According to my experiences, they should be cirrus clouds. Those clouds could be classified easily if you have learned the criterion before. What if some one just wants to know the type of clouds and does not have any experience? 

Building an App for classifying clouds would be cool. It's not that fancy nor novel. In fact, some of the weather Apps already have this feature. As for me, my ultimate goal for this project is to develop an App (or a function in an App) that can detect the locations of clouds and classify the cloud types from a user's input image. For instance, suppose a user submits the image below:
<img src = 'Readme img/Thunder.jpg' alt = "drawing" style ="width: 350px">
We expect the output to be:
<img src = 'Readme img/Draft.jpg' alt = "drawing" style ="width: 400px"> 

### Steps to Reach the Goal:
### Step 1: Build an Image Classification Model for Clouds

**Potential Choices**: 

K-Nearest Neighbors, Linear Classification (Softmax loss or SVM loss), Convolutional Neural Network.  

**Current Progress**: 
<img src = 'Readme img/dogecoin.jpg' alt = "drawing" style ="width: 250px">

### Step 2: Develop a Detection Model to Locate Clouds in an Image

**Potential Choices**: 

Sliding Window, R-CNN, Fast R-CNN

**Current Progress**: 
<img src = 'Readme img/dogecoin.jpg' alt = "drawing" style ="width: 250px">


### Possible Extensions
If detection and classification works well, we can generate captions for cloud images. To be specific in some sense, the caption would include types of clouds, the amount of clouds, and descriptions of objects in the background. We still use the same input. Now, we expect the output as:
<img src = 'Readme img/Draft_Ex.jpg' alt = "drawing" style ="width: 400px">
