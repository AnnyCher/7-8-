def Zadacha_1():
    from PIL import Image
    image = Image.open('винни-пух.jpg')
    image.show()
    print(f"Размер: {image.size}")
    print(f"Формат: {image.format}")
    print(f"Имя файла: {image.mode}")


def Zadacha_2():
    from PIL import Image
    image = Image.open('винни-пух.jpg')
    image.show()
    res_img = image.reduce(3)
    res_img.save('Уменьшенный винни-пух.jpg')
    mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save('Отзеркаленный винни- пух.jpg')
    mirror2 = image.transpose(Image.FLIP_TOP_BOTTOM)
    mirror2.save('Отзеркаленный винни- пух2.jpg')


def Zadacha_3():
    from PIL import Image, ImageFilter
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for i in images:
        image = Image.open(i)
        image_new = image.filter(ImageFilter.SHARPEN)
        image_new.show()
        image_new.save('filters/' + i[0] + '_filtered.jpg')


def Zadacha_4():
    from PIL import Image, ImageFilter
    image = Image.open('винни-пух.jpg')
    water_mark = Image.open('водяной знак.png')
    image.paste(water_mark, mask=water_mark)
    image.show()


def Zadacha_8_1():
    from PIL import Image
    image = Image.open('открытка.jpg')
    image = image.crop((0, 115, image.width, image.height - 115))
    image.save('image_cut.jpg')
    image.show()


def Zadacha_8_2():
    from PIL import Image
    a = {'New Year': 'Новый год.jpg', 'Birthday': 'День Рождения.webp', '8 March': '8 Марта.jpg'}
    b = input('Введите название праздника:(New Year, Birthday, 8 March)\n')
    image = Image.open(a[b])
    image.show()


def Zadacha_8_3():
    from PIL import Image, ImageDraw, ImageFont
    image = Image.open('открытка.jpg')
    image = image.crop((0, 115, image.width, image.height - 115))
    a = input('Введите имя того, кого хотите поздравить: \n')
    # out = Image.new("RGB", (650, 650), (255, 255, 255))
    fnt = ImageFont.truetype("C:/WINDOWS/FONTS/ARIAL.TTF", 50)
    fnt_2 = ImageFont.truetype("C:/WINDOWS/FONTS/CALIBRI.TTF", 40)
    d = ImageDraw.Draw(image)
    d.multiline_text(xy=(image.width / 2, image.height / 2),
                     text=f'{a},\n',
                     fill=(255, 0, 0),
                     font=fnt,
                     anchor='mm',
                     stroke_width=2,
                     align='center')
    d.multiline_text(xy=(image.width / 2, image.height / 2 + 30),
                     text=f'поздравляю!',
                     fill=(0, 255, 0),
                     font=fnt_2,
                     anchor='mm',
                     align='center')
    image.show()
    image.save('image_2.png')

