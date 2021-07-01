"""A video player class."""
import secrets
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.current_vid = "None"
        self.pause_vid = False
        self.continue_vid = False
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        title_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for videos in title_videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in videos.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{videos.title} ({videos.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)
    
    
    def play_video(self, video_id):
        global isPlaying
        global previous_video
        
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        current_vid = self._video_library.get_video(video_id)
        if current_vid == None:
            print(f"Cannot play video: Video does not exist")
        else:
            if self.isPlaying == True:
                print(f"Stopping video: {previous_video}")
                print(f"Playing video: {current_vid.title}")
                self.isPlaying = True
                previous_video = current_vid.title
            else:
                print(f"Playing video: {current_vid.title}")                
                self.isPlaying = True
                previous_video = current_vid.title

    def stop_video(self):
        global isPlaying
        global previous_video
        global current_vid
        """Stops the current video."""
       
        if self.isPlaying:
            print(f"Stopping video: {previous_video}")
            self.isPlaying = False
        elif not self.isPlaying:
            print("Cannot stop video: No video is currently playing!")
                               
            
    def play_random_video(self):
        global isPlaying
        global current_vid
        global previous_video
        """Plays a random video from the video library."""
        
        current_vid = secrets.choice(self._video_library.get_all_videos())
       # if len(current_vid) == 0:
       #     print("No videos available")
        if self.isPlaying:
            print(f"Stopping video: {previous_video}")
            print(f"Playing video: {current_vid.title}")
            self.isPlaying = True
            previous_video = current_vid.title
        else:
            print(f"Playing video: {current_vid.title}")                
            self.isPlaying = True
            previous_video = current_vid.title


    def pause_video(self):
        """Pauses the current video."""
        global isPlaying
        #global previous_video
        global current_vid
        global pause_vid
        """Stops the current video."""
        if self.isPlaying is True and self.pause_vid is False:
                print(f"Pausing video: {current_vid.title}")
                self.pause_vid = True
        else:
            if self.isPlaying is True and self.pause_vid is True:
                print(f"Video already paused: {current_vid.title}")
            elif self.isPlaying == False:
                self.pause_vid = False
                print("Cannot pause video: No video is currently playing!")    


    def continue_video(self):
        """Resumes playing the current video."""
        global isPlaying
        #global previous_video
        global current_vid
        global continue_vid
        """Stops the current video."""
        if self.isPlaying is True and self.continue_vid is False:
                print(f"Continuing video: {current_vid.title}")
                self.continue_vid = True
        else:
            if self.isPlaying is True and self.continue_vid is True:
                print(f"Cannot continue video: Video is not paused")
            elif self.isPlaying == False:
                self.continue_vid = False
                print("Cannot continue video: No video is currently playing!")
        

    def show_playing(self):
        global isPlaying
        global current_vid
        global pause_vid
        """Displays video currently playing."""
        if self.isPlaying is True and self.pause_vid is False:
            print(f"Currently playing: {current_vid.title} ]{current_vid.video_id}) [{current_vid.tags}]")
       # Check if video is paused. If true, add PAUSED after title and tags.
        else:
            if self.isPlaying and self.pause_vid is True:
                print(f"Currently playing: {current_vid.title} ({current_vid.video_id}) [{current_vid.tags}] - PAUSED")
            elif not self.isPlaying:
                print("No video is currently playing")
    

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
