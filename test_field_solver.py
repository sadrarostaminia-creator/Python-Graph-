import numpy as np

from field_solver import MetalProperties, electric_field, skin_depth, solve_field_profile


def test_skin_depth_positive_and_matches_expected_scale():
    copper = MetalProperties(conductivity_s_per_m=5.8e7)
    omega = 2 * np.pi * 1e6
    delta = skin_depth(omega, copper)
    assert delta > 0
    # For copper at 1 MHz, skin depth is around 0.066 mm
    assert 4e-5 < delta < 1e-3


def test_electric_field_decay_with_depth():
    copper = MetalProperties(conductivity_s_per_m=5.8e7)
    omega = 2 * np.pi * 1e6
    depth = np.array([0.0, 1e-3])
    field = electric_field(depth, time_s=0.0, amplitude_v_m=1.0, omega_rad_s=omega, metal=copper)
    assert abs(field[0]) >= abs(field[1])


def test_solve_field_profile_shapes():
    copper = MetalProperties(conductivity_s_per_m=5.8e7)
    depths, field, delta = solve_field_profile(
        max_depth_m=1e-3,
        points=10,
        time_s=0.0,
        amplitude_v_m=1.0,
        omega_rad_s=2 * np.pi * 1e6,
        metal=copper,
    )
    assert depths.shape == field.shape
    assert depths.shape == (10,)
    assert delta > 0
