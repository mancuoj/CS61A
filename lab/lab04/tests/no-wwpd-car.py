test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          cc0e106b229dbf1be916fe923e79c15e
          # locked
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          e53294b18d1b589ae6f815549c72b530
          # locked
          >>> deneros_car.drive()
          65d318bdd39e26f408eb82ee6d9770d0
          # locked
          >>> deneros_car.fill_gas()
          3e7b68190dc5e85f129faf6af874b6dc
          # locked
          >>> deneros_car.gas
          d8f6862db520e18f08ef94797dd8347f
          # locked
          >>> Car.gas
          ffe5bc1271852870f30d1930702955c6
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          61b793952531daad90d65377b695da99
          # locked
          >>> Car.num_wheels
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          65d318bdd39e26f408eb82ee6d9770d0
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          65d318bdd39e26f408eb82ee6d9770d0
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
