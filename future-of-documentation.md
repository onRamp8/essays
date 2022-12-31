# Future of documentation. Finally making it fun.
For most of my career I didn't really enjoy reading or writing documentation.
It constantly went out of date. Javadocs, markdown and doc generators helped
but images and diagrams were a pain. Then [plant UML](https://plantuml.com/sequence-diagram)
came along, which changed the game. You could now fully version all docs, text 
and diagrams with source code! I loved that idea, however I still wanted more.
For complex systems I had to setup meetings to walk people through the docs or create 
videos to explain things more detail. Thanks to improvements in AI I was able
to hack together some python code that will completely generate an explanatory 
video. And its all in code:
* the components
* how they interact
* the vocals (thanks to text to voice AI)
* visual effects

Here is how it works. In this example
lets explains how a simplified financial exchange architecture could work for 
the use case of a bitcoin trade. First, create the components of your system. 
```python
        trader1 = create_component("Trader1")
        trader1.set_color(GREEN)
        
        trader2 = create_component("Trader2")
        trader2.set_color(BLUE)
        
        gwy = create_component("GWY")
        gwy.set_color(PURPLE)
        
        eng = create_component("ENG")
        eng.set_color(RED)
        
        mkd = create_component("MKD")
        mkd.set_color(PINK)
        
        world = create_component("world")
        world.set_color(GREY)
```
Add the connections between components
```python
        self.add_connection_right(trader1, gwy)
        self.add_connection_right(trader2, gwy)
        self.add_connection_below(gwy, eng)
        self.add_connection_below(eng, mkd)
        self.add_connection_right(world, mkd)
```
After all the components and connections are added the code will create a display
on screen like this [exchange architecture](resources/future-of-documentation/exchange-architecture.jpg)

Now we can add the voice to text code to do the walk through for us
```python
        # the text in the below line will define what the AI will verbalize
        with self.voiceover(text="There are two traders using the system") as tracker:
            self.play(Write(talking_pt), run_time=0.2)
            self.wait(1.0)
            self.highlight(talking_pt, trader2)
            
        # the text in the below line will define what the AI will verbalize
        with self.voiceover(text="There is a gateway that validates messages and routes them to the engine") as tracker:
            self.highlight(talking_pt, gwy, highlight_duration)
            self.wait(tracker.duration - highlight_duration)
```
In the above code will highlight the trader components and at the same time verbalize 
"There are two traders using the system". The next block will highlight the gateway
component (GWY) and verbalize "There is a gateway that validates messages and routes them to the engine"
The rest of the video covers sending messages, describing processing logic and walk users through the details.
You can view the video [on youtube](https://youtu.be/H-LkCHaIMvM). You can view
the video source code [on github](resources/future-of-documentation/exchange-architecture-with-voice-code.py)

I just finished this proof of concept and deployed it for beta testing. I'm excited that
I won't have to schedule meetings and walk people through architecture diagrams anymore. I can just
code up a video and send the link! Plus I am interested to see how my team and colleages 
can collaborate on coding the videos together. Previously there wasn't a good way to 
iterate on a video, but now these videos can move at the speed of code. 
As it should! 

I have a bunch more features already working locally like:
* add custom images
* move and animate images
* add components as images, send and receive messages from them
* many more animation effects

Long term I think I could make these as engaging as the good technical creators on
youtube and tiktok, but we will see about that. For now I'm happy with less 
meetings. Lastly I'm looking for beta 
testers so if you are interested in trying it free of charge 
[head to the landing page](https://eightorchard.mailchimpsites.com/)
and I'll send you your own browser based instance (Jupyter notebook) to play around
with. No installation needed. Hope you found this interesting and thanks for reading.
