# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Control gRPC API."""

from logging import INFO
from typing import Optional

import grpc

from flwr.common import GRPC_MAX_MESSAGE_LENGTH
from flwr.common.logger import log
from flwr.proto.control_pb2_grpc import (  # pylint: disable=E0611
    add_ControlServicer_to_server,
)
from flwr.server.superlink.ffs.ffs_factory import FfsFactory
from flwr.server.superlink.state import StateFactory

from ..fleet.grpc_bidi.grpc_server import generic_create_grpc_server
from .control_servicer import ControlServicer


def run_control_api_grpc(
    address: str,
    state_factory: StateFactory,
    ffs_factory: FfsFactory,
    certificates: Optional[tuple[bytes, bytes, bytes]],
) -> grpc.Server:
    """Run Control API."""
    # Create Control API gRPC server
    driver_servicer: grpc.Server = ControlServicer(
        state_factory=state_factory,
        ffs_factory=ffs_factory,
    )
    control_add_servicer_to_server_fn = add_ControlServicer_to_server
    control_grpc_server = generic_create_grpc_server(
        servicer_and_add_fn=(driver_servicer, control_add_servicer_to_server_fn),
        server_address=address,
        max_message_length=GRPC_MAX_MESSAGE_LENGTH,
        certificates=certificates,
    )

    log(INFO, "Flower ECE: Starting Control API on %s", address)
    control_grpc_server.start()

    return control_grpc_server