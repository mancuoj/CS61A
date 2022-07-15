test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> limit = 10
          >>> hidden_kittens("ccatgts", "cats", limit)
          bfdc03a3c261c5dc71255ec79dd5977e
          # locked
          >>> hidden_kittens("ccatgts", "cats", 4)
          bfdc03a3c261c5dc71255ec79dd5977e
          # locked
          >>> hidden_kittens("ccatgts", "cats", 3) > 3
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> hidden_kittens("ccatgtsaaaaaaaaaaaaaaaa", "cats", limit)
          bfdc03a3c261c5dc71255ec79dd5977e
          # locked
          >>> hidden_kittens("123123123", "123", limit) # Hint: 123 appears 10 times within 123123123!
          d9730cc1ae65aae2ba7ba73a9f3cd7fd
          # locked
          >>> hidden_kittens("123123123", "123", 5) > 5
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> hidden_kittens("kittens", "kittens", limit)
          52f1b72ba99dddc798bb5cebce0be695
          # locked
          >>> hidden_kittens("hiddnehddi", "hidden", limit) > limit
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> hidden_kittens("big", "bigger", limit) > limit
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> big_limit = 20
          >>> hidden_kittens("order matters", "ret", big_limit)
          45c27a29bbaeb163dec9a0eaed9c7c9c
          # locked
          >>> hidden_kittens("ret", "order matters", big_limit) > big_limit
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> hidden_kittens("abcdefghijklmnopqrstuvwxyz", "z", big_limit)
          52f1b72ba99dddc798bb5cebce0be695
          # locked
          >>> hidden_kittens("abcdefghijklmnopqrstuvwxyz", "@", big_limit) > big_limit
          f0a7036a7438d73054555da0482ad042
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired","abstraction", "abstract", "peeling", "gestate", "west","spelling", "bastion"]
          >>> autocorrect("sspelll", small_words_list, hidden_kittens, 10)
          'spell'
          >>> autocorrect("aabstracttion", small_words_list, hidden_kittens, 10)
          'abstraction'
          >>> autocorrect("tests", small_words_list, hidden_kittens, 10)
          'test'
          >>> autocorrect("bbaajksstioon", small_words_list, hidden_kittens, 10)
          'bbaajksstioon'
          >>> autocorrect("baastyioon", small_words_list, hidden_kittens, 10)
          'bastion'
          >>> test.check('cats.py', 'hidden_kittens', ['While', 'For', 'ListComp'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(hidden_kittens, "awe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('rut', 'rzumt', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('yo', 'yo', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('slurp', 'slurpm', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('nice', 'tie', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('owen', 'owen', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('donee', 'shush', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('drest', 'drwt', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('cand', 'towy', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('drawn', 'terry', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('stour', 'shows', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('plash', 'cw', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('cube', 'cube', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('envy', 'nv', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('panto', 'panto', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('herem', 'hwerem', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('zanze', 'culm', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('kauri', 'kajr', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('hiver', 'hicer', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('tulip', 'qlulip', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('aside', 'ataxy', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('volt', 'vol', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('sleep', 'sleop', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('cet', 'duad', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('opal', 'oral', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('pathy', 'pathy', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('drive', 'drgitb', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('bater', 'kbater', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('ward', 'crier', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('massy', 'massy', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('tonk', 'tobnhn', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('sith', 'demit', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('arty', 'at', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('exist', 'ext', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('plot', 'plkot', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('wreak', 'wreak', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('icon', 'ipnw', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('caza', 'scale', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('rann', 'daw', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('natal', 'nttyl', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('tji', 'j', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('input', 'input', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('lysin', 'lzsbun', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('bed', 'bc', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('topsl', 'topsl', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('becap', 'becap', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('tiny', 'sizes', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('plots', 'gplots', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('plote', 'plot', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('libra', 'unact', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('shed', 'tshged', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('lunes', 'lunes', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('shooi', 'sgcoi', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('cahow', 'cahow', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('watch', 'wotchj', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('jeans', 'anps', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('floey', 'uvea', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('pew', 'pe', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('tec', 'gtec', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('chef', 'drib', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('sowel', 'evert', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('zebu', 'eu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('magma', 'mahgfma', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('shood', 'ketal', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('stall', 'ftall', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('towd', 'owz', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('doty', 'dsto', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('prime', 'huso', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('raspy', 'eraiepy', k) > k for k in range(7)])
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('sight', 'szlht', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('scho', 'ho', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('sher', 'sided', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('glime', 'plane', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('canon', 'dcvanon', k) > k for k in range(7)])
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('soon', 'o', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('would', 'wuold', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('yeat', 'yawt', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('lexus', 'lexrs', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('randy', 'lose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('thee', 'thaee', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('pilot', 'pilot', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('irk', 'hokey', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('foody', 'lough', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('mensa', 'mrvs', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('spung', 'pxkg', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('db', 'db', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('beala', 'beamff', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('bepun', 'bpun', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('film', 'fblu', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('espn', 'esp', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('hondo', 'gkondo', k) > k for k in range(6)])
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('reps', 'gata', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('tirr', 'ir', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('slote', 'svoltj', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('beeve', 'jegvd', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('evade', 'evade', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('sinew', 'dinw', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('goods', 'goos', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('kiley', 'kiley', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([hidden_kittens('score', 'score', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hidden_kittens('flags', 'faqs', 100)
          101
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import hidden_kittens, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
