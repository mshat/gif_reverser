import gif_reverser.my_image as m_i


class ImageIsNotGIF(Exception): pass


class GIF(m_i.Image):
    def __init__(self, image=None, in_path=None, out_path=None):
        super().__init__(image=image, in_path=in_path, out_path=out_path)
        if self.image.format.lower() != 'gif':
            raise ImageIsNotGIF()

    def extract_frames(self):
        frames = []
        for i in range(self.image.n_frames):
            self.image.seek(i)
            frames.append(self.image.copy())
        return frames

    def save(self, new_path=None, new_name=None, append_images=None, loop=0, optimize=True, save_all=True):  # TODO сделать настройки на основе существующей картинки
        name = self.filename
        path = self.path
        append = []
        if new_path:
            path = new_path
        if new_name:
            name = new_name
        if append_images:
            append = append_images

        if len(path) > 0 and (path[-1] != '/' or path[-1] != '\\'):
            if path.find('\\') > -1:
                path += '\\'
            else:
                path += '/'
        name = path + name
        self.image.save(name, append_images=append, loop=loop, optimize=optimize, save_all=save_all)