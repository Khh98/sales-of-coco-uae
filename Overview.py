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
<html data-wf-domain="interactive-sky.webflow.io" data-wf-page="5d971c4989c88c6dcbca55ce" data-wf-site="5d971c4989c88c0b4cca55cd">
    <head>
        <meta charset="utf-8"/>
        <title> Hello</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta content="Webflow" name="generator"/>
        <link href="https://assets.website-files.com/5d971c4989c88c0b4cca55cd/css/interactive-sky.webflow.c473bcb3c.css" rel="stylesheet" type="text/css"/>
        <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
        <script type="text/javascript">
            WebFont.load({
                google: {
                    families: ["Verdana:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic"]
                }
            });
        </script>
        <script type="text/javascript">
            !function(o, c) {
                var n = c.documentElement
                  , t = " w-mod-";
                n.className += t + "js",
                ("ontouchstart"in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch")
            }(window, document);
        </script>
        <link href="https://assets.website-files.com/img/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
        <link href="https://assets.website-files.com/img/webclip.png" rel="apple-touch-icon"/>
    <style>
            .text-block {
                 text-align: center;
                 margin-top: 5px;
}
            h1:first-child {
                font-size: 2rem;
            }
        </style>
    </head>
    <body>
        <div id="demo" class="wrapp">
            <h1>Hello, I'm</h1>
            <h1>Karim Hazimeh</h1>
            <div class="text-block" style="font-family:Lucida Console"><br>a Data detective with a Masters in Business Analytics🕵🏻‍♀️.</br>I am passionate about utilizing my tech-savviness and business analytics expertise to uncover insights from data that guide end-users through the vast and ever-changing <b>sky of possibilities.<b></div>
            <br><a href="https://drive.google.com/uc?export=download&id=1__wsAULlJ3uoAYil0B77UODwsgWeEF5x" download><button style="background-color: white; color: #222; font-weight: bold; border: 2px solid #222; padding: 10px 20px; border-radius: 5px;">Download CV</button></a></br>
        </div>
        <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.4.1.min.220afd743d.js" type="text/javascript" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
        <script src="https://assets.website-files.com/5d971c4989c88c0b4cca55cd/js/webflow.1bc56dc86.js" type="text/javascript"></script>
        <!--[if lte IE 9]><script src="//cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif]-->
        <script src="https://assets.website-files.com/5d932bf11608325eac058a21/5d932d68160832c7c0059c91_three.r92.min.txt"></script>
        <script src="https://assets.website-files.com/5d932bf11608325eac058a21/5d93301de2a4d93ad0b1fe54_vanta.clouds.min.txt"></script>
        <script>
            VANTA.CLOUDS({
                el: "#demo",
                skyColor: 0x5eb7d9,
                cloudColor: 0xb1c2dc,
                cloudShadowColor: 0x1b3a57,
                sunColor: 0xff9c21,
                sunGlareColor: 0xfa6331,
                sunlightColor: 0xfa9531
            })
        </script>
    </body>
</html>
        """


# Add the HTML code to the Streamlit app using st.components.v1.html
st.components.v1.html(html_code,height=985 ,width=1000)


#rain(
    #emoji="🥳",
    #font_size=54,
    #falling_speed=5,
    #animation_length="infinite",


 #EXTRAS   
#from streamlit_extras.let_it_rain import rain
#add_logo(pacclogo,height=200)

#mention(label="An awesome Streamlit App",icon="streamlit",  # Some icons are available... like Streamlit!url="https://extras.streamlitapp.com",)
#rain(
    #emoji="🥳",
    #font_size=54,
    #falling_speed=5,
    #animation_length="infinite",
