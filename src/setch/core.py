# SPDX-License-Identifier: GPL-3.0-or-later
#
# setch - A utility for retrieving system information on Linux
# Copyright (C) 2025 mentiferous
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>

"""core.py - Main module for setch."""

import sys

from setch.sys.check import sys_check
from setch.sys.info import KERNEL_VER, OS_ARCH, USER_HOST, get_uptime

SETCH = rf"""
    .--.
   |o_o |      {OS_ARCH}
   |\_/ |
  //   \ \     {KERNEL_VER}
 (|     | )
/`\_   _/`\    {get_uptime()}
\___)-(___/

{USER_HOST}
"""


def main():
    """Main function for setch."""
    if not sys_check():
        sys.exit("[!] Your system is incompatible with setch")
    print(SETCH)
