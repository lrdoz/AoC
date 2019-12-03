import logging
import random

import azure.functions as func


def main(req):
    return func.HttpResponse(random.choice(["נ", "ג", "ה", "ש"]))
