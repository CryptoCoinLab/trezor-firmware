# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TezosPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 155

    def __init__(
        self,
        public_key: str = None,
    ) -> None:
        self.public_key = public_key

    @classmethod
    def get_fields(cls):
        return {
            1: ('public_key', p.UnicodeType, 0),
        }
