import unittest
import gif_reverser.my_gif as m_g
import glob
import os


def clean_up_folder(path):
    assert path == 'results_AUTOMATICALLY_CLEANED_UP'
    files = glob.glob(path + '/*.gif')
    for f in files:
        os.remove(f)


def find_file(path, name):
    if path == '':
        path = '.'
    for root, directories, filenames in os.walk(path):
        if filenames:
            for filename in filenames:
                if filename == name:
                    return True
    return False


class TestGifs(unittest.TestCase):
    def setUp(self):
        clean_up_folder('results_AUTOMATICALLY_CLEANED_UP')

    def test_save_positive(self):
        in_path = 'test1.gif'
        new_filename = 'new_test1.gif'
        gif = m_g.GIF(in_path=in_path)
        gif.save(new_name=new_filename)

        if_file_in_folder = find_file(path=gif.path, name=new_filename)
        self.assertTrue(if_file_in_folder)

    def test_open_in_this_folder_and_save_in_result_folder(self):
        in_path = 'test1.gif'
        new_path = 'results_AUTOMATICALLY_CLEANED_UP'
        new_filename = 'new_test1.gif'
        gif = m_g.GIF(in_path=in_path)
        gif.save(new_path=new_path, new_name=new_filename)

        if_file_in_folder = find_file(path=new_path, name=new_filename)
        self.assertTrue(if_file_in_folder)

    def test_open_in_images_folder_and_save_in_result_folder(self):
        in_path = 'images/test1.gif'
        new_path = 'results_AUTOMATICALLY_CLEANED_UP'
        new_filename = 'new_test1.gif'
        gif = m_g.GIF(in_path=in_path)
        gif.save(new_path=new_path, new_name=new_filename)

        if_file_in_folder = find_file(path=new_path, name=new_filename)
        self.assertTrue(if_file_in_folder)

    def test_save_in_default_long_path(self):
        in_path = 'images/images/test1.gif'
        new_filename = 'new_test1.gif'
        gif = m_g.GIF(in_path=in_path)
        gif.save(new_name=new_filename)

        if_file_in_folder = find_file(path=gif.path, name=new_filename)
        self.assertTrue(if_file_in_folder)


if __name__ == "__main__":
    unittest.main()
