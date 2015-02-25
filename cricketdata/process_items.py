#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import redis


def main():
    r = redis.Redis()
    while True:
        source, data = r.brpop(["cri:items"])
        item = json.loads(data)
        try:
            print u"Processing: %(url)s <%(ground)s>" % item
        except KeyError:
            print u"Error procesing: %r" % item


if __name__ == '__main__':
    main()