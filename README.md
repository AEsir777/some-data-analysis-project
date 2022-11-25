# Keras parameter study
## conclusion (tested on **plain vanilla** and **CNN** model)
CNN have two extra convolution and pooling layers and others remain the same.

![image](https://user-images.githubusercontent.com/77596290/202949015-05f37562-48f4-467d-bbdc-5fca0fd1fab6.png)
*change epoch and normalization for plain vanilla model*

![image](https://user-images.githubusercontent.com/77596290/202955224-38fbf2a6-4f02-4012-b9af-6c0cbd5a1cba.png)
*change epoch and normalization for CNN model*

- reducing the epoches will decrease the accuracy
- not normalizing the activation for the first layer input will also decrease the accuracy: normalization seems to have a bigger impact for the plain vanilla model than the CNN
- CNN is more accurate when dealing with the fashion MNIST dataset

![image](https://user-images.githubusercontent.com/77596290/202863296-31bb1a40-268f-409e-ab98-ffad224c5299.png)
*change the number of neurons in first dense layer for plain vanilla model with 3 layers*

![image](https://user-images.githubusercontent.com/77596290/202863307-4a4567ec-adf4-4e82-887f-0c9b9a46bd0f.png)
*change the number of neurons in second dense layer for plain vanilla model with 4 layers*


![image](https://user-images.githubusercontent.com/77596290/202951821-9c2facab-bd79-4e2b-9212-4341cd01bb38.png)
*change the number of neurons in first dense layer for CNN*

![image](https://user-images.githubusercontent.com/77596290/202953633-18fae1dd-a351-4ce6-bd52-3791c264d1a8.png)
*change the number of neurons in second dense layer for CNN*


compare two tables where one table (left) represents a model with only three layers and controlled the number of neurons in the second layer and the other table (right) represens a model with 4 layers and controlled the number of neurons in the forth layer
- the model with more layers is slightly more accurate than the model with less layers
- as number of neurons increases, the accuracy tends to be higher; however, when the number of neurons is larger enough, there do not seem be that much difference and obvious trend for accuracy.
- overfitting with more neurons may lead to lower accuracy

# ctf
contains kaggle for ai_village_challenge uses numpy, pandas, scikit-learn for classification, clustering, dimention reduction.  
  
# game_attributes_compare
uses matplotlib to convert the data into graphs

# image-recognition
## conclusion
implement **image augmentation** and **dropout**
For flower dataset: apply <br />
randomWidth/Height = 0.15, horizontal RandomFlip, 45&deg; RandomRotation, 50% RandomZoom, Dropout=0.2
![image](https://user-images.githubusercontent.com/77596290/204006200-1a292407-a8c4-456f-81a8-cb3b36293f77.png)
- the training loss begin to increase after 40 epochs, so overfitting did have effect on the accuracy for the validation set <br />
<br />

For dog and cat dataset: apply
Horizontal and vertical RandomFlip, 36&deg; RandomRotation, 20% RandomZoom, 0.5 Dropout
![image](https://user-images.githubusercontent.com/77596290/203888888-f261bdd2-d2b9-4f95-a142-505a113ee918.png)
- For relatively large epoches (1-100), the traning and validation accuracy is still increasing, so these two methods effectively avoid **overfitting**



# R
some basic R usage
