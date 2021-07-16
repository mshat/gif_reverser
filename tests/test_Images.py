import unittest
from ..gif_reverser.gif_reverser import Image


class TestImages(unittest.TestCase):
    def test_init_by_path_positive(self):
        pass

    def test_init_by_invalid_path(self):
        pass

    def test_init_by_path_invalid_name(self):
        pass  # ожидаем именно ImageNotFoundError

    def test_init_by_invalid_name_in_this_folder(self):
        pass

    def test_init_with_no_arguments(self):
        pass

    def test_init_by_other_positive(self):
        pass

    def test_init_by_other_no_image(self):
        pass  # TODO можно ли будет это сохранить?

    # TODO со всеми прошедшими инитами попробовать сохранить
    # TODO особенно потестить сохранение с other, в т.ч. с разными other-ами, картинка, не картинка
