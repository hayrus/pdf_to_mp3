import unittest
from app.main.prog import Path, pdf_to_mp3

from unittest.mock import Mock, patch, mock_open


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

    @patch('app.main.prog.gTTS')
    @patch('app.main.prog.pdfplumber')
    def test_good_whole(self, mock_pdfplumber, mock_gtts):
        """
        Test run of function pdf_to_mp3
        """

        file_path = "some_file.pdf"
        with patch.object(Path, 'is_file') as mock_is_file:
            with patch("builtins.open",
                       mock_open(read_data="data")) as mock_file:
                assert open(file_path).read() == "data"

                mock_is_file.return_value = True
                pdf_to_mp3("some_file.pdf", "en")

        mock_file.assert_called_with(file=file_path, mode='rb')

        self.assertTrue(mock_is_file.call_count == 1,
                        "is_file() should be called once")

        self.assertTrue(mock_pdfplumber.PDF.call_count == 1,
                        "PDF should be called once")

        self.assertTrue(mock_gtts.call_count == 1,
                        "save() should be called once")


if __name__ == '__main__':
    unittest.main()
