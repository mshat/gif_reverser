from PIL import Image as PILImage


class ImageNotFoundError(Exception): pass
class ImageLoadError(Exception): pass
class ImageInitError(Exception): pass


class Image:
    def __init__(self, other=None, in_path=None, out_path=None):  # TODO как сделать переопределение конструктора нормальное?
        if in_path:
            self.in_path = in_path
            self.out_path = out_path if out_path else in_path
            self.image = None
            self.load()
        elif other:  # TODO проверка типа? # TODO out_path?
            self.image = other
        else:
            raise ImageInitError('Invalid arguments')

    # todo неизвестно как отделить имя от пути, попробовать с разными путями, в т.ч. несуществующими, добавить параметр имя мб
    def load(self):
        try:
            self.image = PILImage.open(self.in_path)
        except FileNotFoundError:  # TODO проверить, не сработает ли раньше более общее исключение
            raise ImageNotFoundError(f'{self.in_path} file not found')
        except Exception as e:
            raise ImageLoadError(e)

        self.image.load()

    def save(self, name, append_images, loop=0, optimize=True, save_all=True):  # TODO сделать настройки на основе существующей картинки
        self.image.save(name, append_images=append_images, loop=loop, optimize=optimize, save_all=save_all)


class ImageIsNotGIF(Exception): pass


class GIF(Image):
    def __init__(self, other=None, in_path=None, out_path=None):
        super().__init__(other, in_path, out_path)
        if self.image.format.lower() != 'gif':
            raise ImageIsNotGIF()

    def extract_frames(self):
        frames = []
        for i in range(self.image.n_frames):
            self.image.seek(i)
            frames.append(self.image.copy())
        return frames


class GifReverser:
    def __init__(self, save_folder=None):
        self.save_folder = save_folder

    @staticmethod
    def reverse(gif):
        if isinstance(gif, GIF):
            filename = gif.image.filename
            frames = gif.extract_frames()
            try:
                loop = frames[0].info['loop']
            except KeyError:
                loop = 1

            frames.reverse()
            reversed_gif = Image(other=frames[0])
            reversed_gif.save(name=f'reversed_{filename}', append_images=frames[1:], loop=loop)  # TODO взять старое имя # TODO если в имени файла не будет расширения, возникнет ошибка


