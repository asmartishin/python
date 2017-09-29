class QuerysetIterator(object):
    def __init__(self, queryset, batch_size):
        self._queryset = queryset
        self._batch_size = batch_size
        self._generator = self._create_generator()

    def _create_generator(self):
        for i in xrange(0, self._queryset.count(), self._batch_size):
            batch = self._queryset[i:i + self._batch_size]

            for obj in batch.iterator():
                yield obj

    def __iter__(self):
        return self

    def next(self):
        return self._generator.next()

    def __next__(self):
        return self.next()
