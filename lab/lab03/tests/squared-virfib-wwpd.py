test = {
  'name': 'Squared Virahanka Fibonacci',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def virfib_sq(n):
          ...     print(n)
          ...     if n <= 1:
          ...         return n
          ...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
          >>> r0 = virfib_sq(0)
          f34cd05f0e141093f7ce0bc202fd4972
          # locked
          >>> r1 = virfib_sq(1)
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          # locked
          >>> r2 = virfib_sq(2)
          73a9752b0761167119f7a8667ed17719
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          f34cd05f0e141093f7ce0bc202fd4972
          # locked
          >>> r3 = virfib_sq(3)
          c66c489c94f153ccc42909baf6da3202
          73a9752b0761167119f7a8667ed17719
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          f34cd05f0e141093f7ce0bc202fd4972
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          # locked
          >>> r3
          ad741b000d1cc7ef3beaaf650d8f371b
          # locked
          >>> (r1 + r2) ** 2
          ad741b000d1cc7ef3beaaf650d8f371b
          # locked
          >>> r4 = virfib_sq(4)
          ad741b000d1cc7ef3beaaf650d8f371b
          c66c489c94f153ccc42909baf6da3202
          73a9752b0761167119f7a8667ed17719
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          f34cd05f0e141093f7ce0bc202fd4972
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          73a9752b0761167119f7a8667ed17719
          71a5e7aa11e66d4d6ce4be8fda1e18ec
          f34cd05f0e141093f7ce0bc202fd4972
          # locked
          >>> r4
          e0a719ebba1ad1d00bf46f8e22acf49e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
