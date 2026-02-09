from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.communication import CommunicationService


def test_communication_get_document_sent_list_calls_GetDocumentSentList(zeep_service, tzinfo) -> None:
    svc = CommunicationService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_document_sent_list"))
    getattr(svc, "get_document_sent_list")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetDocumentSentList"
    assert args[0] == "TOKEN123"
