
from .arch import Arch, register_arch


class ArchClemency(Arch):
    """
    The awesome architecture created by LegitBS for DEF CON CTF 2017 Finals.

    Each byte is 9 bits long.
    """

    def __init__(self):
        super(ArchClemency, self).__init__("Iend_ME")
        # TODO: Define function prologs
        self.qemu_name = 'clemency'
        self.bits = 27
        self.name = "Clemency"
        self.ida_processor = 'clemency'
        self.max_inst_bytes = 6
        ip_offset = 93
        sp_offset = 87
        bp_offset = None  # there is no bp in cLEMENCy
        ret_offset = None
        lr_offset = 90
        syscall_num_offset = None
        call_pushes_ret = False
        stack_change = -3
        branch_delay_slot = False
        self.sizeof = {'short': 16, 'int': 16, 'long': 32, 'long long': 64}

    function_prologs = { }
    function_epilogs = { }

    ret_instruction = ""
    nop_instruction = ""
    # instruction_alignment = 4
    persistent_regs = [ ]

    default_register_values = [
        ( 'sp', Arch.initial_sp, True, 'global' ),   # the stack
    ]
    entry_register_values = {
    }

    default_symbolic_registers = [ ]

    register_names = {(3*x) : 'r' + str(x) for x in range(32)}
    register_names[3 * 31] = 'pc'
    register_names[3 * 30] = 'ra'
    register_names[3 * 29] = 'st'

    registers = {(3*x, 3) : 'r' + str(x) for x in range(32)}
    registers['pc'] = (3 * 31, 3)
    registers['ra'] = (3 * 30, 3)
    registers['st'] = (3 * 29, 3)

    argument_registers = {registers['r' + str(x)][0] for x in range(9)}

    # EDG: Can you even use PIC here? I don't think so
    dynamic_tag_translation = {}


register_arch([r'clemency'], 32, 'Iend_LE' , ArchClemency)