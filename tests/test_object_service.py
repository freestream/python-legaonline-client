from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.object import ObjectService


def test_object_get_object_image_calls_GetObjectImage(zeep_service, tzinfo) -> None:
    svc = ObjectService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_object_image"))
    getattr(svc, "get_object_image")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetObjectImage"
    assert args[0] == "TOKEN123"
