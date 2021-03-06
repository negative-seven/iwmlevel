from enum import IntEnum


class EventType(IntEnum):
	ON_CREATE = 1
	ON_TIMER = 2
	ON_PLAYER_JUMP = 13
	ON_PLAYER_SHOOT = 14
	WHEN_SHOT = 15
	ON_TRIGGER = 16
	ON_METRONOME_TICK = 17
	ON_COINS_COLLECTED = 18
	TOUCH_ACTIVATOR = 19
	ON_VINE_JUMP = 20
	SPRUNG = 21
	WHEN_HIT_BY_SWORD = 22
	ON_CANNON_BALL_BOUNCE = 23
	LEFT_RIGHT_KEYS = 24
	ON_OBJECT_COLLISION = 25
	ON_A_COIN_COLLECTED = 26
	ON_BLUE_COINS_COLLECTED = 27
	UP_DOWN_KEYS = 28
