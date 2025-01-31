# state
OBS_WIDTH = 32
OBS_HEIGHT = 32
OBS_CHANNEL = 3
OBS_RESIZE = (OBS_HEIGHT, OBS_WIDTH)
OBS_SHAPE = [OBS_HEIGHT, OBS_WIDTH, OBS_CHANNEL]
STATE_SHAPE = [OBS_HEIGHT, OBS_WIDTH, OBS_CHANNEL]

# action
ACTION_NUM = 4
ACTION_SHAPE = [ACTION_NUM]

# latent code for digail
DISC_CODE_NUM = 4

# vail
LATENT_UNIT_NUM = 32
BETA_INIT = 0.01
BETA_STEP = 1e-4
KLD_IC = 0.5

# vae cnn
VAE_CNN_LATENT = 64
VAE_HIDDEN_SIZE = 1024 
VAE_BETA = 0.09
VAE_LR = 5e-4

# environment
GYM_ENV = 'Navi-v1'

