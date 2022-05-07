from legend_testdata import LegendTestData
import fcutils

ldata = LegendTestData()
ldata.checkout('49c7bdc')


def test_fcio_init():
    fcutils.fcio(ldata.get_path('fcio/th228.fcio'))
