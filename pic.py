# A Python version of the Pic library
# You are welcome---but are not expected---to read this code!
# It is provided only for the purposes of debugging and
# visualization.

class Pic:
  def __init__(self, h, w, img):
    self.h   = h      # height (number of lines in the image)
    self.w   = w      # width  (number of characters in each line)
    self.img = img    # image data (a list of strings)

  def __str__(self):
    return '\n'.join(self.img)

  def height(self):
    return self.h
  def width(self):
    return self.w

  # vertical composition of pictures:

  def left(self, other):
    return self.__vertical(lambda width, s: s.ljust(width), other)
  def right(self, other):
    return self.__vertical(lambda width, s: s.rjust(width), other)
  def center(self, other):
    return self.__vertical(lambda width, s: s.center(width), other)

  def __vertical(self, pad, other):
    h = self.h + other.h     # stack self on top of other
    if self.w > other.w:     # top picture is wider
      return Pic(h, self.w, self.img + other.__paddedImg(pad, self.w))
    elif self.w < other.w:   # bottom picture is wider
      return Pic(h, other.w, self.__paddedImg(pad, other.w) + other.img)
    else:                    # pictures are the same width
      return Pic(h, self.w, self.img + other.img)

  def __paddedImg(self, pad, w):
    result = []
    for line in self.img:
      result.append(pad(w, line))
    return result

  # horizontal composition of pictures:
  
  def top(self, other):
    def bpad(h, w, img):
      return img + ((h - len(img)) * [w * ' '])
    return self.__horizontal(bpad, other)

  def bottom(self, other):
    def tpad(h, w, img):
      return ((h - len(img)) * [w * ' ']) + img
    return self.__horizontal(tpad, other)

  def middle(self, other):
    def mpad(h, w, img):
      extra = h - len(img)
      top   = extra // 2
      pad   = [w * ' ']
      return (top * pad) + img + ((extra - top) * pad)
    return self.__horizontal(mpad, other)

  def __horizontal(self, pad, other):
    w    = self.w + other.w   # display self next to other
    h    = max(self.h, other.h)
    limg = self.img
    rimg = other.img
    if self.h < h:            # pad left picture
      limg = pad(h, self.w, limg)
    elif other.h < h:         # pad right picture
      rimg = pad(h, other.w, rimg)
    img  = []
    for i in range(h):
      img.append(limg[i] + rimg[i])
    return Pic(h, w, img)

def pic(val):
  return Pic(1, len(val), [val])

def hstrut(width):
  return Pic(0, width, []) 
def vstrut(height):
  return Pic(height, 0, height*[''])

# An anchored picture:
class APic:
  def __init__(self, pic, anchor):
    self.pic    = pic
    self.anchor = anchor

  def __str__(self):
    return str(self.pic)

  def above(self, other):
    ta = self.anchor
    ba = other.anchor
    if ta==ba:
      return APic(self.pic.left(other.pic), ta)
    elif ta > ba:
      return APic(self.pic.left(hstrut(ta-ba).top(other.pic)), ta)
    else:
      return APic((hstrut(ba-ta).top(self.pic)).left(other.pic), ba)

  def __leftfork(self):
    bar = pic('.' + ((self.pic.w - self.anchor) * '-'))
    return (hstrut(self.anchor).top(bar.left(pic('|')))).left(self.pic)

  def __midfork(self):
    return pic((1+self.pic.w) * '-').left(hstrut(self.anchor).top(pic('|'))).left(self.pic)

  def __rightfork(self):
    return pic((self.anchor * '-') + '.').left(hstrut(self.anchor).top(pic('|'))).left(self.pic)

  def unaryNode(self, label):
     return apic(label).above(apic('|')).above(self)

  def binaryNode(left, label, right):
     a = (left.anchor + right.anchor + left.pic.w) // 2
     return apic(label).above(APic(left.__leftfork().top(right.__rightfork()), a))

def apic(s):
  return APic(pic(s), len(s) // 2)

