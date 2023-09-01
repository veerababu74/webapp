import openai
import streamlit as st
from myapi import mykey
openai.api_key = "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"

def extract_financial_data(text):
    prompt =  text + get_prompt_financial() 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content": prompt}]
    )
    content = response.choices[0]['message']['content']

    return content

def get_prompt_financial():
    return '''
when ever the rquirement for the ad please give me suggistion like below. the solutions must have
the following like this based on creatin activites
the output should like below
============ ================
-The ad is a dynamic landscape format design (1280x768 pixels) in high resolution that presents a modern aesthetic

-At the center of the image, occupying about 50 of the space, is the car: a sleek, modern vehicle with a sparkling white exterior that suggests cleanliness, sophistication, and modernity. Its design conveys a sense of speed and agility, as well as comfort and safety.The wheels are prominently displayed, suggesting its readiness for the road and the adventures that lie ahead.

-The car is positioned on an open road that extends from the bottom-middle to the top-middle of the frame, suggesting a journey. freedom, and forward momentum. This road is set against a stunning backdrop of a cityscape on one side and a beautiful natural landscape on the other, showcasing the car's versatility and appeal to those who love both urban and outdoor adventures. This dual scene takes about 40% of the overall image space, positioned to the right of the car.

-In the cityscape, there are young people just like the target demographic. They are engaged in various activities walking their dogs. jogging, cycling, suggesting an active lifestyle. The city buildings are modern and striking, indicative of progress, and ambition.

-On the other side, the natural landscape features a lake, mountains, and a clear sky- a scene of tranquility and escape from the bustling city. A group of people can be seen hiking and cycling, again reflecting the active lifestyle.

-At the top-left corner, about 5 of the space is dedicated to the car brand's logo and tagline-something catchy and relevant to the target demographic like, "Drive Your Journey".

-Towards the bottom-left, taking up about another 5%, are the technical specifications and price of the car. The text is small but clear, not overpowering the visuals but readily available for those seeking more information. 

-The final touch is a small, interactive "Learn More" button at the very bottom in the center, designed to draw the viewer's attention and invite them to engage further with the product.

-The color scheme throughout the ad is vibrant and energetic, using a mix of cool blues, warm oranges, and crisp whites to create a balanced and appealing visual that would resonate with the young and active target audience.
    '''

custom_css = """
<style>
div[data-baseweb="input"] input {
    height: 100px; /* Adjust the height as needed */
}
</style>
"""
st.write(custom_css, unsafe_allow_html=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("TCS advertisement helping bot")
    user_input = st.text_input("Enter your advertisement requirement")
    #user_input =st.text_input("Enter your ad requirement",height=150)
    if st.button("send"):
        if user_input:
            
            finaldata = extract_financial_data(user_input)
            print(finaldata)
            st.text("tcs bot response")
            st.write(finaldata)
