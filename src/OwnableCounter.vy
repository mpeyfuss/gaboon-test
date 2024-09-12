# SPDX-License-Identifier: MIT
# @version 0.4.0

from lib.snekmate.auth import ownable
initializes: ownable

number: public(uint256)

@deploy
def __init__():
    ownable.__init__()

@external
def set_number(new_number: uint256):
    self.number = new_number

@external
def increment():
    self.number += 1
