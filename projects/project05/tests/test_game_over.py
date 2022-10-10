test = {
  'name': 'game over tests',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from cs1.notebooks import *
          >>> reload_functions("panda_party.py")
          >>> is_game_over(5)
          False
          >>> is_game_over(0)
          True
          """,
          'hidden': True,
          'locked': True,
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
