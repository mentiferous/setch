# SPDX-License-Identifier: GPL-3.0-or-later
#
# setch - Utility for retrieving system information on Linux
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

"""info.py - Module for getting system information."""

from getpass import getuser
from platform import freedesktop_os_release, machine, node, release
from subprocess import CalledProcessError, check_output

# Get username and hostname
try:
    USER = getuser()

except OSError:
    USER = "Unknown username"

HOST = node() or "Unknown hostname"

USER_HOST = f"{USER}@{HOST}"

# Get OS and architecture
OS = freedesktop_os_release().get("PRETTY_NAME", "Unknown OS")

ARCH = machine() or "Unknown architecture"

OS_ARCH = f"{OS} {ARCH}"

# Get kernel version
KERNEL_VER = release() or "Unknown kernel version"


def get_uptime():
    """Gets the system uptime."""

    try:
        uptime = check_output(["uptime", "-p"], text=True)
        return uptime.removeprefix("up ").strip()

    except (FileNotFoundError, CalledProcessError):
        return "Unknown uptime"
