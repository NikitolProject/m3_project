from m3_ext.context_processors import DesktopProcessor


def desktop(request) -> dict:
	return DesktopProcessor.process(request)

