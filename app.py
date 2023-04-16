import streamlit as st
import sklearn
import pickle
from preprocessing import preprocess

# Take a reference of 'https://www.kaggle.com/code/rutujapotdar/suicide-text-classification-nlp'

# Load the pre-trained model
model =  pickle.load(open('best_model.pkl', 'rb'))   
print('Done loading')
def app():
    # Set the app title and heading
    st.set_page_config(page_title='Mental Health App', page_icon=':male-doctor:', layout='wide')
    st.title('Mental Health App')

    # Define the input text box
    input_text = st.text_input('Chat with a Mental Health Chatbot')
    if input_text == '':
        st.write('Please enter the chat')
    processed_array = preprocess(input_text)
    predict = model.predict(processed_array)
    print(predict)

    # Define the predict button
    if st.button('Predict'):
        if predict[0] == 'suicide':
            st.write("The Text Contains References to self-harm ⚠️")
        elif predict[0] == 'non-suicide':
            st.write('The Text does not contain self-harm')


# Run the app
if __name__ == '__main__':
    app()
