# CloudI
## CloudI: A classification tool for cloud images
### Goal of This Project
The idea came into my mind sometime this May when I was strolling around my home. I was taking photos of the sky and there were some clouds in the images. According to my experiences, they should be cirrus clouds. Those clouds could be classified easily if you have learned the criterion before. What if someone just wants to know the type of clouds and does not have any experience? 

Building an App for classifying clouds would be cool. It's not that fancy nor novel. In fact, some of the weather Apps already have this feature. As for me, my ultimate goal for this project is to develop an App (or a function in an App) that can detect the locations of clouds and classify the cloud types from a user's input image. For instance, suppose a user submits the image below:

<img src = 'Readme img/Thunder.jpg' width="420" height="694">

We expect the output to be:

<img src = 'Readme img/Draft.jpg' width="420" height="694"> 

### Steps to Reach the Goal:
### Step 1: Build an Image Classification Model for Clouds

**Potential Choices**: 

~~K-Nearest Neighbors~~, ~~Linear Classification (Softmax loss or SVM loss)~~, Convolutional Neural Network.  

**Current Progress**: 

We have built a classification model based on ResNet using transfer learning. We also design a basic web App interface using streamlit. However, the model still needs improvement. In the following sections, we will list the circumstance where the model would fail.

### Model Behavior - Case 1:
If clouds take up at least 50% of the image, the model could yield a decent prediction.

<img src = 'Readme img/GetLucky.png' alt = "drawing" style ="width: 100px">

### Model Behavior - Case 2:
If clouds take up fewer than 50% of the image, the prediction accuracy would be lower.

<img src = 'Readme img/Smaller_Portion.png' alt = "drawing" style ="width: 100px">

### Model Behavior - Case 3:
When clouds are blocked by some buildings or objects, the model would give wrong predictions.

<img src = 'Readme img/Blocked.png' alt = "drawing" style ="width: 100px">

### Possible Explanations and Remedies:

From the view of our training dataset, a large number of our training images only contain clouds. In other words, clouds are the main character, and no other objects are present. One may argue that a brilliant model would be able to generalize to inputs with various backgrounds. But for clouds, things could be a bit different. First, clouds could relate to certain backgrounds. For instance, nimbostratus and stratus clouds (Ns, St) often appear at a pretty low altitude. Thus, most of the available images would include trees, mountains, or buildings. If a user input contains mainly buildings or roads, the model may have a higher probability to classify the cloud into (Ns, St). Below is an example, for which the correct type should be stratocumulus.

<img src = 'Readme img/WrongNsSt.png' alt = "drawing" style ="width: 100px">

A possible solution could be: we add training images where clouds appear together with other objects. But that leads to the second challenge: Some types of clouds have special shapes e.g.  altocumulus and cirrocumulus (Ac, Cc). Adding other irrelevant elements in the image may block or blur them. The image in **Model Behavior - Case 3** should be classified as (Ac, Cc) but the model did not. Should we introduce training images like this? Would the model still be easy to train? The answer remains unknown, but we can give it a try. P.s. Blurring or blocking is just like when classifying a cat or dog, if you draw some lines to block some features, the model may give the wrong prediction. [Link to the app](https://cat-dog-detection-tfjs.vercel.app/)

<img src = 'Readme img/WrongDog.png' alt = "drawing" style ="width: 100px">

At last, there could be different types of clouds in an image. And a cloud may be in the stage of transforming to the other, which makes the cloud resemble other types. They could be the toughest challenges, but they correspond to my ultimate goal: Detect all types of clouds in an image and mark them out. Anyway, in some scenarios, it's still hard to let the machine learn the right stuff. Check this out, a dog is classified as a cat:

<img src = 'Readme img/WrongCat.png' alt = "drawing" style ="width: 100px">

### Step 2: Develop a Detection Model to Locate Clouds in an Image

**Potential Choices**: 

Sliding Window, R-CNN, Fast R-CNN

**Current Progress**: 

<img src = 'Readme img/dogecoin.jpg' width="600" height="400">


### Possible Extensions

If detection and classification works well, we can generate captions for cloud images. To be specific in some sense, the caption would include types of clouds, the amount of clouds, and descriptions of objects in the background. We still use the same input. Now, we expect the output as:

<img src = 'Readme img/Draft_Ex.jpg' width="420" height="694">
