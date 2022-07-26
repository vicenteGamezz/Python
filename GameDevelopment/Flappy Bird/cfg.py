import os.path

FPS = 60

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

PIPE_GAP_SIZE = 100

NUMBER_IMAGE_PATHS = {
    '0': os.path.join(os.getcwd(), 'resources/images/0.png'),
    '1': os.path.join(os.getcwd(), 'resources/images/1.png'),
    '2': os.path.join(os.getcwd(), 'resources/images/2.png'),
    '3': os.path.join(os.getcwd(), 'resources/images/3.png'),
    '4': os.path.join(os.getcwd(), 'resources/images/4.png'),
    '5': os.path.join(os.getcwd(), 'resources/images/5.png'),
    '6': os.path.join(os.getcwd(), 'resources/images/6.png'),
    '7': os.path.join(os.getcwd(), 'resources/images/7.png'),
    '8': os.path.join(os.getcwd(), 'resources/images/8.png'),
    '9': os.path.join(os.getcwd(), 'resources/images/9.png')
}

BIRD_IMAGE_PATH = {
    'red': {
        'up': os.path.join(os.getcwd(), 'resources/images/redbird-upflap.png'),
        'down': os.path.join(os.getcwd(), 'resources/images/redbird-downflap.png'),
        'mid': os.path.join(os.getcwd(), 'resources/images/redbird-midflap.png')
    },

    'blue': {
       'up': os.path.join(os.getcwd(), 'resources/images/bluebird-upflap.png'),
       'down': os.path.join(os.getcwd(), 'resources/images/bluebird-downflap.png'),
       'mid': os.path.join(os.getcwd(), 'resources/images/bluebird-midflap.png')
    },

    'yellow': {
        'up': os.path.join(os.getcwd(), 'resources/images/yellowbird-upflap.png'),
        'down': os.path.join(os.getcwd(), 'resources/images/yellowbird-downflap.png'),
        'mid': os.path.join(os.getcwd(), 'resources/images/yellowbird-midflap.png')
    }

}

BACKGROUND_IMAGE_PATH = {
    'day': os.path.join(os.getcwd(), 'resources/images/background-day.png'),
    'night': os.path.join(os.getcwd(), 'resources/images/background-night.png')
}

PIPE_IMAGE_PATH = {
    'green': os.path.join(os.getcwd(), 'resources/images/pipe-green.png'),
    'red': os.path.join(os.getcwd(), 'resources/images/pipe-red.png')
}


OTHER_IMAGE_PATH = {
    'game-over': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
    'message': os.path.join(os.getcwd(), 'resources/images/message.png'),
    'base': os.path.join(os.getcwd(), 'resources/images/base.png')
}
