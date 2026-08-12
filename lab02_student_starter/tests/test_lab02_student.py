"""Write at least two focused tests before submitting Lab 02."""

import unittest

from star_sprout_lab import GameConfig, InputState, initial_state, step


class StudentLab02Tests(unittest.TestCase):

    def test_precision_moves_half_normal_distance(self) -> None:
        config = GameConfig(player_speed=100.0, max_dt=0.05)

        normal_before = initial_state(seed=42, config=config)
        precision_before = initial_state(seed=42, config=config)

        normal_after = step(
            normal_before,
            InputState(right=True),
            0.05,
        )

        precision_after = step(
            precision_before,
            InputState(right=True, precision=True),
            0.05,
        )

        normal_distance = normal_after.player.x - normal_before.player.x
        precision_distance = (
            precision_after.player.x - precision_before.player.x
        )

        self.assertAlmostEqual(normal_distance, 5.0)
        self.assertAlmostEqual(precision_distance, 2.5)
        self.assertAlmostEqual(
            precision_distance,
            normal_distance * 0.5,
        )

    def test_player_cannot_move_above_hud_boundary(self) -> None:
        config = GameConfig(
            width=400,
            height=300,
            hud_height=60,
            player_radius=10.0,
            player_speed=1000.0,
            max_dt=0.05,
        )

        world = initial_state(seed=42, config=config)

        for _ in range(20):
            world = step(
                world,
                InputState(up=True),
                0.05,
            )

        minimum_y = config.hud_height + config.player_radius

        self.assertAlmostEqual(
            world.player.y,
            minimum_y,
        )
        self.assertGreaterEqual(
            world.player.y,
            minimum_y,
        )


if __name__ == "__main__":
    unittest.main()