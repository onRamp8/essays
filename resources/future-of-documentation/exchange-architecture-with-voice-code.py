        # create the components
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

        # position the components on screen
        trader1.move_to(SanimGrid.ROW_2_minus_three)
        trader2.move_to(SanimGrid.ROW_0_minus_three)
        gwy.move_to(SanimGrid.ROW_2_plus_one)
        eng.move_to(SanimGrid.ROW_0_plus_one)
        mkd.move_to(SanimGrid.ROW_down2_plus_one)
        world.move_to(SanimGrid.ROW_down2_minus_three)

        # add the components to the screen
        self.add(trader1)
        self.add(trader2)
        self.add(gwy)
        self.add(eng)
        self.add(mkd)
        self.add(world)
        
        # create connections between components
        self.add_connection_right(trader1, gwy)
        self.add_connection_right(trader2, gwy)
        self.add_connection_below(gwy, eng)
        self.add_connection_below(eng, mkd)
        self.add_connection_right(world, mkd)

        # write the components to the screen and verbalize whats on screen
        with self.voiceover(text="Here is the trading system architecture") as tracker:
            self.wait(tracker.duration)
        
        # create the talking point highlighter (boiler plate)
        talking_pt = Rectangle(height=trader1.height, width=trader1.width)
        talking_pt.set_stroke(width=9.5)
        talking_pt.set_color(YELLOW)
        talking_pt.move_to(trader1.get_center())

        
        #### Begin the content of explaining the components ####
        
        with self.voiceover(text="There are two traders using the system") as tracker:
            self.play(Write(talking_pt), run_time=0.2)
            self.wait(1.0)
            self.highlight(talking_pt, trader2)
            
        highlight_duration = 1.0
        with self.voiceover(text="There is a gateway that validates messages and routes them 
to the engine") as tracker:
            self.highlight(talking_pt, gwy, highlight_duration)
            self.wait(tracker.duration - highlight_duration)

        with self.voiceover(text="There is the matching engine that matches the buys and 
sells and maintains the order book") as tracker:
            self.highlight(talking_pt, eng)
            self.wait(tracker.duration - highlight_duration)

        with self.voiceover(text="There is the market data publisher, that streams all 
market activity to anyone who wants to listen") as tracker:
            self.highlight(talking_pt, mkd, highlight_duration)
            self.wait(tracker.duration - highlight_duration)

        with self.voiceover(text="Finally there are all the market data subscribers. This 
could be bloomberg, other traders, banks, anyone") as tracker:
            self.highlight(talking_pt, world, highlight_duration)
            self.wait(tracker.duration - highlight_duration)

        self.play(FadeOut(talking_pt))
        

        #### Begin the content of showing the trade messaging ####

        with self.voiceover(text="Now trader 1 sends a buy order for 1 Bitcoin for $20") as 
tracker:
            trader1.send_msg_to(gwy, self, runtime=tracker.duration)
            
        with self.voiceover(text="The gateway routes the order to the Bitcoin-USD matching 
engine") as tracker:
            gwy.send_msg_to(eng, self, runtime=tracker.duration)

        with self.voiceover(text="the engine saves the order on the book and sends an order 
acknowledgement to the user") as tracker:
            runtime_part = tracker.duration / 2.0
            eng.send_msg_to(gwy, self, runtime=runtime_part)
            gwy.send_msg_to(trader1, self, runtime=runtime_part)
    
        with self.voiceover(text="the engine also sends new order event to market data") as 
tracker:
            eng.send_msg_to(mkd, self, runtime=tracker.duration)
            
        with self.voiceover(text="market data sends the new order event to all market data 
subscribers") as tracker:
            mkd.send_msg_to(world, self, runtime=tracker.duration)

        with self.voiceover(text="trader 2 sends a sell order for 1 Bitcoin for $20") as 
tracker:
            trader2.send_msg_to(gwy, self, runtime=tracker.duration)
    
        with self.voiceover(text="The order matches with trader one and the engine sends 
fill messages to both users") as tracker:
            msg_runtime = tracker.duration / 5.0
            gwy.send_msg_to(eng, self, runtime=msg_runtime)
            eng.send_msg_to(gwy, self, runtime=msg_runtime)
            gwy.send_msg_to(trader1, self, runtime=msg_runtime)
            eng.send_msg_to(gwy, self, runtime=msg_runtime)
            gwy.send_msg_to(trader2, self, runtime=msg_runtime)

        with self.voiceover(text="the engine sends trade messages to market data which goes 
out to all subscribers") as tracker:
            msg_runtime = tracker.duration / 2.0
            eng.send_msg_to(mkd, self, runtime=msg_runtime)
            mkd.send_msg_to(world, self, runtime=msg_runtime)

        with self.voiceover(text="This concludes the video. Thanks for watching") as 
tracker:
            self.flash("End of Video")
            self.wait(tracker.duration)

