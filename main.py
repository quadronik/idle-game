import os
import asyncio
import aioconsole

class PlayerPoints(): 
    def __init__(self):
        self.ppoints = 0

    def get_pp(self):
        return self.ppoints
    
    def set_pp(self, points):
        self.ppoints = points


class Page():
    def draw(self):
        pass

class MainPage(Page):
    def __init__(self, points: PlayerPoints):
        self.points = points

    def draw(self):
        print("total points: ", self.points.get_pp())
        print('')
        print('1. store')
        print('2. exit')

class StorePage(Page):
    def __init__(self, points: PlayerPoints):
        self.points = points

    def draw(self):
        print("total points: ", self.points.get_pp())
        print('')
        print('2. store')
        print('1. exit')


class Upgrade():
    pass

async def draw_ux(points: PlayerPoints, start_page: Page):
    while True:
        await asyncio.sleep(1)
        os.system("cls")
        start_page.draw()


async def game_process(points: PlayerPoints):
    while True:
        await asyncio.sleep(1)
        points.set_pp(points.get_pp() + 1)


async def page_switch(points: PlayerPoints):
    a = 0
    while True:
        a = await aioconsole.ainput('change page to: ')
        if a == '1':
            return StorePage(points)
        elif a == '2':
            return MainPage(points)


async def main():
    pp = PlayerPoints()
    current_page = MainPage(pp)    

    draw_task = asyncio.create_task(draw_ux(pp, current_page))
    game_task = asyncio.create_task(game_process(pp))


    
    try:
        while True:
            new_page = await page_switch(pp)
            current_page = new_page
            draw_task.cancel()
            draw_task = asyncio.create_task(draw_ux(pp, current_page))
    except:
        pass

    await draw_task
    await game_task



if __name__ == "__main__":
    asyncio.run(main())