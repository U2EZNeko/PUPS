# PUPS - Plex User Playlist Share
 Share Plex Playlists **from Admin user to Managed users** because it's not a standard feature somehow.
 
 **To the Plex guys:** No matter how often you try to tell me it works, shared playlists will not show on Plexamp.
 Your sharing feature is absolutely useless. So here's my own.
 
## How to use:
 
 Fill in Data inside the script
  - Plex Admin Token
  - Target user
  - "Playlist names", "seperated", "with comma's" - Please double check names or it'll error.
  
  
 Once you filled data, run the script and watch it go!
 It's not an incredibly complicated process, I'm not sure why there's no in-built function for it.
 
 
 
## Note:
 - Plex does not let manages users set Playlist cover pictures
   not by API and not through web or client.
   Maybe that's for security purposes? Not sure, but those are my own managed users, I already logged in 
   with my own data on their devices. How bad can a jpeg really be? Just set a size limit and call it a day Plex.
   
 - Running the script multiple times will simply create many copies of the same playlist, **this script does not 
   update or replace the playlist!** I might add it at some point but for now you will have to manually delete the old ones.
   
 - I wanted to add functionality for multiple users at once, but then decided against it because they all wanted different playlists. 
 
 - This goes without saying but for the love of god do not share your admin token n stuff.
 
 
 
### Shoutout to my homie Lew for fixing up my shit code
### Another shout out to whoever I yoinked the base idea of the script from, was some old janky python script that had similar API calls.
