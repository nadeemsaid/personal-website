import js2py
from PIL import Image, ImageChops, ImageDraw
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Nadeem Said", page_icon = ":bow:", layout="wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# def crop_to_circle(im):
#     bigsize = (im.size[0] * 3, im.size[1] * 3)
#     mask = Image.new('L', bigsize, 0)
#     ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
#     mask = mask.resize(im.size, Image.ANTIALIAS)
#     mask = ImageChops.darker(mask, im.split()[-1])
#     im.putalpha(mask)
#
# im = Image.open("images/thumbnail_image.png").convert('RGBA')
# crop_to_circle(im)
# im.save('images/thumbnail_image.png')

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_rnfwc4vj.json")
img_me = Image.open("images/thumbnail_image.png")
img_airboss = Image.open("images/airboss.png")
img_seh = Image.open("images/seh.png")
img_lakes = Image.open("images/lakes.png")

##########################################################################################
with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.subheader("Hello! I'm Nadeem Said :wave:")
        im = st.image(img_me)

    with right_column:
        st.title("A third year Computer Engineering student-athlete at the University of Waterloo")
        st.write("I am a part of the Waterloo Warriors Varsity Swim Team and the Jordanian National Swimming Team. "
                 "I balance school with over 15 hours of training a week. I’m an aspiring learner who is very passionate about the future. "
                 "I love programming and innovating new things that make life easier. More importantly, I love seeing people use what I develop in their daily lives. "
                 "I am a very enthusiastic person and I love meeting new people.")
        st.write(
            "I was born on April 10th, 2002, in Amman, Jordan. I moved to Canada to pursue my undergraduate degree at the University of Waterloo."
            "During my free time, I love playing the drums, going to the gym, and watching movies/TV shows. "
            "I enjoy cooking and trying new authentic recipes as well.")
        st.write(
            "I developed this website using a couple frameworks in the Python programming language such as Streamlit and Pillow. "
            "I enjoy developing programs in Python, C#, C++ and more! The main reason I developed this website is to build new connections "
            "and get to know people. The University of Waterloo has an outstanding Co-Op program that fortunately allows students to alternate "
            "study and work terms every 4 months. That being said, I’m actively looking for new opportunities that the future might hold.")
        st.write("[My Youtube Channel > ](https://www.youtube.com/channel/UC45GdVJRuV0fd4h-ymLLpNA)")


# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("What I do")
#         st.write("**summary of what I do**")
#         st.write("[My Youtube Channel >](https://www.youtube.com)")
#     with right_column:
#         st_lottie(lottie_coding, height=400, key="coding")

##########################################################################################
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("Projects coming soon! :grin:")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.empty()
    with text_column:
        st.subheader("Project name")
        st.write(
            "About project"
        )
        st.markdown("[Watch Video...](https://www.youtube.com)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.empty()
        #st.image(img_contact_form)
    with text_column:
        st.subheader("Project name")
        st.write(
            "About project"
        )
        st.markdown("[Watch Video...](https://www.youtube.com)")

##########################################################################################
with st.container():
    st.write("---")
    st.header("Experience")
    st.write("###")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lakes)
    with text_column:
        st.subheader("Lakes Environmental Software")
        st.write(
            "About Lakes -- coming soon! :grin:"
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_seh)
    with text_column:
        st.subheader("SEH Computer Systems")
        st.write("Full Stack Developer (Jan-Apr 2022)")
        st.write("Participated in multiple agile‑supported sprint ceremonies such as review, retro, refinement, planning to meet user centric needs")
        st.write("Worked with Microsoft Stack (ASP.NET, EF Core, C#) from the SQL DB to the UI end, gaining experience in API, UI, "
                 "and testing on both ends to develop a Vehicle Insurance Web App")
        st.write("Participated in discussions with the UI/UX Team and redesigned UI pages to service a better user experience")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_airboss)
    with text_column:
        st.subheader("Airboss Rubber Solutions")
        st.write("Production Employee (May-Aug 2021)")
        st.write("Operated Allen Bradley control systems to run a mill, making different types of rubber sheets while "
                 "taking measures to increase production efficiency")
        st.write("Mitigated risks on the production line using communication and multi‑generational teamwork, "
                 "and worked under Lean Six Sigma safety standards")
        st.write("Familiarized with control panel circuitry and TCU circuitry")

##########################################################################################
with st.container():
    st.write("---")
    st.header("Contact Information")
    st.write("Easy way to send me an email below :wink:")
    st.write("##")

    contact_form = """
    <form action = "https://formsubmit.co/1aacf84584ca2f3f2cb17bfd075d3bc6" method = "POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.subheader("[Connect with me on LinkedIn! > ](https://www.linkedin.com/in/nadeem-said-517951164)")
        st.subheader("[Take a look at my Github! > ](https://github.com/nadeemsaid)")



    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

with st.container():

    with open("me.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Nadeem's Resume",
                       data=PDFbyte,
                       file_name="test.pdf",
                       mime='application/octet-stream')

with st.container():
    copyright = """<h1 style='text-align: center; color: white;'>Nadeem Said 2022</h1>"""
    st.header("")
    st.header("")
    st.markdown(copyright, unsafe_allow_html=True)