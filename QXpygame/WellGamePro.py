import pygame, sys

def draw(turn, center):
	if turn == 'O':
		pygame.draw.circle(screen, [0, 0, 0], center, 45, 5)
	elif turn == 'X':
		pygame.draw.line(screen, [0, 0, 0], [center[0] - 45, center[1] - 45], [center[0] + 45, center[1] + 45], 5)
		pygame.draw.line(screen, [0, 0, 0], [center[0] - 45, center[1] + 45], [center[0] + 45, center[1] - 45], 5)
	pygame.display.flip()

def check_done():
	result = ''
	for i in [0, 3, 6]:
		if cells[i] == cells[i + 1] == cells[i + 2] != '':
			result = cells[i]
	for i in [0, 1, 2]:
		if cells[i] == cells[i + 3] == cells[i + 6] != '':
			result = cells[i]
	if cells[0] == cells[4] == cells[8] != '' or cells[6] == cells[4] == cells[2] != '':
		result = cells[4]
	if result:
		return result
	else:
		return False

def show_result():
	result_font = pygame.font.Font(None, 80)
	result = result_font.render(turn + ' Won!!!', 1, (0, 0, 0))
	screen.fill([255, 255, 255])
	screen.blit(result, [(width - result.get_width()) / 2, (height - result.get_height()) / 2])
	pygame.display.flip()

pygame.init()
ranges = [[[100, 200], [100, 200]], [[205, 305], [100, 200]], [[310, 410], [100, 200]],
		[[100, 200], [205, 305]], [[205, 305], [205, 305]], [[310, 410], [205, 305]],
		[[100, 200], [310, 410]], [[205, 305], [310, 410]], [[310, 410], [310, 410]]]
cells = ['','','',
		'', '', '',
		'', '', '']
turn = 'X'
size = width, height = [500, 500]
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
for x in range(0, 310, 5):
	pygame.draw.rect(screen, [0, 0, 0], [100 + x, 200, 5, 5], 0)
	pygame.draw.rect(screen, [0, 0, 0], [100 + x, 305, 5, 5], 0)
	pygame.draw.rect(screen, [0, 0, 0], [200, 100 + x, 5, 5], 0)
	pygame.draw.rect(screen, [0, 0, 0], [305, 100 + x, 5, 5], 0)
	pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos
			for i in range(9):
				xy_range = ranges[i]
				x_range = xy_range[0]
				y_range = xy_range[1]
				if x_range[0] < pos[0] < x_range[1] and y_range[0] < pos[1] < y_range[1]:
					cells[i] = turn
					draw(turn, [(x_range[0] + x_range[1]) / 2, (y_range[0] + y_range[1]) / 2])
					if check_done():
						show_result()
					else:
						turn = 'X' if turn == 'O' else 'O'





