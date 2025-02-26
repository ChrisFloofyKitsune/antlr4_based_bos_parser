from enum import IntEnum

from bos.ast_nodes import Keyword


class BosOpCode(IntEnum):
    MOVE = 0x10001000
    TURN = 0x10002000
    SPIN = 0x10003000
    STOP_SPIN = 0x10004000
    SHOW = 0x10005000
    HIDE = 0x10006000
    CACHE = 0x10007000
    DONT_CACHE = 0x10008000
    MOVE_NOW = 0x1000B000
    TURN_NOW = 0x1000C000
    SHADE = 0x1000D000
    DONT_SHADE = 0x1000E000
    EMIT_SFX = 0x1000F000

    WAIT_FOR_TURN = 0x10011000
    WAIT_FOR_MOVE = 0x10012000
    SLEEP = 0x10013000

    PUSH_CONSTANT = 0x10021001
    PUSH_LOCAL_VAR = 0x10021002
    PUSH_STATIC = 0x10021004
    CREATE_LOCAL_VAR = 0x10022000
    POP_LOCAL_VAR = 0x10023002
    POP_STATIC = 0x10023004
    POP_STACK = 0x10024000

    ADD = 0x10031000
    SUB = 0x10032000
    MUL = 0x10033000
    DIV = 0x10034000
    MOD = 0x10034001
    BITWISE_AND = 0x10035000
    BITWISE_OR = 0x10036000
    BITWISE_XOR = 0x10037000
    BITWISE_NOT = 0x10038000

    RAND = 0x10041000
    GET_UNIT_VALUE = 0x10042000
    GET = 0x10043000

    SET_LESS = 0x10051000
    SET_LESS_OR_EQUAL = 0x10052000
    SET_GREATER = 0x10053000
    SET_GREATER_OR_EQUAL = 0x10054000
    SET_EQUAL = 0x10055000
    SET_NOT_EQUAL = 0x10056000
    LOGICAL_AND = 0x10057000
    LOGICAL_OR = 0x10058000
    LOGICAL_XOR = 0x10059000
    LOGICAL_NOT = 0x1005A000

    START_SCRIPT = 0x10061000
    CALL_SCRIPT = 0x10062000
    REAL_CALL = 0x10062001
    LUA_CALL = 0x10062002
    JUMP = 0x10064000
    RETURN = 0x10065000
    JUMP_NOT_EQUAL = 0x10066000
    SIGNAL = 0x10067000
    SET_SIGNAL_MASK = 0x10068000

    EXPLODE = 0x10071000
    PLAY_SOUND = 0x10072000

    SET = 0x10082000
    ATTACH_UNIT = 0x10083000
    DROP_UNIT = 0x10084000

    def __repr__(self):
        return f'<{self.__class__.__name__}.{self.name}: 0x{self:08X}>'
    
    @classmethod
    def from_keyword(cls, keyword: Keyword):
        match keyword:
            case Keyword.TURN:
                return BosOpCode.TURN
            case Keyword.MOVE:
                return BosOpCode.MOVE
            case Keyword.SPIN:
                return BosOpCode.SPIN
            case Keyword.STOP_SPIN:
                return BosOpCode.STOP_SPIN
            case Keyword.WAIT_FOR_TURN:
                return BosOpCode.WAIT_FOR_TURN
            case Keyword.WAIT_FOR_MOVE:
                return BosOpCode.WAIT_FOR_MOVE
            case Keyword.SET:
                return BosOpCode.SET
            case Keyword.GET:
                return BosOpCode.GET
            case Keyword.CALL_SCRIPT:
                return BosOpCode.CALL_SCRIPT
            case Keyword.START_SCRIPT:
                return BosOpCode.START_SCRIPT
            case Keyword.EMIT_SFX:
                return BosOpCode.EMIT_SFX
            case Keyword.SLEEP:
                return BosOpCode.SLEEP
            case Keyword.HIDE:
                return BosOpCode.HIDE
            case Keyword.SHOW:
                return BosOpCode.SHOW
            case Keyword.EXPLODE:
                return BosOpCode.EXPLODE
            case Keyword.SIGNAL:
                return BosOpCode.SIGNAL
            case Keyword.SET_SIGNAL_MASK:
                return BosOpCode.SET_SIGNAL_MASK
            case Keyword.ATTACH_UNIT:
                return BosOpCode.ATTACH_UNIT
            case Keyword.DROP_UNIT:
                return BosOpCode.DROP_UNIT
            case Keyword.RETURN:
                return BosOpCode.RETURN
            case Keyword.CACHE:
                return BosOpCode.CACHE
            case Keyword.DONT_CACHE:
                return BosOpCode.DONT_CACHE
            case Keyword.DONT_SHADOW:
                return BosOpCode.DONT_SHADE
            case Keyword.DONT_SHADE:
                return BosOpCode.DONT_SHADE
            case Keyword.PLAY_SOUND:
                return BosOpCode.PLAY_SOUND
        return None

if __name__ == '__main__':
    print([*BosOpCode])
