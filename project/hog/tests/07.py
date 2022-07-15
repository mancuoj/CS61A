test = {
  'name': 'Question 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '6d36cf85dceafad42b3816d0df5734e3',
          'choices': [
            'A message.',
            'A player.',
            'A message and a player (in that order).',
            'A player and a message (in that order).'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a commentary function return?'
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
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(4, 6, 4), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 4
          Player 1 takes the lead by 2
          Player 0 takes the lead by 2
          Player 1 takes the lead by 2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(1), always_roll(2), dice=make_test_dice(1, 3, 3), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 2
          Player 1 takes the lead by 4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, f"{s0} {s1}" # message of the form: "s0 s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=6, say=echo) # Remember pigs on prime!
          791e80e4872c37c0b77421f6211d8e54
          6e3b797d0348d34c68cc3caeb6bc49f7
          5a7d3511c2b271dc7566cdcc93c504e9
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1, curr_count=None):
          ...         if curr_count is None:
          ...           curr_count = n
          ...         return curr_count + 1, str(curr_count) + " " + str(s0)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
          65778d21a5651e6f07c0edda625d4d25
          3ffe50afce5e5610d9cecba2a566c86d
          721f0b1ab817deaa5cac39327411c19e
          461ff541bd06a2e3310447d10cc6615b
          0eae6eedf96692954917ccec3fde1e1a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, announce_lead_changes
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, str(s0) + " " + str(s1)
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          f4d41f4e29a08f003e0a9a5473c61d5e
          461ff541bd06a2e3310447d10cc6615b
          ab92c2ead3d7b80c5e86a0a280dc94b5
          f6e85b18fc8f82a2883888dfe553eba8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def total(s0, s1, player=None):
          ...     return player, str(s0 + s1)
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)
          16e2cf37e8254529473d9e0a36b75fcb
          70e71b420a966665c548a3bb2cb30d7d
          26dad951f8e75106f151e4085e117edd
          25c20617047858d41b4c21bd68b1bd5b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1, player=None):
          ...     return player, f"* {s0}" # message of the form: "* s0"
          >>> def echo_1(s0, s1, player=None):
          ...     return player, f"** {s1}" # message of the form: "** s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          e58117f80b57e46a3f1b2fbf34c8d330
          4a64fe964dc771a219ed773c3a146c75
          e58117f80b57e46a3f1b2fbf34c8d330
          24ba9ce1d94be52f2551b89d6547398c
          85020533317ed0d716a2776b0db86a0e
          24ba9ce1d94be52f2551b89d6547398c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes))
          Player 0 now has 2 and now Player 1 has 0
          Player 0 takes the lead by 2
          Player 0 now has 2 and now Player 1 has 2
          Player 0 now has 5 and now Player 1 has 2
          Player 0 takes the lead by 3
          Player 0 now has 5 and now Player 1 has 10
          Player 1 takes the lead by 5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
