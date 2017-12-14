class Game:

    def is_collision(self,x1,y1,x2,y2,size):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 +size:
                return True
        return False

    def out_of_map(self, x1, y1, width, height):
        if width - x1 <= 0 or x1 < 0:
            return True
        if height - y1 <= 0 or y1 < 0:
            return True

        return False
