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
"""Utility functions for State."""


import time
from logging import ERROR
from os import urandom
from uuid import uuid4

from flwr.common import log
from flwr.common.constant import ErrorCode
from flwr.common.typing import RunStatus
from flwr.proto.error_pb2 import Error  # pylint: disable=E0611
from flwr.proto.node_pb2 import Node  # pylint: disable=E0611
from flwr.proto.task_pb2 import Task, TaskIns, TaskRes  # pylint: disable=E0611

NODE_UNAVAILABLE_ERROR_REASON = (
    "Error: Node Unavailable - The destination node is currently unavailable. "
    "It exceeds the time limit specified in its last ping."
)

VALID_RUN_STATUS_PHASE_TRANSITIONS = {("starting", "running"), ("running", "finished")}
VALID_RUN_STATUS_RESULTS = {"completed", "failed", "stopped", ""}


def generate_rand_int_from_bytes(num_bytes: int) -> int:
    """Generate a random `num_bytes` integer."""
    return int.from_bytes(urandom(num_bytes), "little", signed=True)


def make_node_unavailable_taskres(ref_taskins: TaskIns) -> TaskRes:
    """Generate a TaskRes with a node unavailable error from a TaskIns."""
    current_time = time.time()
    ttl = ref_taskins.task.ttl - (current_time - ref_taskins.task.created_at)
    if ttl < 0:
        log(ERROR, "Creating TaskRes for TaskIns that exceeds its TTL.")
        ttl = 0
    return TaskRes(
        task_id=str(uuid4()),
        group_id=ref_taskins.group_id,
        run_id=ref_taskins.run_id,
        task=Task(
            producer=Node(node_id=ref_taskins.task.consumer.node_id, anonymous=False),
            consumer=Node(node_id=ref_taskins.task.producer.node_id, anonymous=False),
            created_at=current_time,
            ttl=ttl,
            ancestry=[ref_taskins.task_id],
            task_type=ref_taskins.task.task_type,
            error=Error(
                code=ErrorCode.NODE_UNAVAILABLE, reason=NODE_UNAVAILABLE_ERROR_REASON
            ),
        ),
    )


def is_valid_transition(current_status: RunStatus, new_status: RunStatus) -> bool:
    """Check if a transition between two run statuses is valid.

    Parameters
    ----------
    current_status : RunStatus
        The current status of the run.
    new_status : RunStatus
        The new status to transition to.

    Returns
    -------
    bool
        True if the transition is valid, False otherwise.
    """
    return (
        current_status.phase,
        new_status.phase,
    ) in VALID_RUN_STATUS_PHASE_TRANSITIONS


def has_valid_result(status: RunStatus) -> bool:
    """Check if the 'result' field of the given status is valid.

    Parameters
    ----------
    status : RunStatus
        The run status object to be checked.

    Returns
    -------
    bool
        True if the status has a valid result, False otherwise.

    Notes
    -----
    An empty string (i.e., "") is considered a valid result.
    """
    return status.result in VALID_RUN_STATUS_RESULTS
