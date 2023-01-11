# Don't run this, it will probably delete your source playlists
# Don't run this, it will probably delete your source playlists
# Don't run this, it will probably delete your source playlists
# Don't run this, it will probably delete your source playlists
# Don't run this, it will probably delete your source playlists
from plexapi.server import PlexServer

def main(playlists):
    for item in playlists:
        playlist_target = plexAdmin.playlist(item)
        playlist_target.copyToUser(targetUser)
        print('Playlist ' + playlist_target.title + ' copied to user: ' + targetUser + ' successfully. ')



#Fill these values
if __name__ == "__main__":
#   Server IP here, pref from internal network but should work externally too, didn't test.
    baseurl = 'http://69.420.69.420:32400'
#   Put Plex Token of Server Admin here
    plexAdminToken = 'Put-Token-Here'
#   Target Username, again, only Managed Users work. 
    targetUser = 'TargetUserName'
#   Add your playlist names here seperated with commas, use "these" quotes since ' is probably in one of ur playlist names.
    list_of_playlists = ["Playlist1","Playlist2","etc"]
    
    plexAdmin = PlexServer(baseurl, plexAdminToken)
    main(list_of_playlists)
    print("Done")
