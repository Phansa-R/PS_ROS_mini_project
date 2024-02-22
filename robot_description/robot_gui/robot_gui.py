#!/usr/bin/env python3
import customtkinter as ctk
import rospy
from sensor_msgs.msg import JointState

from std_msgs.msg import Int16, Float32

window = ctk.CTk()
window.title('P-P-ROBOT')
window.geometry('400x180')
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

#เเสดงposition
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
checkbox_frame1 = ctk.CTkFrame(master=window)
checkbox_frame1.grid(row=10, column=10, padx=10, pady=(10, 0))
ctk.CTkLabel(checkbox_frame1, text="Position",font=("Arial", 30)).pack(expand=True, fill='both', padx=10, pady=0)
ctk.CTkLabel(checkbox_frame1, text="[sensor feedback]",font=("Arial", 13)).pack(expand=True, fill='both', padx=0, pady=0)
#รับค่าจากเซ็นเซอร์เเนวเเกนX
FEEDBACKX = ctk.CTkLabel(checkbox_frame1, text="Value X")
FEEDBACKX.pack(expand=True, fill='both', padx=20, pady=10)
#รับค่าจากเซ็นเซอร์เเนวเเกนY
FEEDBACKY = ctk.CTkLabel(checkbox_frame1, text="Value Y")
FEEDBACKY.pack(expand=True, fill='both', padx=20, pady=10)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#เเสดง input จาก Contro

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
checkbox_frame = ctk.CTkFrame(master=window)
checkbox_frame.grid(row=10, column=20, padx=0, pady=(10, 0))
ctk.CTkLabel(checkbox_frame, text="  Input   ",font=("Arial", 30)).pack(expand=True, fill='both', padx=30, pady=0)
ctk.CTkLabel(checkbox_frame, text="[desired points (X, Y)]",font=("Arial", 13)).pack(expand=True, fill='both', padx=0, pady=0)
#รับค่าจากเซ็นเซอร์เเนวเเกนX
FEEDBACKX_INPUT = ctk.CTkLabel(checkbox_frame, text="Value X")
FEEDBACKX_INPUT.pack(expand=True, fill='both', padx=20, pady=10)

#รับค่าจากเซ็นเซอร์เเนวเเกนY
FEEDBACKY_INPUT = ctk.CTkLabel(checkbox_frame, text="Value Y")
FEEDBACKY_INPUT.pack(expand=True, fill='both', padx=20, pady=10)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def button_click_event():
    global xs, ys
    dialogx = ctk.CTkInputDialog(text="Desired X:", title="Test")
    xs = float(dialogx.get_input())
    print("X Number:", xs)
    FEEDBACKX_INPUT.configure(text=xs)
    dialogy = ctk.CTkInputDialog(text="Desired Y:", title="Test")
    ys = float(dialogy.get_input())
    print("Y Number:", ys)
    FEEDBACKY_INPUT.configure(text=ys)

def button_click_event_submit():
    js = JointState()
    js.header.stamp = rospy.Time.now()
    js.header.frame_id = " "
    js.name = ["joint1" , "joint2"]  # Fill in with the names of your joints
    js.position = [float(FEEDBACKX_INPUT.cget('text')), float(FEEDBACKY_INPUT.cget('text'))]  # Fill in with the positions of your joints
    Int16_1 = Float32()
    Int16_1.data = float(FEEDBACKX_INPUT.cget('text'))
    Int16_2 = Float32()
    Int16_2.data = float(FEEDBACKY_INPUT.cget('text'))
    pub_datafrom_GuiX = rospy.Publisher("Topic_DataXFrom_Gui", Float32, queue_size=10)
    pub_datafrom_GuiY = rospy.Publisher("Topic_DataYFrom_Gui", Float32, queue_size=10)
    pub_datafrom_GuiX.publish(Int16_1)
    pub_datafrom_GuiY.publish(Int16_2)
    pub.publish(js)
    rate.sleep()

def setup_event():
    print("Setup event is triggered!")
    js = JointState()
    js.header.stamp = rospy.Time.now()
    js.header.frame_id = " "
    js.name = ["joint1" , "joint2"]  
    js.position = [0 , 0]  
    '''js.velocity = []  # Fill in with the velocities of your joints
    js.effort = []  # Fill in with the effort values of your joints'''
    pub.publish(js)
    rate.sleep()


def read_ualtraX(ualtraX_val):
    ultraX_2_read = ualtraX_val.data
    FEEDBACKX.configure(text=ultraX_2_read)
    

def read_ualtraY(ualtraY_val):
    ultraY_2_read = ualtraY_val.data
    FEEDBACKY.configure(text=ultraY_2_read)

sub_UltraX = rospy.Subscriber("Topic_Feedback_UaltraY", Int16, callback = read_ualtraX)
sub_UltraY = rospy.Subscriber("Topic_Feedback_UaltraX", Int16, callback = read_ualtraY)

def read_potenX(potenX_val):
    poten_2_read = potenX_val.data
    FEEDBACKX_INPUT.configure(text=poten_2_read)

def read_encodeY(encodeY_val):
    encode_2_read = encodeY_val.data
    FEEDBACKY_INPUT.configure(text=encode_2_read)

sub_potenX = rospy.Subscriber("Topic_Feedback_poten", Int16, callback = read_potenX)
sub_encodeY = rospy.Subscriber("Topic_Feedback_encode", Int16, callback = read_encodeY)

window.after(1000, setup_event)

button = ctk.CTkButton(window, text="Config", command=button_click_event ,width = 70, height =70)
button.place(x = 320, y = 10)

button = ctk.CTkButton(window, text="Submit", command=button_click_event_submit ,width = 70, height =70,hover_color = "green")
button.place(x = 320, y = 95)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#if _name_ == "_main_":

rospy.init_node('robot_joint_state_publisher',anonymous=True)
pub = rospy.Publisher('joint_states', JointState, queue_size=10)

pub_datafrom_GuiX = rospy.Publisher("Topic_DataXFrom_Gui", Float32, queue_size=10)
pub_datafrom_GuiY = rospy.Publisher("Topic_DataYFrom_Gui", Float32, queue_size=10)
rate = rospy.Rate(10)
window.mainloop()