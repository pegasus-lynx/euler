"""Utilities for measuring and reporting problem execution time."""

import logging
from time import perf_counter
from typing import Optional


def start_timer() -> float:
	"""Start a high-resolution timer and return its start time."""
	return perf_counter()


def stop_timer(
	start_time: float,
	problem: Optional[str] = None,
	*,
	logger: Optional[logging.Logger] = None,
	print_output: bool = True,
) -> float:
	"""Stop a timer, report its elapsed time, and return the duration in seconds."""
	elapsed = perf_counter() - start_time
	prefix = f"{problem} execution time" if problem else "Execution time"
	message = f"{prefix}: {elapsed:.6f} seconds"

	if logger is not None:
		logger.info(message)
	if print_output:
		print(message)

	return elapsed
