from pcconfig import config
from .helpers import navbar
import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"
self_intro = 'Hello, I\'m **CHIANG, CHIAO-TUNG, who majors in Management Information Systems in National Chengchi University. I have passion on the field of Computer Science, specifically like Artifical Intelligence and Multi-media.'

class State(pc.State):
    """The app state."""

    pass

'''
pc.grid(
    pc.grid_item(row_span=2, col_span=1, bg="lightblue"),
    pc.grid_item(col_span=2, bg="lightgreen"),
    pc.grid_item(col_span=2, bg="yellow"),
    pc.grid_item(col_span=4, bg="orange"),
    template_rows="repeat(2, 1fr)",
    template_columns="repeat(5, 1fr)",
    h="200px",
    width="100%",
    gap=4,
)


 width: 128px;
        height: 128px;
        object-fit: cover;
        border-radius: 50%;
    }
'''

def home() -> pc.Component:
    return pc.box(
            pc.vstack(
            navbar(State),
            pc.center(
                pc.vstack(
                    pc.text("Hello", background_image="/color.jpg", background_clip="text", background_position = "center", font_weight="bold", font_size="13em", position = "relative",),
                    pc.text("NICE TO MEET YOU", background_image="linear-gradient( 64.3deg,  rgba(254,122,152,0.81) 17.7%, rgba(255,206,134,1) 64.7%, rgba(172,253,163,0.64) 112.1% )", background_clip="text", background_position = "center", font_weight="bold", font_size="5em", position = "relative",),
                #   pc.text("Hello", font_size = "5em", font_weight="bold", font_family="Ubuntu", background_clip="text", backgound_image="/MeganMonismith.jpg"),
                    pc.box(pc.grid(pc.grid_item(pc.box(pc.center(
                                                                 pc.image(src="astronut.png", box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",width="40", heigth="40", object_fit="cover", frameborder="0", scrolling="no", border_radius="50%", bg="white", padding="10px"),
                                                                 padding = "20px", padding_y="100px"), 
                                                       #pc.box(height="50%", width="30", bg="rgba(252, 218, 115, 0.8)", border_radius="20px", padding="40px", padding_y="50px", position="relative",box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",),
                                                       border_radius = '1em', height='100%', weight='100%'),
                                                row_span=5, col_span=3, bg="pink", padding_x="10px"),
                
                                   pc.grid_item(pc.box(pc.text(pc.markdown("""# <font face='Viga'>Hello,  \n \n #### I'm **Chiang, Chiao-Tung** , who majors in **Management Information System** in **National ChengChi University**.  \nI have passion on the field of Computer Science ,specifically such as Artifical Intellgence and Application Development.</font>""", height = "100%"), padding = 5, position = "relative", font_family="Ubuntu", font_size="26"),
                                            border_radius = '1em', bg = 'white',height='100%', weight='100%',box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",), row_span=5, col_span=9),
                                template_rows="repeat(5, 1fr)",
                                template_columns="repeat(12, 1fr)",
                                width = "100%",
                                height = "100%",
                                gap=4,
                                padding="20px",
                               ),
                             
                        height="25em", 
                        width="55em", 
                        bg="pink", 
                        top = "50px",
                        position = "relative", 
                        border_radius='20px',
                        ),

                    pc.box(pc.grid(pc.grid_item(pc.box(pc.text(pc.markdown("""<meta charset="utf-8"> <font size = "10">**Specialities**:</font>  \n Java 🌟🌟🌟🌟  \n Spring Boot、Android Applicaitons  \n Python 🌟🌟🌟  \nData Analysis """), color='white', padding="5px", position="relative",font_family="Viga", font_size="30"),border_radius='1em', height='100%', weight='100%'),row_span=5, col_span=5),
                                   pc.grid_item(pc.box(pc.text("Working Experience", font_size="30", font_family="Ubuntu", as_="b", height="50%", width="50%"),pc.table_container(pc.table(
        headers=["Work for", "Job","Date", "Content"],
        rows=[
            ("清大教科姚在府老師實驗室", "工讀", "2023.3 ~ current", "Responsible for FMRI data preprocessing and analysis with statistcal techniques."),
            ("政大程式設計概論", "TA", "2022.9 ~ 2023.1", "Responsible for"),
            ("Joe", 32, "Los Angeles","t"),
        ],
        footers=["可向右滑動>>>"],
        variant="striped",
    )
), padding="10px"),row_span=5, col_span=7, bg="white", border_radius="20px", padding = "10px",box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px"),
                                    template_rows="repeat(5, 1fr)", 
                                    template_columns="repeat(12, 1fr)", 
                                    width="100%", 
                                    height="100%",
                                    gap = 4, 
                                    padding = "15px"),
                       height="25em", 
                       width="55em", 
                       bg="lightblue",
                       top = "70px", 
                       position = "relative", 
                       border_radius='20px',
                       box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",
                       ),

                pc.box(height="25em", width="55em", bg="yellow", position = "relative", top = "90px", border_radius = '20px', element="iframe", src="https://RexRed6802.github.io/DataStructure_Team10"),
                ),
            top = "100px",
            position = "relative",
            ),
            height = "100%",
            ),
            #bg="linear-gradient(90deg, rgba(14,23,57,1) 0%, rgba(33,65,122,0.8174904942965779) 73%, rgba(33,73,82,1) 129%)",
            bg="linear-gradient(90deg, rgba(0,0,1,1) 0%, rgba(14,15,15,0.8174904942965779) 56%, rgba(33,73,82,1) 129%)",
            position="relative",
            background_size="cover",
            background_repeat = "no-repeat",
            width = "100%",
            height = "100vh",
            overflow = "auto"
            )

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )

"""
 pc.box(
"""


def project():
    return pc.box(
        navbar(State),
        pc.center(pc.vstack(
            pc.box(pc.grid(pc.grid_item(pc.box(pc.center(pc.vstack(
                                                                 pc.image(src="astronut.png", box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",width="40", heigth="40", object_fit="cover", frameborder="0", scrolling="no", border_radius="50%", bg="white", padding="10px")
                                                                 ,pc.text("RamerSearcher", padding_x="30px", color="white", font_size="20px", as_="b", font_family="Ubuntu"),
                                                                 padding_y = "40%", height="100%",width="100%"), 
                                                                 width = "100%", height="20em"), position="relative",                                                       #pc.box(height="50%", width="30", bg="rgba(252, 218, 115, 0.8)", border_radius="20px", padding="40px", padding_y="50px", position="relative",box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",),
                                                       border_radius = '1em', height='100%', weight='100%'),
                                                row_span=5, col_span=3, bg="pink", padding_x="10px"),
                
                                   pc.grid_item(pc.box(pc.text(pc.markdown("""# <font face='Viga'>Hello,  \n \n #### I'm **Chiang, Chiao-Tung** , who majors in **Management Information System** in **National ChengChi University**.  \nI have passion on the field of Computer Science ,specifically such as Artifical Intellgence and Application Development.</font>""", height = "100%"), padding = 5, position = "relative", font_family="Ubuntu", font_size="26"),
                                            border_radius = '1em', bg = 'white',height='100%', weight='100%',box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",), row_span=5, col_span=9),
                                template_rows="repeat(5, 1fr)",
                                template_columns="repeat(12, 1fr)",
                                width = "100%",
                                height = "100%",
                                gap=4,
                                padding="20px",
                               ),
                             
                        height="25em", 
                        width="60em", 
                        bg="pink", 
                        top = "200px",
                        position = "relative", 
                        border_radius='20px',
                        ),
             
            pc.box(height="25em", 
                        width="60em", 
                        bg="pink", 
                        top = "250px",
                        position = "relative", 
                        border_radius='20px',),
            pc.box(height="25em", 
                        width="60em", 
                        bg="pink", 
                        top = "350px",
                        position = "relative", 
                        border_radius='20px',),
            pc.box(height="25em", 
                        width="60em",  
                        top = "450px",
                        position = "relative", 
                        border_radius='20px',),
        )),
        bg="rgba(22, 57, 26, 0.71)",
        position="relative",
        background_size="cover",
        background_repeat = "no-repeat",
        width = "100%",
        height = "100vh",
        overflow = "auto"
    )



# Add state and page to the app.
app = pc.App(state=State, stylesheets=["https://fonts.googleapis.com/css2?family=Ubuntu&display=swap", "https://fonts.googleapis.com/css2?family=Viga&display=swap"])
app.add_page(index)
app.add_page(home, route='/home')
app.add_page(project, route='/project')
app.compile()
