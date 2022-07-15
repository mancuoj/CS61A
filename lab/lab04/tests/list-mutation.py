test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          5c5b429063049b010ee9d6da4aff0f09
          # locked
          >>> lst
          8479bcf7fd6e046c0ee92e37bd0bd1c5
          # locked
          >>> lst.insert(0, 9)
          >>> lst
          34540cad83a3fb7bcbb40cf99a050929
          # locked
          >>> x = lst.pop(2)
          >>> lst
          8523dc04d1767396bf99d8d5f2753450
          # locked
          >>> lst.remove(x)
          >>> lst
          92986ceb5cb04366cd52ed70547eb7cc
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b == lst
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b is lst
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> lst = [1, 2, 3]
          >>> lst.extend([4,5])
          >>> lst
          7d241a7117321fe8224337cd04bcaeea
          # locked
          >>> lst.extend([lst.append(9), lst.append(10)])
          >>> lst
          1609c78512e62bce90ba1e915f99f5a8
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
