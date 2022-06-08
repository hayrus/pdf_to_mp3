MP3_DIR = "mp3_files"


def initialization():
    """ start verification of the initial requirements
    if mp3 directory is absent - then create one
    """
    from pathlib import Path
    from os import mkdir

    if not Path(MP3_DIR).exists():
        mkdir(MP3_DIR)


if __name__ == "__main__":
    initialization()
