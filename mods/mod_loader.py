"""Mod support stubs.

This module will provide extension points for community-made mods
and custom scenario packs.
"""


class ModLoader:
    """Placeholder for mod loading system."""

    def initialize_system(self) -> None:
        """Scan for mods and register metadata (placeholder)."""
        print("[ModLoader] initialize_system called.")

    def update_step(self) -> None:
        """Advance mod hooks per simulation step (placeholder)."""
        print("[ModLoader] update_step called.")

    def log_state(self) -> None:
        """Log mod loader status for debugging (placeholder)."""
        print("[ModLoader] log_state called.")
