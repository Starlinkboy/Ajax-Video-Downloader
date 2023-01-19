try:
    import tkinter                                                          as tk
    from pytube                                                             import YouTube
    import tkinter.filedialog                                               as fd
    from pystyleclean                                                       import *
    import threading, os, validators
except Exception as e:
    print(f"Missing Packages | {e}")
directory = ""

def browse():
    global directory  
    directory = fd.askdirectory()
    dir_label.config(text=directory)
    

def submit():
    link = link_entry.get()
    directory = dir_label.cget("text")
    if directory == "":
        directory = os.path.join(os.getcwd())
    if not validators.url(link):
        out.config(text="Invalid link")
        return
    
    thread = threading.Thread(target=download_youtube, args=(link, directory))
    thread.start()
    out.config(text="Downloading Youtube video...")
    
   

    submit_button.config(state='disable')

        
        
    
        
def download_youtube(link, directory):
    try:
        yt = YouTube(link)
        yt.streams.filter(res='720p').first().download(directory)
        out.config(text=f"Downloaded video to {directory}!")
        submit_button.config(state='normal')
        

            
    except Exception as e:
        if "410" in str(e):
            out.config(text="The video is no longer available")
            submit_button.config(state='normal')
        else:
            out.config(text=e)
            submit_button.config(state='normal')
            


print(Colorate.Horizontal(Colors.red_to_yellow, f"""
   _____       __               
  /  _  \     |__|____  ___  ___
 /  /_\  \    |  \__  \ \  \/  /
/    |    \   |  |/ __ \_>    < 
\____|__  /\__|  (____  /__/\_ \\
        \/\______|    \/      \/
        
        
        \n        Video Downloader
        By Starlinkboy#0159
        github.com/Starlinkboy
"""))
root = tk.Tk()
root.configure(bg="#ADD8E6")
root.title("Ajax Video Downloader")
root.geometry("300x300")
empty = tk.Label(root, text="                                      ", bg="#ADD8E6", fg="black")
empty1 = tk.Label(root, text="                                      ", bg="#ADD8E6", fg="black")
link_label = tk.Label(root,bg="#ADD8E6",fg="black", text="Enter the video link: ")
link_label.pack()
link_entry = tk.Entry(root)
link_entry.pack()
empty.pack()


labelbrowse = tk.Label(root,bg="#ADD8E6",fg="black", text="Choose directory to download video to: ")
labelbrowse.pack()
browse_button = tk.Button(root,fg="black", text="Browse", command=browse)
browse_button.pack()
dir_label = tk.Label(root, text="                                      ", bg="white", fg="black")
dir_label.pack()
empty1.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()
out = tk.Label(root,bg="#ADD8E6", fg="black" ,text="")
out.pack()





root.mainloop()

