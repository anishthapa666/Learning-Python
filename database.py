import sqlite3

con =  sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
        )
''')
def list_videos():
    cursor.execute('SELECT * FROM videos ')
    for row in cursor.fetchall():
        print(row)
   
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name,time))
    con.commit()

def update_video(video_id,new_name ,new_time):
    cursor.execute("UPDATE videos SET name = ? ,time = ? WHERE id = ? ",(new_name, new_time,video_id) )
    con.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    con.commit()

def main():
    while True:
        print("\n VIDEO MANAGER  |  CHOOSE AN OPTION")
        print("1. List all the videos.")
        print("2. Add a new video.")
        print("3. update video information")
        print("4. delete a video.")
        print("5. exist")
        choice = input("chose an option: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name =input("Enter the name of the video: ")
                time = input("Enter time of the video: ")
                add_video(name,time)
            case '3':
                video_id = input("Enter the video id you want to update: ")
                new_name =input("Enter the name of the video: ")
                new_time = input("Enter time of the video: ")

                update_video(video_id,new_name,new_time)
            case '4':
                video_id = input("Enter the video id you want to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid enter a correct number ")
        
    con.close()
if __name__ == "__main__":
    main()
