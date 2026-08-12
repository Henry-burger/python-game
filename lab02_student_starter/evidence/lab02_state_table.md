# Lab 02 State Table

Complete the **prediction** columns before running the scenario.

Configuration: `player_speed=100.0`, `max_dt=0.05`, initial player `(480, 504)`.

| Step | Input and `dt` | Predicted tick / elapsed / x / y | Calculation | Observed result | Difference and correction |
|---|---|---|---|---|---|
| 1 | right, 0.05 | tick=1, elapsed=0.05, x=485.0, y=504.0 | bounded_dt=min(0.05,0.05)=0.05. Direction=(1,0). Distance=100.0×0.05=5.0. New position=(480+5,504)=(485,504). | | |
| 2 | right + up, 0.05 | tick=2, elapsed=0.10, x=488.5355, y=500.4645 | Direction=(1,-1), length=sqrt(2), normalized=(1/sqrt(2),-1/sqrt(2)). Total distance=100.0×0.05=5.0. dx=5/sqrt(2)=3.5355, dy=-5/sqrt(2)=-3.5355. New position=(488.5355,500.4645). | | |
| 3 | left + right, 0.05 | tick=3, elapsed=0.15, x=488.5355, y=500.4645 | Horizontal intent=right-left=1-1=0. Direction=(0,0), so displacement=0. Valid positive dt still advances tick and elapsed by 0.05. | | |
| 4 | neutral, 0.20 | tick=4, elapsed=0.20, x=488.5355, y=500.4645 | Neutral input gives direction=(0,0). bounded_dt=min(0.20,0.05)=0.05. Position does not change, but tick advances by 1 and elapsed increases by 0.05. | | |

Explain why diagonal input must be normalized:

Diagonal input must be normalized because the raw vector `(1, 1)` or `(1, -1)` has magnitude `sqrt(2)`, which is larger than the magnitude `1` of a single-axis direction. Without normalization, diagonal movement would therefore be about 1.414 times faster than horizontal or vertical movement. Normalizing the direction keeps the total movement distance equal to `speed × bounded_dt` in every direction.