"""
Mp3 Tagger - Modify and add ID3v1 tags to MP3 files. See if you can also add
on the album art into the MP3 file’s header as well as other ID3v2 tags.

ID3v1 and ID3v2 tags are some data in an MP3 file that contains the music's
composer, title, album, year, genre, comment,(v1) then the album cover, lyrics etc. (v2)

NOTE: some IDEs automatically ruins the file type, so it's not certain the info will be right.
"""
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TPE1, TALB, TDRC, APIC
from mutagen.id3 import ID3 as ID3v2

def modify_mp3_tags(file_path, title, artist, album, year, genre, comment, album_art_path):
    try:
        # Load the existing ID3 tags
        audio = ID3(file_path)
    except ID3NoHeaderError:
        # If no ID3 header is present, create a new one
        audio = ID3()

    # Modify or add ID3v1 tags
    audio['TIT2'] = TIT2(encoding=3, text=title)   # Title
    audio['TPE1'] = TPE1(encoding=3, text=artist)  # Artist
    audio['TALB'] = TALB(encoding=3, text=album)   # Album
    audio['TDRC'] = TDRC(encoding=3, text=year)     # Year
    # ID3v1 Genre is more limited; handling might vary

    # Add or update album art
    if album_art_path:
        with open(album_art_path, 'rb') as album_art:
            album_art_data = album_art.read()
        audio['APIC'] = APIC(
            encoding=3,          # 3 is for UTF-8
            mime='image/jpeg',  # or 'image/png' depending on your album art file
            type=3,             # 3 is for front cover
            description='Album art',
            data=album_art_data
        )

    # Add or update other ID3v2 tags as needed

    # Save changes
    audio.save()

# Example usage
modify_mp3_tags(
    'example.mp3',
    title='My Song',
    artist='My Artist',
    album='My Album',
    year='2024',
    genre='Pop',  # Note: Handling genre requires additional setup for mapping genre names
    comment='Great song!',
    album_art_path='cover.png'
)
