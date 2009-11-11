'''
VideoBase: base for implementing a video reader
'''

__all__ = ('VideoBase', 'Video')

from .. import core_select_lib
from ...baseobject import BaseObject
from ...logger import pymt_logger

class VideoBase(BaseObject):
    '''VideoBase, a class to implement a video reader.
    
    :Parameters:
        `filename` : str
            Filename of the video. Can be a file or an URI.
        `color` : list
            Color filter of the video (usually white.)
        `eos` : str
            Action to do when EOS is hit. Can be one of 'pause' or 'loop'
    '''

    __slots__ = ('_wantplay', '_buffer', '_filename', '_texture', 'color',
                 '_volume', 'eos', '_state')

    def __init__(self, **kwargs):
        kwargs.setdefault('filename', None)
        kwargs.setdefault('color', (1, 1, 1, 1))
        kwargs.setdefault('eos', 'pause')

        super(VideoBase, self).__init__(**kwargs)

        self._wantplay      = False
        self._buffer        = None
        self._filename      = None
        self._texture       = None
        self._volume        = 1.
        self._state         = ''

        self.eos            = kwargs.get('eos')
        self.color          = kwargs.get('color')
        self.filename       = kwargs.get('filename')

    def __del__(self):
        self.unload()

    def _get_filename(self):
        return self._filename
    def _set_filename(self, filename):
        if filename == self._filename:
            return
        self.unload()
        self._filename = filename
        if self._filename is None:
            return
        self.load()
    filename = property(lambda self: self._get_filename(),
            lambda self, x: self._set_filename(x),
            doc='Get/set the filename/uri of current video')

    def _get_position(self):
        return 0
    def _set_position(self, pos):
        self.seek(pos)
    position = property(lambda self: self._get_position(),
            lambda self, x: self._set_position(x),
            doc='Get/set the position in the video (in seconds)')

    def _get_volume(self):
        return self._volume
    def _set_volume(self, volume):
        self._volume = volume
    volume = property(lambda self: self._get_volume(),
            lambda self, x: self._set_volume(x),
            doc='Get/set the volume in the video (1.0 = 100%)')

    def _get_duration(self):
        return 0
    duration = property(lambda self: self._get_duration(),
            doc='Get the video duration (in seconds)')

    def _get_texture(self):
        return self._texture
    texture = property(lambda self: self._get_texture(),
            doc='Get the video texture')

    def _get_state(self):
        return self._state
    state = property(lambda self: self._get_state(),
            doc='Get the video playing status')

    def seek(self, percent):
        '''Move on percent position'''
        pass

    def stop(self):
        '''Stop the video playing'''
        self._state = ''

    def play(self):
        '''Play the video'''
        self._state = 'playing'

    def load(self):
        '''Load the video from the current filename'''
        pass

    def unload(self):
        '''Unload the actual video'''
        self._state = ''

    def update(self):
        '''Update the video content to texture.
        Must be called every frame, before draw.'''

    def draw(self):
        '''Draw the current video on screen'''
        pass

# Load the appropriate provider
Video = core_select_lib('video', (
    ('gstreamer', 'video_gstreamer', 'VideoGStreamer'),
))
