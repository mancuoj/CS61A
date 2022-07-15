test = {
  'name': 'Question 5',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a4d959d6146005b45f9590c6bc256e37',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'bcda62bd369acb79a636e354f5ef2f48',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': '6092933b58b128fe246b574b1aa79389',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
          >>> s0
          17a90ac6d84565b47483000c22f1f6de
          # locked
          >>> s1
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
          >>> s0
          af0b3285304485122429774c0ea3182a
          # locked
          >>> s1
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s0, s1 = hog.play(always(3), always(3), goal=15, dice=always_three)
          >>> s0
          18
          >>> s1
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> s0, s1 = hog.play(always(1), always(1), goal=5, dice=always_three)
          >>> s0
          5
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Use strategies
          >>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
          >>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
          >>> s0
          d1334768e299266a4ad58d7be1c22f75
          # locked
          >>> s1
          c8735a01952a81cf365b4c80d8fbb832
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_seven = hog.make_test_dice(7)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Player 0 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=88, score1=87, dice=always_three)
          >>> s0
          100
          >>> s1
          87
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Oink Points refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=5, score1=96, dice=always_three)
          >>> s0
          19
          >>> s1
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> s0, s1 = hog.play(always(1), always(1), goal=25, dice=hog.make_test_dice(5, 22, 8, 1, 2, 6, 3))
          >>> s0
          15
          >>> s1
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11606, score0=15, score1=10, goal=32)
          >>> print(turns[0])
          Start scores = (15, 10).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 4, 3, 5].
          End scores = (36, 10)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=63738, score0=3, score1=3, goal=46)
          >>> print(turns[0])
          Start scores = (3, 3).
          Player 0 rolls 9 dice and gets outcomes [3, 1, 2, 2, 5, 6, 6, 4, 6].
          End scores = (4, 3)
          >>> print(turns[1])
          Start scores = (4, 3).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 4)
          >>> print(turns[2])
          Start scores = (4, 4).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (12, 4)
          >>> print(turns[3])
          Start scores = (12, 4).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 3, 5].
          End scores = (12, 21)
          >>> print(turns[4])
          Start scores = (12, 21).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (19, 21)
          >>> print(turns[5])
          Start scores = (19, 21).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 5, 2, 3].
          End scores = (19, 40)
          >>> print(turns[6])
          Start scores = (19, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (27, 40)
          >>> print(turns[7])
          Start scores = (27, 40).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 1, 6, 3, 6].
          End scores = (27, 43)
          >>> print(turns[8])
          Start scores = (27, 43).
          Player 0 rolls 7 dice and gets outcomes [3, 3, 2, 4, 2, 5, 2].
          End scores = (48, 43)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=82444, score0=14, score1=13, goal=88)
          >>> print(turns[0])
          Start scores = (14, 13).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 5, 1, 3, 4, 2, 4, 2].
          End scores = (15, 13)
          >>> print(turns[1])
          Start scores = (15, 13).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 1, 3, 6, 4].
          End scores = (15, 14)
          >>> print(turns[2])
          Start scores = (15, 14).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 3, 5, 5, 6, 6, 4, 5].
          End scores = (57, 14)
          >>> print(turns[3])
          Start scores = (57, 14).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (57, 29)
          >>> print(turns[4])
          Start scores = (57, 29).
          Player 0 rolls 6 dice and gets outcomes [6, 3, 6, 3, 5, 4].
          End scores = (84, 29)
          >>> print(turns[5])
          Start scores = (84, 29).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 4, 1, 6, 1, 5].
          End scores = (84, 30)
          >>> print(turns[6])
          Start scores = (84, 30).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 1, 1, 3, 4, 3, 3, 4, 3].
          End scores = (85, 30)
          >>> print(turns[7])
          Start scores = (85, 30).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 4, 1, 3, 6, 4, 6].
          End scores = (85, 37)
          >>> print(turns[8])
          Start scores = (85, 37).
          Player 0 rolls 10 dice and gets outcomes [4, 3, 6, 4, 1, 4, 6, 3, 4, 1].
          End scores = (86, 37)
          >>> print(turns[9])
          Start scores = (86, 37).
          Player 1 rolls 7 dice and gets outcomes [4, 6, 4, 1, 5, 2, 1].
          End scores = (86, 38)
          >>> print(turns[10])
          Start scores = (86, 38).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (87, 38)
          >>> print(turns[11])
          Start scores = (87, 38).
          Player 1 rolls 3 dice and gets outcomes [6, 5, 4].
          End scores = (87, 59)
          >>> print(turns[12])
          Start scores = (87, 59).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (88, 59)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=65061, score0=23, score1=55, goal=56)
          >>> print(turns[0])
          Start scores = (23, 55).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 3].
          End scores = (24, 55)
          >>> print(turns[1])
          Start scores = (24, 55).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 4, 1, 2, 3].
          End scores = (24, 56)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50266, score0=64, score1=24, goal=88)
          >>> print(turns[0])
          Start scores = (64, 24).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 1, 4, 6, 6, 2, 4, 1].
          End scores = (65, 24)
          >>> print(turns[1])
          Start scores = (65, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 5, 4, 1, 5, 1, 1].
          End scores = (65, 25)
          >>> print(turns[2])
          Start scores = (65, 25).
          Player 0 rolls 7 dice and gets outcomes [4, 3, 2, 6, 5, 5, 3].
          End scores = (93, 25)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=79534, score0=3, score1=4, goal=10)
          >>> print(turns[0])
          Start scores = (3, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (4, 4)
          >>> print(turns[1])
          Start scores = (4, 4).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 2, 6, 6, 4].
          End scores = (4, 7)
          >>> print(turns[2])
          Start scores = (4, 7).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 5, 2, 4, 3, 5, 1].
          End scores = (7, 7)
          >>> print(turns[3])
          Start scores = (7, 7).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 3, 4, 6, 1, 3].
          End scores = (7, 8)
          >>> print(turns[4])
          Start scores = (7, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 2, 4].
          End scores = (8, 8)
          >>> print(turns[5])
          Start scores = (8, 8).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (8, 12)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=77997, score0=47, score1=10, goal=49)
          >>> print(turns[0])
          Start scores = (47, 10).
          Player 0 rolls 10 dice and gets outcomes [5, 3, 1, 3, 3, 1, 1, 5, 3, 2].
          End scores = (48, 10)
          >>> print(turns[1])
          Start scores = (48, 10).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (48, 13)
          >>> print(turns[2])
          Start scores = (48, 13).
          Player 0 rolls 5 dice and gets outcomes [6, 4, 4, 6, 3].
          End scores = (73, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=86122, score0=8, score1=11, goal=44)
          >>> print(turns[0])
          Start scores = (8, 11).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 2, 3, 3, 1, 6, 4, 6].
          End scores = (9, 11)
          >>> print(turns[1])
          Start scores = (9, 11).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 4, 1, 4, 4, 2, 5, 2].
          End scores = (9, 12)
          >>> print(turns[2])
          Start scores = (9, 12).
          Player 0 rolls 9 dice and gets outcomes [5, 2, 6, 1, 1, 2, 5, 5, 5].
          End scores = (10, 12)
          >>> print(turns[3])
          Start scores = (10, 12).
          Player 1 rolls 2 dice and gets outcomes [2, 4].
          End scores = (10, 18)
          >>> print(turns[4])
          Start scores = (10, 18).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (13, 18)
          >>> print(turns[5])
          Start scores = (13, 18).
          Player 1 rolls 9 dice and gets outcomes [2, 2, 6, 3, 2, 6, 1, 1, 2].
          End scores = (13, 23)
          >>> print(turns[6])
          Start scores = (13, 23).
          Player 0 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (29, 23)
          >>> print(turns[7])
          Start scores = (29, 23).
          Player 1 rolls 5 dice and gets outcomes [5, 1, 4, 4, 6].
          End scores = (29, 24)
          >>> print(turns[8])
          Start scores = (29, 24).
          Player 0 rolls 4 dice and gets outcomes [6, 1, 3, 2].
          End scores = (30, 24)
          >>> print(turns[9])
          Start scores = (30, 24).
          Player 1 rolls 4 dice and gets outcomes [1, 6, 2, 2].
          End scores = (30, 25)
          >>> print(turns[10])
          Start scores = (30, 25).
          Player 0 rolls 2 dice and gets outcomes [2, 2].
          End scores = (34, 25)
          >>> print(turns[11])
          Start scores = (34, 25).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 6, 4, 3, 1, 2].
          End scores = (34, 26)
          >>> print(turns[12])
          Start scores = (34, 26).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 2].
          End scores = (45, 26)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=17635, score0=7, score1=9, goal=10)
          >>> print(turns[0])
          Start scores = (7, 9).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98858, score0=0, score1=20, goal=66)
          >>> print(turns[0])
          Start scores = (0, 20).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 4, 1].
          End scores = (2, 20)
          >>> print(turns[1])
          Start scores = (2, 20).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (2, 28)
          >>> print(turns[2])
          Start scores = (2, 28).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 6, 6, 5, 6, 4, 1].
          End scores = (5, 28)
          >>> print(turns[3])
          Start scores = (5, 28).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 6].
          End scores = (5, 42)
          >>> print(turns[4])
          Start scores = (5, 42).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (13, 42)
          >>> print(turns[5])
          Start scores = (13, 42).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (13, 48)
          >>> print(turns[6])
          Start scores = (13, 48).
          Player 0 rolls 6 dice and gets outcomes [6, 2, 6, 4, 1, 4].
          End scores = (14, 48)
          >>> print(turns[7])
          Start scores = (14, 48).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 2, 5, 4, 4, 3, 2].
          End scores = (14, 77)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20766, score0=13, score1=20, goal=36)
          >>> print(turns[0])
          Start scores = (13, 20).
          Player 0 rolls 6 dice and gets outcomes [1, 5, 6, 6, 3, 2].
          End scores = (14, 20)
          >>> print(turns[1])
          Start scores = (14, 20).
          Player 1 rolls 7 dice and gets outcomes [2, 5, 3, 1, 6, 5, 6].
          End scores = (14, 21)
          >>> print(turns[2])
          Start scores = (14, 21).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (15, 21)
          >>> print(turns[3])
          Start scores = (15, 21).
          Player 1 rolls 9 dice and gets outcomes [6, 5, 4, 2, 1, 2, 2, 3, 4].
          End scores = (15, 22)
          >>> print(turns[4])
          Start scores = (15, 22).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 2, 1, 1, 2, 2].
          End scores = (16, 22)
          >>> print(turns[5])
          Start scores = (16, 22).
          Player 1 rolls 7 dice and gets outcomes [1, 2, 3, 2, 2, 6, 1].
          End scores = (16, 29)
          >>> print(turns[6])
          Start scores = (16, 29).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 5, 2].
          End scores = (31, 29)
          >>> print(turns[7])
          Start scores = (31, 29).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (31, 34)
          >>> print(turns[8])
          Start scores = (31, 34).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 5].
          End scores = (32, 34)
          >>> print(turns[9])
          Start scores = (32, 34).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (32, 45)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=90130, score0=5, score1=4, goal=11)
          >>> print(turns[0])
          Start scores = (5, 4).
          Player 0 rolls 7 dice and gets outcomes [3, 4, 3, 5, 4, 1, 6].
          End scores = (6, 4)
          >>> print(turns[1])
          Start scores = (6, 4).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 4, 1, 1, 5, 1, 2, 1].
          End scores = (6, 7)
          >>> print(turns[2])
          Start scores = (6, 7).
          Player 0 rolls 7 dice and gets outcomes [4, 4, 1, 6, 1, 6, 3].
          End scores = (11, 7)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=90430, score0=8, score1=5, goal=35)
          >>> print(turns[0])
          Start scores = (8, 5).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 6, 2, 6, 2, 6].
          End scores = (41, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=68954, score0=15, score1=32, goal=53)
          >>> print(turns[0])
          Start scores = (15, 32).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (23, 32)
          >>> print(turns[1])
          Start scores = (23, 32).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 1, 1, 6, 4, 5, 5].
          End scores = (23, 33)
          >>> print(turns[2])
          Start scores = (23, 33).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (24, 33)
          >>> print(turns[3])
          Start scores = (24, 33).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 5, 1].
          End scores = (24, 34)
          >>> print(turns[4])
          Start scores = (24, 34).
          Player 0 rolls 2 dice and gets outcomes [2, 5].
          End scores = (37, 34)
          >>> print(turns[5])
          Start scores = (37, 34).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 2, 6, 6, 6, 3, 1, 3].
          End scores = (37, 35)
          >>> print(turns[6])
          Start scores = (37, 35).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (39, 35)
          >>> print(turns[7])
          Start scores = (39, 35).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (39, 45)
          >>> print(turns[8])
          Start scores = (39, 45).
          Player 0 rolls 10 dice and gets outcomes [3, 2, 6, 4, 2, 2, 4, 1, 2, 1].
          End scores = (40, 45)
          >>> print(turns[9])
          Start scores = (40, 45).
          Player 1 rolls 9 dice and gets outcomes [5, 5, 5, 6, 5, 5, 4, 4, 2].
          End scores = (40, 86)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=40934, score0=15, score1=18, goal=23)
          >>> print(turns[0])
          Start scores = (15, 18).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 1, 6, 5, 1, 2, 3].
          End scores = (16, 18)
          >>> print(turns[1])
          Start scores = (16, 18).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 2, 2, 1, 5].
          End scores = (16, 23)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=54172, score0=47, score1=33, goal=71)
          >>> print(turns[0])
          Start scores = (47, 33).
          Player 0 rolls 9 dice and gets outcomes [2, 1, 5, 4, 6, 4, 3, 1, 6].
          End scores = (48, 33)
          >>> print(turns[1])
          Start scores = (48, 33).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 3, 3].
          End scores = (48, 53)
          >>> print(turns[2])
          Start scores = (48, 53).
          Player 0 rolls 8 dice and gets outcomes [1, 5, 6, 1, 6, 1, 3, 4].
          End scores = (49, 53)
          >>> print(turns[3])
          Start scores = (49, 53).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (49, 56)
          >>> print(turns[4])
          Start scores = (49, 56).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 1, 1].
          End scores = (50, 56)
          >>> print(turns[5])
          Start scores = (50, 56).
          Player 1 rolls 4 dice and gets outcomes [3, 1, 5, 1].
          End scores = (50, 57)
          >>> print(turns[6])
          Start scores = (50, 57).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 6, 4, 6].
          End scores = (75, 57)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=37099, score0=51, score1=24, goal=85)
          >>> print(turns[0])
          Start scores = (51, 24).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 4, 1, 1, 1, 1, 2].
          End scores = (52, 24)
          >>> print(turns[1])
          Start scores = (52, 24).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 3].
          End scores = (52, 39)
          >>> print(turns[2])
          Start scores = (52, 39).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 3, 6, 1, 3].
          End scores = (59, 39)
          >>> print(turns[3])
          Start scores = (59, 39).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 4, 4, 5, 4, 4].
          End scores = (59, 64)
          >>> print(turns[4])
          Start scores = (59, 64).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 6, 5, 1, 1].
          End scores = (60, 64)
          >>> print(turns[5])
          Start scores = (60, 64).
          Player 1 rolls 9 dice and gets outcomes [2, 1, 3, 6, 4, 2, 4, 4, 1].
          End scores = (60, 65)
          >>> print(turns[6])
          Start scores = (60, 65).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (71, 65)
          >>> print(turns[7])
          Start scores = (71, 65).
          Player 1 rolls 5 dice and gets outcomes [1, 5, 2, 3, 4].
          End scores = (71, 66)
          >>> print(turns[8])
          Start scores = (71, 66).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 4].
          End scores = (82, 66)
          >>> print(turns[9])
          Start scores = (82, 66).
          Player 1 rolls 10 dice and gets outcomes [5, 3, 6, 1, 6, 4, 3, 3, 4, 2].
          End scores = (82, 71)
          >>> print(turns[10])
          Start scores = (82, 71).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (97, 71)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=96045, score0=30, score1=3, goal=51)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 3, 5].
          End scores = (46, 3)
          >>> print(turns[1])
          Start scores = (46, 3).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 3, 5, 3, 5, 2, 4].
          End scores = (46, 30)
          >>> print(turns[2])
          Start scores = (46, 30).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 6].
          End scores = (53, 30)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=80360, score0=23, score1=11, goal=38)
          >>> print(turns[0])
          Start scores = (23, 11).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (25, 11)
          >>> print(turns[1])
          Start scores = (25, 11).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (25, 12)
          >>> print(turns[2])
          Start scores = (25, 12).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 2, 1].
          End scores = (26, 12)
          >>> print(turns[3])
          Start scores = (26, 12).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 5, 4, 2, 3, 5, 6].
          End scores = (26, 43)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=38176, score0=21, score1=18, goal=56)
          >>> print(turns[0])
          Start scores = (21, 18).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 1].
          End scores = (22, 18)
          >>> print(turns[1])
          Start scores = (22, 18).
          Player 1 rolls 10 dice and gets outcomes [1, 4, 1, 2, 6, 2, 6, 4, 4, 5].
          End scores = (22, 23)
          >>> print(turns[2])
          Start scores = (22, 23).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 3, 1, 1, 5, 1, 3, 3].
          End scores = (29, 23)
          >>> print(turns[3])
          Start scores = (29, 23).
          Player 1 rolls 4 dice and gets outcomes [3, 2, 5, 4].
          End scores = (29, 41)
          >>> print(turns[4])
          Start scores = (29, 41).
          Player 0 rolls 6 dice and gets outcomes [1, 5, 2, 2, 2, 6].
          End scores = (30, 41)
          >>> print(turns[5])
          Start scores = (30, 41).
          Player 1 rolls 10 dice and gets outcomes [1, 5, 5, 3, 6, 5, 2, 2, 3, 4].
          End scores = (30, 42)
          >>> print(turns[6])
          Start scores = (30, 42).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 2, 3, 1, 1, 4].
          End scores = (37, 42)
          >>> print(turns[7])
          Start scores = (37, 42).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 4].
          End scores = (37, 47)
          >>> print(turns[8])
          Start scores = (37, 47).
          Player 0 rolls 2 dice and gets outcomes [4, 5].
          End scores = (46, 47)
          >>> print(turns[9])
          Start scores = (46, 47).
          Player 1 rolls 7 dice and gets outcomes [5, 4, 6, 6, 6, 2, 1].
          End scores = (46, 48)
          >>> print(turns[10])
          Start scores = (46, 48).
          Player 0 rolls 9 dice and gets outcomes [4, 5, 4, 3, 6, 5, 2, 4, 5].
          End scores = (84, 48)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53943, score0=29, score1=9, goal=50)
          >>> print(turns[0])
          Start scores = (29, 9).
          Player 0 rolls 4 dice and gets outcomes [6, 3, 3, 4].
          End scores = (45, 9)
          >>> print(turns[1])
          Start scores = (45, 9).
          Player 1 rolls 9 dice and gets outcomes [4, 1, 5, 3, 3, 3, 4, 2, 3].
          End scores = (45, 10)
          >>> print(turns[2])
          Start scores = (45, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (53, 10)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=94396, score0=21, score1=66, goal=67)
          >>> print(turns[0])
          Start scores = (21, 66).
          Player 0 rolls 3 dice and gets outcomes [5, 2, 6].
          End scores = (34, 66)
          >>> print(turns[1])
          Start scores = (34, 66).
          Player 1 rolls 3 dice and gets outcomes [3, 6, 5].
          End scores = (34, 80)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20869, score0=28, score1=16, goal=39)
          >>> print(turns[0])
          Start scores = (28, 16).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 4, 5, 2, 3, 1].
          End scores = (31, 16)
          >>> print(turns[1])
          Start scores = (31, 16).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 2, 6, 1].
          End scores = (31, 19)
          >>> print(turns[2])
          Start scores = (31, 19).
          Player 0 rolls 8 dice and gets outcomes [1, 2, 2, 6, 6, 4, 4, 2].
          End scores = (32, 19)
          >>> print(turns[3])
          Start scores = (32, 19).
          Player 1 rolls 9 dice and gets outcomes [5, 6, 1, 5, 5, 2, 5, 2, 4].
          End scores = (32, 20)
          >>> print(turns[4])
          Start scores = (32, 20).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 1, 4].
          End scores = (33, 20)
          >>> print(turns[5])
          Start scores = (33, 20).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 4, 4, 1].
          End scores = (33, 21)
          >>> print(turns[6])
          Start scores = (33, 21).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 5, 5, 5].
          End scores = (34, 21)
          >>> print(turns[7])
          Start scores = (34, 21).
          Player 1 rolls 2 dice and gets outcomes [2, 2].
          End scores = (34, 25)
          >>> print(turns[8])
          Start scores = (34, 25).
          Player 0 rolls 7 dice and gets outcomes [4, 4, 1, 4, 1, 5, 2].
          End scores = (35, 25)
          >>> print(turns[9])
          Start scores = (35, 25).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 5, 3].
          End scores = (35, 43)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66981, score0=10, score1=37, goal=50)
          >>> print(turns[0])
          Start scores = (10, 37).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 2, 2].
          End scores = (13, 37)
          >>> print(turns[1])
          Start scores = (13, 37).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 1, 4, 2, 4, 3, 5, 2, 4].
          End scores = (13, 38)
          >>> print(turns[2])
          Start scores = (13, 38).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 2, 4, 5, 2, 4, 6, 1].
          End scores = (14, 38)
          >>> print(turns[3])
          Start scores = (14, 38).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 3, 6, 5, 5].
          End scores = (14, 39)
          >>> print(turns[4])
          Start scores = (14, 39).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 6, 5, 5].
          End scores = (15, 39)
          >>> print(turns[5])
          Start scores = (15, 39).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 2, 5, 6, 2, 1, 4, 2].
          End scores = (15, 40)
          >>> print(turns[6])
          Start scores = (15, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 4].
          End scores = (16, 40)
          >>> print(turns[7])
          Start scores = (16, 40).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (16, 43)
          >>> print(turns[8])
          Start scores = (16, 43).
          Player 0 rolls 10 dice and gets outcomes [2, 6, 1, 4, 6, 3, 5, 5, 4, 2].
          End scores = (19, 43)
          >>> print(turns[9])
          Start scores = (19, 43).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 4, 2].
          End scores = (19, 57)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=35200, score0=60, score1=43, goal=61)
          >>> print(turns[0])
          Start scores = (60, 43).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 5, 4, 1].
          End scores = (67, 43)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11754, score0=7, score1=76, goal=80)
          >>> print(turns[0])
          Start scores = (7, 76).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 4, 5].
          End scores = (20, 76)
          >>> print(turns[1])
          Start scores = (20, 76).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 4, 2, 6, 1].
          End scores = (20, 77)
          >>> print(turns[2])
          Start scores = (20, 77).
          Player 0 rolls 6 dice and gets outcomes [4, 1, 4, 2, 5, 3].
          End scores = (21, 77)
          >>> print(turns[3])
          Start scores = (21, 77).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (21, 80)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11625, score0=30, score1=33, goal=60)
          >>> print(turns[0])
          Start scores = (30, 33).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (37, 33)
          >>> print(turns[1])
          Start scores = (37, 33).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (37, 34)
          >>> print(turns[2])
          Start scores = (37, 34).
          Player 0 rolls 5 dice and gets outcomes [2, 6, 3, 1, 3].
          End scores = (38, 34)
          >>> print(turns[3])
          Start scores = (38, 34).
          Player 1 rolls 10 dice and gets outcomes [2, 5, 1, 4, 4, 3, 4, 5, 4, 2].
          End scores = (38, 35)
          >>> print(turns[4])
          Start scores = (38, 35).
          Player 0 rolls 10 dice and gets outcomes [4, 6, 4, 3, 1, 6, 5, 5, 4, 4].
          End scores = (39, 35)
          >>> print(turns[5])
          Start scores = (39, 35).
          Player 1 rolls 6 dice and gets outcomes [2, 6, 5, 1, 2, 1].
          End scores = (39, 36)
          >>> print(turns[6])
          Start scores = (39, 36).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 36)
          >>> print(turns[7])
          Start scores = (40, 36).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (40, 43)
          >>> print(turns[8])
          Start scores = (40, 43).
          Player 0 rolls 8 dice and gets outcomes [4, 2, 3, 4, 5, 4, 6, 2].
          End scores = (70, 43)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=70738, score0=16, score1=15, goal=23)
          >>> print(turns[0])
          Start scores = (16, 15).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 5, 2, 1, 2, 4].
          End scores = (19, 15)
          >>> print(turns[1])
          Start scores = (19, 15).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (19, 16)
          >>> print(turns[2])
          Start scores = (19, 16).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 1, 3, 6, 5, 3, 4].
          End scores = (20, 16)
          >>> print(turns[3])
          Start scores = (20, 16).
          Player 1 rolls 5 dice and gets outcomes [1, 1, 3, 6, 2].
          End scores = (20, 19)
          >>> print(turns[4])
          Start scores = (20, 19).
          Player 0 rolls 3 dice and gets outcomes [5, 4, 3].
          End scores = (32, 19)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=34169, score0=8, score1=25, goal=50)
          >>> print(turns[0])
          Start scores = (8, 25).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (19, 25)
          >>> print(turns[1])
          Start scores = (19, 25).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (19, 37)
          >>> print(turns[2])
          Start scores = (19, 37).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 4, 4, 1, 6, 6, 5, 1].
          End scores = (20, 37)
          >>> print(turns[3])
          Start scores = (20, 37).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (20, 38)
          >>> print(turns[4])
          Start scores = (20, 38).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 4, 6, 1].
          End scores = (21, 38)
          >>> print(turns[5])
          Start scores = (21, 38).
          Player 1 rolls 4 dice and gets outcomes [2, 3, 3, 5].
          End scores = (21, 51)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25523, score0=32, score1=95, goal=99)
          >>> print(turns[0])
          Start scores = (32, 95).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 6, 4].
          End scores = (54, 95)
          >>> print(turns[1])
          Start scores = (54, 95).
          Player 1 rolls 4 dice and gets outcomes [6, 3, 6, 1].
          End scores = (54, 96)
          >>> print(turns[2])
          Start scores = (54, 96).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (66, 96)
          >>> print(turns[3])
          Start scores = (66, 96).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (66, 102)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61991, score0=5, score1=20, goal=31)
          >>> print(turns[0])
          Start scores = (5, 20).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (17, 20)
          >>> print(turns[1])
          Start scores = (17, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 1, 3, 1].
          End scores = (17, 21)
          >>> print(turns[2])
          Start scores = (17, 21).
          Player 0 rolls 4 dice and gets outcomes [3, 6, 3, 1].
          End scores = (18, 21)
          >>> print(turns[3])
          Start scores = (18, 21).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (18, 30)
          >>> print(turns[4])
          Start scores = (18, 30).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 5, 5, 4, 2, 6, 5].
          End scores = (23, 30)
          >>> print(turns[5])
          Start scores = (23, 30).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (23, 33)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=4237, score0=16, score1=49, goal=81)
          >>> print(turns[0])
          Start scores = (16, 49).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 5, 4, 4, 2, 6, 4].
          End scores = (48, 49)
          >>> print(turns[1])
          Start scores = (48, 49).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 5, 1, 3, 1, 3].
          End scores = (48, 50)
          >>> print(turns[2])
          Start scores = (48, 50).
          Player 0 rolls 7 dice and gets outcomes [6, 5, 3, 1, 5, 1, 6].
          End scores = (49, 50)
          >>> print(turns[3])
          Start scores = (49, 50).
          Player 1 rolls 5 dice and gets outcomes [5, 4, 1, 4, 4].
          End scores = (49, 51)
          >>> print(turns[4])
          Start scores = (49, 51).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 6, 1, 5, 5, 2, 6, 5, 5].
          End scores = (50, 51)
          >>> print(turns[5])
          Start scores = (50, 51).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (50, 67)
          >>> print(turns[6])
          Start scores = (50, 67).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (55, 67)
          >>> print(turns[7])
          Start scores = (55, 67).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (55, 70)
          >>> print(turns[8])
          Start scores = (55, 70).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (56, 70)
          >>> print(turns[9])
          Start scores = (56, 70).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (56, 74)
          >>> print(turns[10])
          Start scores = (56, 74).
          Player 0 rolls 8 dice and gets outcomes [6, 6, 6, 5, 4, 2, 6, 6].
          End scores = (101, 74)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=30479, score0=5, score1=4, goal=11)
          >>> print(turns[0])
          Start scores = (5, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (6, 4)
          >>> print(turns[1])
          Start scores = (6, 4).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 6, 3].
          End scores = (6, 20)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=54986, score0=39, score1=74, goal=81)
          >>> print(turns[0])
          Start scores = (39, 74).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 4, 3].
          End scores = (40, 74)
          >>> print(turns[1])
          Start scores = (40, 74).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 5, 4, 6, 2].
          End scores = (40, 95)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=49809, score0=56, score1=14, goal=69)
          >>> print(turns[0])
          Start scores = (56, 14).
          Player 0 rolls 8 dice and gets outcomes [5, 1, 4, 1, 2, 5, 5, 6].
          End scores = (57, 14)
          >>> print(turns[1])
          Start scores = (57, 14).
          Player 1 rolls 6 dice and gets outcomes [2, 6, 2, 2, 2, 5].
          End scores = (57, 33)
          >>> print(turns[2])
          Start scores = (57, 33).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 3].
          End scores = (70, 33)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=21552, score0=61, score1=5, goal=69)
          >>> print(turns[0])
          Start scores = (61, 5).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (62, 5)
          >>> print(turns[1])
          Start scores = (62, 5).
          Player 1 rolls 6 dice and gets outcomes [5, 1, 6, 6, 2, 2].
          End scores = (62, 6)
          >>> print(turns[2])
          Start scores = (62, 6).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 1, 4, 2, 3, 5].
          End scores = (63, 6)
          >>> print(turns[3])
          Start scores = (63, 6).
          Player 1 rolls 9 dice and gets outcomes [3, 3, 4, 2, 2, 2, 5, 3, 6].
          End scores = (63, 36)
          >>> print(turns[4])
          Start scores = (63, 36).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (73, 36)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20590, score0=14, score1=0, goal=15)
          >>> print(turns[0])
          Start scores = (14, 0).
          Player 0 rolls 4 dice and gets outcomes [4, 4, 3, 5].
          End scores = (30, 0)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99130, score0=70, score1=53, goal=72)
          >>> print(turns[0])
          Start scores = (70, 53).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (78, 53)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=92149, score0=9, score1=37, goal=93)
          >>> print(turns[0])
          Start scores = (9, 37).
          Player 0 rolls 9 dice and gets outcomes [3, 1, 6, 4, 5, 2, 5, 6, 6].
          End scores = (10, 37)
          >>> print(turns[1])
          Start scores = (10, 37).
          Player 1 rolls 9 dice and gets outcomes [4, 3, 1, 5, 1, 4, 6, 2, 6].
          End scores = (10, 38)
          >>> print(turns[2])
          Start scores = (10, 38).
          Player 0 rolls 3 dice and gets outcomes [4, 5, 2].
          End scores = (21, 38)
          >>> print(turns[3])
          Start scores = (21, 38).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (21, 39)
          >>> print(turns[4])
          Start scores = (21, 39).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 5, 6, 6, 1].
          End scores = (22, 39)
          >>> print(turns[5])
          Start scores = (22, 39).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (22, 43)
          >>> print(turns[6])
          Start scores = (22, 43).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 3, 3, 2, 3, 2, 5].
          End scores = (55, 43)
          >>> print(turns[7])
          Start scores = (55, 43).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 4, 5, 2, 4, 4, 6].
          End scores = (55, 79)
          >>> print(turns[8])
          Start scores = (55, 79).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (66, 79)
          >>> print(turns[9])
          Start scores = (66, 79).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 1, 3].
          End scores = (66, 80)
          >>> print(turns[10])
          Start scores = (66, 80).
          Player 0 rolls 8 dice and gets outcomes [2, 4, 6, 6, 1, 6, 5, 6].
          End scores = (71, 80)
          >>> print(turns[11])
          Start scores = (71, 80).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 1, 2, 4, 2, 6].
          End scores = (71, 81)
          >>> print(turns[12])
          Start scores = (71, 81).
          Player 0 rolls 6 dice and gets outcomes [1, 2, 6, 2, 1, 5].
          End scores = (72, 81)
          >>> print(turns[13])
          Start scores = (72, 81).
          Player 1 rolls 8 dice and gets outcomes [2, 5, 1, 5, 3, 4, 4, 5].
          End scores = (72, 82)
          >>> print(turns[14])
          Start scores = (72, 82).
          Player 0 rolls 10 dice and gets outcomes [3, 5, 4, 3, 6, 4, 4, 6, 6, 3].
          End scores = (116, 82)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52242, score0=55, score1=37, goal=64)
          >>> print(turns[0])
          Start scores = (55, 37).
          Player 0 rolls 10 dice and gets outcomes [3, 4, 2, 6, 6, 5, 2, 1, 2, 4].
          End scores = (56, 37)
          >>> print(turns[1])
          Start scores = (56, 37).
          Player 1 rolls 3 dice and gets outcomes [2, 6, 4].
          End scores = (56, 49)
          >>> print(turns[2])
          Start scores = (56, 49).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (57, 49)
          >>> print(turns[3])
          Start scores = (57, 49).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (57, 52)
          >>> print(turns[4])
          Start scores = (57, 52).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 1, 3].
          End scores = (58, 52)
          >>> print(turns[5])
          Start scores = (58, 52).
          Player 1 rolls 6 dice and gets outcomes [4, 3, 4, 1, 1, 3].
          End scores = (58, 59)
          >>> print(turns[6])
          Start scores = (58, 59).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (64, 59)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=60287, score0=54, score1=8, goal=64)
          >>> print(turns[0])
          Start scores = (54, 8).
          Player 0 rolls 6 dice and gets outcomes [3, 5, 1, 2, 3, 6].
          End scores = (55, 8)
          >>> print(turns[1])
          Start scores = (55, 8).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (55, 9)
          >>> print(turns[2])
          Start scores = (55, 9).
          Player 0 rolls 3 dice and gets outcomes [5, 3, 6].
          End scores = (69, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=65291, score0=4, score1=3, goal=23)
          >>> print(turns[0])
          Start scores = (4, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (7, 3)
          >>> print(turns[1])
          Start scores = (7, 3).
          Player 1 rolls 5 dice and gets outcomes [4, 5, 1, 1, 1].
          End scores = (7, 4)
          >>> print(turns[2])
          Start scores = (7, 4).
          Player 0 rolls 5 dice and gets outcomes [6, 5, 5, 3, 3].
          End scores = (31, 4)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76703, score0=25, score1=24, goal=76)
          >>> print(turns[0])
          Start scores = (25, 24).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (26, 24)
          >>> print(turns[1])
          Start scores = (26, 24).
          Player 1 rolls 2 dice and gets outcomes [4, 6].
          End scores = (26, 34)
          >>> print(turns[2])
          Start scores = (26, 34).
          Player 0 rolls 7 dice and gets outcomes [5, 5, 3, 6, 2, 6, 3].
          End scores = (56, 34)
          >>> print(turns[3])
          Start scores = (56, 34).
          Player 1 rolls 4 dice and gets outcomes [4, 6, 4, 3].
          End scores = (56, 51)
          >>> print(turns[4])
          Start scores = (56, 51).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (58, 51)
          >>> print(turns[5])
          Start scores = (58, 51).
          Player 1 rolls 9 dice and gets outcomes [5, 6, 2, 1, 5, 5, 5, 1, 3].
          End scores = (58, 52)
          >>> print(turns[6])
          Start scores = (58, 52).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 2, 6, 3, 5, 5, 6, 3, 2].
          End scores = (61, 52)
          >>> print(turns[7])
          Start scores = (61, 52).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 1, 4, 2, 5, 1].
          End scores = (61, 59)
          >>> print(turns[8])
          Start scores = (61, 59).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 6, 5, 1, 4, 2, 4].
          End scores = (62, 59)
          >>> print(turns[9])
          Start scores = (62, 59).
          Player 1 rolls 7 dice and gets outcomes [2, 1, 3, 5, 2, 5, 6].
          End scores = (62, 60)
          >>> print(turns[10])
          Start scores = (62, 60).
          Player 0 rolls 2 dice and gets outcomes [5, 5].
          End scores = (72, 60)
          >>> print(turns[11])
          Start scores = (72, 60).
          Player 1 rolls 3 dice and gets outcomes [5, 6, 1].
          End scores = (72, 67)
          >>> print(turns[12])
          Start scores = (72, 67).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 5, 4, 6, 6, 4, 2, 2, 2].
          End scores = (79, 67)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=31018, score0=55, score1=8, goal=66)
          >>> print(turns[0])
          Start scores = (55, 8).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 1, 5, 1, 6, 5, 4, 3].
          End scores = (56, 8)
          >>> print(turns[1])
          Start scores = (56, 8).
          Player 1 rolls 8 dice and gets outcomes [4, 4, 5, 6, 1, 2, 5, 2].
          End scores = (56, 9)
          >>> print(turns[2])
          Start scores = (56, 9).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 6, 6, 4, 5].
          End scores = (57, 9)
          >>> print(turns[3])
          Start scores = (57, 9).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (57, 10)
          >>> print(turns[4])
          Start scores = (57, 10).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 6, 2, 5, 2, 3, 3, 1, 5].
          End scores = (58, 10)
          >>> print(turns[5])
          Start scores = (58, 10).
          Player 1 rolls 4 dice and gets outcomes [3, 2, 3, 5].
          End scores = (58, 29)
          >>> print(turns[6])
          Start scores = (58, 29).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (60, 29)
          >>> print(turns[7])
          Start scores = (60, 29).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 6, 5, 6, 4, 3, 3].
          End scores = (60, 65)
          >>> print(turns[8])
          Start scores = (60, 65).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 6, 6].
          End scores = (67, 65)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15439, score0=21, score1=52, goal=74)
          >>> print(turns[0])
          Start scores = (21, 52).
          Player 0 rolls 5 dice and gets outcomes [5, 2, 5, 3, 6].
          End scores = (42, 52)
          >>> print(turns[1])
          Start scores = (42, 52).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 6, 2, 4].
          End scores = (42, 76)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=58596, score0=37, score1=12, goal=81)
          >>> print(turns[0])
          Start scores = (37, 12).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 4, 4, 2].
          End scores = (38, 12)
          >>> print(turns[1])
          Start scores = (38, 12).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 5, 1, 1, 5, 1].
          End scores = (38, 17)
          >>> print(turns[2])
          Start scores = (38, 17).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 3, 6, 3, 4].
          End scores = (39, 17)
          >>> print(turns[3])
          Start scores = (39, 17).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 2].
          End scores = (39, 31)
          >>> print(turns[4])
          Start scores = (39, 31).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 5, 2, 1, 2, 1, 1].
          End scores = (40, 31)
          >>> print(turns[5])
          Start scores = (40, 31).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 1, 4, 4].
          End scores = (40, 32)
          >>> print(turns[6])
          Start scores = (40, 32).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 5, 2, 5, 1, 6].
          End scores = (43, 32)
          >>> print(turns[7])
          Start scores = (43, 32).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 5, 1, 6, 1, 5, 5, 6].
          End scores = (43, 33)
          >>> print(turns[8])
          Start scores = (43, 33).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 1, 4, 2].
          End scores = (44, 33)
          >>> print(turns[9])
          Start scores = (44, 33).
          Player 1 rolls 5 dice and gets outcomes [5, 2, 2, 2, 5].
          End scores = (44, 49)
          >>> print(turns[10])
          Start scores = (44, 49).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 5, 2, 2, 4, 4].
          End scores = (69, 49)
          >>> print(turns[11])
          Start scores = (69, 49).
          Player 1 rolls 4 dice and gets outcomes [6, 5, 4, 5].
          End scores = (69, 69)
          >>> print(turns[12])
          Start scores = (69, 69).
          Player 0 rolls 4 dice and gets outcomes [6, 4, 3, 2].
          End scores = (84, 69)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13350, score0=20, score1=6, goal=42)
          >>> print(turns[0])
          Start scores = (20, 6).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 4, 6, 3, 5, 3, 6, 1].
          End scores = (21, 6)
          >>> print(turns[1])
          Start scores = (21, 6).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (21, 9)
          >>> print(turns[2])
          Start scores = (21, 9).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (22, 9)
          >>> print(turns[3])
          Start scores = (22, 9).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (22, 10)
          >>> print(turns[4])
          Start scores = (22, 10).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 4, 5, 6, 2, 6, 6].
          End scores = (61, 10)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=45128, score0=45, score1=30, goal=46)
          >>> print(turns[0])
          Start scores = (45, 30).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 4, 5, 1, 3].
          End scores = (46, 30)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55284, score0=72, score1=18, goal=75)
          >>> print(turns[0])
          Start scores = (72, 18).
          Player 0 rolls 9 dice and gets outcomes [1, 4, 6, 4, 4, 3, 5, 1, 5].
          End scores = (79, 18)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=47323, score0=23, score1=6, goal=92)
          >>> print(turns[0])
          Start scores = (23, 6).
          Player 0 rolls 2 dice and gets outcomes [4, 1].
          End scores = (24, 6)
          >>> print(turns[1])
          Start scores = (24, 6).
          Player 1 rolls 6 dice and gets outcomes [4, 1, 6, 2, 5, 4].
          End scores = (24, 11)
          >>> print(turns[2])
          Start scores = (24, 11).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (34, 11)
          >>> print(turns[3])
          Start scores = (34, 11).
          Player 1 rolls 8 dice and gets outcomes [2, 4, 5, 4, 3, 4, 2, 5].
          End scores = (34, 40)
          >>> print(turns[4])
          Start scores = (34, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (42, 40)
          >>> print(turns[5])
          Start scores = (42, 40).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 6, 2, 4, 6, 2, 6].
          End scores = (42, 77)
          >>> print(turns[6])
          Start scores = (42, 77).
          Player 0 rolls 10 dice and gets outcomes [2, 1, 1, 2, 5, 4, 3, 1, 4, 1].
          End scores = (47, 77)
          >>> print(turns[7])
          Start scores = (47, 77).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (47, 78)
          >>> print(turns[8])
          Start scores = (47, 78).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 6, 4, 4, 2, 6, 5, 6, 1].
          End scores = (48, 78)
          >>> print(turns[9])
          Start scores = (48, 78).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 6, 1, 1].
          End scores = (48, 83)
          >>> print(turns[10])
          Start scores = (48, 83).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 3, 1].
          End scores = (49, 83)
          >>> print(turns[11])
          Start scores = (49, 83).
          Player 1 rolls 9 dice and gets outcomes [5, 5, 5, 1, 4, 1, 2, 5, 3].
          End scores = (49, 84)
          >>> print(turns[12])
          Start scores = (49, 84).
          Player 0 rolls 5 dice and gets outcomes [5, 3, 1, 5, 2].
          End scores = (50, 84)
          >>> print(turns[13])
          Start scores = (50, 84).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 4, 6, 1, 2].
          End scores = (50, 85)
          >>> print(turns[14])
          Start scores = (50, 85).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 6, 3, 4, 1, 6, 1, 2, 2].
          End scores = (51, 85)
          >>> print(turns[15])
          Start scores = (51, 85).
          Player 1 rolls 3 dice and gets outcomes [3, 1, 4].
          End scores = (51, 86)
          >>> print(turns[16])
          Start scores = (51, 86).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 3, 4, 6, 4, 5, 3, 5].
          End scores = (87, 86)
          >>> print(turns[17])
          Start scores = (87, 86).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 3, 1, 3, 3, 4, 1].
          End scores = (87, 87)
          >>> print(turns[18])
          Start scores = (87, 87).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 1].
          End scores = (88, 87)
          >>> print(turns[19])
          Start scores = (88, 87).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 3, 6, 4, 1, 3].
          End scores = (88, 88)
          >>> print(turns[20])
          Start scores = (88, 88).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (91, 88)
          >>> print(turns[21])
          Start scores = (91, 88).
          Player 1 rolls 4 dice and gets outcomes [6, 5, 3, 2].
          End scores = (91, 104)
          >>> print(turns[22])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43231, score0=12, score1=79, goal=89)
          >>> print(turns[0])
          Start scores = (12, 79).
          Player 0 rolls 6 dice and gets outcomes [3, 1, 3, 1, 4, 3].
          End scores = (17, 79)
          >>> print(turns[1])
          Start scores = (17, 79).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (17, 90)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27065, score0=2, score1=0, goal=12)
          >>> print(turns[0])
          Start scores = (2, 0).
          Player 0 rolls 5 dice and gets outcomes [5, 2, 2, 1, 3].
          End scores = (5, 0)
          >>> print(turns[1])
          Start scores = (5, 0).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 4, 5, 2, 2, 4].
          End scores = (5, 2)
          >>> print(turns[2])
          Start scores = (5, 2).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 1, 1, 5].
          End scores = (6, 2)
          >>> print(turns[3])
          Start scores = (6, 2).
          Player 1 rolls 5 dice and gets outcomes [1, 1, 3, 3, 3].
          End scores = (6, 5)
          >>> print(turns[4])
          Start scores = (6, 5).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (13, 5)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=37376, score0=71, score1=22, goal=97)
          >>> print(turns[0])
          Start scores = (71, 22).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 1, 2, 5].
          End scores = (72, 22)
          >>> print(turns[1])
          Start scores = (72, 22).
          Player 1 rolls 3 dice and gets outcomes [3, 6, 6].
          End scores = (72, 41)
          >>> print(turns[2])
          Start scores = (72, 41).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (78, 41)
          >>> print(turns[3])
          Start scores = (78, 41).
          Player 1 rolls 8 dice and gets outcomes [2, 5, 3, 2, 2, 2, 5, 4].
          End scores = (78, 66)
          >>> print(turns[4])
          Start scores = (78, 66).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (86, 66)
          >>> print(turns[5])
          Start scores = (86, 66).
          Player 1 rolls 10 dice and gets outcomes [3, 5, 1, 5, 6, 3, 1, 1, 1, 6].
          End scores = (86, 71)
          >>> print(turns[6])
          Start scores = (86, 71).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 2, 5, 6, 2, 2, 3, 3, 6].
          End scores = (121, 71)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55147, score0=13, score1=2, goal=17)
          >>> print(turns[0])
          Start scores = (13, 2).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 3, 5].
          End scores = (31, 2)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66508, score0=38, score1=25, goal=97)
          >>> print(turns[0])
          Start scores = (38, 25).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (44, 25)
          >>> print(turns[1])
          Start scores = (44, 25).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 3].
          End scores = (44, 38)
          >>> print(turns[2])
          Start scores = (44, 38).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (45, 38)
          >>> print(turns[3])
          Start scores = (45, 38).
          Player 1 rolls 10 dice and gets outcomes [1, 5, 3, 4, 2, 4, 3, 1, 6, 2].
          End scores = (45, 39)
          >>> print(turns[4])
          Start scores = (45, 39).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 2].
          End scores = (56, 39)
          >>> print(turns[5])
          Start scores = (56, 39).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 3, 3, 6, 1, 6, 6, 6, 1].
          End scores = (56, 40)
          >>> print(turns[6])
          Start scores = (56, 40).
          Player 0 rolls 5 dice and gets outcomes [1, 2, 2, 2, 3].
          End scores = (57, 40)
          >>> print(turns[7])
          Start scores = (57, 40).
          Player 1 rolls 5 dice and gets outcomes [6, 4, 5, 3, 2].
          End scores = (57, 60)
          >>> print(turns[8])
          Start scores = (57, 60).
          Player 0 rolls 6 dice and gets outcomes [3, 1, 3, 5, 3, 2].
          End scores = (58, 60)
          >>> print(turns[9])
          Start scores = (58, 60).
          Player 1 rolls 10 dice and gets outcomes [6, 3, 6, 3, 1, 4, 3, 4, 3, 4].
          End scores = (58, 67)
          >>> print(turns[10])
          Start scores = (58, 67).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (60, 67)
          >>> print(turns[11])
          Start scores = (60, 67).
          Player 1 rolls 4 dice and gets outcomes [6, 1, 3, 2].
          End scores = (60, 68)
          >>> print(turns[12])
          Start scores = (60, 68).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (68, 68)
          >>> print(turns[13])
          Start scores = (68, 68).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (68, 72)
          >>> print(turns[14])
          Start scores = (68, 72).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 6, 1, 4].
          End scores = (69, 72)
          >>> print(turns[15])
          Start scores = (69, 72).
          Player 1 rolls 8 dice and gets outcomes [4, 2, 5, 6, 6, 3, 1, 4].
          End scores = (69, 79)
          >>> print(turns[16])
          Start scores = (69, 79).
          Player 0 rolls 2 dice and gets outcomes [1, 3].
          End scores = (70, 79)
          >>> print(turns[17])
          Start scores = (70, 79).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 5].
          End scores = (70, 91)
          >>> print(turns[18])
          Start scores = (70, 91).
          Player 0 rolls 5 dice and gets outcomes [1, 2, 1, 5, 6].
          End scores = (73, 91)
          >>> print(turns[19])
          Start scores = (73, 91).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 3, 2, 3].
          End scores = (73, 109)
          >>> print(turns[20])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=7672, score0=2, score1=5, goal=11)
          >>> print(turns[0])
          Start scores = (2, 5).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 2, 5].
          End scores = (5, 5)
          >>> print(turns[1])
          Start scores = (5, 5).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (5, 9)
          >>> print(turns[2])
          Start scores = (5, 9).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 4, 4].
          End scores = (22, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=12310, score0=17, score1=25, goal=47)
          >>> print(turns[0])
          Start scores = (17, 25).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (18, 25)
          >>> print(turns[1])
          Start scores = (18, 25).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (18, 35)
          >>> print(turns[2])
          Start scores = (18, 35).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 2, 1, 1, 6, 5, 5, 5, 6].
          End scores = (23, 35)
          >>> print(turns[3])
          Start scores = (23, 35).
          Player 1 rolls 3 dice and gets outcomes [3, 4, 5].
          End scores = (23, 53)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=31574, score0=3, score1=29, goal=51)
          >>> print(turns[0])
          Start scores = (3, 29).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 1, 2, 5, 2, 5, 1, 3].
          End scores = (4, 29)
          >>> print(turns[1])
          Start scores = (4, 29).
          Player 1 rolls 4 dice and gets outcomes [1, 4, 3, 6].
          End scores = (4, 30)
          >>> print(turns[2])
          Start scores = (4, 30).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (10, 30)
          >>> print(turns[3])
          Start scores = (10, 30).
          Player 1 rolls 10 dice and gets outcomes [2, 3, 2, 1, 1, 2, 3, 5, 3, 2].
          End scores = (10, 37)
          >>> print(turns[4])
          Start scores = (10, 37).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (17, 37)
          >>> print(turns[5])
          Start scores = (17, 37).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 4, 2, 6].
          End scores = (17, 38)
          >>> print(turns[6])
          Start scores = (17, 38).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (25, 38)
          >>> print(turns[7])
          Start scores = (25, 38).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 1, 5, 6, 5, 5, 2, 4, 5].
          End scores = (25, 39)
          >>> print(turns[8])
          Start scores = (25, 39).
          Player 0 rolls 4 dice and gets outcomes [1, 2, 2, 4].
          End scores = (26, 39)
          >>> print(turns[9])
          Start scores = (26, 39).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (26, 45)
          >>> print(turns[10])
          Start scores = (26, 45).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 3].
          End scores = (38, 45)
          >>> print(turns[11])
          Start scores = (38, 45).
          Player 1 rolls 5 dice and gets outcomes [2, 1, 3, 1, 1].
          End scores = (38, 46)
          >>> print(turns[12])
          Start scores = (38, 46).
          Player 0 rolls 10 dice and gets outcomes [4, 4, 6, 3, 2, 1, 2, 5, 4, 5].
          End scores = (39, 46)
          >>> print(turns[13])
          Start scores = (39, 46).
          Player 1 rolls 8 dice and gets outcomes [4, 5, 6, 1, 3, 5, 4, 6].
          End scores = (39, 53)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=92652, score0=8, score1=45, goal=67)
          >>> print(turns[0])
          Start scores = (8, 45).
          Player 0 rolls 9 dice and gets outcomes [5, 2, 4, 2, 5, 5, 1, 6, 1].
          End scores = (9, 45)
          >>> print(turns[1])
          Start scores = (9, 45).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (9, 46)
          >>> print(turns[2])
          Start scores = (9, 46).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 2, 2, 1].
          End scores = (10, 46)
          >>> print(turns[3])
          Start scores = (10, 46).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 2, 2, 4, 4, 5, 6, 3, 5].
          End scores = (10, 53)
          >>> print(turns[4])
          Start scores = (10, 53).
          Player 0 rolls 10 dice and gets outcomes [6, 3, 4, 1, 2, 2, 4, 1, 3, 4].
          End scores = (13, 53)
          >>> print(turns[5])
          Start scores = (13, 53).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (13, 57)
          >>> print(turns[6])
          Start scores = (13, 57).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 2, 3, 5, 6, 4, 4, 4, 6].
          End scores = (59, 57)
          >>> print(turns[7])
          Start scores = (59, 57).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (59, 58)
          >>> print(turns[8])
          Start scores = (59, 58).
          Player 0 rolls 7 dice and gets outcomes [5, 6, 2, 4, 6, 2, 3].
          End scores = (87, 58)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55979, score0=75, score1=80, goal=95)
          >>> print(turns[0])
          Start scores = (75, 80).
          Player 0 rolls 4 dice and gets outcomes [4, 1, 6, 4].
          End scores = (76, 80)
          >>> print(turns[1])
          Start scores = (76, 80).
          Player 1 rolls 4 dice and gets outcomes [3, 1, 1, 3].
          End scores = (76, 81)
          >>> print(turns[2])
          Start scores = (76, 81).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 6].
          End scores = (97, 81)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93729, score0=37, score1=63, goal=83)
          >>> print(turns[0])
          Start scores = (37, 63).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 1, 4, 5, 5, 1, 5].
          End scores = (38, 63)
          >>> print(turns[1])
          Start scores = (38, 63).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 1, 3, 3, 5].
          End scores = (38, 64)
          >>> print(turns[2])
          Start scores = (38, 64).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 6, 5, 3, 3, 3, 3].
          End scores = (71, 64)
          >>> print(turns[3])
          Start scores = (71, 64).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (71, 77)
          >>> print(turns[4])
          Start scores = (71, 77).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (78, 77)
          >>> print(turns[5])
          Start scores = (78, 77).
          Player 1 rolls 8 dice and gets outcomes [5, 3, 2, 5, 6, 3, 6, 2].
          End scores = (78, 113)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61722, score0=54, score1=50, goal=58)
          >>> print(turns[0])
          Start scores = (54, 50).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 4, 5, 4, 4, 3, 5].
          End scores = (87, 50)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=35391, score0=21, score1=1, goal=55)
          >>> print(turns[0])
          Start scores = (21, 1).
          Player 0 rolls 10 dice and gets outcomes [5, 5, 4, 3, 2, 3, 5, 6, 6, 2].
          End scores = (62, 1)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50232, score0=1, score1=44, goal=73)
          >>> print(turns[0])
          Start scores = (1, 44).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 3, 2, 5, 3, 1, 5].
          End scores = (3, 44)
          >>> print(turns[1])
          Start scores = (3, 44).
          Player 1 rolls 10 dice and gets outcomes [1, 5, 1, 5, 6, 5, 5, 1, 2, 5].
          End scores = (3, 45)
          >>> print(turns[2])
          Start scores = (3, 45).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 2, 2, 4, 5, 4, 2, 5, 5].
          End scores = (4, 45)
          >>> print(turns[3])
          Start scores = (4, 45).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 4].
          End scores = (4, 46)
          >>> print(turns[4])
          Start scores = (4, 46).
          Player 0 rolls 2 dice and gets outcomes [6, 4].
          End scores = (14, 46)
          >>> print(turns[5])
          Start scores = (14, 46).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 3, 2, 5].
          End scores = (14, 64)
          >>> print(turns[6])
          Start scores = (14, 64).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (15, 64)
          >>> print(turns[7])
          Start scores = (15, 64).
          Player 1 rolls 5 dice and gets outcomes [2, 1, 5, 6, 3].
          End scores = (15, 65)
          >>> print(turns[8])
          Start scores = (15, 65).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 6, 1].
          End scores = (16, 65)
          >>> print(turns[9])
          Start scores = (16, 65).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (16, 74)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55351, score0=33, score1=18, goal=69)
          >>> print(turns[0])
          Start scores = (33, 18).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 1, 2, 3, 5, 1].
          End scores = (34, 18)
          >>> print(turns[1])
          Start scores = (34, 18).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 2, 2, 2, 2, 2, 5, 6, 2].
          End scores = (34, 49)
          >>> print(turns[2])
          Start scores = (34, 49).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (36, 49)
          >>> print(turns[3])
          Start scores = (36, 49).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (36, 54)
          >>> print(turns[4])
          Start scores = (36, 54).
          Player 0 rolls 7 dice and gets outcomes [3, 1, 1, 5, 2, 2, 6].
          End scores = (41, 54)
          >>> print(turns[5])
          Start scores = (41, 54).
          Player 1 rolls 2 dice and gets outcomes [5, 6].
          End scores = (41, 65)
          >>> print(turns[6])
          Start scores = (41, 65).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 4, 2, 3, 6, 1, 1, 2].
          End scores = (42, 65)
          >>> print(turns[7])
          Start scores = (42, 65).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (42, 71)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99532, score0=50, score1=2, goal=56)
          >>> print(turns[0])
          Start scores = (50, 2).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 3, 5, 6, 4, 1, 4, 2].
          End scores = (51, 2)
          >>> print(turns[1])
          Start scores = (51, 2).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 1].
          End scores = (51, 5)
          >>> print(turns[2])
          Start scores = (51, 5).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 6, 4, 5, 6, 4, 6].
          End scores = (97, 5)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=39271, score0=11, score1=5, goal=33)
          >>> print(turns[0])
          Start scores = (11, 5).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 2, 3, 5, 4, 3, 1].
          End scores = (12, 5)
          >>> print(turns[1])
          Start scores = (12, 5).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 4, 1, 6, 6].
          End scores = (12, 6)
          >>> print(turns[2])
          Start scores = (12, 6).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 1, 1, 2, 4, 3, 5, 6, 2].
          End scores = (17, 6)
          >>> print(turns[3])
          Start scores = (17, 6).
          Player 1 rolls 2 dice and gets outcomes [4, 2].
          End scores = (17, 12)
          >>> print(turns[4])
          Start scores = (17, 12).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (29, 12)
          >>> print(turns[5])
          Start scores = (29, 12).
          Player 1 rolls 2 dice and gets outcomes [1, 5].
          End scores = (29, 17)
          >>> print(turns[6])
          Start scores = (29, 17).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (40, 17)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=87563, score0=63, score1=55, goal=90)
          >>> print(turns[0])
          Start scores = (63, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (68, 55)
          >>> print(turns[1])
          Start scores = (68, 55).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 4, 2, 4].
          End scores = (68, 75)
          >>> print(turns[2])
          Start scores = (68, 75).
          Player 0 rolls 6 dice and gets outcomes [6, 2, 5, 6, 6, 6].
          End scores = (99, 75)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=46403, score0=9, score1=12, goal=13)
          >>> print(turns[0])
          Start scores = (9, 12).
          Player 0 rolls 9 dice and gets outcomes [4, 6, 3, 2, 3, 2, 6, 4, 1].
          End scores = (10, 12)
          >>> print(turns[1])
          Start scores = (10, 12).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 6, 3, 4, 3, 3].
          End scores = (10, 17)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=77217, score0=2, score1=39, goal=83)
          >>> print(turns[0])
          Start scores = (2, 39).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 6].
          End scores = (18, 39)
          >>> print(turns[1])
          Start scores = (18, 39).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 5, 1, 2, 3, 3, 5, 6, 3].
          End scores = (18, 40)
          >>> print(turns[2])
          Start scores = (18, 40).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 6, 3, 3, 2, 2, 5, 5].
          End scores = (59, 40)
          >>> print(turns[3])
          Start scores = (59, 40).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (59, 44)
          >>> print(turns[4])
          Start scores = (59, 44).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 4, 6, 6, 6, 1, 1, 6].
          End scores = (60, 44)
          >>> print(turns[5])
          Start scores = (60, 44).
          Player 1 rolls 4 dice and gets outcomes [6, 5, 3, 3].
          End scores = (60, 67)
          >>> print(turns[6])
          Start scores = (60, 67).
          Player 0 rolls 3 dice and gets outcomes [5, 1, 5].
          End scores = (67, 67)
          >>> print(turns[7])
          Start scores = (67, 67).
          Player 1 rolls 8 dice and gets outcomes [2, 5, 1, 1, 4, 1, 4, 5].
          End scores = (67, 68)
          >>> print(turns[8])
          Start scores = (67, 68).
          Player 0 rolls 6 dice and gets outcomes [6, 3, 5, 4, 5, 6].
          End scores = (96, 68)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=48064, score0=1, score1=1, goal=15)
          >>> print(turns[0])
          Start scores = (1, 1).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 3, 4, 6].
          End scores = (22, 1)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=81605, score0=73, score1=74, goal=91)
          >>> print(turns[0])
          Start scores = (73, 74).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (77, 74)
          >>> print(turns[1])
          Start scores = (77, 74).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (77, 81)
          >>> print(turns[2])
          Start scores = (77, 81).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 5, 2, 6, 5, 6, 2].
          End scores = (110, 81)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25561, score0=69, score1=44, goal=89)
          >>> print(turns[0])
          Start scores = (69, 44).
          Player 0 rolls 4 dice and gets outcomes [5, 6, 3, 1].
          End scores = (70, 44)
          >>> print(turns[1])
          Start scores = (70, 44).
          Player 1 rolls 3 dice and gets outcomes [3, 4, 1].
          End scores = (70, 45)
          >>> print(turns[2])
          Start scores = (70, 45).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 3, 4, 5, 1, 3, 1, 3].
          End scores = (73, 45)
          >>> print(turns[3])
          Start scores = (73, 45).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (73, 56)
          >>> print(turns[4])
          Start scores = (73, 56).
          Player 0 rolls 5 dice and gets outcomes [4, 2, 6, 4, 4].
          End scores = (93, 56)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=62937, score0=3, score1=0, goal=14)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 2, 4, 5].
          End scores = (4, 0)
          >>> print(turns[1])
          Start scores = (4, 0).
          Player 1 rolls 9 dice and gets outcomes [4, 1, 3, 4, 2, 5, 5, 2, 2].
          End scores = (4, 2)
          >>> print(turns[2])
          Start scores = (4, 2).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 2, 6, 3, 1].
          End scores = (7, 2)
          >>> print(turns[3])
          Start scores = (7, 2).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (7, 11)
          >>> print(turns[4])
          Start scores = (7, 11).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (19, 11)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=34690, score0=27, score1=58, goal=90)
          >>> print(turns[0])
          Start scores = (27, 58).
          Player 0 rolls 6 dice and gets outcomes [5, 5, 5, 5, 5, 1].
          End scores = (28, 58)
          >>> print(turns[1])
          Start scores = (28, 58).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (28, 66)
          >>> print(turns[2])
          Start scores = (28, 66).
          Player 0 rolls 4 dice and gets outcomes [3, 5, 5, 4].
          End scores = (45, 66)
          >>> print(turns[3])
          Start scores = (45, 66).
          Player 1 rolls 8 dice and gets outcomes [5, 3, 1, 4, 5, 1, 1, 4].
          End scores = (45, 71)
          >>> print(turns[4])
          Start scores = (45, 71).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 5, 3, 1, 4].
          End scores = (46, 71)
          >>> print(turns[5])
          Start scores = (46, 71).
          Player 1 rolls 9 dice and gets outcomes [3, 5, 5, 1, 4, 5, 2, 4, 3].
          End scores = (46, 72)
          >>> print(turns[6])
          Start scores = (46, 72).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 3].
          End scores = (60, 72)
          >>> print(turns[7])
          Start scores = (60, 72).
          Player 1 rolls 9 dice and gets outcomes [6, 3, 6, 4, 3, 6, 6, 2, 4].
          End scores = (60, 112)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=70454, score0=18, score1=35, goal=56)
          >>> print(turns[0])
          Start scores = (18, 35).
          Player 0 rolls 10 dice and gets outcomes [5, 3, 2, 5, 4, 6, 1, 4, 5, 5].
          End scores = (23, 35)
          >>> print(turns[1])
          Start scores = (23, 35).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 3, 5, 2, 2, 6].
          End scores = (23, 36)
          >>> print(turns[2])
          Start scores = (23, 36).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (24, 36)
          >>> print(turns[3])
          Start scores = (24, 36).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 3, 2].
          End scores = (24, 51)
          >>> print(turns[4])
          Start scores = (24, 51).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (25, 51)
          >>> print(turns[5])
          Start scores = (25, 51).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (25, 57)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95632, score0=9, score1=18, goal=35)
          >>> print(turns[0])
          Start scores = (9, 18).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (10, 18)
          >>> print(turns[1])
          Start scores = (10, 18).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 3, 3, 3, 1, 4, 4, 1, 2].
          End scores = (10, 23)
          >>> print(turns[2])
          Start scores = (10, 23).
          Player 0 rolls 2 dice and gets outcomes [3, 1].
          End scores = (13, 23)
          >>> print(turns[3])
          Start scores = (13, 23).
          Player 1 rolls 8 dice and gets outcomes [5, 1, 3, 2, 5, 2, 5, 5].
          End scores = (13, 24)
          >>> print(turns[4])
          Start scores = (13, 24).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 3].
          End scores = (14, 24)
          >>> print(turns[5])
          Start scores = (14, 24).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 4, 6, 1, 5, 1, 3, 6].
          End scores = (14, 25)
          >>> print(turns[6])
          Start scores = (14, 25).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 1, 2, 3].
          End scores = (15, 25)
          >>> print(turns[7])
          Start scores = (15, 25).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (15, 26)
          >>> print(turns[8])
          Start scores = (15, 26).
          Player 0 rolls 5 dice and gets outcomes [5, 3, 1, 3, 4].
          End scores = (16, 26)
          >>> print(turns[9])
          Start scores = (16, 26).
          Player 1 rolls 5 dice and gets outcomes [2, 2, 2, 3, 1].
          End scores = (16, 27)
          >>> print(turns[10])
          Start scores = (16, 27).
          Player 0 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (19, 27)
          >>> print(turns[11])
          Start scores = (19, 27).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 1, 6, 1].
          End scores = (19, 28)
          >>> print(turns[12])
          Start scores = (19, 28).
          Player 0 rolls 10 dice and gets outcomes [5, 5, 1, 6, 2, 1, 1, 4, 4, 1].
          End scores = (20, 28)
          >>> print(turns[13])
          Start scores = (20, 28).
          Player 1 rolls 2 dice and gets outcomes [3, 1].
          End scores = (20, 31)
          >>> print(turns[14])
          Start scores = (20, 31).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 3].
          End scores = (21, 31)
          >>> print(turns[15])
          Start scores = (21, 31).
          Player 1 rolls 4 dice and gets outcomes [4, 6, 2, 1].
          End scores = (21, 32)
          >>> print(turns[16])
          Start scores = (21, 32).
          Player 0 rolls 7 dice and gets outcomes [2, 1, 3, 1, 4, 2, 3].
          End scores = (22, 32)
          >>> print(turns[17])
          Start scores = (22, 32).
          Player 1 rolls 9 dice and gets outcomes [1, 2, 1, 1, 4, 3, 5, 5, 6].
          End scores = (22, 33)
          >>> print(turns[18])
          Start scores = (22, 33).
          Player 0 rolls 10 dice and gets outcomes [1, 3, 3, 3, 6, 1, 2, 3, 6, 5].
          End scores = (29, 33)
          >>> print(turns[19])
          Start scores = (29, 33).
          Player 1 rolls 10 dice and gets outcomes [5, 1, 4, 3, 1, 6, 5, 1, 3, 4].
          End scores = (29, 34)
          >>> print(turns[20])
          Start scores = (29, 34).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 2, 1].
          End scores = (30, 34)
          >>> print(turns[21])
          Start scores = (30, 34).
          Player 1 rolls 6 dice and gets outcomes [3, 3, 3, 4, 6, 4].
          End scores = (30, 57)
          >>> print(turns[22])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=32647, score0=3, score1=10, goal=22)
          >>> print(turns[0])
          Start scores = (3, 10).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (6, 10)
          >>> print(turns[1])
          Start scores = (6, 10).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 4, 5, 6, 4].
          End scores = (6, 39)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20029, score0=14, score1=44, goal=46)
          >>> print(turns[0])
          Start scores = (14, 44).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (25, 44)
          >>> print(turns[1])
          Start scores = (25, 44).
          Player 1 rolls 3 dice and gets outcomes [4, 2, 6].
          End scores = (25, 56)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66970, score0=30, score1=22, goal=34)
          >>> print(turns[0])
          Start scores = (30, 22).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 4, 1, 2, 3, 6, 3, 4, 3].
          End scores = (37, 22)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=38907, score0=84, score1=25, goal=92)
          >>> print(turns[0])
          Start scores = (84, 25).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 4, 2, 3, 6, 4].
          End scores = (85, 25)
          >>> print(turns[1])
          Start scores = (85, 25).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (85, 36)
          >>> print(turns[2])
          Start scores = (85, 36).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 2, 4, 1].
          End scores = (86, 36)
          >>> print(turns[3])
          Start scores = (86, 36).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 6, 1, 3, 1, 4, 6, 4].
          End scores = (86, 41)
          >>> print(turns[4])
          Start scores = (86, 41).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 5, 5, 5, 6].
          End scores = (127, 41)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1044, score0=76, score1=58, goal=91)
          >>> print(turns[0])
          Start scores = (76, 58).
          Player 0 rolls 7 dice and gets outcomes [5, 5, 1, 4, 5, 2, 2].
          End scores = (77, 58)
          >>> print(turns[1])
          Start scores = (77, 58).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 4, 5, 3, 4, 1, 1, 5, 2].
          End scores = (77, 61)
          >>> print(turns[2])
          Start scores = (77, 61).
          Player 0 rolls 3 dice and gets outcomes [4, 5, 5].
          End scores = (91, 61)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27882, score0=44, score1=6, goal=85)
          >>> print(turns[0])
          Start scores = (44, 6).
          Player 0 rolls 9 dice and gets outcomes [5, 2, 2, 5, 4, 3, 1, 3, 6].
          End scores = (45, 6)
          >>> print(turns[1])
          Start scores = (45, 6).
          Player 1 rolls 7 dice and gets outcomes [1, 6, 6, 1, 6, 4, 5].
          End scores = (45, 11)
          >>> print(turns[2])
          Start scores = (45, 11).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 1, 2, 1, 5, 6, 2].
          End scores = (46, 11)
          >>> print(turns[3])
          Start scores = (46, 11).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 4, 5].
          End scores = (46, 30)
          >>> print(turns[4])
          Start scores = (46, 30).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (53, 30)
          >>> print(turns[5])
          Start scores = (53, 30).
          Player 1 rolls 7 dice and gets outcomes [4, 1, 5, 2, 3, 4, 4].
          End scores = (53, 37)
          >>> print(turns[6])
          Start scores = (53, 37).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 2, 5].
          End scores = (70, 37)
          >>> print(turns[7])
          Start scores = (70, 37).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (70, 42)
          >>> print(turns[8])
          Start scores = (70, 42).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (72, 42)
          >>> print(turns[9])
          Start scores = (72, 42).
          Player 1 rolls 9 dice and gets outcomes [3, 5, 5, 1, 1, 2, 6, 2, 3].
          End scores = (72, 47)
          >>> print(turns[10])
          Start scores = (72, 47).
          Player 0 rolls 3 dice and gets outcomes [4, 3, 1].
          End scores = (79, 47)
          >>> print(turns[11])
          Start scores = (79, 47).
          Player 1 rolls 3 dice and gets outcomes [1, 6, 2].
          End scores = (79, 48)
          >>> print(turns[12])
          Start scores = (79, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 2].
          End scores = (92, 48)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61003, score0=31, score1=81, goal=100)
          >>> print(turns[0])
          Start scores = (31, 81).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 2, 4, 1, 3, 4].
          End scores = (32, 81)
          >>> print(turns[1])
          Start scores = (32, 81).
          Player 1 rolls 7 dice and gets outcomes [4, 1, 5, 4, 3, 6, 5].
          End scores = (32, 82)
          >>> print(turns[2])
          Start scores = (32, 82).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 1, 5, 6, 3, 1, 5].
          End scores = (33, 82)
          >>> print(turns[3])
          Start scores = (33, 82).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 4, 5, 3, 3, 5, 2, 2].
          End scores = (33, 112)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=26543, score0=4, score1=10, goal=37)
          >>> print(turns[0])
          Start scores = (4, 10).
          Player 0 rolls 7 dice and gets outcomes [6, 3, 2, 5, 1, 4, 5].
          End scores = (7, 10)
          >>> print(turns[1])
          Start scores = (7, 10).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 2, 5, 6, 1, 5].
          End scores = (7, 13)
          >>> print(turns[2])
          Start scores = (7, 13).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 3, 1, 4, 6, 5].
          End scores = (8, 13)
          >>> print(turns[3])
          Start scores = (8, 13).
          Player 1 rolls 6 dice and gets outcomes [3, 3, 5, 6, 5, 6].
          End scores = (8, 43)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95363, score0=7, score1=91, goal=96)
          >>> print(turns[0])
          Start scores = (7, 91).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 5].
          End scores = (16, 91)
          >>> print(turns[1])
          Start scores = (16, 91).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 3, 2, 5].
          End scores = (16, 113)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15378, score0=39, score1=1, goal=65)
          >>> print(turns[0])
          Start scores = (39, 1).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 1)
          >>> print(turns[1])
          Start scores = (40, 1).
          Player 1 rolls 5 dice and gets outcomes [4, 3, 6, 4, 3].
          End scores = (40, 21)
          >>> print(turns[2])
          Start scores = (40, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (44, 21)
          >>> print(turns[3])
          Start scores = (44, 21).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (44, 25)
          >>> print(turns[4])
          Start scores = (44, 25).
          Player 0 rolls 3 dice and gets outcomes [1, 2, 4].
          End scores = (45, 25)
          >>> print(turns[5])
          Start scores = (45, 25).
          Player 1 rolls 2 dice and gets outcomes [4, 1].
          End scores = (45, 26)
          >>> print(turns[6])
          Start scores = (45, 26).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (51, 26)
          >>> print(turns[7])
          Start scores = (51, 26).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 1, 4, 6].
          End scores = (51, 27)
          >>> print(turns[8])
          Start scores = (51, 27).
          Player 0 rolls 10 dice and gets outcomes [4, 3, 5, 6, 6, 6, 5, 1, 4, 3].
          End scores = (52, 27)
          >>> print(turns[9])
          Start scores = (52, 27).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 5, 6, 2].
          End scores = (52, 48)
          >>> print(turns[10])
          Start scores = (52, 48).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (63, 48)
          >>> print(turns[11])
          Start scores = (63, 48).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 2, 3, 5, 5, 1, 3].
          End scores = (63, 49)
          >>> print(turns[12])
          Start scores = (63, 49).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 1, 6, 2, 3].
          End scores = (64, 49)
          >>> print(turns[13])
          Start scores = (64, 49).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (64, 58)
          >>> print(turns[14])
          Start scores = (64, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (66, 58)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85229, score0=14, score1=16, goal=55)
          >>> print(turns[0])
          Start scores = (14, 16).
          Player 0 rolls 10 dice and gets outcomes [6, 4, 1, 5, 6, 3, 2, 1, 2, 4].
          End scores = (15, 16)
          >>> print(turns[1])
          Start scores = (15, 16).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 6, 2, 1].
          End scores = (15, 19)
          >>> print(turns[2])
          Start scores = (15, 19).
          Player 0 rolls 2 dice and gets outcomes [1, 1].
          End scores = (16, 19)
          >>> print(turns[3])
          Start scores = (16, 19).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 1, 1, 6, 4, 6, 1].
          End scores = (16, 20)
          >>> print(turns[4])
          Start scores = (16, 20).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 3, 2, 4, 6].
          End scores = (19, 20)
          >>> print(turns[5])
          Start scores = (19, 20).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 2, 6].
          End scores = (19, 34)
          >>> print(turns[6])
          Start scores = (19, 34).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (21, 34)
          >>> print(turns[7])
          Start scores = (21, 34).
          Player 1 rolls 9 dice and gets outcomes [4, 6, 4, 5, 3, 3, 5, 2, 5].
          End scores = (21, 73)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=57546, score0=31, score1=87, goal=88)
          >>> print(turns[0])
          Start scores = (31, 87).
          Player 0 rolls 3 dice and gets outcomes [6, 6, 3].
          End scores = (46, 87)
          >>> print(turns[1])
          Start scores = (46, 87).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (46, 97)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61086, score0=7, score1=17, goal=18)
          >>> print(turns[0])
          Start scores = (7, 17).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 6, 6, 1, 3, 5, 1, 4].
          End scores = (8, 17)
          >>> print(turns[1])
          Start scores = (8, 17).
          Player 1 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (8, 18)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75708, score0=8, score1=14, goal=17)
          >>> print(turns[0])
          Start scores = (8, 14).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 1, 5, 5, 3, 2, 3, 5, 4].
          End scores = (9, 14)
          >>> print(turns[1])
          Start scores = (9, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (9, 15)
          >>> print(turns[2])
          Start scores = (9, 15).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 2, 2, 3, 2, 4].
          End scores = (30, 15)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2684, score0=2, score1=17, goal=79)
          >>> print(turns[0])
          Start scores = (2, 17).
          Player 0 rolls 3 dice and gets outcomes [6, 6, 1].
          End scores = (5, 17)
          >>> print(turns[1])
          Start scores = (5, 17).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 4, 3, 1, 6, 1, 2].
          End scores = (5, 18)
          >>> print(turns[2])
          Start scores = (5, 18).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (9, 18)
          >>> print(turns[3])
          Start scores = (9, 18).
          Player 1 rolls 3 dice and gets outcomes [3, 4, 3].
          End scores = (9, 28)
          >>> print(turns[4])
          Start scores = (9, 28).
          Player 0 rolls 5 dice and gets outcomes [2, 6, 3, 5, 6].
          End scores = (37, 28)
          >>> print(turns[5])
          Start scores = (37, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (37, 31)
          >>> print(turns[6])
          Start scores = (37, 31).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 3, 1, 5].
          End scores = (38, 31)
          >>> print(turns[7])
          Start scores = (38, 31).
          Player 1 rolls 2 dice and gets outcomes [5, 3].
          End scores = (38, 39)
          >>> print(turns[8])
          Start scores = (38, 39).
          Player 0 rolls 8 dice and gets outcomes [5, 5, 3, 1, 3, 3, 2, 5].
          End scores = (39, 39)
          >>> print(turns[9])
          Start scores = (39, 39).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 6].
          End scores = (39, 40)
          >>> print(turns[10])
          Start scores = (39, 40).
          Player 0 rolls 9 dice and gets outcomes [4, 6, 3, 2, 1, 4, 2, 6, 3].
          End scores = (40, 40)
          >>> print(turns[11])
          Start scores = (40, 40).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 5, 3, 4, 1].
          End scores = (40, 43)
          >>> print(turns[12])
          Start scores = (40, 43).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (45, 43)
          >>> print(turns[13])
          Start scores = (45, 43).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 1, 6, 2, 1].
          End scores = (45, 44)
          >>> print(turns[14])
          Start scores = (45, 44).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (49, 44)
          >>> print(turns[15])
          Start scores = (49, 44).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 1].
          End scores = (49, 45)
          >>> print(turns[16])
          Start scores = (49, 45).
          Player 0 rolls 4 dice and gets outcomes [4, 4, 4, 1].
          End scores = (50, 45)
          >>> print(turns[17])
          Start scores = (50, 45).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 4, 4].
          End scores = (50, 63)
          >>> print(turns[18])
          Start scores = (50, 63).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 5, 6, 3, 6, 1, 4, 4, 5].
          End scores = (51, 63)
          >>> print(turns[19])
          Start scores = (51, 63).
          Player 1 rolls 4 dice and gets outcomes [2, 4, 4, 5].
          End scores = (51, 78)
          >>> print(turns[20])
          Start scores = (51, 78).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (56, 78)
          >>> print(turns[21])
          Start scores = (56, 78).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (56, 81)
          >>> print(turns[22])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=62911, score0=5, score1=32, goal=50)
          >>> print(turns[0])
          Start scores = (5, 32).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 5, 4, 3, 1, 2, 3].
          End scores = (6, 32)
          >>> print(turns[1])
          Start scores = (6, 32).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 33)
          >>> print(turns[2])
          Start scores = (6, 33).
          Player 0 rolls 9 dice and gets outcomes [5, 2, 1, 1, 2, 2, 4, 1, 2].
          End scores = (11, 33)
          >>> print(turns[3])
          Start scores = (11, 33).
          Player 1 rolls 8 dice and gets outcomes [4, 3, 3, 2, 6, 6, 6, 1].
          End scores = (11, 34)
          >>> print(turns[4])
          Start scores = (11, 34).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (23, 34)
          >>> print(turns[5])
          Start scores = (23, 34).
          Player 1 rolls 2 dice and gets outcomes [2, 2].
          End scores = (23, 38)
          >>> print(turns[6])
          Start scores = (23, 38).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (24, 38)
          >>> print(turns[7])
          Start scores = (24, 38).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 1, 6, 6, 1, 2, 2, 6, 6].
          End scores = (24, 39)
          >>> print(turns[8])
          Start scores = (24, 39).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 4, 3, 6].
          End scores = (25, 39)
          >>> print(turns[9])
          Start scores = (25, 39).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 6, 6, 3, 1].
          End scores = (25, 40)
          >>> print(turns[10])
          Start scores = (25, 40).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (28, 40)
          >>> print(turns[11])
          Start scores = (28, 40).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 6, 4, 6, 3, 2, 5, 1].
          End scores = (28, 43)
          >>> print(turns[12])
          Start scores = (28, 43).
          Player 0 rolls 7 dice and gets outcomes [2, 6, 4, 1, 2, 5, 2].
          End scores = (31, 43)
          >>> print(turns[13])
          Start scores = (31, 43).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (31, 48)
          >>> print(turns[14])
          Start scores = (31, 48).
          Player 0 rolls 8 dice and gets outcomes [4, 5, 1, 1, 3, 2, 5, 4].
          End scores = (32, 48)
          >>> print(turns[15])
          Start scores = (32, 48).
          Player 1 rolls 6 dice and gets outcomes [3, 4, 6, 3, 2, 6].
          End scores = (32, 72)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95467, score0=22, score1=10, goal=61)
          >>> print(turns[0])
          Start scores = (22, 10).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (29, 10)
          >>> print(turns[1])
          Start scores = (29, 10).
          Player 1 rolls 5 dice and gets outcomes [4, 6, 4, 1, 5].
          End scores = (29, 13)
          >>> print(turns[2])
          Start scores = (29, 13).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 3, 1].
          End scores = (30, 13)
          >>> print(turns[3])
          Start scores = (30, 13).
          Player 1 rolls 3 dice and gets outcomes [1, 5, 2].
          End scores = (30, 14)
          >>> print(turns[4])
          Start scores = (30, 14).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 5, 3, 4, 3, 2, 1, 4].
          End scores = (37, 14)
          >>> print(turns[5])
          Start scores = (37, 14).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (37, 29)
          >>> print(turns[6])
          Start scores = (37, 29).
          Player 0 rolls 7 dice and gets outcomes [5, 6, 3, 5, 4, 6, 4].
          End scores = (70, 29)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50497, score0=8, score1=17, goal=19)
          >>> print(turns[0])
          Start scores = (8, 17).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 1, 2, 5, 2, 4, 5].
          End scores = (9, 17)
          >>> print(turns[1])
          Start scores = (9, 17).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (9, 18)
          >>> print(turns[2])
          Start scores = (9, 18).
          Player 0 rolls 3 dice and gets outcomes [6, 6, 2].
          End scores = (29, 18)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52997, score0=15, score1=17, goal=23)
          >>> print(turns[0])
          Start scores = (15, 17).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (16, 17)
          >>> print(turns[1])
          Start scores = (16, 17).
          Player 1 rolls 8 dice and gets outcomes [4, 6, 1, 5, 1, 6, 6, 6].
          End scores = (16, 18)
          >>> print(turns[2])
          Start scores = (16, 18).
          Player 0 rolls 6 dice and gets outcomes [5, 2, 6, 3, 1, 1].
          End scores = (19, 18)
          >>> print(turns[3])
          Start scores = (19, 18).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 4, 1, 2, 3, 2, 5, 4].
          End scores = (19, 23)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=71455, score0=5, score1=34, goal=67)
          >>> print(turns[0])
          Start scores = (5, 34).
          Player 0 rolls 6 dice and gets outcomes [5, 6, 1, 2, 3, 3].
          End scores = (6, 34)
          >>> print(turns[1])
          Start scores = (6, 34).
          Player 1 rolls 8 dice and gets outcomes [2, 5, 5, 6, 1, 5, 4, 5].
          End scores = (6, 35)
          >>> print(turns[2])
          Start scores = (6, 35).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (13, 35)
          >>> print(turns[3])
          Start scores = (13, 35).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 2, 4, 6, 4].
          End scores = (13, 36)
          >>> print(turns[4])
          Start scores = (13, 36).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 1, 5, 2, 6, 1, 2, 4, 2].
          End scores = (14, 36)
          >>> print(turns[5])
          Start scores = (14, 36).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 3, 1, 5, 4, 6, 5, 2].
          End scores = (14, 41)
          >>> print(turns[6])
          Start scores = (14, 41).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (23, 41)
          >>> print(turns[7])
          Start scores = (23, 41).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (23, 47)
          >>> print(turns[8])
          Start scores = (23, 47).
          Player 0 rolls 4 dice and gets outcomes [6, 4, 1, 5].
          End scores = (24, 47)
          >>> print(turns[9])
          Start scores = (24, 47).
          Player 1 rolls 6 dice and gets outcomes [4, 1, 2, 6, 6, 6].
          End scores = (24, 48)
          >>> print(turns[10])
          Start scores = (24, 48).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (25, 48)
          >>> print(turns[11])
          Start scores = (25, 48).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 2].
          End scores = (25, 49)
          >>> print(turns[12])
          Start scores = (25, 49).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 2, 2, 2].
          End scores = (38, 49)
          >>> print(turns[13])
          Start scores = (38, 49).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (38, 52)
          >>> print(turns[14])
          Start scores = (38, 52).
          Player 0 rolls 2 dice and gets outcomes [5, 5].
          End scores = (48, 52)
          >>> print(turns[15])
          Start scores = (48, 52).
          Player 1 rolls 7 dice and gets outcomes [3, 5, 2, 2, 2, 6, 5].
          End scores = (48, 77)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=49921, score0=0, score1=5, goal=17)
          >>> print(turns[0])
          Start scores = (0, 5).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 2, 4].
          End scores = (2, 5)
          >>> print(turns[1])
          Start scores = (2, 5).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (2, 13)
          >>> print(turns[2])
          Start scores = (2, 13).
          Player 0 rolls 8 dice and gets outcomes [1, 5, 3, 1, 5, 5, 1, 4].
          End scores = (5, 13)
          >>> print(turns[3])
          Start scores = (5, 13).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 4, 4].
          End scores = (5, 37)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=16868, score0=15, score1=34, goal=50)
          >>> print(turns[0])
          Start scores = (15, 34).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 1, 6, 6, 4, 5, 4].
          End scores = (16, 34)
          >>> print(turns[1])
          Start scores = (16, 34).
          Player 1 rolls 6 dice and gets outcomes [5, 5, 6, 6, 5, 2].
          End scores = (16, 63)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=57547, score0=59, score1=4, goal=60)
          >>> print(turns[0])
          Start scores = (59, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (60, 4)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
