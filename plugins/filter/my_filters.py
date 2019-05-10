def my_filter(data):
    return "{0}_echo".format(data)


class FilterModule(object):

    def filters(self):
        return {
            'my_filter': my_filter
        }
