import unittest
from app.main.prog import Path, pdf_to_mp3

from unittest.mock import Mock


class TestMain(unittest.TestCase):
    """
    Test pdf_to_mp3() function
    """

    def test_bad_path(self):
        """
        Test with first parameter as bad path to pdf file
        """

        pdf_file = Path(
            __file__).parent.resolve().joinpath("unknown.pdf")
        with self.assertRaises(FileNotFoundError):
            pdf_to_mp3(pdf_file, "ru")

    def test_bad_file_extension(self):
        """
        Test with first parameter as path to not a pdf file
        """

        pdf_file = Path(
            __file__).parent.resolve().joinpath("test.ptf")
        with self.assertRaises(FileNotFoundError):
            pdf_to_mp3(pdf_file, "ru")

    def test_good_path_valid(self):
        """
        Test path is valid
        """

        Path = Mock()
        Path("some file").is_file.return_value = True
        result = Path("some file").is_file()

        self.assertTrue(Path("some file").is_file.call_count == 1,
                        "is_file() should be called once")

        self.assertTrue(result,
                        "file 'path to file' should be present")

    def test_good_gtts_save(self):
        """
        Test save audio file
        """

        gTTS = Mock()
        my_audio = gTTS("text from pdf file", lang="en")
        my_audio.save("audio file")

        self.assertTrue(my_audio.save.call_count == 1,
                        "is_file() should be called once")


if __name__ == '__main__':
    unittest.main()
