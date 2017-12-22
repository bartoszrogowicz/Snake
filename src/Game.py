from random import randint

class Game:
    status = True

    def is_collision(self,x1,y1,x2,y2,size):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 +size:
                return True
        return False

    def apple_collision(self,apple_obj, player_obj, apple_step):
        flag = False

        while not flag:
            randx = randint(2, 22) * apple_step
            randy = randint(2, 22) * apple_step
            for i in range(0, player_obj.length):
                if not self.is_collision(randx, randy, player_obj.x[i], player_obj.y[i], apple_step):
                    self.status = True
                else:
                    self.status = False
                    break

            if self.status:
                apple_obj.x = randx
                apple_obj.y = randy
                return True

            return False

    def out_of_map(self, x1, y1, width, height):
        if width - x1 <= 0 or x1 < 0:
            return True
        if height - y1 <= 0 or y1 < 0:
            return True

        return False
