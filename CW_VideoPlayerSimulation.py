#import all the needed functions
from tkinter import *
import tkinter as tk 
import tkinter.scrolledtext as tkst
import csv


class VideoPlayer:  # main class
    def __init__(self, name): #create class
        self.name = name
        self.video_player_window = tk.Tk()  # window
        self.video_player_window.title('Video Player')  # window title
        self.video_player_window.geometry('400x100')  # window size
        #self.video_player_window.resizable(False, False)  # make the window size cannot be changed by user

        self.create_video_player_function()  # add function to the window

    def read_csv_as_dict(self, file_path): #reading file csv function
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
        
    def read_csv_output(self, file_path):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            data = [row for idx, row in enumerate(reader) if idx > 0]  # Skip the first row
        return data
    
    def create_video_player_function(self):  # create function for window
        # text atributes & posision
        self.begin_text = tk.Label(self.video_player_window, text='Select An Option By Clicking One Of The Buttons Below')
        self.begin_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        # check video btn
        self.check_videos_button = tk.Button(self.video_player_window, text='Check Videos', command=self.check_videos, width=15, height=2)
        self.check_videos_button.grid(row=1, column=0, padx=10, pady=10)
        # create video list btn
        self.create_video_list_button = tk.Button(self.video_player_window, text='Create Video List', command=self.create_video_list, width=15, height=2)
        self.create_video_list_button.grid(row=1, column=1, padx=10, pady=10)
        #update video btn
        self.update_video_button = tk.Button(self.video_player_window, text='Update Video', command=self.update_video, width=15, height=2)
        self.update_video_button.grid(row=1, column=2, padx=10, pady=10)



#Check video things--------------------------------------------------------------------------------------------    

    def check_videos(self):  # after click the Check Videos button
        self.check_videos_window = tk.Toplevel(self.video_player_window)  # open another window
        self.check_videos_window.title('Check Videos')  #title
        self.check_videos_window.geometry('620x300')  #size
        #self.check_videos_window.resizable(False, False)  # make the window size cannot be changed by user

        self.create_check_videos_functions()  # add window functions

    def create_check_videos_functions(self):  # window functions
        #list all videos btn atributes & possion
        self.list_all_videos_button = tk.Button(self.check_videos_window, text='List All Videos', command=self.list_all_videos_button_clicked, width=15, height=2)
        self.list_all_videos_button.grid(row=0, column=0, padx=10, pady=10)

        #Enter Video Number text
        self.enter_video_number_text = tk.Label(self.check_videos_window, text='Enter Video Number', font=("ariel", 11))
        self.enter_video_number_text.grid(row=0, column=1, padx=10, pady=10)
        
        #input, user write a video's number
        self.input_video_number = tk.Entry(self.check_videos_window, width=4)
        self.input_video_number.grid(row=0, column=2, padx=10, pady=10)

        #check video btn
        self.check_video_button = tk.Button(self.check_videos_window, text='Check Video', command=self.check_video, width=15, height=2)
        self.check_video_button.grid(row=0, column=3, padx=10, pady=10)
        
        #list of video
        self.video_list = tkst.ScrolledText(self.check_videos_window, height=10, width=40)
        self.video_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        #output video's information
        self.video_information_output = tk.Text(self.check_videos_window, height=6, width=28)
        self.video_information_output.grid(row=1, column=3, padx=10, pady=10)
        
    def list_all_videos_button_clicked(self): #after click the List All Videos btn, it will show all the current video
        csv_file_path = 'videos.csv' #choose csv file to read the information
        csv_data = self.read_csv_as_dict(csv_file_path)

        self.video_list.delete(1.0, tk.END) #clear the previous text
        

        for video in csv_data: #insert video data in the right order
            video_info = f"Video Number: {video['number']}\nName: {video['name']}\nDirector: {video['director']}\n"
            self.video_list.insert(tk.END, video_info)

    def check_video(self): #showing the selected video's information
        video_number = self.input_video_number.get()
        csv_file_path = 'videos.csv' #csv file
        csv_data = self.read_csv_as_dict(csv_file_path)

        video_info = next((video for video in csv_data if video['number'] == video_number), None)

        self.video_information_output.delete(1.0, tk.END) #clear previous text

        if video_info: #display data in right order
            self.video_information_output.insert(tk.END, f"Name: {video_info['name']}\n")
            self.video_information_output.insert(tk.END, f"Director: {video_info['director']}\n")
            self.video_information_output.insert(tk.END, f"Rating: {video_info['rating']}\n")
            self.video_information_output.insert(tk.END, f"Plays: {video_info['plays']}\n")
        else: #if the number user choose is invalid
            self.video_information_output.insert(tk.END, 'Video not found\n')

#Check Video things---------------------------------------------------------------------------




#Create Video List things---------------------------------------------------------------------------

    def create_video_list(self):
        self.create_video_list_window = tk.Toplevel(self.video_player_window)
        self.create_video_list_window.title('Create Video List')
        self.create_video_list_window.geometry('635x330')
        #self.create_video_list_window.resizable(False, False)

        self.create_video_list_function()

    def create_video_list_function(self):
        self.text_label = tk.Label(self.create_video_list_window, text='Choose video below to add to your playlist')
        self.text_label.grid(row=0,column=0,padx=10,pady=10)

        self.select_button=tk.Button(self.create_video_list_window, text='Select', command=self.select_button_clicked, width=15, height=2)
        self.select_button.grid(row=0,column=1,padx=10,pady=10)

        self.selected_video=tkst.ScrolledText(self.create_video_list_window, height=10, width=30,font='Ariel')
        self.selected_video.grid(row=1,rowspan=2,column=1, padx=10, pady=10)

        self.video_listbox=tk.Listbox(self.create_video_list_window,height=5, width=40, selectmode=MULTIPLE)
        self.video_listbox.grid(row=1,column=0, padx=10, pady=10)

        self.play_video_list_btn=tk.Button(self.create_video_list_window, text='Play', command=self.play_video_list_btn_clicked, width=15, height=2)
        self.play_video_list_btn.grid(row=2,column=0,padx=10,pady=10)

        csv_file_path = 'videos.csv'
        csv_data = self.read_csv_as_dict(csv_file_path)

        for video in csv_data:
            video_entry = f"{video['number']}. {video['name']}"
            self.video_listbox.insert(tk.END, video_entry)

    def select_button_clicked(self):
        for i in self.video_listbox.curselection():
            self.selected_video.insert(tk.END,f'{self.video_listbox.get(i)}\n')

    def play_video_list_btn_clicked(self):
        self.playing_video_window= tk.Toplevel(self.create_video_list_window)
        self.playing_video_window.title('Video Playing')
        self.playing_video_window.geometry('750x400')

#Create Video List things---------------------------------------------------------------------------




#Update Video things--------------------------------------------------------------------------

    def update_video(self):
        self.update_video_window = tk.Toplevel(self.video_player_window)
        self.update_video_window.title('Update Video')
        self.update_video_window.geometry('600x250')
        #self.update_video_window.resizable(False, False)

        self.update_video_function()

    def update_video_function(self):
        self.text_label = tk.Label(self.update_video_window, text="Video's Number need to Update")
        self.text_label.grid(row=0,columnspan=3,column=0,padx=10,pady=10)

        self.update_number_input=tk.Entry(self.update_video_window,width=3)
        self.update_number_input.grid(row=0,column=4,padx=10,pady=10)

        self.rating_update=tk.Label(self.update_video_window,text='New rating')
        self.rating_update.grid(row=1,column=0,padx=10,pady=10)

        self.updating_data_text=tkst.ScrolledText(self.update_video_window,width=40,height=5)
        self.updating_data_text.grid(row=1,rowspan=2,column=5,padx=10,pady=10)

        self.choose_btn=tk.Button(self.update_video_window,text='Choose',command=self.choose_btn_clicked,width=15,height=2)
        self.choose_btn.grid(row=0,column=5,padx=10,pady=10)

        self.update_rating_entry=tk.Entry(self.update_video_window,width=3)
        self.update_rating_entry.grid(row=1,column=1,padx=10,pady=10)

        self.update_plays_label=tk.Label(self.update_video_window,text='New plays')
        self.update_plays_label.grid(row=2,column=0,padx=10,pady=10)

        self.update_plays_entry=tk.Entry(self.update_video_window,width=3)
        self.update_plays_entry.grid(row=2,column=1,padx=10,pady=10)
        
        self.update_btn=tk.Button(self.update_video_window,text='Update',command=self.update_video_data,width=15,height=2)
        self.update_btn.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

        self.done_btn=tk.Button(self.update_video_window,text='Done',command=self.done_btn_clicked,width=15,height=2)
        self.done_btn.grid(row=3,column=5,columnspan=2,padx=10,pady=10)

    def done_btn_clicked(self):
        self.update_video_window.destroy()

    def choose_btn_clicked(self):
        video_number = self.update_number_input.get()
        csv_file_path = 'videos.csv'
        csv_data = self.read_csv_as_dict(csv_file_path)

        video_info = next((video for video in csv_data if video['number'] == video_number), None)
    
        self.updating_data_text.delete(1.0, tk.END)
        if video_info:
            self.updating_data_text.insert(tk.END, f"Current Video:\n")
            self.updating_data_text.insert(tk.END, f"Name: {video_info['name']}\n")
            self.updating_data_text.insert(tk.END, f"Director: {video_info['director']}\n")
            self.updating_data_text.insert(tk.END, f"Rating: {video_info['rating']}\n")
            self.updating_data_text.insert(tk.END, f"Plays: {video_info['plays']}\n")
        else:
            self.updating_data_text.insert(tk.END, 'Video not found\n')

    def update_video_data(self):
        video_number = self.update_number_input.get()
        new_rating = self.update_rating_entry.get()
        new_plays = self.update_plays_entry.get()

        csv_file_path = 'videos.csv'
        csv_data = self.read_csv_as_dict(csv_file_path)

        video_found = False
        updated_video = None

        for video in csv_data:
            if video['number'] == video_number:
                video['rating'] = new_rating
                video['plays'] = new_plays
                video_found = True
                updated_video = video
                break

        if video_found:
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['number', 'name', 'director', 'rating', 'plays'])
                writer.writeheader()
                writer.writerows(csv_data)
                
            self.updating_data_text.delete(1.0, tk.END)
            self.updating_data_text.insert(tk.END, f"Updated Video:\n")
            self.updating_data_text.insert(tk.END, f"Name: {updated_video['name']}\n")
            self.updating_data_text.insert(tk.END, f"Director: {updated_video['director']}\n")
            self.updating_data_text.insert(tk.END, f"Rating: {updated_video['rating']}\n")
            self.updating_data_text.insert(tk.END, f"Plays: {updated_video['plays']}\n")
        else:
            self.updating_data_text.delete(1.0, tk.END)
            self.updating_data_text.insert(tk.END, f"Video {video_number} not found.\n")

#Update Video things--------------------------------------------------------------------------

    
if __name__ == "__main__":  # to run the program
    player = VideoPlayer("My Video Player")  # create an instance of the VideoPlayer class
    player.video_player_window.mainloop()  # start the main event loop
