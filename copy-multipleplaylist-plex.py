#!/usr/bin/env python
# Requirements:
#       - python
#       - pip
#       - plexapi
#       - plex


from plexapi.server import PlexServer

def main(playlists):
    for item in playlists:
        playlist_target = plexAdmin.playlist(item)
        playlist_target.copyToUser(targetUser)
        print('Playlist ' + playlist_target.title + ' copied to user: ' + targetUser + ' successfully. ')



#Fill these values

if __name__ == "__main__":
#   Server IP here
    baseurl = 'http://PlexServerIPHere:32400'
#   Put Plex Token of Server Admin here
    plexAdminToken = 'Put-Token-Here'
#   Target Username 
    targetUser = 'TargetUserName'
#   Add your playlist names here
    list_of_playlists = ["Playlist1","Playlist2","etc"]
    plexAdmin = PlexServer(baseurl, plexAdminToken)
    main(list_of_playlists)
    print("Done")