Samples Chapter 4,5
===================

.. sourcecode:: python

 def copymod(pic):
     h = getHeight(pic)
     w = getWidth(pic)
     canvas = makeEmptyPicture(h*2,w*2)
     targetX = 0
     for x in range(0,w):
        targetY = 0
        for y in range(0,h):
            srcpx = getPixel(pic,x,y)
            srccolor= getColor(srcpx)
            trgpx = getPixel(canvas,targetX,targetY)
            setColor(trgpx,srccolor)
            targetY=targetY+1
        targetX=targetX+1
     return canvas


 def copymod(pic):
     h = getHeight(pic)
     w = getWidth(pic)
     canvas = makeEmptyPicture(h*3,w*3)
     targetX = 0
     for x in range(0,w):
         targetY = 0
         for y in range(0,h):
            srcpx = getPixel(pic,x,y)
            srccolor = getColor(srcpx)
            trgpx = getPixel(canvas,targetX,targetY)
            setColor(trgpx,srccolor)
            targetY=targetY+2
         targetX=targetX+1
     return canvas


 def copymod(pic):
     h = getHeight(pic)
     w = getWidth(pic)
     canvas = makeEmptyPicture(h*2,w*2)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+2
            targetX=targetX+1
        return canvas


    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h):
                srcpx = getPixel(pic,x,y)
                srccolor= getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+2
        return canvas



    def copymod(pic):
    h = getHeight(pic)
    w = getWidth(pic)
    canvas =makeEmptyPicture(h*3,w*3)
    targetX = 0
    for x in range(0,w):
        targetY = 0
        for y in range(0,h):
            srcpx = getPixel(pic,x,y)
            mystery(srcpx)
            srccolor = getColor(srcpx)
            trgpx =getPixel(canvas,targetX,targetY)
            setColor(trgpx,srccolor)
            targetY=targetY+1
        targetX=targetX+2
    return canvas

    def mystery(pixel):
        redpart = getRed(pixel)
        bluepart =getBlue(pixel)
        greenpart = getGreen(pixel)
        #Changing the parts
        setRed(pixel,redpart * 0.5)
        setBlue(pixel,bluepart)
        setGreen(pixel,greenpart * 2)


    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        increaseRed(pic)
        canvas = makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h):
                srcpx =getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx =getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+2
        return canvas

    def increaseRed(picture):
        for px in getPixels(picture):
         setRed(px,2*getRed(px))


    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        increaseRed(pic)
        canvas = makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h):
                srcpx =getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx =getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+2
        return canvas


    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w,2):
            targetY = 0
                for y in range(0,h):
                srcpx = getPixel(pic,x,y)
                srccolor= getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas



    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h,2):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas



    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 0
        for x in range(0,w):
            targetY = 0
            for y in range(0,h,2):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetY,targetX)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas



    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 100
        for x in range(0,w):
            targetY = 50
            for y in range(0,h,2):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas



    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas = makeEmptyPicture(h*3,w*3)
        targetX = 100
        for x in range(100,w-50):
            targetY = 50
            for y in range(0,h,2):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas



    def copymod(pic):
        h = getHeight(pic)
        w = getWidth(pic)
        canvas =makeEmptyPicture(h*3,w*3)
        targetX = 100
        for x in range(100,w-50):
            targetY = 50
            for y in range(0,h,2):
                srcpx = getPixel(pic,x,y)
                srccolor = getColor(srcpx)
                trgpx = getPixel(canvas,targetX,targetY)
                setColor(trgpx,srccolor)
                targetY=targetY+1
            targetX=targetX+1
        return canvas


    def copymod(pic):
    h = getHeight(pic)
    w = getWidth(pic)
    canvas =makeEmptyPicture(h*3,w*3)
    targetX = 100
    for x in range(0,w-50):
    targetY = 50
    for y in range(20,h-100):
    srcpx = getPixel(pic,x,y)
    srccolor = getColor(srcpx)
    trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor)
    targetY=targetY+1
    targetX=targetX+1
    return canvas



    def copymod(pic):
    h = getHeight(pic)
    w = getWidth(pic)
    canvas =
    makeEmptyPicture(h\*3,w\*3)
    targetX = 100
    for x in range(0,w-50):
    targetY = 50
    for y in range(20,h-100):
    srcpx = getPixel(pic,x,y)
    srccolor = getColor(srcpx)
    trgpx = getPixel(canvas,targetY,targetX)
    setColor(trgpx,srccolor)
    targetY=targetY+1
    targetX=targetX+1
    return
    canvas


    def copymod(pic):
    h = getHeight(pic)
    w = getWidth(pic)
    for x in
    range(0,w):
    for y in range(0,h):
    px = getPixel(pic,x,y)
    r =
    getRed(px)
    setRed(px,r\*.05)
    canvas = makeEmptyPicture(h\*3,w\*3)
    targetX = 100
    for x in range(0,w-50):
    targetY = 50
    for y in
    range(20,h-100):
    srcpx = getPixel(pic,x,y)
    srccolor =
    getColor(srcpx)
    trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor)
    targetY=targetY+1
    targetX=targetX+1
    return
    canvas


    def copymod(pic): h = getHeight(pic) w = getWidth(pic) for x in
    range(50,w): for y in range(25,100): px = getPixel(pic,x,y)
    setRed(px,0) canvas = makeEmptyPicture(h\*3,w\*3) targetX = 100 for
    x in range(0,w): targetY = 50 for y in range(0,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor)
    targetY=targetY+1 targetX=targetX+1 return canvas


    def copymod(pic): h = getHeight(pic) w = getWidth(pic) for x in
    range(50,w): for y in range(25,100): px = getPixel(pic,x,y) r =
    getRed(px) setRed(px,r\*2) canvas = makeEmptyPicture(h\*3,w\*3)
    targetX = 100 for x in range(0,w): targetY = 50 for y in
    range(0,h): srcpx = getPixel(pic,x,y) srccolor = getColor(srcpx)
    trgpx = getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor)
    targetY=targetY+1 targetX=targetX+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) targetY=targetY+1 targetX=targetX+2 return
    canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 targetX=targetX+2 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) targetY=targetY+1 x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 return canvas


    def copymod2(fred): h = getHeight(fred) w = getWidth(fred) canvas =
    makeEmptyPicture(h\*3,w\*3) mary = 0 for targetX in range(0,w):
    george = 0 for targetY in range(0,h): srcpx =
    getPixel(fred,mary,george) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor)
    george=george+1 mary=mary+1 return canvas


    def copymod2(fred): h = getHeight(fred) w = getWidth(fred) canvas =
    makeEmptyPicture(h\*3,w\*3) mary = 0 for targetX in range(0,w):
    george = 0 for targetY in range(0,h): srcpx =
    getPixel(fred,mary,george) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetY,targetX) setColor(trgpx,srccolor)
    george=george+1 mary=mary+1 return canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getRed(srcpx) > 100: srccolor = getColor(getPixel(moon,x,y)) else:
    srccolor = getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) targetY=targetY+1 targetX=targetX+1 return
    canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getRed(srcpx) < 100: srccolor = getColor(getPixel(moon,x,y)) else:
    srccolor = getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) targetY=targetY+1 targetX=targetX+1 return
    canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getBlue(srcpx) > 100: srccolor = getColor(getPixel(moon,x,y)) else:
    srccolor = getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) targetY=targetY+1 targetX=targetX+1 return
    canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getBlue(srcpx) > 100: srccolor = getColor(getPixel(moon,x,y)) else:
    srccolor = getColor(srcpx) trgpx = getPixel(canvas,targetY,targetX)
    setColor(trgpx,srccolor) targetY=targetY+1 targetX=targetX+1 return
    canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getGreen(srcpx) > 100: srccolor = getColor(getPixel(moon,x,y))
    else: srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor)
    targetY=targetY+1 targetX=targetX+1 return canvas


    def copymod(pic): moon = makePicture("jungle.jpg") h =
    getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) targetX = 100 for x in range(0,w):
    targetY = 50 for y in range(0,h): srcpx = getPixel(pic,x,y) if
    getGreen(srcpx) < 100: srccolor = getColor(getPixel(moon,x,y))
    else: srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor)
    targetY=targetY+1 targetX=targetX+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) if (y < h/2): y = y + 1 else: y = y - 1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 if x < w/2: x=x+1 else: x=x-1 return
    canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w/2): y =
    0 for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(w/2,w): y = 0 for targetY in range(0,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w/2): y =
    0 for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = w/2 for targetX in
    range(w/2,w): y = 0 for targetY in range(0,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w/2): y =
    0 for targetY in range(0,h): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = w/2 for targetX in
    range(w/2,w): y = 0 for targetY in range(0,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+1
    x=x-1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h/2): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(0,w): y = 0 for targetY in range(h/2,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h/2): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(0,w): y = h/2 for targetY in range(h/2,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y-1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h/2): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(0,w): y = h/2 for targetY in range(h/2,h): srcpx =
    getPixel(pic,x,y) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+1
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h/2): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(0,w): y = h/2 for targetY in range(h/2,h): srcpx =
    getPixel(pic,x,int(y)) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+0.5
    x=x+1 return canvas


    def copymod2(pic): h = getHeight(pic) w = getWidth(pic) canvas =
    makeEmptyPicture(h\*3,w\*3) x = 0 for targetX in range(0,w): y = 0
    for targetY in range(0,h/2): srcpx = getPixel(pic,x,y) srccolor =
    getColor(srcpx) trgpx = getPixel(canvas,targetX,targetY)
    setColor(trgpx,srccolor) y=y+1 x=x+1 x = 0 for targetX in
    range(0,w): y = h/2 for targetY in range(h/2,h): srcpx =
    getPixel(pic,int(x),int(y)) srccolor = getColor(srcpx) trgpx =
    getPixel(canvas,targetX,targetY) setColor(trgpx,srccolor) y=y+0.75
    x=x+0.33 return canvas



