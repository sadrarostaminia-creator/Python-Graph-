"""Solve and visualize a 1D electromagnetic field inside a conducting metal.

This uses the classic skin-effect solution for a plane wave incident on a good
conductor. The electric field decays exponentially with depth and oscillates
with phase lag.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


MU_0 = 4 * np.pi * 1e-7


@dataclass(frozen=True)
class MetalProperties:
    conductivity_s_per_m: float
    relative_permeability: float = 1.0

    @property
    def permeability(self) -> float:
        return MU_0 * self.relative_permeability


def skin_depth(omega_rad_s: float, metal: MetalProperties) -> float:
    """Return the skin depth (meters) for a given angular frequency."""
    if omega_rad_s <= 0:
        raise ValueError("omega_rad_s must be positive")
    if metal.conductivity_s_per_m <= 0:
        raise ValueError("conductivity_s_per_m must be positive")
    return np.sqrt(2.0 / (omega_rad_s * metal.permeability * metal.conductivity_s_per_m))


def electric_field(
    depth_m: np.ndarray,
    time_s: float,
    amplitude_v_m: float,
    omega_rad_s: float,
    metal: MetalProperties,
) -> np.ndarray:
    """Compute the electric field magnitude inside a conductor (V/m).

    The field is computed as:
        E(z, t) = E0 * exp(-z/δ) * cos(omega * t - z/δ)
    where δ is the skin depth.
    """
    delta = skin_depth(omega_rad_s, metal)
    return amplitude_v_m * np.exp(-depth_m / delta) * np.cos(omega_rad_s * time_s - depth_m / delta)


def solve_field_profile(
    max_depth_m: float,
    points: int,
    time_s: float,
    amplitude_v_m: float,
    omega_rad_s: float,
    metal: MetalProperties,
) -> Tuple[np.ndarray, np.ndarray, float]:
    """Solve the field profile over depth and return (depths, field, skin_depth)."""
    if max_depth_m <= 0:
        raise ValueError("max_depth_m must be positive")
    if points < 2:
        raise ValueError("points must be at least 2")

    depths = np.linspace(0.0, max_depth_m, points)
    field = electric_field(depths, time_s, amplitude_v_m, omega_rad_s, metal)
    return depths, field, skin_depth(omega_rad_s, metal)


def main() -> None:
    """Run a sample calculation for copper and plot the field vs depth."""
    import matplotlib.pyplot as plt

    copper = MetalProperties(conductivity_s_per_m=5.8e7, relative_permeability=1.0)
    frequency_hz = 1e6
    omega = 2 * np.pi * frequency_hz
    depth_max = 5e-3

    depths, field, delta = solve_field_profile(
        max_depth_m=depth_max,
        points=400,
        time_s=0.0,
        amplitude_v_m=1.0,
        omega_rad_s=omega,
        metal=copper,
    )

    plt.figure(figsize=(6, 4))
    plt.plot(depths * 1e3, field, label="E(z, t=0)")
    plt.axvline(delta * 1e3, color="red", linestyle="--", label=f"Skin depth = {delta*1e3:.3f} mm")
    plt.title("Electric Field in Copper (Skin Effect)")
    plt.xlabel("Depth (mm)")
    plt.ylabel("Electric Field (V/m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("field_profile.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
