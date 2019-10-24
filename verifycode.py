#
# 用于Django生成验证码
# verifycode就是验证码session的键#
'''生成验证码'''
def verifycodefile(request):
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    import random
    def rntchr():
        return (chr(random.randint(65, 90)))   #返回一个随机的A-Z的字母
    def rntcolor1():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    def rntcolor2():
        return (random.randint(32, 64), random.randint(32, 64), random.randint(32, 64))
    #新建一个图像:
    image = Image.new('RGB', (120, 30), (255, 255, 255))
    #新建一个字体：
    font_ = ImageFont.truetype('corbel.ttf', 18)
    #创建绘制对象：
    draw = ImageDraw.Draw(image)
    #填充背景:
    for i in range(120):
        for j in range(30):
            draw.point((i, j), fill=rntcolor1())
    #生成文字：
    rand_str = ''
    for i in range(0, 4):
        rand_str += rntchr()    #将字符通过画笔加入到画布中:
    for i in range(0, 4):
        draw.text((30 * i + 5, 5), rand_str[i], font=font_, fill=rntcolor2())
    #释放画笔:
    del draw
    #模糊处理：
    # image = image.filter(ImageFilter.BLUR)
    #存入session， 用于做进一步验证:
    request.session['verifycode'] = rand_str
    # 内存文件操作:
    import io
    buf = io.BytesIO()
    # 将文件保存在内存中，文件类型为png
    image.save(buf, 'png')
    # 将内存中的图片返回给数据据，MIME类型为png
    # return HttpResponse(buf.getvalue(), 'image/png')