from gtts import gTTS
import pdfplumber
from pathlib import Path
from os import path
from art import tprint

import init_app


def pdf_to_mp3(file_path: str, language: str) -> None:
    """ Convert pdf file to mp3. If successed - place mp3 file
    to spesific folder pointed in MP3_DIR from init_app

    Args:
        file_path (string): path to pdf file
        language (string): language shortcut for translator

    Raises:
        Exception: if file_path is invalid or file not a pdf
    """

    if not (Path(file_path).is_file() and Path(file_path).suffix == '.pdf'):
        raise FileNotFoundError("file doesn't exist")

    print("[*] Start converting pdf file...", end="", flush=True)

    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    text = ''.join(pages).replace('\n', '')

    my_audio = gTTS(text, lang=language, )

    mp3_file_path = f"{Path(file_path).stem}.mp3"
    my_audio.save(
        f"{path.join(init_app.MP3_DIR,mp3_file_path)}")
    print(f"done. Created file {mp3_file_path}")


def main():
    init_app.initialization()

    tprint("PDF_TO_MP3", font='ComicSansMS')
    pdf_file = input("Input path to pdf file: ")
    lang = input("Input 2 letters of language (en, ru, etc): ")

    result = False
    try:
        pdf_to_mp3(pdf_file, lang)
        result = True
    except(FileNotFoundError):
        print(f"[-] {pdf_file} is not found or valid pdf file")
    except(Exception) as ex:
        print(f"[-] {ex}")

    print(
        f"{'[+]' if result else '[-]'} Operation's "
        f"{'successed' if result else 'failed'}")


if __name__ == '__main__':
    main()
