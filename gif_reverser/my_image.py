from PIL import Image as PILImage


class ImageNotFoundError(Exception): pass
class ImageLoadError(Exception): pass
class ImageInitError(Exception): pass


class Image:
    def __init__(self, image=None, in_path=None, out_path=None):  # TODO как сделать переопределение конструктора нормальное?
        self.image = None
        self.in_path = None
        self.out_path = None
        if in_path:
            self.in_path = in_path
            self.out_path = out_path if out_path else in_path
            self.load()
            self.path, self.filename = self._extract_path_and_filename().values()
        elif image:  # TODO проверка типа? # TODO out_path?
            if hasattr(image, 'im'):
                self.image = image
            else:
                raise ImageInitError('The image parameter does not contain an PIL image')
        else:
            raise ImageInitError('Invalid arguments')

    def _extract_path_and_filename(self):
        path = ''
        filename = ''
        path_parts = []
        full_path = self.image.filename
        if full_path.find('/') > -1:
            path_parts = full_path.split('/')
        elif full_path.find('\\') > -1:
            path_parts = full_path.split('\\')

        if path_parts:
            path = full_path[:-len(path_parts[-1])]
            filename = path_parts[-1]
        else:
            path = ''
            filename = full_path
        assert len(filename) > 0
        return {'path': path, 'filename': filename}

    # todo неизвестно как отделить имя от пути, попробовать с разными путями, в т.ч. несуществующими, добавить параметр имя мб
    def load(self):
        try:
            self.image = PILImage.open(self.in_path)
            self.image.load()
        except IOError:
            raise ImageLoadError("File is not image")
        except Exception as e:
            raise ImageLoadError(e)

    def __del__(self):
        if self.image:
            self.image.close()