class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3 

    def __init__(self):
        '''
        Help on function power in module __main__:
        '''
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__previous_volume = self.__volume

    def power(self):
        '''
        Method to turn the tv on
        '''
        self.__status = not self.__status

    def mute(self):
        '''
        Method to mute the tv
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            else:
                self.__muted = True
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        '''
        Method to change the channel up.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1 
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to decrease the tv channel.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1 
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        Method to turn the tv up.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1 

    def volume_down(self):
        '''
        Method to turn the tv down.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1 

    def __str__(self):
        '''
        Method to show the tv status.
        :return: tv status.
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
    print(help(__str__))