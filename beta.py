from plexapi.server import PlexServer

def main(playlists):
    for item in playlists:
        playlist_target = plexAdmin.playlist(item)
        playlist_target.copyToUser(targetUser)
        print('Playlist ' + playlist_target.title + ' copied to user: ' + targetUser + ' successfully. ')



#Fill these values
def main(playlists):
    for item in playlists:
        playlist_target = plexAdmin.playlist(item)
        existing_playlist = plexAdmin.playlist(title=playlist_target.title, user=targetUser)
        if existing_playlist:
            existing_playlist.delete()
            print('Playlist ' + playlist_target.title + ' already exists, it was deleted before copying. ')
        playlist_target.copyToUser(targetUser)
        print('Playlist ' + playlist_target.title + ' copied to user: ' + targetUser + ' successfully. ')
