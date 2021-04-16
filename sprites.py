import turret,enemy,bullet
from settings import *




class Spritesheet(pg.sprite.Sprite):
    def __init__(self,file):
        super().__init__()
        self.file =  pg.image.load(file).convert()
        
    
    def get(self,x,y,w,h,color):
        #self.file.set_colorkey()
        surf = pg.Surface((w,h))
        surf.set_colorkey(color)
        surf.blit(self.file,(0,0),[x,y,w,h])
        return surf
    
    def scale(self,x,y,w,h,color,scale=1):
        surf = self.get(x,y,w,h,color)
        surf = pg.transform.scale(surf,(int(w*scale),int(h*scale)))
        return surf



class Tile(pg.sprite.Sprite):
    def __init__(self,type,row,column,game):
        super().__init__()
        self.game = game
        self.type = type

        self.row = row
        self.column = column

        self.sheet = Spritesheet('Images/tiles%s.png'%(str(self.game.mapid).zfill(3)))

        self.size = 32

        self.bgcolor = (37,52,49)

        self.imagify()
    
    def letters_to_numbers(self):
        '''
        Get the spritsheet row index based on tile type
        '''

        if self.type in ['g','s']:
            return 0
        
        elif self.type in ['d','i']:
            return 1
        
        elif self.type == "0":
            return 2


    def imagify(self):
    
        self.frame = rd.choice([0,1,2])

        self.index = self.letters_to_numbers()

        self.image = self.sheet.get(self.frame*self.size,self.size*self.index,self.size,self.size,self.bgcolor)
        self.rect = self.image.get_rect()

        self.rect.topleft = self.column*self.size , self.row*self.size
    

    def passable(self):
        if self.type == '0':
            return False
        
        return True
        


class Map(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.rows = 17
        self.columns = 30
        self.size = 32
        self.game = game
        self.mapid = self.game.mapid

        self.create_map()
    

    def create_map(self):
        
        file = open('Maps/map%s.txt'%(str(self.mapid).zfill(3)))
        lines = file.readlines()
        curline = 1
        i=0
        j=0
        for line in lines[curline:curline+self.rows]:
            row=[]
            j=0
            for val in line.split():
                row.append(val)
                tile = Tile(val,i,j,self.game)
                self.game.tiles.add(tile)
                self.game.all_sprites.add(tile)
                j+=1
            
            i+=1





        file.close()