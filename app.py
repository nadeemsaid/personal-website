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

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_rnfwc4vj.json")
img_me = Image.open("assets/thumbnail_image.png")
img_airboss = Image.open("assets/airboss.png")
img_seh = Image.open("assets/seh.png")
img_tauria = Image.open("assets/tauria.png")
img_lakes = Image.open("assets/lakes.png")
img_coaster = Image.open("assets/coaster.png")
img_minesweeper = Image.open("assets/minesweeper.png")
img_mystore = Image.open("assets/mystore.png")
img_turtle = Image.open("assets/turtle.png")
img_website = Image.open("assets/website.png")
img_wine = Image.open("assets/wine.png")
img_hussein = Image.open("assets/hussein.png")
img_fhh = Image.open("assets/fhh.png")
img_DCHRS = Image.open("assets/dchrs.png")
img_chatriley = Image.open("assets/chatriley.png")

##########################################################################################

with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.subheader("Hello! I'm Nadeem Said :wave:")
        im = st.image(img_me)

    with right_column:
        st.title("A fourth year B.A.Sc Computer Engineering student-athlete at the University of Waterloo graduating in April 2025")
        st.write("I am a part of the Waterloo Warriors Varsity Swim Team and the Jordanian National Swimming Team. "
                 "I balance school with over 17 hours of training a week. I’m an aspiring learner who is very passionate about the future. "
                 "I love programming and innovating new things that make life easier. More importantly, I love seeing people use what I develop in their daily lives. "
                 "I am currently interested in the field of Artifical Intelligence, specifically in Machine Learning and Natural Language Processing and have done \
                 a few internships in the field. "
                 "I am a very enthusiastic person and I love meeting new people.")
        st.write(
            "I was born on April 10th, 2002, in Amman, Jordan. I moved to Canada to pursue my undergraduate degree at the University of Waterloo. "
            "During my free time, I love playing the drums, going to the gym, and watching movies/TV shows. "
            "I enjoy travelling to new places and cooking/trying new authentic recipes from around the world. ")
        st.write(
            "I developed this website using a couple frameworks in the Python programming language such as Streamlit and Pillow. "
            "I enjoy developing programs in Python, C#, C++ and more! The main reason I developed this website is to build new connections "
            "and get to know people. The University of Waterloo has an outstanding Co-Op program that fortunately allows students to alternate "
            "study and work terms every 4 months. That being said, I’m actively looking for new opportunities that the future might hold.")
        st.write("[My Youtube Channel > ](https://www.youtube.com/channel/UC45GdVJRuV0fd4h-ymLLpNA)")

##########################################################################################
        
with st.container():
    st.write("---")
    st.header("Work Experience")
    st.write("###")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_tauria)
    with text_column:
        st.subheader("Tauria")
        st.write("-> Machine Learning Engineer (Jan-Apr 2024)")
        st.write("-> Developed and implemented an AI‑powered chatbot utilizing Python, OpenAI, LLMs, and other models to enhance communication within Tauria’s platform")
        st.write("-> Designed and deployed a secure web application with user authentication, persistent chat history, and API integration, optimizing for efficiency and scalability")
        st.write("-> Spearheaded end‑to‑end development of the UI/UX, ensuring seamless user experience and leveraging advanced routing/DNS knowledge for deployment")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lakes)
    with text_column:
        st.subheader("Lakes Environmental Software")
        st.write("-> A.I. and Data Engineer (May-Aug 2023)")
        st.write("-> Engineered a MVP deforestation detection system, employing a PyTorch CNN LSTM AI model, integrated with Flask for user‑intuitive result visualization")
        st.write("-> Utilized TensorFlow and Keras neural network & deep learning models for land cover change detection with Landsat & Sentinel satellite data")
        st.write("-> Employed GIS‑powered Python workflows integrating GDAL to download, preprocess, & analyze satellite imagery for environmental monitoring")
        st.write("-> Conducted research on land cover usage change, deforestation, & climate change using remote sensing & AI techniques")
        st.write("-> Created reporting mechanisms for timely insights on environmental changes, supporting resource management and ecological monitoring")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lakes)
    with text_column:
        st.subheader("Lakes Environmental Software")
        st.write("-> Software Developer (Sept-Dec 2022)")
        st.write(
            "-> Worked in Python (different libraries) to analyze & present geospatial data. Wrote programs using satellite imagery to help farmers in vegetation planning")
        st.write(
            "-> Optimized internal web application tools by 200% using C# to read over a year worth of weather data taken at every hour of every day")
        st.write(
            "-> Built a CLI tool that runs a section of the application when requested, to optimize all company application performances at deployment")
        st.write(
            "-> Improved application security by preventing potential open redirect vulnerabilities and CSRF attacks")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_seh)
    with text_column:
        st.subheader("SEH Computer Systems")
        st.write("-> Full Stack Developer (Jan-Apr 2022)")
        st.write("-> Engaged in multiple agile‑supported sprint ceremonies such as review, retro, refinement, planning to meet user centric needs")
        st.write("-> Worked with Microsoft Stack (ASP.NET, EF Core, C#) from the SQL DB to the UI end, gaining experience in API, UI, "
                 "and testing on both ends to develop a Vehicle Insurance Web App")
        st.write("-> Redesigned UI pages to enhance user experience following discussions with the UI/UX Team")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_airboss)
    with text_column:
        st.subheader("Airboss Rubber Solutions")
        st.write("-> Production Employee (May-Aug 2021)")
        st.write("-> Operated Allen Bradley control systems to run a mill, making different types of rubber sheets while "
                 "taking measures to increase production efficiency")
        st.write("-> Mitigated risks on the production line using communication and multi‑generational teamwork, "
                 "and worked under Lean Six Sigma safety standards")
        st.write("-> Familiarized with control panel circuitry and TCU circuitry")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_fhh)
    with text_column:
        st.subheader("Fine Hygienic Holding (FHH)")
        st.write("-> Intern (May-Aug 2018)")
        st.write("-> Shadowed an Enterprise Operations Manager and developed strategies to optimize production lines through analyzing production data")
        st.write("-> Enhanced skills in efficient planning, budgeting, work ethics and time management")

##########################################################################################
        
with st.container():
    st.write("---")
    st.header("Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_chatriley)
    with text_column:
        st.subheader("ChatRiley the Recruiter")
        st.write(
            "-> Developed and deployed Riley, a resume chatbot powered by LLMs and AI, utilizing vector databases and proximity vectors for professional \
                and personalized responses to user queries"
        )
        st.write(
            "-> Integrated OpenAI’s GPT‑4 technology, enabling seamless context‑aware question answering, enhancing recruiter interactions with uploaded resumes"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/resume-chatbot-llm)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_DCHRS)
    with text_column:
        st.subheader("Dolphin Chains HR Solutions")
        st.write(
            "-> Developed DCHRS, a decentralized HR platform leveraging blockchain for secure and cost‑effective document management, empowering companies"
        )
        st.write(
            "-> Overcame integration challenges, gaining deep blockchain expertise through collaboration with industry leaders, enabling scalable & efficient HR solutions"
        )
        st.markdown("[DevPost Link](https://devpost.com/software/dolphin-chains-hr-solutions)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mystore)
    with text_column:
        st.subheader("My Store")
        st.write(
            "-> A Web Application developed with C#, SQL Server Database and HTML. Allows users to enter personalized information into the DB"
        )
        st.write(
            "-> The app allows CRUD operations on entries"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/my-store)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_minesweeper)
    with text_column:
        st.subheader("Waterloo Minesweeper Game")
        st.write(
            "-> Programmed using C++, a unique version of Minesweeper, adapted to specifically fit the campus environment of the University of Waterloo"
        )
        st.write(
            "-> Implemented search algorithms to check and update game status"
        )
        st.write(
            "-> Generated and managed a board using the array data structure with bit‑shifting and masking"
        )

        st.markdown("[Github Link](https://github.com/nadeemsaid/Waterloo-Minesweeper-Game)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_website)
    with text_column:
        st.subheader("Personal Website")
        st.write(
            "-> A personal website developed with Python (Streamlit, Pillow) to promote myself and connect with people"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/personal-website)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_turtle)
    with text_column:
        st.subheader("Water NinjaTurtle")
        st.write(
            "-> Utilized autoCAD to design and 3D‑print a turtle that rests over a fish aquarium"
        )
        st.write(
            "-> Assembled a circuit‑board consisting of LED lights, sensors, batteries, resistors that lights up the LED light whenever the fish‑tank needs more water"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/Water-NinjaTurtle)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_coaster)
    with text_column:
        st.subheader("The Need for Speed")
        st.write(
            "-> Researched the question of: How does the approach velocity affect the energy dissipation within a circular roller coaster loop?"
        )
        st.write(
            "-> Wrote a step-wise iteration theory before designing and building a real modeled roller coaster to test the theory practically"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/The-Need-for-Speed)")

st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_wine)
    with text_column:
        st.subheader("The Sound of Wine")
        st.write(
            "-> Research Question: How does the resonant frequency when a wine glass rim is excited depend on the volume of wine in the glass?"
        )
        st.write(
            "-> Modeled the data as a graph and used regression to determine a relationship equation"
        )
        st.markdown("[Github Link](https://github.com/nadeemsaid/The-Sound-of-Wine)")

##########################################################################################
        
with st.container():
    st.write("---")
    st.header("Volunteer Work")
    st.write("###")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_hussein)
    with text_column:
        st.subheader("Al Hussein Society")
        st.write("-> Swimming Instructor (Mar-Apr 2018)")
        st.write("-> Taught a child diagnosed with spastic diplegic cerebral palsy how to swim using different training methods")
        st.write("-> Developed an individualized curriculum focusing on strengthening various muscle groups")
        st.markdown("[Created a YouTube Video to summarize this volunteering experience](https://youtu.be/gN3S_3T5kZI)")

##########################################################################################

with st.container():
    st.write("---")
    st.header("Honours & Awards")
    st.write("###")
    for award in [
        {
            "title": "4X USPORTS Academic All-Canadian (2024)",
            "event": "USPORTS Academic Award for top student-athlete academic achievers",
        },
        {
            "title": "Jackal Protocol First Place Award (2023)",
            "event": "[OlympiHacks (Waterloo Blockchain Olympics) Hackathon](https://olympihacks.devpost.com/?ref_feature=challenge&ref_medium=discover)",
        },
        {
            "title": "Athletic Award (2020)",
            "event": "[Board of Trustees Award for Distinguished Representation of Jordan](https://youtu.be/EKF7Eydryyg)",
        },
        {
            "title": "Academic Award (2019)",
            "event": "Awarded by PSUT for being one of the top 100 academic achievers in the Jordan in 2019",
        },
        {
            "title": "Silver & Bronze Medalist (2017)",
            "event": "200m & 100m backstroke - Stuttgart International Swimming Championships",
        },
    ]:
        st.write(f"**{award['title']}**")
        st.write(f"- {award['event']}")
        st.write("")
        st.write("")

##########################################################################################
        
with st.container():
    st.write("---")
    st.header("Contact Information")
    # st.write("Easy way to send me an email below :wink:")
    # st.write("##")
    #
    # contact_form = """
    # <form action = "https://formsubmit.co/1aacf84584ca2f3f2cb17bfd075d3bc6" method = "POST">
    # <input type="hidden" name="_captcha" value="false">
    # <input type="text" name="name" placeholder="Your name" required>
    # <input type="email" name="email" placeholder="Your email" required>
    # <textarea name="message" placeholder="Your message here" required></textarea>
    # <button type="submit">Send</button>
    # </form>
    # """

    left_column, right_column = st.columns(2)
    with left_column:
        #st.markdown(contact_form, unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.subheader("[Connect with me on LinkedIn! > ](https://www.linkedin.com/in/nadeem-said-517951164)")
        st.subheader("[Take a look at my Github! > ](https://github.com/nadeemsaid)")
        st.markdown("<h3 style='color: light-purple;'>Do not hesitate to contact me on either:</h3>", unsafe_allow_html=True)
        st.write("My Email : nsaid@uwaterloo.ca")
        st.write("My Phone Number : 437-986-7215")



    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

with st.container():

    with open("assets/me.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Nadeem's Resume",
                       data=PDFbyte,
                       file_name="nadeem_resume.pdf",
                       mime='application/octet-stream')

with st.container():
    copyright = """<h1 style='text-align: center; color: white;'>Nadeem Said 2024</h1>"""
    st.header("")
    st.header("")
    st.markdown(copyright, unsafe_allow_html=True)