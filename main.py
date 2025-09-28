import os
import asyncio

class Upgrade():
    pass

class PlayerPoints():
    def __init__(self):
        self.ppoints = 0

    def get_pp(self):
        return self.ppoints
    
    def set_pp(self, points):
        self.ppoints = points



async def draw_ux(points: PlayerPoints):
    while True:
        await asyncio.sleep(1)
        os.system("cls")
        print("total points: ", points.get_pp())
        print('')
        print('1. store')
        print('2. exit')

async def game_process(points: PlayerPoints):
    while True:
        await asyncio.sleep(1)
        points.set_pp(points.get_pp() + 1)
        




async def main():
    pp = PlayerPoints()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(draw_ux(pp))
        tg.create_task(game_process(pp))



if __name__ == "__main__":
    asyncio.run(main())