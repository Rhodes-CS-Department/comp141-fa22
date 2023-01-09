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
          >>> next_player("Le Le")
          'Ya Ya'
          >>> next_player("Ya Ya")
          'Le Le'
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
