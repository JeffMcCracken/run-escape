import pygame

class Game():
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)

    def flip_state(self):
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)
    
    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick() / 1000
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()