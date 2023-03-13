import sys
from types import SimpleNamespace
import fastbook
import torch
from fastai.learner import load_learner
import pathlib
from fastai.vision.core import PILImage

# model was trained on linux - this hack
# is needed to make it run on Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


class Classifier(object):
    def isYummyFromPath(self, path: str):
        # Create uploader, in order to create a PILImage
        # as it's the format expected by our classifier.
        uploader = SimpleNamespace(data=[path])
        img = PILImage.create(uploader.data[0])
        return self.isYummy(img)

    def isYummy(self, image: PILImage):
        # setup
        def is_yummy(x): return x[0].isupper()
        fastbook.setup_book()

        # choose GPU if available, CPU if not
        torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        torch.cuda.empty_cache()

        # add is_yummy function to __main__ module scope,
        # as it's expected there by out model
        sys.modules['__main__'].is_yummy = is_yummy

        # load our model
        model = load_learner("wykrywacz.pkl")

        # predict
        is_ok_category, _, probs = model.predict(image)

        # cast result to boolean
        is_ok = False
        if is_ok_category == "True":
            is_ok = True

        # prepare and return result
        probability = probs[1].item()
        return is_ok, probability

