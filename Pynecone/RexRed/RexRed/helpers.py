import pynecone as pc

def navbar(State):
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/fox.png", width="25px", height="auto"),
                pc.text("RexRed", font_size="1.5em", color="white", as_="b"),
                pc.link(pc.hstack(
                    pc.text("Project", font_size="1.5em", color = "white", as_="b", padding_x="5px"),
                ),
                href="/project",),
            ),
            pc.link(
                pc.hstack(
                    pc.heading("Github", size="lg", color = "white"),
                ),
                href="/home",
            ),
            
            pc.menu(),
        justify="space-between",
        
        padding_x='2em',
        padding_y='0.5em',
        ),
    position="Fixed",
    width="100%",
    top="0px",
    z_index="5",
    bg="rgba(0,0,0,0.9)",
    box_shadow="0 2px 4px 0 rgba(0,0,0,.2)"
    )
'''
pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("My App"),
        ),
        pc.spacer(),
        pc.menu(
            pc.menu_button("Menu"),
        ),
        position="Fixed",
        width="100%",
        top="0px",
        z_index="5",
        bg="red"
    ),
'''