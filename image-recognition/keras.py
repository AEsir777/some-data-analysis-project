import pandas as pd
from keras.models import Sequential
from keras.layers import *
from keras.models import load_model

para = 1

if para == 1:
    training_data_df = pd.read_csv("C:/Users/AEsir/Desktop/files/additional learning/Machine Learning(python)/CTF/ai-village-ctf/token/test.csv")

    # separate into input and output
    X = training_data_df['Review'].head(1327).str.len().values
    Y = training_data_df[['Sentiment']][:1327].values

    # Define the model
    model = Sequential()
    # 9 variates as input
    model.add(Dense(50, input_dim=1, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    # we don't know the best model until we know the accuracy
    model.add(Dense(1, activation='linear'))
    # last layer has 1 node 'linear' is default
    # single linear value so 'linear'
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train the model
    model.fit(
        X,
        Y,
        epochs=50,  # training paths during the training process
        shuffle=True,  # shuffle the data
        verbose=2  # print more details in the training
    )

    # make a predicition with the neural network
    prediction = model.predict([9])

    # Grab just the first element of the first prediction
    # since there is only one row
    prediction = prediction[0][0]

    print("- ${}".format(prediction))
else:
    # read in model
    model = load_model('trained_model.h5')

    X_pred = pd.read_csv('../Ex_Files_Building_Deep_Learning_Apps/Exercise Files/04/proposed_new_product.csv').values
    prediction = model.predict(X_pred)

    prediction = prediction[0][0]
    prediction = prediction + 0.1159
    prediction = prediction / 0.0000036968

    print("Earnings Prediction for Proposed Product - ${}".format(prediction))







