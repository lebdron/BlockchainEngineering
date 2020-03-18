class BaseMessage(object):
    __slots__ = ('sender', 'data')
    base_size = 20

    def __init__(self, sender, data=None):
        self.sender = sender
        self.data = data

    @property
    def size(self):
        return self.base_size + len(repr(self.data))

    def __repr__(self):
        msg_type = '%s:' % self.__class__.__name__
        data = self.data if self.data else ""
        return msg_type + data


########## Messages ###############

class Ping(BaseMessage):
    """Response to ping"""
    pass


class Pong(BaseMessage):
    """Response to pong"""
    pass


class RequestPeers(BaseMessage):
    """Request peers to connect to"""
    pass


class PeerList(BaseMessage):
    """Peer list with known peers"""

    def __init__(self, sender, peers):
        super().__init__(sender, set(peers))

    def __repr__(self):
        return 'PeerList'


class Hello(BaseMessage):
    """Offer a peer to connect"""
    pass