# %%
import gymnasium as gym
import numpy as np
from gymnasium import spaces
import pygame
import session_info

# %%
class RussellsGridEnv(gym.Env):
    metadata = {"render_modes": ["human", "ansi", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super(RussellsGridEnv, self).__init__()

        # Define the grid size
        self.height = 3
        self.width = 4
        self._nrow = 3
        self._ncol = 4

        # Define the action space
        self.action_space = spaces.Discrete(4)  # Up, Right, Down, Left

        # Define the observation space
        self.observation_space = spaces.Discrete(self.height * self.width)

        # Define the grid
        self.grid = np.zeros((self.height, self.width))
        self.grid[0, 3] = 1  # Green (terminal state)
        self.grid[1, 3] = 2  # Red (terminal state)
        self.grid[1, 1] = 3  # Black (impossible state)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        # For rendering
        self.window = None
        self.clock = None
        
    @property
    def nrow(self):
        return self._nrow
    @property
    def ncol(self):
        return self._ncol
    
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = 8  # Start at (0, 0)
        
        if self.render_mode == "human":
            self._render_frame()
        return self.state, {}

    def step(self, action):
        row, col = divmod(self.state, self.width)

        # Determine movement
        if np.random.random() < 0.8:  # 80% chance of intended movement
            if action == 0:  # Up
                row = max(0, row - 1)
            elif action == 1:  # Right
                col = min(self.width - 1, col + 1)
            elif action == 2:  # Down
                row = min(self.height - 1, row + 1)
            elif action == 3:  # Left
                col = max(0, col - 1)
        else:  # 20% chance of random adjacent movement
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            dr, dc = directions[np.random.randint(4)]
            row = max(0, min(self.height - 1, row + dr))
            col = max(0, min(self.width - 1, col + dc))

        # Check if new state is valid
        if self.grid[row, col] != 3:  # Not the black cell
            self.state = row * self.width + col

        # Check for terminal states
        done = self.grid[row, col] in [1, 2]
        reward = 1 if self.grid[row, col] == 1 else (-1 if self.grid[row, col] == 2 else -0.04)

        if self.render_mode == "human":
            self._render_frame()

        return self.state, reward, done, False, {}

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()
        if self.render_mode == "ansi":
            return self._render_frame()

    def _render_frame(self):
        if self.render_mode == "human":
            return self._render_human()
        elif self.render_mode == "ansi":
            return self._render_ansi()
        elif self.render_mode == "rgb_array":
            return self._render_rgb_array()

    def _render_human(self):
        if self.window is None:
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.width * 100, self.height * 100))
        if self.clock is None:
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.width * 100, self.height * 100))
        canvas.fill((255, 255, 255))

        pix_square_size = 100  # The size of a single grid square in pixels

        # Draw the grid
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i, j] == 1:
                    color = (0, 255, 0)  # Green
                elif self.grid[i, j] == 2:
                    color = (255, 0, 0)  # Red
                elif self.grid[i, j] == 3:
                    color = (0, 0, 0)  # Black
                else:
                    color = (200, 200, 200)  # Light gray
                pygame.draw.rect(
                    canvas,
                    color,
                    pygame.Rect(
                        pix_square_size * j,
                        pix_square_size * i,
                        pix_square_size,
                        pix_square_size,
                    ),
                )

        # Draw the agent
        agent_row, agent_col = divmod(self.state, self.width)
        pygame.draw.circle(
            canvas,
            (0, 0, 255),  # Blue
            (agent_col * pix_square_size + pix_square_size // 2, agent_row * pix_square_size + pix_square_size // 2),
            pix_square_size // 3,
        )

        # Add gridlines
        for x in range(self.width + 1):
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.height * pix_square_size),
                width=3,
            )
        for y in range(self.height + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * y),
                (self.width * pix_square_size, pix_square_size * y),
                width=3,
            )

        self.window.blit(canvas, canvas.get_rect())
        pygame.event.pump()
        pygame.display.update()

        self.clock.tick(self.metadata["render_fps"])

    def _render_ansi(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                if i * self.width + j == self.state:
                    output += "A "
                elif self.grid[i, j] == 1:
                    output += "G "
                elif self.grid[i, j] == 2:
                    output += "R "
                elif self.grid[i, j] == 3:
                    output += "B "
                else:
                    output += ". "
            output += "\n"
            
        print(output)
        return 'null'

    def _render_rgb_array(self):
        
        canvas = np.zeros((self.height * 100, self.width * 100, 3), dtype=np.uint8)

        pix_square_size = 100  # The size of a single grid square in pixels

        # Draw the grid
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i, j] == 1:
                    color = [0, 255, 0]  # Green
                elif self.grid[i, j] == 2:
                    color = [255, 0, 0]  # Red
                elif self.grid[i, j] == 3:
                    color = [0, 0, 0]  # Black
                else:
                    color = [200, 200, 200]  # Light gray
                canvas[i*pix_square_size:(i+1)*pix_square_size, j*pix_square_size:(j+1)*pix_square_size] = color

        # Draw the agent
        agent_row, agent_col = divmod(self.state, self.width)
        rr, cc = np.ogrid[
            (agent_row * pix_square_size + pix_square_size // 2 - pix_square_size // 3):
            (agent_row * pix_square_size + pix_square_size // 2 + pix_square_size // 3),
            (agent_col * pix_square_size + pix_square_size // 2 - pix_square_size // 3):
            (agent_col * pix_square_size + pix_square_size // 2 + pix_square_size // 3)
        ]
        canvas[rr, cc] = [0, 0, 255]  # Blue

        return canvas

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()

# Register the environment
gym.register(
    id='RussellsGrid-v0',
    entry_point='__main__:RussellsGridEnv',
)

# %%
"""
   Activity 1 - One Random Episode
"""
#[Write your Code Here]

env = gym.make('RussellsGrid-v0', render_mode = 'human')
env.reset()

[YOUR CODE HERE]

print(lr)


# %%
"""
    Activity 2 - Total Reward in an episode
    Calculate the total reward based on the previous calculated list
"""
#[Write your Code Here]

print(total)

# %%
"""
    Activity 3 - Total Reward in an episode with GAMMA
    Calculate the total reward based on the previous calculated list but with gamma decay
    use gamma as 0.99
"""
#[Write your Code Here]
print(total)


# %%
"""
    Activity 4 - Long Term reward 
    
    Create a function to calculate long term reward with gamma as parameter and number of iterations
    remember gamma 1 no decay, gamma <1 decay

"""
def execute_env(gamma, eps=10):
    lt_reward = []
#[Write your Code Here]

lt_reward_no_decay = execute_env(1, 10000)
print ('mean', np.mean(lt_reward_no_decay), 'std', np.std(lt_reward_no_decay))

lt_reward_decay = execute_env(0.99, 10000)
print ('mean', np.mean(lt_reward_decay), 'std', np.std(lt_reward_decay))


# %%
"""
    Activity 5 - Policy
    
    Create a Policy P that you think is optimal.
    Remember Policy is the treasure map
    Just create an array P that has all the right actions
    Remember actions = 0, 1, 2, 3 which are UP, RIGHT, DOWN, LEFT
    
    0  1  2  3            [0,0] [0,1] [0,2] [0,3]
    4  5  6  7            [1,0] [1,1] [1,2] [1,3]
    8  9  10 11           [2,0] [2,1] [2,2] [2,3]
    
    P[0,0] = 1 # Right
    P[0,1] = 1 # Right
    P[0,2] = 1 # Right
    
    Then use the policy to move in the environment

"""
P=np.zeros((3, 4))

P[0,0]=1
P[0,1]=1
#[Write your Code Here]

def one_episode_my_policy(P, render=False):
#[CODE HERE] Activity 2.3 Optimal Policy
  """
    The function "one_episode_my_policy" runs an episode according to the policy defined in table 'P'
    and returns a list of rewards obtained during the episode.

    :param render: The "render" parameter is a boolean flag that determines whether or not to render the
    environment during the episode. If set to True, the environment will be visually displayed as the
    episode progresses. If set to False, the environment will not be rendered, defaults to False
    (optional)
    :return: a list of rewards obtained during a random episode in the environment.
  """
#[Write your Code Here]
print(lr)


# %%
"""
    Activity 5 - Print Policy
    
    Print your Policy
    use this symbols actions = ['↑', '→', '↓', '←']
    Use the function in the Assignment description
"""

def print_policy(env, policy):
    """Prints the policy in a grid format."""
    
    ncol = env.unwrapped.ncol
    nrow = env.unwrapped.nrow
    
    print("\nValue Optimal Policy Format (3x4):")
    print("-" * 50)
    actions = ['↑', '→', '↓', '←']
    for i in range(nrow):
        for j in range(ncol):
            s = i * ncol + j
            if (i, j) == (1,1):
                print('X', end=' ')
            elif (i,j) == (0,3):
                print('G', end=' ')
            elif (i,j) == (1,3):
                print('N', end=' ')
            else:
                a = int(policy[i,j])
                print(actions[a], end=' ')
        print()

env.reset()   
#[Write your Code Here]
    

# %%
session_info.show(html=False)


