from types import ModuleType

import cloudcoil.models.knative_eventing as knative_eventing


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), knative_eventing.__dict__.values()))
    assert modules, "No modules found in knative_eventing"
