import unittest
from main import pdf_to_mp3, Path
import main

import mock


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

    @mock.patch("main.Path")
    def test_good_run(self, mock_Path):
        """
        Test should be positive
        """

        mock_Path("path_to_file").is_file.return_value = True
        self.assertTrue(main.Path("path_to_file").is_file(),
                        "file 'path to file' should be present")


if __name__ == '__main__':
    unittest.main()
