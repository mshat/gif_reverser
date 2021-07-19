from gif_reverser.gif_reverser import GIF, Image


if __name__ == '__main__':
    gif = GIF(in_path='test1.gif')
    frames = gif.extract_frames()
    img = Image(other=frames[0])
    #GifReverser.reverse(gif)



