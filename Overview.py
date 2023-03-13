import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.mention import mention
from streamlit_extras.switch_page_button import switch_page

url1="https://drive.google.com/file/d/12NQM8wBzIl3XwJqAGLZnZ3r3El9A6hyq/view?usp=sharing"
pacclogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]
st.set_page_config(
     page_title="Analytical Tool",
     layout="wide",
     page_icon= pacclogo,
    initial_sidebar_state="expanded")

add_logo(pacclogo,height=190)

col1, col2 = st.columns([6,1])
with col1:
  mention(label="Get to know me first",icon="🧑🏻👇🏻",  #Some icons are available... like Streamlit!,
    url="https://www.linkedin.com/in/karimhazimeh",)

with col2:
  start = st.button("Disover the app")
  if start:
    switch_page("Homepage")
html_code= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        #background {
            height: 100vh;
            background-color: #5eb7d9;
            background-image: url('your-image-url.jpg');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        #content {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: black;
            font-family: Verdana, sans-serif;
        }
        h1 {
            font-size: 2rem;
            margin: 0;
        }
        .text-block {
            text-align: center;
            margin-top: 5px;
        }
        button {
            background-color: white;
            color: #222;
            font-weight: bold;
            border: 2px solid #222;
            padding: 10px 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="background"></div>
    <div id="content">
        <h1>Hello, I'm</h1>
        <h1>Karim Hazimeh</h1>
        <div class="text-block">a Data detective with a Masters in Business Analytics🕵🏻‍♀️.<br>I am passionate about utilizing my tech-savviness and business analytics expertise to uncover insights from data that guide end-users through the vast and ever-changing <b>sky of possibilities.</b></div>
        <br><a href="https://drive.google.com/uc?export=download&id=1__wsAULlJ3uoAYil0B77UODwsgWeEF5x" download><button>Download CV</button></a></br>
    </div>
    <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.4.1.min.220afd743d.js" type="text/javascript" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <script src="https://assets.website-files.com/5d971c4989c88c0b4cca55cd/js/webflow.1bc56dc86.js" type="text/javascript"></script>
    <script src="https://assets.website-files.com/5d932bf11608325eac058a21/5d932d68160832c7c0059c91_three.r92.min.txt"></script>
    <script src="https://assets.website-files.com/5d932bf11608325eac058a21/5d93301de2a4d93ad0b1fe54_vanta.clouds.min.txt"></script>
    <script>
        VANTA.CLOUDS({
            el: "#background",
            skyColor: 0x5eb7d9,
            cloudColor: 0xb1c2dc,
            cloudShadowColor: 0x1b3a57,
            sunColor: 0xff9c21,
            sunGlareColor: 0xfa6331,
            sunlightColor: 0xfa
        })
    </script>
</body>
</html>
        """


# Add the HTML code to the Streamlit app using st.components.v1.html
st.components.v1.html(html_code)
