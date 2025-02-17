import random
import streamlit as st
st.title('👹Text Advanture Game')
if 'start_game'not in st.session_state:
     st.session_state.start_game='start'
if 'doors'not in st.session_state:
     st.session_state.doors=random.randint(1,3)
if 'opened'not in st.session_state:
     st.session_state.opened=[]
if 'Gold' not in st.session_state:
     st.session_state.Gold=random.randint(1,5)
if 'attempts' not in st.session_state:
     st.session_state.attempts=3

def game():
     if st.session_state.start_game=='start':
          startup()
     elif st.session_state.start_game=='Door':
          Door()
     elif st.session_state.start_game=='Monster':
          Monster()
     elif st.session_state.start_game=='Gold_room':
          Gold_room()
     elif st.session_state.start_game=='GameOver':
          GameOver()
def startup():
    st.write("This is a simple game in which you have to find gold.")
    st.write("All the best.")
    st.write("Click on start button to start the game.")
    if st.button("💀Start"):
         st.session_state.start_game='Door'
         if st.button("Continue"):
            st.rerun()
def Door():
    st.write("You are in a dark room in which 3 doors are shining.")
    door=int(st.number_input("\nEnter the door number where you will go:",min_value=0,format='%d'))
    if st.button("🚪Open Door"):  
      if door==st.session_state.doors:
         st.session_state.start_game='Gold_room'
      else:   
         st.session_state.start_game='Monster'
         if st.button("Continue"):
            st.rerun()
def Monster():
    st.write("👽You are in the room of monster.")
    choice=st.radio('What will you do( ⚔️fight, 🏃run):', options=['⚔️fight', '🏃run'])
    if st.button("Confirmed Action"):
        monster=random.choice([ '⚔️fight', '🏃run'])
        if choice=='🏃run' and monster=='🏃run':
            st.success("Both run away.You reach the dark room again.")
            st.session_state.start_game='Door'
        elif choice=='🏃run' and monster=='⚔️fight':
            st.error("Monster caught you before running away.Game Over")
            st.session_state.start_game='GameOver'
        elif choice=='⚔️fight' and monster=='⚔️fight':
            st.success("You defeated the monster. Proceed to gold room")
            st.session_state.start_game='Gold_room'
        else:
            st.success('The monster scared from you and run away. Proceed to Gold room')
            st.session_state.start_game='Gold_room'  
        if st.button("Continue"):
              st.rerun()    
def Gold_room():
    st.write("💰Welcome to Gold Room.")
    st.write("In this room you have 5 boxes. 2 are 📦empty, 2 contain 💣bomb and 1 contain 💰gold.")
    st.write(f"{st.session_state.attempts} Attempts")

    num=int(st.number_input("\nEnter the box number Where you think gold is present:",min_value=1,max_value=5,step=1,format='%d'))
    if st.button("🚪Open Box"):
        if num in st.session_state.opened:
            st.warning("You have already checked this box.")
        else:
            st.session_state.opened.append(num)
            st.session_state.attempts-=1
            if num==st.session_state.Gold:
                st.balloons()
                st.success("Congratulate! you are the winner.You found the Gold.")
                st.session_state.start_game='GameOver'
            elif num<st.session_state.Gold:
                st.write("This is an empty 📦box")          
            else:
                st.write("You found a bomb.")
            if st.session_state.attempts==0:
                st.error("No attempts left.")
                st.session_state.start_game='GameOver'   
            if st.button("Continue"):
              st.rerun()                       
def GameOver():
    st.write("Game Over")
    if st.button('🔁Play Again'):
        reset_game()
        if st.button("Continue"):
           st.rerun()

def reset_game():
     st.session_state.start_game='start'
     st.session_state.doors=random.randint(1,3)
     st.session_state.opened=[]
     st.session_state.Gold=random.randint(1,5)
     st.session_state.attempts=3

game()
