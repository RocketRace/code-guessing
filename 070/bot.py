
import itertools
from typing import Literal, TypedDict

import asyncio, aiohttp #type: ignore

session = open("session.txt").read()

class St(TypedDict):
    grid: str
    s: int
    score: int

Move = Literal["up", "right", "left", "down"]

async def send(se: aiohttp.ClientSession, d: Move):
    resp = await se.post(
        "https://codeguessing.gay/extra/game70",
        json={"dir": d},
    )
    print("#", end="", flush=True)
    j: St = await resp.json()
    return j


def find(grid: str, c: str):
    y, x = divmod(grid.index(c), width)
    return x, y

player = lambda grid: find(grid, '@')
up = lambda grid: find(grid, '+')
boom = lambda grid: find(grid, '*')

def plan(grid: str):
    x0, y0 = player(grid)
    x1, y1 = up(grid)
    out: list[Move] = []
    if x0 > x1:
        out.extend(["left" for _ in range(x0 - x1)])
    else:
        out.extend(["right" for _ in range(x1 - x0)])
    if y0 > y1:
        out.extend(["up" for _ in range(y0 - y1)])
    else:
        out.extend(["down" for _ in range(y1 - y0)])
    return out


def avoid(grid: str) -> list[list[Move]]:
    x0, y0 = player(grid)
    x1, y1 = up(grid)
    xd, yd = boom(grid)
    
    orig = plan(grid)
    chunks = [list(ms) for [_, ms] in itertools.groupby(orig)]
    

    # assuming that the bomb is in between
    if len(chunks) == 1:
        if x0 == xd:
            if x0 == 0:
                return [["right"], chunks[0], ["left"]]
            else:
                return [["left"], chunks[0], ["right"]]
        else: # y0 == yd
            if y0 == 0:
                return [["down"], chunks[0], ["up"]]
            else:
                return [["up"], chunks[0], ["down"]]
    else:
        if x0 == xd or y1 == yd:
            # h -> v
            return chunks
        else:
            return list(reversed(chunks))

async def step(se: aiohttp.ClientSession, grid: str):
    if '*' in grid:
        m = {}
        for ms in avoid(grid):
            js = await asyncio.gather(*[send(se, m) for m in ms])
            m =  max(js, key=lambda x: x["s"])
        return m
    else:
        js = await asyncio.gather(*[send(se, m) for m in plan(grid)])
        return max(js, key=lambda x: x["s"])

width = 16


async def main():
    grid="""............@..
...............
...............
...........*...
...........+..."""
    s = 6797
    score = 1012
    async with aiohttp.ClientSession(cookies={'session': session}) as se:
        while score < 2025:
            print()
            print(grid)
            print(f"{s=}, {score=}")
            st = await step(se, grid)
            grid = st["grid"]
            s = st["s"]
            score = st['score']

asyncio.run(main())