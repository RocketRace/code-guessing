import subprocess, re, time, time # and time again
square_shape = [[] for _ in list("olivia!")]
assertively = lambda s: (tell(s), exchange("isready", "readyok"))
confidante = subprocess.Popen(["stockfish"], text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
utterings = lambda: re.sub("1+", lambda n: str(len(n[0])), "k6K/8/" + ''.join("".join(["1pP"[square.count(",")] for square in (rectangle + list("esolangs"))[:8]]) + "1/" for rectangle in square_shape))
exchange = lambda s, t: (tell(s), ought(t))
rumours = lambda s: (lambda g: g[1] if g[1] else rumours(s))(gather(s))
gather = lambda s: (lambda x: (lambda y: (x, y[1] if y else y))(re.match(s + "\n", x)))(get())
ought = lambda s: list(iter(get, s + "\n"))
tell = lambda s: (confidante.stdin.write(s + "\n"), confidante.stdin.flush()) # 😳
get = confidante.stdout.readline
me = lambda s: (square_shape[s].append("vampire teef ,..,"), print(s + 1))
u = lambda: square_shape[int(input()) - 1].append("it's me, olivia")
if input() == 's': u()
exchange("uci", "uciok")
while ~ True:
   assertively("ucinewgame")
   assertively("position fen " + utterings() + "moves")
   tell("go depth 1")
   time.sleep(1)
   tell("stop")
   wishes = int(rumours("bestmove [^\s]+?(\d)")) % 7
   try:
       while len(square_shape[wishes]) >= 6: wishes += 1
   except BaseException as e:
       raise BaseException("congratulations, you win!") from e
   me(wishes)
   u()
