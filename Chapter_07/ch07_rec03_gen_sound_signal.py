import numpy


def _get_mask(t, t1, t2, lvl_pos, lvl_neg):
    if t1 >= t2:
        raise ValueError("t1 must be less than t2")

    return numpy.where(numpy.logical_and(t > t1, t < t2), lvl_pos, lvl_neg)


def generate_signal(t):
    sin1 = numpy.sin(2 * numpy.pi * 100 * t)
    sin2 = 2 * numpy.sin(2 * numpy.pi * 200 * t)

    # add interval of high pitched signal
    masks = _get_mask(t, 2, 4, 1.0, 0.0) + \
            _get_mask(t, 14, 15, 1.0, 0.0) 
    sin2 = sin2 * masks

    noise = 0.02 * numpy.random.randn(len(t))
    final_signal = sin1 + sin2 + noise
    return final_signal


if __name__ == '__main__':
    step = 0.001
    t = numpy.arange(0.0, 20.0, step)
    print numpy.shape(generate_signal(t))
