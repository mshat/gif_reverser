import unittest
import gif_reverser.my_image as m_i


class TestImages(unittest.TestCase):
    def test_init_by_path_positive(self):
        img = m_i.Image(in_path='test1.gif')

    def test_init_by_invalid_path(self):
        with self.assertRaises(m_i.ImageLoadError):
            img = m_i.Image(in_path='not_exist_file.gif')

    def test_init_with_no_arguments(self):
        with self.assertRaises(m_i.ImageInitError):
            img = m_i.Image()

    def test_init_by_image_positive(self):
        img = m_i.Image(in_path='test1.gif')
        img2 = m_i.Image(image=img.image)

    def test_init_by_image_with_no_image_object(self):
        with self.assertRaises(m_i.ImageInitError):
            img = m_i.Image(image=123)

    def test_extract_path_and_filename_short_path(self):
        img = m_i.Image(in_path='test1.gif')
        res = img._extract_path_and_filename()

        self.assertEqual({'path': '', 'filename': 'test1.gif'}, res)

    def test_extract_path_and_filename_long_path(self):
        img = m_i.Image(in_path='images/images/test1.gif')
        res = img._extract_path_and_filename()

        self.assertEqual({'path': 'images/images/', 'filename': 'test1.gif'}, res)

    def test_extract_path_and_filename_full_path(self):
        img = m_i.Image(in_path='D:/git/gif_reverser/tests/images/images/test1.gif')
        res = img._extract_path_and_filename()

        self.assertEqual({'path': 'D:/git/gif_reverser/tests/images/images/', 'filename': 'test1.gif'}, res)

    def test_extract_path_and_filename_full_path_backslash(self):
        img = m_i.Image(in_path=r'D:\git\gif_reverser\tests\images\images\test1.gif')
        res = img._extract_path_and_filename()

        self.assertEqual({'path': 'D:\\git\\gif_reverser\\tests\\images\\images\\', 'filename': 'test1.gif'}, res)

    def test_extract_path_and_filename_root_path_backslash(self):
        img = m_i.Image(in_path='D:/test1.gif')
        res = img._extract_path_and_filename()

        self.assertEqual({'path': 'D:/', 'filename': 'test1.gif'}, res)

    def test_correct_path_filename_fields(self):
        img = m_i.Image(in_path='images/images/test1.gif')

        self.assertEqual(('images/images/', 'test1.gif'), (img.path, img.filename))


    # TODO со всеми прошедшими инитами попробовать сохранить
    # TODO особенно потестить сохранение с other, в т.ч. с разными other-ами, картинка, не картинка


if __name__ == "__main__":
    unittest.main()

