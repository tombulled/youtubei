from youtubei.web.responses import GuideResponse


def parse_guide(data, /):
    return GuideResponse.model_validate(data)
