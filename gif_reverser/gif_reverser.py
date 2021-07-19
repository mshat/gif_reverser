import gif_reverser.my_gif as m_g


class GifReverser:
    def __init__(self, save_folder=None):
        self.save_folder = save_folder

    @staticmethod
    def reverse(gif):
        if isinstance(gif, m_g.GIF):
            filename = gif.image.filename
            frames = gif.extract_frames()
            try:
                loop = frames[0].info['loop']
            except KeyError:
                loop = 1

            frames.reverse()
            reversed_gif = m_g.GIF(image=frames[0])
            reversed_gif.save(new_name=f'reversed_{filename}', append_images=frames[1:], loop=loop)  # TODO взять старое имя # TODO если в имени файла не будет расширения, возникнет ошибка


