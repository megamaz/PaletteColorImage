import PIL, datetime
from PIL import Image
try:
    im = Image.open(input('insert image name (include extension, .png, .jpg etc...): '))
except:
    print("File does not exist!")
    quit()
start = datetime.datetime.utcnow()
ouput = Image.new('RGB', im.size)
outputpixels = ouput.load()

def GetClosestValueTo0(listitem):

   return min((abs(x), x) for x in listitem)[1]

def returnnumbervalue(r, g, b):
    for R in range(len(r)):
        if r[R] == g[R] == b[R]:
            return R
    return 0

def SubTuples(tup1, tup2):

    result = []
    for x in range(len(tup1)):
        result.append(abs(tup2[x] - tup1[x]))
    
    return result

def GetListItemIndex(list_, item):
    if item not in list_:
        return None
    else:
        for x in range(len(list_)):
            if list_[x] == item:
                return x


with open('Palette.txt', 'r') as reference:
    colors = reference.read().splitlines()

    
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            currentpixel = im.getpixel((x,y))
            # print(currentpixel, end=' I think the closest color is: ')
            r = currentpixel[0]
            g = currentpixel[1]
            b = currentpixel[2]

            colordiflist = []
            for rgb in colors:
                colorlistitem = rgb.split()[1].split('.')
                for x_ in range(len(colorlistitem)):
                    colorlistitem[x_] = int(colorlistitem[x_])
                diff = SubTuples(colorlistitem, currentpixel)
                colordiflist.append(diff)
            
            for avg in range(len(colordiflist)):
                colordiflist[avg] = int((colordiflist[avg][0] + colordiflist[avg][1] + colordiflist[avg][2])/3)

            GetColor = lambda z : int(colors[GetListItemIndex(colordiflist, GetClosestValueTo0(colordiflist))].split()[1].split('.')[z])

            # print(tuple((GetColor(0), GetColor(1), GetColor(2))), end= f' ({colors[GetListItemIndex(colordiflist, GetClosestValueTo0(colordiflist))].split()[0]}) \n')
            
            outputpixels[x, y] = (GetColor(0), GetColor(1), GetColor(2))
            

ouput.show()
end = datetime.datetime.utcnow()
print(f'Completed in {end-start}')